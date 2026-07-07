---
title: 'ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping'
authors: Jiacheng Chen, Tao Zhang, Manxi Lin, Dunxian Huang, Teng Shi, et al. (26
  人)
date: 2026-06
venue: arXiv
topic: agentic-rec
topic_name: Agent推荐
topic_icon: 🧭
idea: 针对LLM代理通过外部搜索/推荐接口实现购物意图时的信息损耗，提出模型原生的商品空间操作基础模型ShopX。利用语义可恢复的混合全局-局部SID统一意图理解、执行规划与灵活的商品操作（检索/排序/捆绑），减少工具交互的带宽损失。通过SID对齐、领域预训练、多教师在线策略蒸馏与联合奖励训练，在保留通用能力的同时获得意图到商品的深度实现能力。
paperUrl: https://arxiv.org/abs/2606.31693
codeUrl: null
tags:
- Agentic Shopping
- Foundation Model
- Semantic ID
- On-policy Distillation
- Joint RL
unverified: true
---

## 核心思路
解决现有LLM代理在购物场景中将丰富意图和上下文通过低带宽的搜索/推荐工具调用传递，导致细粒度信号（偏好、约束、跨商品兼容性）丢失的问题。ShopX将商品空间操作直接内置到模型内部，通过语义ID（SID）作为可生成的商品桥梁，使模型能原生执行检索、排序、捆绑等商品级操作，并在统一框架下完成意图理解、规划和输出，从而减少lossy tool hand-offs，提升多轮交互中的上下文保持和反馈适应能力。

## 整体实现思路
端到端流程如下：

```
1. 输入：用户查询、上下文（用户画像、行为历史SID序列）、会话状态
2. 模型通过Serving Harness定义的动作协议（Plan → Execute → Fulfill → Update）进行响应
   - Plan: 理解意图，决定执行路径（检索/排序/捆绑/澄清等）
   - Execute: 基于SID执行商品空间操作（beam search检索、种子扩展、捆绑生成），利用Catalog获取商品证据
   - Fulfill: 生成包含SID和自然语言交错的用户回复
   - Update: 输出需要持久化的状态更新信号（偏好摘要、任务上下文）
3. 训练管线：
   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐
   │ 基座LLM  │ → │ SID对齐  │ → │ 领域CPT  │ → │ 后训练SFT │ → │ OPD–RL联合 │ → ShopX模型
   └──────────┘   └──────────┘   └──────────┘   └───────────┘   └───────────┘
   - SID对齐：冻结主体，仅训练新SID token embeddings
   - 领域CPT：混合购物数据与通用数据，全参数继续预训练
   - SFT：监督微调覆盖一般指令和商品任务
   - OPD–RL：多教师在线策略蒸馏+任务特定奖励联合优化
4. 部署：ShopX模型嵌入harness，通过动作槽位与服务接口交互，完整占有商品空间决策。
```

## 子模块实现（可复现细节）

### 1. 语义ID构造（SID Construction）

**目标**：为每个商品生成一个模型可自回归生成的离散ID序列，同时保留可恢复的语义信息。

**输入**：商品多模态数据 $x_i = (v_i, a_i, t_i)$，其中 $v_i$ 是商品图片，$a_i$ 是结构化属性，$t_i$ 是标题。

**输出**：混合全局–局部SID序列，形如 $G_2(i) \parallel L_4(i) = [z_{i,1}^G, z_{i,2}^G, z_{i,1}^L, z_{i,2}^L, z_{i,3}^L, z_{i,4}^L]$，其中前2个token为全局前缀（从RQ-VAE得到），后4个token为局部后缀（从VQ得到）。

#### 1.1 多模态商品表征学习

**编码器**：Qwen3-VL-Embedding-2B，直接处理商品图片、属性、标题，输出以下两种结构：
- 单向量 (SV): $E_\theta^{\text{SV}}(x_i) = g_i$ （全局向量）
- 多向量 (MV): $E_\theta^{\text{MV}}(x_i) = (g_i, \ell_{i,1}, \ldots, \ell_{i,M})$ （全局向量 + 局部向量，文中取 $M=4$）

**对比损失**（等效商品监督 + 同类别困难负样本）：
设正对关系 $\mathcal{R}_{\text{EP}}$（同一底层商品的不同listing），困难负样本集 $\mathcal{H}(i)$。信息噪声对比损失（soft-target InfoNCE）：
$$ \mathcal{L}_{\text{CL}}(\mathcal{R}) = -\frac{1}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} \sum_{k \in \mathcal{C}(i)} q_{i,k} \log \frac{\exp(\text{sim}(g_i,g_k)/\tau)}{\sum_{u \in \mathcal{C}(i)} \exp(\text{sim}(g_i,g_u)/\tau)} $$
其中 $\mathcal{C}(i) = \mathcal{P}_{\mathcal{R}}(i) \cup \mathcal{H}(i) \cup \mathcal{N}(i)$，$q_{i,k}$ 对正对赋权重1，困难负样本赋权重 $\alpha \in (0,1)$，其余负样本权重0，并做归一化。$\text{sim}$ 是余弦相似度，$\tau$ 为温度系数。

**重建损失**：
使用冻结的Qwen3-4B解码器 $D_\psi$ 和可训练适配器 $A_\eta$，将商品表示 $Z_i$ 映射为解码器条件token，通过下一个token预测进行三类重建：
- 类别重建：$Z_i^{\text{cat}} = (g_i)$，prompt + 目标 $y_i^{\text{cat}}$
- 图片描述重建：$Z_i^{\text{cap}} = (g_i, \ell_{i,1}, \ldots, \ell_{i,M})$，prompt + 目标 $y_i^{\text{cap}}$
- 属性重建：$Z_{i,m}^{\text{attr}} = (g_i, \ell_{i,m})$，prompt + 目标 $y_i^{\text{attr}}$

损失函数：
$$ \mathcal{L}_{\text{NTP}}(Z_i, q_i, y_i) = -\sum_{r=1}^{|y_i|} \log p_\psi(y_{i,r}| y_{i,<r}, q_i, A_\eta(Z_i)) $$
最终重建损失：
$$ \mathcal{L}_{\text{TR}} = \frac{1}{|\mathcal{B}|} \sum_{i \in \mathcal{B}} (\ell_i^{\text{cat}} + \ell_i^{\text{cap}}) + \frac{1}{|\mathcal{B}|M} \sum_{i \in \mathcal{B}} \sum_{m=1}^M \ell_{i,m}^{\text{attr}} $$
总表征损失：$\mathcal{L}_{\text{rep}} = \mathcal{L}_{\text{CL}}(\mathcal{R}) + \lambda_{\text{TR}} \mathcal{L}_{\text{TR}}$。

#### 1.2 混合全局–局部SID Tokenization

**全局前缀 (Global RQ Prefix)**：
对全局向量 $g_i$ 进行残差量化 (RQ-VAE)，$K$ 层码本 $\mathcal{C}_k^G = \{e_{k,c}^G\}_{c=1}^{V_k^G}$。
设 $r_{i,0} = g_i$，逐层选择：
$$ z_{i,k}^G = \arg\min_{c} \| r_{i,k-1} - e_{k,c}^G \|_2^2, \quad r_{i,k} = r_{i,k-1} - e_{k,z_{i,k}^G}^G $$
得到前缀序列 $G_K(i) = (z_{i,1}^G, \ldots, z_{i,K}^G)$，文中使用 $K=2$。

**局部后缀 (Local VQ Suffix)**：
局部向量 $\ell_{i,m}$ 分别通过VQ量化，码本 $\mathcal{C}_m^L = \{e_{m,c}^L\}_{c=1}^{V_m^L}$：
$$ z_{i,m}^L = \arg\min_{c} \| \ell_{i,m} - e_{m,c}^L \|_2^2 $$
得到后缀序列 $L_M(i) = (z_{i,1}^L, \ldots, z_{i,M}^L)$，文中使用 $M=4$。

最终SID：$G_2(i) \parallel L_4(i)$。码本大小未公开。

#### 1.3 轻量级验证
在25万商品子集上，固定4B基座LLM，进行少量SID对齐和SFT后，测试双向接地：
- 正向：详细描述 → SID解码 → 目录商品解析，评估命中率
- 反向：SID输入 → 描述/属性恢复，评估ROUGE-L等

### 2. SID Token Alignment

**目标**：为新添加的SID token建立与语言token的关联，使模型能将SID视为可操作的商品标识符。

**数据**：商品目录的 item-描述 ↔ SID 重建对，约200B tokens，覆盖全部1.2B商品。

**训练设置**：
- 冻结原始LLM的所有参数，仅训练新增的SID token嵌入层
- 优化器：Adam，峰值学习率 $1\times10^{-4}$
- 序列长度：1024 tokens
- 训练1个epoch
- 最终选用的 $G2+L4$ SID词汇量由码本大小决定（如256×256或更大）

### 3. 领域继续预训练 (Domain CPT)

**目标**：注入购物领域知识，使模型理解商品目录结构、用户偏好与行为的语义，同时保持通用能力。

**数据混合** (表2)：
- 购物数据 (66.6% tokens, 91.0% examples)：
  - 目录-SID接地：240.7M 样本，31.33B tokens（如SID-标题/属性配对）
  - 意图/行为到商品接地：34.7M 样本，40.84B tokens（查询-商品映射、序列预测、文本化推荐等）
  - 用户偏好理解：200K 样本，3.67B tokens（长行为序列摘要）
- 通用重放数据 (33.4% tokens, 9.0% examples)：知识推理、指令跟随、数学编程
- 领域:通用 token 比 = 2:1

**训练设置**：
- 从SID对齐后的检查点开始，更新全部参数
- 上下文长度：20,480
- 优化器：Adam，峰值学习率 $5\times10^{-5}$，1000步warmup后恒定
- 训练1个epoch

### 4. 后训练-SFT

**目标**：将模型对齐到ShopX动作协议和各类商品任务格式。

**数据混合** (表3)：
- 通用数据占74.9% tokens（81.2% examples）：通用指令、多轮对话、工具使用、数学、代码
- 购物数据占25.1% tokens（18.8% examples）：
  - SID原生实现：542.9K 样本，1.33B tokens（SID-文本对齐、文本化排序、SID检索/排序、文本-SID交错推荐）
  - 用户/上下文理解：229.0K 样本，1.07B tokens（画像/行为摘要、证据抽取）
  - 购物对话：300.4K 样本，148.7M tokens（多轮引导、商品比较、偏好约束细化）

**训练设置**：
- 全参数微调，使用Qwen3 chat模板
- 上下文长度：81,920
- 优化器：Adam，峰值学习率 $5\times10^{-6}$，300步warmup后恒定
- 训练1个epoch

### 5. 后训练-OPD–RL联合优化

**目标**：强化SID预测准确性，恢复通用能力，并对排序、文本-SID交错等任务引入结果级奖励。

**任务路由与教师/奖励分配** (表4)：
- 五个任务族各占20% prompts，每步采样256个prompt，每个prompt生成16条轨迹

| 任务族 | 解码方式 | 教师信号 | 奖励信号 |
|--------|----------|----------|----------|
| General | 随机采样 | General Teacher (预对齐基座) | 通用回答质量 judge 奖励 (0-1) |
| SID Prediction | Beam search | SID Prediction Teacher (SFT后继续用SID数据微调) | 无 |
| Ranking | 随机采样 | 无 | NDCG奖励 |
| Interleave | 随机采样 | 无 | Interleaved Fulfillment Reward |
| Other | 随机采样 | Self Teacher (冻结的SFT模型) | 无 |

**MOPD目标**：
对于有教师监督的任务 $k \in \{\text{General, SID Prediction, Other}\}$，计算 token 级权重：
$$ \hat{A}_{\text{Teacher},g,t}^{\phi(k)} = \textbf{sg}\left[ \log \frac{\pi_{\phi(k)}(y_{g,t}|x,y_{g,<t})}{\pi_\theta(y_{g,t}|x,y_{g,<t})} \right] $$
MOPD损失：
$$ \mathcal{L}_{\text{MOPD}}(\theta) = -\mathbb{E} \left[ \frac{1}{G}\sum_{g=1}^G \sum_{t=1}^{T_g} \hat{A}_{\text{Teacher},g,t}^{\phi(k)} \log \pi_\theta(y_{g,t}|...)\right] $$

**奖励设计**：
- *General reward*: LLM judge对响应打分(0-10)，归一化到[0,1]
- *Interleaved Fulfillment Reward*: 组合以下三项：
  1. 规则惩罚：缺失SID、重复、超长等
  2. 分层SID匹配得分：预测与参考SID的最优匹配，按最深匹配前缀深度计分
  3. 目录接地judge得分：将SID展开为商品元数据，由LLM judge评估美观性、意图满足度等多元化（归一化）
  最终奖励 = (judge得分 + SID匹配得分) × 规则惩罚系数
- *Ranking reward*: 输出有效排列则NDCG得分，否则零。

**联合目标**：
对于任务族 $k$，每条轨迹优势为：
$$ \hat{A}_{g,t}^k = \mathbf{1}[k \in \mathcal{K}_{\text{OPD}}] \hat{A}_{\text{Teacher},g,t}^{\phi(k)} + \alpha_k \mathbf{1}[k \in \mathcal{K}_R] \hat{A}_{\text{Reward},g}^{\psi(k)} $$
其中 $\hat{A}_{\text{Reward},g}$ 是群组归一化的奖励优势（GRPO风格），$\alpha_k$ 为任务特定权重。最终损失：
$$ \mathcal{L}_{\text{Joint}}(\theta) = -\mathbb{E} \left[ \frac{1}{G}\sum_{g=1}^G \sum_{t=1}^{T_g} \hat{A}_{g,t}^k \log \pi_\theta(y_{g,t}|...)\right] $$

**训练设置**：
- 共200步，batch size 256，$G=16$
- SID Prediction 使用6级beam search (beam size 渐进 [8,32,64,64,64,64])
- 优化器：Adam，恒定学习率 $5\times10^{-7}$，前50步warmup

### 6. 服务框架 (Serving Harness)

- **动作协议**：
  - `Plan`: 输入当前查询、上下文、历史；输出执行计划（检索/排序/捆绑/澄清等）
  - `Execute`: 输入计划、意图、种子商品等；通过SID beam search或生成进行商品操作，并可查询Catalog获得元数据
  - `Fulfill`: 输入选定的商品、证据、上下文；输出文本-SID交错的回复
  - `Update`: 输入当前轮次交互信息；输出状态更新信号（偏好记忆等）
- **支撑界面**：
  - `Context`: 用户画像、行为序列、会话信息
  - `Catalog`: SID到商品元数据的解析服务
  - `State`: 多轮状态存储，模型可读写
- **检索细节**：SID beam search，在能力诊断时使用 progressive beam schedule (与训练一致)；框架评估时用 beam size 30。

## 实验设置与结果

### 框架级评估
基于淘宝生产日志构造，1.2B商品快照，279单轮+80多轮任务（真实用户查询）。对比ShopX-4B/8B与工具中介系统InteRecAgent (Qwen3-8B) 和 Chat-REC (Qwen3-8B)，工具方提供检索+排序API。

**指标定义**（0-100）：
- Intent Fulfillment: 单轮意图满足率+多轮目标达成率
- Item Precision: 单轮类别精确度
- Ranking Quality: NDCG@5
- Category Coverage: 单/多轮类别覆盖度
- Personalization: 画像对齐程度
- Constraint Grounding: 约束、偏好遵循度
- Feedback Adaptation: 多轮反馈响应
- Cross-turn Reference: 跨轮次商品引用解析

**结果** (选取部分)：

| 系统 | 意图实现 | 商品精确 | 排序质量 | 类别覆盖 | 个性化 | 约束接地 | 反馈适应 | 跨轮引用 |
|------|----------|----------|----------|----------|--------|----------|----------|----------|
| ShopX-4B | 65.6 | 91.1 | 92.0 | 84.7 | 65.7 | 74.7 | 66.5 | 60.9 |
| ShopX-8B | 69.2 | 95.0 | 95.5 | 83.9 | 65.9 | 76.4 | 71.5 | 68.3 |
| InteRecAgent | 59.5 | 89.8 | 90.0 | 77.1 | 63.4 | 71.8 | 55.9 | 41.8 |

ShopX在各指标全面超越工具中介方案，尤其在反馈适应和跨轮引用上优势显著。

### 能力诊断
在四项诊断任务上评估模型本身（固定harness），部分结果如下：

| 能力块 | 任务示例 | 主要指标 | ShopX-4B | 通用LLM (基线) |
|----------|----------|----------|----------|----------------|
| 购物语义 | 意图摘要、商品联想 | Judge评分 | 显著更高 | - |
| 上下文证据抽取 | 画像/行为相关信号提取 | 相关得分/IoU | 较优 | - |
| 文本化推荐 | 个性化顺序推荐 | HR@64 | 0.195 | 0.117 (GPT-4) |
| 商品空间实现 | 描述到商品解析 | HitRate@64 | 0.574 | - |
| 商品空间实现 | 文本-SID交错实现 | rubrics评分 | 83.1 | - |

ShopX展现出较强的商品语义理解和SID操作能力。

### 消融实验关键结论

- **SID设计**：多向量MV显著优于单向量SV；混合 G2+L4 比纯全局 G6 在语义恢复和生成操控性上更佳。
- **CPT数据混合**：领域:通用 2:1 比例在保持通用能力的同时最大化购物指标。
- **后训练策略**：联合OPD–RL在所有能力块上均带来提升；仅SFT会损害通用能力，仅RL奖励在SID预测上训练不稳定。多教师设置中，General Teacher 对维持通用能力至关重要。

## 思考与可参考价值

**局限性**：
- 依赖海量商品目录数据和预训练资源，SID构建需大规模多模态编码器训练
- 混合SID对新品冷启动仍不够灵活，码本固定可能需定期更新
- 评估基于仿真用户和LLM judge，对真实用户场景的泛化性待验证
- OPD–RL联合训练需维护多个教师和奖励函数，工程复杂度较高

**可借鉴点**：
- **模型原生商品空间操作**范式：将检索、排序等传统模块融入LLM内部，减少工具接口的信息损失，可推广至其他垂直领域的agent设计
- **语义ID设计**：RQ-VAE生成全局可自回归的前缀，VQ补充局部语义的混合方案，为LLM可操作的商品表示提供了可复用的思路
- **保留通用能力的多阶段训练配方**：SID对齐→领域CPT（带通用重放）→均衡SFT→多教师+奖励联合优化，平衡专业化和通用性，对需要注入领域知识的LLM应用有参考价值
- **联合蒸馏与RL**：利用教师token级监督 + 任务特定奖励的联合框架，在推荐/搜索等具有明确结果信号的任务中，较纯RL或纯SFT更有效。
