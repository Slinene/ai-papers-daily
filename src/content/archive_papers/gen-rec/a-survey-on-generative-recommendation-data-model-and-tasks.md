---
title: "A Survey on Generative Recommendation: Data, Model, and Tasks"
authors: "Min Hou, Le Wu, Yuxin Liao, Yonghui Yang, …, Han Wu, Richang Hong (9 人)"
affiliation: 合肥工业大学 × 新加坡国立大学
date: 2025-10
venue: arXiv (投稿 Elsevier)
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: |
  200+ 篇论文的生成式推荐全景综述，最大价值不是"又一份清单"，而是它选定的切分维度：不按模型类型分类，而是按生成能力**注入推荐流水线的哪个环节**分成 data / model / task 三层——数据层（用 LLM 造数据与统一异构信号）、模型层（LLM-based / 大推荐模型 LRM / 扩散三条路线）、任务层（对话、可解释、推理、个性化内容生成）。这个切法同时对应了该领域的历史演进顺序：早期只敢用 LLM 补数据，中期把生成机制搬进架构，现在扩展到全新任务形态。文中最实用的是四张对照表——文本 prompt / 协同信号 / item tokenization 三类对齐范式的代表工作逐条列了 backbone 与用户建模方式，以及把 SFT / SSL / RL / DPO 四种训练目标写成统一公式并列。另一条硬结论：生成式**并非普遍优于**判别式，只在数据稀疏跨域、天生生成型任务、大规模训练三种条件下才有可靠增益。
paperUrl: https://arxiv.org/abs/2510.27157
codeUrl: null
tags:
  - Survey
  - Generative Recommendation
  - Large Recommendation Model
  - Item Tokenization
  - Diffusion Rec
unverified: false
---

## 核心思路

**一句话问题**：生成式推荐这两年爆炸式增长，但已有综述（2024 年及以前）大多停在「LLM 怎么用在推荐里」的层面，漏掉了 2025 年之后的 agent 化推荐、超越 SFT 的训练范式、以及工业界的大推荐模型（LRM）路线。

**关键 idea**：不按「模型是什么」分类，而是按**生成能力被注入推荐流水线的哪个环节**分类——data / model / task 三层。

这个切分之所以值得单独说，是因为它同时是**方法学维度**和**历史演进轴**：

- **早期**：只敢用生成模型补数据（造 profile、造交互、补图谱）——data-level
- **中期**：把生成机制搬进推荐架构本身（生成式检索、扩散去噪、LRM）——model-level
- **现在**：扩展到判别式根本做不了的新任务（对话、解释、推理、个性化内容生成）——task-level

![Figure 2：survey 的整体组织框架——data / model / task 三层机会 + 三类开放挑战](/ai-papers-daily/figures/a-survey-on-generative-recommendation-data-model-and-tasks/fig1.png)

**范式区分（第 2 章的地基）**。判别式学的是条件概率 $P(y|x)$，生成式学的是联合分布 $P(x,y)$。落到推荐上：

```
判别式：学打分函数 f(u,i)，推理时 TopK_u = Top-K_{i∈I} f(u,i)
        损失 = MSE(显式) / BCE(pointwise) / BPR(pairwise)
        ——必须有预定义候选集，逐个打分再排序

生成式：直接生成目标 item 的标识（token 序列 / 文本 / 语义码）
        ——无需候选集，可开放域生成
```

论文把生成式的优势归纳为五条：**世界知识**、**自然语言理解**、**推理能力**、**Scaling Law**、**创造性生成**。

**但最值得记住的是它诚实地划了边界**（§2.3）——生成式**不是**普遍优于判别式，只在三种条件下有可靠增益：

1. **数据稀疏 / 跨域场景**：LLM 的世界知识补偿行为信号不足，冷启动、zero-shot 上判别式追不上
2. **天生生成型任务**：对话推荐、可解释推荐、个性化内容创作——判别式打分函数根本无法提供开放式生成
3. **大规模训练体制**：如 HSTU 所证，生成式架构享受 scaling law，判别式过了某个规模就 plateau

这三条是我认为整篇综述最有决策价值的部分——它直接回答了「我这个场景该不该上生成式」。

## 整体实现思路

survey 的组织即是它的"pipeline"，三层各自的输入输出如下：

| 层 | 输入 | 生成模型做什么 | 输出 |
|---|---|---|---|
| **Data (§3)** | 原始 $(\mathcal{U}, \mathcal{I}, \mathcal{A})$ | $\mathcal{U}', \mathcal{I}', \mathcal{A}' = G_{data}(\mathcal{U},\mathcal{I},\mathcal{A} \mid \theta_g)$ | 增强后的训练集 |
| **Model (§4)** | 用户历史 + item | 作为核心推荐引擎（LLM / LRM / Diffusion） | 直接生成推荐 |
| **Task (§5)** | 用户意图 | 重构任务形态 | Top-K / 解释 / 对话 / 新内容 |

三层之上是三类开放挑战：**Data（缺动态交互式 benchmark、指标失配）**、**Model（偏置与鲁棒性）**、**Deployment（训练与推理效率）**。

## 分层拆解（技术细节）

### 一、Data-Level：生成模型当数据工厂

#### 1.1 开放世界知识增强（四类，附代表作）

| 类型 | 做什么 | 代表工作 |
|---|---|---|
| **Content Aug.** | 生成用户/item 的自然语言 profile、总结历史、补稀疏元数据 | ONCE (WSDM'24)、LLM-Rec (NAACL'24)、KAR (RecSys'24)、SeRALM (SIGIR'24)、LettinGo (KDD'25) |
| **Representation Aug.** | 自动特征构造、多模态属性抽取、层级类目生成 | DynLLM、GE4Rec (ICML'24)、HyperLLM (SIGIR'25) |
| **Behavior Aug.** | 生成伪交互，解决冷启与公平性 | ColdLLM (WSDM'25)、LLM-FairRec (SIGIR'25)、LLM4IDRec (TOIS'25) |
| **Structure Aug.** | 关系发现、图补全、知识图谱构建 | LLMRec (WSDM'24)、CORONA (SIGIR'25)、LLM-KERec (CIKM'24)、COSMO (SIGMOD'24) |

**这里有一条容易被忽略的技术要点**：原始 LLM 知识与推荐目标是**不对齐**的。SeRALM 用对齐导向的 prompt 引导 LLM 生成「面向推荐目标」的描述并过滤噪声；LettinGo 更进一步——用**生成的 profile 对推荐结果的实际影响**做 DPO，让 profile 自适应。TRAWL 则把生成文本编码成 embedding 后用 adapter 对齐到推荐任务空间。**「LLM 生成的文本 ≠ 对推荐有用的文本」这个 gap 需要显式建模**，这是所有做数据增强的人都会踩的坑。

#### 1.2 Agent-based 行为模拟

- **交互模拟**：Agent4Rec（事实记忆 + 情感记忆的用户 agent）、AgentCF（**同时**模拟 user agent 与 item agent，把协同过滤的概念 agent 化）、STEAM（结构化演化记忆，突破"单条被覆写的偏好摘要"，保留多面兴趣并追踪演化）、SimUSER / SUBER（情景记忆 + persona grounding + MDP 交互规划）
- **社会模拟**：RecAgent（交互式沙盒，研究信息茧房与从众）、GGBond（基于兴趣相似度/人格兼容性/结构同质性建模社交纽带演化）

### 二、Model-Level：三条并行路线

#### 2.1 LLM-based 生成式推荐

**（a）四种对齐范式**——这是全文最实用的一张图，把「怎么把用户历史喂给 LLM」的设计空间说清楚了：

![Figure 6：对齐 LLM 做推荐的四种范式——(a) 文本元数据 (b) 协同 token (c) ID 数字 (d) 可训练 ID token](/ai-papers-daily/figures/a-survey-on-generative-recommendation-data-model-and-tasks/fig2.png)

按「用户 profile 如何注入结构」分三大类：

**① 文本 prompting**：完全用自然语言构建 profile。TALLRec 在模板里插显式偏好陈述 + LoRA 轻量适配；LlamaRec 先用序列推荐器**收缩候选集**再给 LLM；Reason4Rec 用评论抽取偏好与显著属性。**短板**：缺显式协同信号，item 间依赖关键的场景排序质量不足。

**② 协同信号注入**：三个方向——(i) 把协同与语义表征映射到共享空间再拼接（iLoRA / LLaRA / CoLLM / E4SRec）；(ii) LLM 辅助摘要喂给传统推荐器（CORONA 用 LLM 推理 + GNN 的粗到细流水线）；(iii) **把协同信号"口语化"**——CoRAL 直接写成句子 "User A also prefers X, Y, Z"，绕开 dense embedding 对 LLM 不可读的问题。**短板**：dense embedding 需要投影或 verbalize，这个映射本身引入协同-文本语义 gap。

**③ Item Tokenization**（五个演进阶段，最值得关注）：

| 阶段 | 做法 | 问题 / 代表 |
|---|---|---|
| (i) ID-based | 每个 user/item 一个特殊 token | 词表爆炸、无语义、冷启差（P5、CLLM4Rec） |
| (ii) Text-based | 用标题/描述当标识 | 序列过长、无协同知识（BIGRec、M6、IDGenRec） |
| (iii) Codebook-based | 离散码序列（Semantic ID） | 紧凑但难平衡文本与协同（**TIGER**、LC-Rec、ActionPiece） |
| (iv) Codebook + CF | 把协同信号灌进 tokenization | **LETTER**（RQ-VAE + 对比对齐）、TokenRec（量化 masked embedding）、SETRec（历史编码为无序集）、CCFRec（code masking）、LLM2Rec |
| (v) 自适应 tokenization | **让 LLM 自己在训练中refine 标识** | SIIT——缓解外部 tokenizer 带来的不一致 |

**（b）四种训练目标（统一公式并列，可直接对照实现）**：

```
SFT   :  L = − log π_θ(y⁺ | x)
SSL   :  L = − log [ exp(sim(y⁺,y⁻)/τ) / Σ_{y∈N} exp(sim(y⁺,y)/τ) ]
RL    :  L = − [ r_φ(x,y⁺) − β · D_KL( π_θ(y|x) ‖ π_ref(y|x) ) ]
DPO   :  L = − log σ( β·log[π_θ(y⁺|x)/π_ref(y⁺|x)] − log[π_θ(y⁻|x)/π_ref(y⁻|x)] )
```

各自的边界条件说得很清楚：**SFT 只学正样本、无显式负例**，学不到排序 margin；**SSL** 降低对人工模板依赖（EasyRec 做文本-行为对齐）；**RL** 能建模负例与不可导指标，但需大规模反馈、训练不稳；**PO** 免 reward model（RosePO 定制偏好构造、SPRec 用 self-play 稳定训练）。

**（c）推理侧**：Reranking（RecRanker 两阶段 + position shifting 缓解输入偏置；LLM4Rerank 多节点多跳推理权衡准确/多样/公平；GFN4Rec 用 GFlowNets 自回归生成列表）与 Acceleration（FELLAS 只让 LLM 出 embedding、轻量模型做预测；GenRec prompt 蒸馏；**AtSpeed 用投机解码 + 树注意力做到 2–2.5× 加速且保持 Top-K 一致性**）。

#### 2.2 大推荐模型（LRM）——工业界最该看的一节

![Figure 7：LRM 的两个方向——(a) LRM 架构 (b) 端到端替代级联架构](/ai-papers-daily/figures/a-survey-on-generative-recommendation-data-model-and-tasks/fig3.png)

**动机是两个工业瓶颈**：① 判别式模型复杂度的边际收益递减（DIN → MIMN 提升越来越小，所有大厂同一规律）；② 级联架构（召回→粗排→精排→重排）维护成本与层间通信/缓存开销爆炸。

**方向一：原生 Scaling Law**。Meta 的 **HSTU** 是里程碑——把 CTR 判别任务改成生成式序列建模，将同一用户的多条 pointwise 样本合并成**一条**包含交互 item、行为类型、用户与 item 类目特征的行为序列，因果自回归建模，把召回与排序统一成序列生成。序列长度 **1024–8192**（远超判别式能处理的长度），最终做到 **1.5 万亿参数仍在涨**，而判别式在 **~2000 亿**就停滞。衍生工作：美团 MTGR（补回 cross feature 防信息损失 + Group LayerNorm + 动态混合掩码）、小红书 GenRank（**把 item 当位置信息、只迭代预测 action**，避免 HSTU 拼接 item+action 导致序列翻倍，适合资源敏感的精排）。

**方向二：端到端替代级联**。快手 **OneRec** 用一个端到端生成模型替掉召回-粗排-精排：encoder-decoder + MoE 扩容量，**session-wise 生成整个推荐列表**（而非 pointwise），训练加一个 DPO 偏好对齐阶段。线上总观看时长 **+1.68%**，算力利用率 **11% → 28.8%**，运行成本仅为级联架构的 **10.6%**。OneSug 扩到 query 推荐（RQ-VAE 语义 ID + Reward-Weighted Ranking），EGA-V2 进一步把用户兴趣建模、POI 生成、创意选择、广告分配、计费统一进单个生成框架。

#### 2.3 扩散式生成推荐

分两大类：

**(A) 增强数据生成**——三个子范式：生成高质量交互数据（DGFedRS 预训练扩散捕获个性化信息；MoDiCF / TDM 处理模态缺失；DiffuRec 把表征当分布、注入高斯噪声带来不确定性与多样性）；生成鲁棒表征（ARD 精炼社交网络、DDRM / DRGO 学鲁棒表征）；偏好注入的条件生成（DMCDR 用源域偏好信号引导反向过程生成目标域用户表征；InDiRec 引导生成同意图的前向视图）。

**(B) 目标 item 生成**——**DiffRec** 把交互预测当去噪过程（L-DiffRec 处理大规模 item、T-DiffRec 处理时序）；**DreamRec** 对目标 item 加噪以探索 item 空间分布并直接生成推荐 item，**免负采样**且能探索整个 item 空间；DiQDiff 用语义向量量化增强引导鲁棒性 + 对比差异最大化区分不同用户的去噪轨迹；HorizonRec 提出 align-for-fusion 替代传统 align-then-fusion。另有专门针对**扩散推荐 embedding collapse** 的定制优化目标（ADRec、PreferDiff）。

### 三、Task-Level：生成模型解锁的新任务

**§5.1 Top-K 推荐的 grounding 问题**（生成式独有）——生成的 token 必须落到真实 item 上，三种策略：

1. **词表约束解码**：P5 用预定义 item 词表 + beam search；IDGenRec 用前缀树；Trie 类方法保证从第一个 token 起就合法——**但 Trie 严格从首 token 生成，准确率高度依赖前几个 token**。TransRec 用 **FM-index 实现位置无关的约束生成**（允许从合法标识的任意位置开始生成），并引入多面标识（ID/标题/属性）+ Aggregated Grounding Module 映射回库内 item。
2. **生成后过滤**：BIGRec 用生成 token 序列表征与 item 表征的 **L2 距离**做 grounding。高效可扩展，但重度依赖 item embedding 质量。
3. **Prompt 增强**：把候选集塞进 prompt 让模型从中选（LLaRA、A-LLMRec、iLoRA）。

**§5.2 个性化内容生成**——论文特意区分了它与通用 AIGC：**个性化内容生成是 preference-conditioned 且 task-situated 的**，目标是提升推荐体验而非产出独立创作。视觉侧 DiFashion（个性化穿搭组合）、DreamVTON（模板驱动优化 + normal-style LoRA 解决多视角一致性）、OOTDiffusion（outfitting UNet + outfitting dropout 实现 classifier-free guidance）；文本侧评论生成与新闻标题生成（PENS 基于微软新闻点击历史的个性化标题 benchmark）。

**§5.3 对话推荐**五个方向：prompting/zero-shot（off-the-shelf LLM 可超过有监督 CRS baseline）、检索增强/知识增强（缓解幻觉但增加延迟与知识维护成本）、统一架构（PECRS 重构为单一 NLP 任务、MemoCRS 引入记忆模块）、评估（BehaviorAlignment 主张评估策略是否符合人类预期而非只看准确率）。

**§5.5 推理推荐**三类：
- **显式推理**：Reason4Rec（deliberative recommendation，偏好蒸馏→偏好匹配→反馈预测的多专家框架）、Reason-to-Recommend（Interaction-of-Thought，把交互链组织成结构化推理路径，两阶段 SFT+RL）、OneRec-Think（从剪枝后的用户上下文抽取连贯推理轨迹再引导 CoT 生成，做工业噪声场景的上下文蒸馏）
- **隐式推理**：**LatentR³**（把推理编码成紧凑 latent token 序列而非长文本 CoT，SFT + RL）、ReaRec（推理位置嵌入 + 自回归处理隐状态做多步 latent 推理）、STREAM-Rec（**迭代残差推理**——逐步计算并拟合当前输出与目标行为表征的残差，中间残差修正即推理路径）
- **推理增强**：DeepRec（LLM 假设偏好 → 查询传统 RS 取候选 → 迭代精炼）、LLMRG（构造推理图再用 GNN 融入推荐模型）

## 开放挑战与评测现状

![Figure 9：判别式推荐 vs 生成式推荐助手——右侧同时列出了三类挑战](/ai-papers-daily/figures/a-survey-on-generative-recommendation-data-model-and-tasks/fig4.png)

### 评测指标的系统性失配（§6.2.1，我认为是全文第二有价值的部分）

论文把指标分成五类并逐一指出其在生成式场景下的失效原因：

| 类别 | 指标 | 用在生成式上的问题 |
|---|---|---|
| 排序 | NDCG@K, Recall@K, HR@K, MRR, AUC, CTR, CVR | **预设固定候选集 + 二值相关性标签**，对开放式生成根本不适用 |
| 内容质量 | BLEU, ROUGE-L, SBERT, LLM-E, FID | BLEU/ROUGE 靠词面重叠，反映不了自由personalized 生成的语义质量；LLM-E 灵活但**非确定性**且大规模评测成本高 |
| 多样性 | ILD, Coverage, Novelty | 很少与准确率**联合**优化或报告 |
| 公平性 | DP, EO | 同上，缺整体性评估 |
| 对话 | Success Rate, Average Turns | 严重依赖对话模拟器的保真度，而模拟器本身可信度存疑 |

**Agent 模拟当评测器的"鸡生蛋"困境**说得很到位：要建准确的用户模拟器需要大规模真实行为数据，而模拟的动机恰恰是补偿这类数据的缺失——结果模拟行为可能只反映预训练语料的分布偏置而非真实用户多样性。而且现有模拟框架多把用户建模成**固定 persona 的静态 agent**，捕捉不了偏好漂移、情绪驱动决策等动态性。

### 偏置与鲁棒性（§6.2.2）

- **流行度偏置**：**SFT 最大化似然容易在热门 item 上过拟合**、放大流行度偏置；**DPO 倾向压制非偏好响应**，强化数据中既有模式且对偏好对质量极度敏感
- **公平性**：模型可能从交互或预训练数据中**隐式利用人口统计属性**，按群体假设做推荐
- **位置偏置**：行为序列与候选 item 以文本序列输入，继承 LLM 自身的位置敏感性——候选数量、顺序、描述复杂度的微小变化都会改变注意力分布，**LLM 天然更偏好排在前面的 item**
- **文本模拟攻击**（新风险）：把目标 item 描述改写成语义相似、风格一致的虚假版本。相比传统需要注入大量恶意 profile 的攻击，**文本攻击成本极低、可黑盒执行、且在不同 LLM 推荐模型与任务间可迁移**——单个模型上定制的对抗 prompt 可能同时攻破多个系统。现有防御对数据投毒效果有限。

### 部署效率（§6.2.3）

推理侧最硬的约束：**推荐需要生成 Top-K 条不同的序列，必须用 beam search，这使得投机解码等 NLP 常用加速手段难以直接套用**。当前缓解手段主要是知识蒸馏（把 LLM 推荐模型蒸到轻量传统推荐器或小语言模型）。训练侧，PEFT 仍不足以应对数据规模增长；数据选择方法需要算每个样本的影响或梯度信息，开销大，且基于单条交互的选择会忽略交互间的相关性。

## 思考与可参考价值

### 可直接借鉴的点

1. **§2.3 的三条适用边界是最有决策价值的内容**。「数据稀疏跨域 / 天生生成型任务 / 大规模训练体制」——这三条可以直接当技术选型的 checklist。反过来说：如果你的场景数据密集、任务是纯打分排序、模型规模上不去，那生成式大概率是负收益。这比综述里任何一个方法都更该记住。

2. **Item tokenization 的五阶段演进是 Semantic ID 工作的完整地图**。特别是 (iv)→(v) 这一跃：从「外部 tokenizer 固定生成码」到「LLM 在训练中自适应 refine 标识」（SIIT）。我们做 SID 时用的是固定 RQ-VAE 码本，属于 (iii)/(iv)，**外部 tokenizer 与下游模型不一致**这个问题是真实存在的，值得跟进 (v)。另外 CoRAL 的「把协同信号口语化成句子」是个便宜且立刻能试的技巧。

3. **HSTU 的样本重组方式值得单独抄**：把同一用户的多条 pointwise 样本合并成一条包含 item、行为类型、类目特征的长序列做因果自回归——这个改造让序列长度从几十跳到 1024–8192，是解锁 scaling 的关键动作，而不是单纯把模型堆大。小红书 GenRank 的「item 当位置、只预测 action」对资源敏感场景是更实际的变体。

4. **OneRec 那组数字是端到端路线最有力的论据**：观看时长 +1.68%、算力利用率 11%→28.8%、运行成本仅级联的 10.6%。**成本降到 1/10 这条比指标提升更值得注意**——它说明级联架构的层间通信与缓存开销被严重低估了。

5. **Grounding 三策略对做生成式检索的直接价值**。Trie 约束解码「高度依赖前几个 token」这个已知缺陷，与我上一篇读的 APAO 指出的「Prefix 0 最关键」是**同一个现象的两种表述**——这进一步印证了浅层码的判别力是整条链路的瓶颈。TransRec 的 FM-index 位置无关生成是另一条绕开路径，值得对比评估。

6. **评测指标失配那张表可以直接拿去做内部评估体系的自查**。尤其「排序指标预设固定候选集 + 二值相关性」这条——一旦上了开放域生成，NDCG@K 就不再是可信的主指标了。

7. **文本模拟攻击是被低估的安全风险**。低成本、黑盒可执行、跨模型可迁移——对任何把 item 描述暴露给第三方（商家自填标题/详情）的电商场景，这是个现实威胁面，而现有防御「对数据投毒效果有限」。

### 局限与存疑

1. **综述的通病：广度换深度**。三层框架下每个分支都只有 1–3 句话 + 引用编号，读者拿到的是**索引而非理解**。真正要用某个方法仍必须回去读原文。这不算缺点，但要清楚它的定位——它是地图，不是教程。

2. **几乎没有横向定量比较**。全文没有任何一张「不同方法在同一 benchmark 上的性能对比表」，四张表列的都是「用了什么 backbone、怎么建模用户」这类**定性属性**。所以它无法回答「这些方法到底谁更好」，而这往往是读者最想知道的。

3. **Data-level 与 Model-level 的边界并不干净**。比如 item tokenization 既可看作数据表示（data）也可看作模型设计（model），LLM-as-Enhancer 同样横跨两层。论文把 tokenization 放在 §4.1 model 层，但 §3.2 的 data unification 里又讨论了多模态统一表示——这两处的界限读起来是模糊的。

4. **对失败案例与负面结果的收录几乎为零**。全文基本是「某方法提出了什么、取得了什么」的正向叙述。而这个领域里最有价值的信息之一恰恰是负面结果（比如序列级 DPO 在生成式推荐上常不如朴素 CE）。综述如果能系统收录「什么不 work」，价值会高一个量级。

5. **时效性问题已经开始显现**。v2 更新到 2026 年 5 月，但生成式推荐是月度迭代的领域——OneRec 系列已经出到 V2/Think，RecGPT 已到 V3，这些在文中只有一两句。任何做这个方向的人都不能只靠这篇。

6. **中文/国内工业界工作的覆盖偏薄**。快手 OneRec、美团 MTGR、小红书 GenRank 有提到，但淘宝 RecGPT 系列、字节侧的工作基本没有覆盖，而这些恰恰是落地最深的一批。

**一句话定位**：这篇适合当**领域地图与文献索引**用——建立框架、找相关工作、做技术选型自查（尤其 §2.3 三条边界和 §6.2 的指标失配表）；不适合当作理解某个具体方法的入口。
