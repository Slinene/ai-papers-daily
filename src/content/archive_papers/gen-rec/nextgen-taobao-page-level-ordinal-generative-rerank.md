---
title: "NextGen: A Multi-Objective Generative Re-ranking Framework for Taobao Recommendation"
authors: "Longxiang Xiong, Chaoqun Hou, Zihao Zhu, Cheng Guo, Tong Liu et al. (6 人)"
affiliation: "Alibaba (Taobao & Tmall Group)"
date: "2026-09"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把生成式重排的监督从「预测下一个曝光 item」换成「页面级累计点击/成交数的有序回归」：每一步预测若把候选放在第 t 位，前缀累计点击/支付数 ≥ j 的概率（j=1..K）。Encoder 对 user+全部 100 个候选+历史做全局自注意力，Decoder 自回归出 hidden state，再用共享 MLP 一次前向给全部候选打分；上游 CTR/CVR 分在 embedding 层和打分层双重注入做残差式增量重排，推理时用相邻步分数差+统一阈值+rank 归一融合 CTR/CVR/GMV 再加 MMR。"
paperUrl: https://doi.org/10.1145/3773078.3831881
codeUrl: null
tags:
- "Generative Re-ranking"
- "Page-level Ordinal Regression"
- "Full-candidate Decoding"
- "Multi-Objective Fusion"
- "Residual Upstream Scores"
unverified: false
---
> 淘宝秒杀场景的生成式重排。核心是把监督信号从「下一个曝光 item」换成「页面前缀累计点击/支付数的有序回归」，再用 Encoder-Decoder 一次前向给全部 100 个候选打分，替代同团队 SIGIR'25 的 Sort-gen。

## 核心思路

现有生成式重排有两个缺口：一是监督太弱，GReF、TIGER 一类方法学的是 next-item 曝光，跟整页点击量、成交量这些业务目标没有直接关系；二是太慢，Sort-gen 要把每个候选单独送进 decoder 算一个「序列价值」，线上只能看 top-30，每轮只处理 3 个。

NextGen 的处理方式：

1. **页面级有序回归监督**：第 t 步的标签是「到第 t 位为止累计点击数 ≥ j」（j=1..K），CTR 和 CVR（累计支付数）各有一组 K 维 sigmoid 输出。模型学的是「把候选 c_i 放在第 t 位后，整页前缀累计效用会到哪个档位」。
2. **全候选单次前向**：Encoder 编码 user + 全部 N=100 个候选 + 历史，Decoder 每步只产出一个 hidden state q_t，再由共享 MLP 和每个候选的 z_i 拼接打分，复杂度近似 O(K·N) 次 MLP。
3. **残差式增量重排**：上游精排的 CTR/CVR 分同时注入输入 embedding 和最终打分 MLP，让模型只学「相对精排的非线性修正」。
4. **冻结 LLM 语义向量**：TBStar（淘宝多模态大模型）对标题+图片离线编码出 256 维向量，作为普通特征查表，线上不需要做 LLM 推理。

## 整体实现思路

- **问题定义**：pi* = argmax_{pi ∈ Π(C_u, K)} R(pi | u, C_u, I_u)，在 N 个候选中选 K 个并排序，R 为页面级多目标价值。按自回归分解成 P(pi) = ∏_t P(pi_t | pi_<t, u, C_u, I_u)。
- **训练**：用真实曝光序列 D_u 做 teacher forcing，每步只在真实曝光 item 上计算有序回归 BCE；打分网络对所有 item、所有步共享，靠海量日志学到依赖上下文的候选效用。
- **推理**：贪心解码 K=10 步。每步对剩余候选算 CTR/CVR 的 K 维有序概率，构造 GMV 代理，对相邻步做差得到边际增益，选一个统一阈值，做 rank 归一后加权融合，最后用 MMR 加入多样性，再取 argmax。
- **线上约束**：外层还有硬多样性规则（任意连续 5 个 item 不能出现重复叶子类目），Sort-gen 和 NextGen 共用同一套 MMR 系数与硬规则。

## 子模块实现（可复现细节）

### 1. 特征与 item 表示

e_i = Proj([e_i^id ; e_i^side ; e_i^llm ; e_i^pos ; e_i^ctr ; e_i^cvr])

- e^id：item ID embedding；e^side：类目、品牌、历史统计（历史 CTR/CVR 等）；
- e^llm：TBStar 对 title+image 编码后 mean pooling 得到的 256 维冻结向量。存量 item 预先算好存在离线特征表里，线上加载进 item embedding table；新品上线前异步调用模型生成并写入。因此延迟开销和普通特征一样；
- e^pos：该 item 在上游排序中的位次；
- e^ctr / e^cvr：精排 CTR/CVR 分的 embedding（论文未说明分桶方式）；
- Proj：线性投影到 d 维（实现中 d=256）。

用户侧特征包括 user ID、设备类型和时间特征；历史序列 I_u 取最近 M 个点击（M 未给出）。

### 2. Encoder：全局候选集建模

Z = Encoder([e_u ; e_1 ; … ; e_N ; e_{i1} ; … ; e_{iM}])

使用 L=2 层标准 Transformer encoder，hidden 256，4 头。每个候选都能 attend 到其他所有候选和用户历史，以此学习互补、替代等关系。消融显示这一模块最关键：去掉后 CTR AUC 下降 0.0775、CVR AUC 下降 0.1104。

### 3. Decoder：因果解码

q_t = Decoder(e_{d1}, …, e_{d(t-1)} ; Z)

使用 2 层 Transformer decoder，包括 masked self-attn、对 Z 的 cross-attn 和 FFN。训练时输入真实曝光前缀，推理时输入已选的 pi_<t。

### 4. 候选打分（多目标有序概率）

- f_{t,i} = MLP([q_t ; z_i ; e_i^ctr ; e_i^cvr])
- p^ctr_{t,i,j} = σ(w_j^ctr · f_{t,i} + b_j^ctr)，j = 1..K；CVR 是另一组结构相同的 K 个头。

这里第二次注入 e^ctr/e^cvr，加上输入层那一次，就是所谓「残差连接」。论文称两处都注入比只注入一次效果更好。消融中去掉打分层的注入，CTR/CVR AUC 分别下降 0.0546/0.0623。

### 5. 标签与损失

- 累计点击：Y_t^ctr = Σ_{s≤t} 1[click(d_s)=1]
- 有序标签：l_{t,j}^ctr = 1[Y_t^ctr ≥ j]，j = 1..K（阈值数等于 K，因为一页最多 K 次点击）
- CVR 用前缀累计支付数，构造方式相同
- 单步损失：L_ord = -(1/K) Σ_j [ l_j log p_j + (1 - l_j) log(1 - p_j) ]
- 总损失：L = (1/K) Σ_t ( L_ord,t^ctr + L_ord,t^cvr )
- 优化器 Adam，lr 0.001，batch 1024

### 6. 推理：多目标差分融合 + MMR（Algorithm 1）

1. **GMV 代理**：p^gmv_{t,i,j} = p^ctr_{t,i,j} · p^cvr_{t,i,j} · price_i，不单独训练 GMV 头。
2. **差分效用**：Δs^o_{t,i,j} = s^o_{t,i,j} - s^o_{t-1,i,j}，o ∈ {ctr, cvr, gmv}；t=1 时直接用原始分。论文把它解释为候选 c_i 在第 t 位对累计页面效用的边际贡献。
3. **统一阈值**：对每个候选、每个目标取差分最大的阈值 j_i^o = argmax_{j ≤ min(t,K)} Δs^o_{t,i,j}，再取全局最大 j*_t = max_i max_o j_i^o。意思是在当前最有区分度的档位上比较所有候选。
4. **rank 归一**：Δs^{o,uni}_{t,i} = Δs^o_{t,i,j*_t}，s~ = φ(Δs) = 1 / log(1 + rank + ε)，ε = 1e-8，rank 1 表示最好。
5. **融合**：Δv_{t,i} = α_ctr s~^ctr + α_cvr s~^cvr + α_gmv s~^gmv，三个权重都取 0.33。
6. **MMR**：Sim(i, pi_<t) = max_{j ∈ pi_<t} cos(e_i, e_j)，用静态表示 e_i，不用上下文表示 z_i；s^mmr = λΔv - (1 - λ)Sim，λ = 0.5。
7. 选 argmax 加入序列，并从候选集中移除，重复直到选满 K=10 个。

作者认为，推理只比较差分，所以不要求有序概率满足单调性（p_j ≥ p_{j+1}）。

## 实验设置与结果

**数据**：淘宝秒杀（限时折扣）场景，3 个月生产流量。**配置**：N=100，K=10，Encoder/Decoder 各 2 层、256 维、4 头，与 Sort-gen 保持一致。

### 在线 A/B（14 天，5% 流量，相对 RULE，均 p<0.01）

| 方法 | V2P Rate | GMV | CTR | Order Vol. |
|---|---|---|---|---|
| FastDPP | +0.61% | +1.70% | −0.73% | +0.47% |
| PRM | +0.19% | +2.24% | +2.73% | +2.21% |
| FFT-Context | +2.43% | +2.87% | +1.82% | +2.24% |
| Sort-gen | +2.74% | +4.95% | +1.09% | +2.90% |
| **NextGen** | **+14.84%** | **+24.73%** | **+20.08%** | **+15.61%** |

相对 Sort-gen 的提升：V2P +11.78%、GMV +18.85%、CTR +18.77%、订单 +12.35%。按 14 天逐日数据算的 95% 置信区间：V2P +11.81% [11.07%, 12.56%]，人均 GMV +18.25% [16.39%, 20.12%]，人均点击 +18.53% [17.52%, 19.54%]，人均订单 +14.05% [10.88%, 17.22%]，14 天里每一天都是 NextGen 更好。另做了 14 天 A/A 测试，差异为 +0.35% / −0.77% / −0.30% / +0.40%，都不显著。

Sort-gen 的数字比原论文低，原因是加了多样性约束：

| 配置 | V2P | GMV | CTR | Order | Bad Case |
|---|---|---|---|---|---|
| Sort-gen | base | base | base | base | 34% |
| + 多样性优化 | −3.12% | −9.47% | −8.24% | −3.07% | 0.6% |

### 离线 AUC（K 个阈值的平均 AUC）

| 方法 | CTR AUC | CVR AUC |
|---|---|---|
| Sort-gen | 0.7705 | 0.7739 |
| NextGen (top-30) | 0.7812 | 0.8016 |
| NextGen (top-100) | **0.8123** | **0.8433** |

把候选同样限制在 top-30 时，NextGen 仍高出 Sort-gen +0.0107 / +0.0277，说明仅架构本身就有收益；扩到 top-100 后提升更大。

### 消融

| 变体 | CTR AUC | CVR AUC |
|---|---|---|
| NextGen (Full) | 0.8123 | 0.8433 |
| w/o 候选间上下文 | 0.7348 | 0.7329 |
| w/o 残差连接 | 0.7577 | 0.7810 |
| w/o LLM 语义向量 | 0.8101 | 0.8211 |

### 其他分析

- **候选覆盖**：NextGen 的 GMV 中，精排第 31–100 位的 item 占 21.03%，这部分 Sort-gen 完全够不着。作者因此认为，任何只在 top-30 内重排的方法，最多会损失约 21% 的 GMV。
- **延迟**：26ms，Sort-gen 是 24ms，多 2ms（+8.3%），硬件相同。
- **Case**：精排第 47 位的羽毛球手胶，因为和已选的球拍、羽毛球互补而被提上来，最终成交。
- **版式泛化**：K 只决定解码步数，换成不同坑位数的版式时调整 K 即可，必要时再微调。

## 思考与可参考价值

**值得借鉴的点**

- **累计业务量有序回归**是这篇最可迁移的设计。它把「整页能到几次点击/几单」拆成 K 个二分类，标签可以直接从曝光日志按前缀累加得到，几乎没有额外成本，也很容易扩展到加购、收藏等目标。比起 next-item CE，它让生成式列表模型直接面向业务指标。
- **重排场景不需要 SID**。候选只有 100 级时，用 encoder 编码候选、decoder 的 hidden state 加共享 MLP 对候选打分，相当于 pointer 式生成，延迟可控。SID 和全词表生成更适合召回。（推断：如果要把生成式召回和重排串起来，可以在重排侧沿用这种 pointer 打分，SID 只放在召回侧。）
- **上游分双重注入**几乎是免费收益，适用于任何在强精排信号上做增量的模块。
- **冻结多模态 LLM 向量**主要对 CVR 有帮助（+0.0222），对 CTR 几乎没有影响（+0.0022）。新品异步生成向量的服务链路可以直接参考。

**需要警惕的点**

- **收益归因**：在线 +18.85% GMV 中，有相当一部分可能来自候选从 30 扩到 100（31–100 位贡献 21.03% GMV 是上界参考）。作者承认没有做 top-30 限制的在线 A/B。自己落地时应先单独测候选扩容的收益。
- **训练与推理不一致**：监督只落在真实曝光的 item 上，推理却要对 100 个候选打分，其中大多数从未在该位置曝光过。打分在反事实候选上是否校准，论文没有验证。（推断：可以加入随机探索流量，或用 evaluator 生成伪标签来缓解。）
- **推理启发式缺少消融**：差分、全局最大阈值 j*、rank 归一、0.33 等权这些步骤，论文都只给了直觉解释，没有逐项对比。尤其是 j* 取全局最大，可能让所有候选都在一个只有少数候选能达到的高档位上比较，噪声较大。迁移时应逐项验证。
- **场景单一**：秒杀场景购买意图强、价格敏感，CVR 信号密集。普通信息流或内容场景下累计支付数会非常稀疏，CVR 有序头能否学好需要重新评估。
- **离线评估偏弱**：只报告了阈值平均 AUC，没有列表级离线指标，也没有和判别式方法做离线对比；论文没有开源代码。
