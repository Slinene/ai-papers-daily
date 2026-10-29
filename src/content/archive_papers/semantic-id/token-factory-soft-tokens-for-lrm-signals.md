---
title: "Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation Models"
authors: "Xilun Chen, Shao-Chuan Wang, Baykal Cakici, Lukasz Heldt, Lichan Hong et al. (9 人)"
affiliation: "Google"
date: "2026-06"
venue: "RecSys 2026"
topic: semantic-id
topic_name: Semantic ID
topic_icon: 🗂
idea: "把“文本化 SID + 自定义 token 表示稠密特征”的 prompt 范式，换成“传统特征 → soft token”的新模态：每个历史行为把 SID、频道、客户端、观看时长等异构特征拼接后经 MLP 投成 1 个 d_model 维 soft token，与文本 token 交错输入 LRM（PLUM）。每条历史从 12 个文本 token 压到 1 个，prompt 1536→480 时排序 AUC 持平、训练提速约 200%；生成式召回线上 Unique Impressions +16.8%，1 天新视频 +67.1%。"
paperUrl: https://arxiv.org/abs/2606.19635
codeUrl: null
tags:
- "Soft Token"
- "Feature-to-Token Projection"
- "Prompt Compression"
- "PLUM / YouTube"
- "Long Sequence Compression"
unverified: false
---
## 核心思路

Google PLUM 这类大推荐模型（LRM）把物品表示为文本化 Semantic ID，传统推荐特征（完播率、观看时长、距今时间、设备、人口属性等）则用自定义 tokenizer 变成文本 token。这样一条观看历史在排序任务里要占 12 个 token（8 个 SID + 1 个频道 + 3 个稠密特征），200 条历史就把 prompt 撑到 1536 以上。

Token Factory 的做法是把所有传统信号当作一种新模态：每个 **Token Maker** 把一组异构特征拼起来，经可微映射 G（通常是 MLP）直接输出固定数量的 d_model 维 **soft token**，与文本 token 交错放进 prompt，并和 LRM 端到端联合训练。一条观看历史从 12 个文本 token 变成 1 个 soft token。

核心论点有两层：
1. **效率**：prompt 长度可控且确定，训练/推理更便宜；
2. **质量**：省下的上下文可以换成更长的历史、更大的 batch，同时 soft token 能融合更多交互特征。

## 整体实现思路

视频推荐场景中，Token Factory 由三个 Token Maker 组成：

| Token Maker | 输入 | 输出 |
|---|---|---|
| WH Token Maker | 每条观看历史：视频 SID、频道名、客户端信息、观看时长等 | 每条历史 1 个 soft token |
| Query Token Maker | 用户/请求级特征（region、年龄、性别、设备等） | 若干 soft token |
| Candidate Token Maker | 候选视频级及其他非 query 级特征 | 若干 soft token |

Prompt 的变化：

- 之前（PLUM 文本 SID）：`A100 B100 C100 D100 E100 F100 G100 H100 5.00% 50.00s 2.5h | ... region PH | user 32 years female | device small ANDROID | video baby shark...`
- 之后：`[watch_history]<emb><emb>...<emb>[end_watch_history] <emb>...<emb> video baby shark <emb><emb>...<emb>`

视频标题等文本仍保留，以利用 LM 的语言理解能力。query 级 soft token 在同一请求的多个候选之间不变，可以预计算并用 prefix cache 复用。

论文列出的架构收益：prompt 紧凑、长度确定（每个 Token Maker 固定输出数）、可装下更长的交互序列、训练和服务更高效。

## 子模块实现（可复现细节）

### Token Maker

- 原始特征 F_input = [f1; f2; ...; fn]，每个特征按类型做归一化或 embedding lookup，得到 t_i(f_i)。
- 拼接：E_input = Concat(t1(f1), t2(f2), ..., tn(fn))。
- 映射：T_output = G(E_input)，G 输出 N × d_model 的向量，再 reshape 成 N 个 soft token。
- G 可以是 MLP，也可以是更复杂的网络或 Transformer；与 LRM 端到端共训，使 soft token 对齐 LM 的语义空间和任务目标。
- N 的选取按经验：简单特征 N=1；长交互序列压到固定小预算（例如 N=10）。
- 观看历史：对每条历史逐条施加同一投影，得到与历史等长的 soft token 序列。

论文未给出 MLP 层数、隐藏维、d_model、sparse 特征 embedding 表规模、初始化和学习率等细节。

### 序列二次压缩

当历史有成千上万条时，1 条 1 token 仍不够省：

1. **MLP 压缩**：历史 soft token 形状为 [batch_size, N, token_dim]，在第二维（序列维）施加形状 [N, ..., M] 的 MLP，把 N 个 token 压成 M 个，压缩比 M/N。
2. **注意力池化**（借鉴 LONGER）：轻量 Transformer，每 K 个 item 以最后一个 item 做 attention pooling，汇成 1 个 soft token，压缩比 1/K。

论文的长历史实验使用 10% 压缩比，但没有说明用的是哪种压缩方法，也没有对比两种方法。

### 与 LRM 的集成

- 排序：PLUM，基于 110M 参数 MoE 版 Gemini encoder，预测下一视频点击（CTR）。
- 生成式召回：PLUM，基于 210M 参数 MoE 版 Gemini decoder，输出下一视频的 SID。
- 输入侧历史改成 soft token 后，SID 子 token 之间不再有 token 级注意力；输出侧（召回）仍生成文本 SID。

## 实验设置与结果

### 排序（CTR）

| 设置 | 每条历史 token 数 | prompt 长度 | 历史条数 |
|---|---|---|---|
| 基线（文本 SID + 自定义 token） | 12（8 SID + 1 频道 + 3 稠密） | 1536（超出左截断） | 200 |
| Token Factory | 1 | 480 | 200 |

- 同 global batch：处理组初期 AUC 偏低，约 **1.5M 步**追平基线并此后持平。作者解释为新增的 Token Maker 和 sparse embedding 表是随机初始化，需要从头学习投影。
- prompt 长度约为基线 **30%**，训练速度提升约 **200%**。
- 处理组 global batch 增大 200% 后，从训练早期起 AUC 就**超过**基线。
- 以上结论只以 AUC 曲线图呈现，正文没有具体 AUC 数值。

### 生成式召回（YouTube 首页）

| 设置 | 每条历史 token 数 | prompt 长度 |
|---|---|---|
| 基线 | 5（SID 序列随机哈希 1 + 频道哈希 1 + 稠密 3），人口属性为文本 | 768 |
| Token Factory | 1，人口属性也转为 soft token | 256（含 200 条历史） |

| 离线 Recall@10 | Unique Impressions | Unique Impressions（1 天新鲜） | Satisfied Watchers | Satisfied Watch Time |
|---|---|---|---|---|
| +2.0% | +16.8% | +67.1% | +0.04% | +0.05% |

作者将新鲜视频曝光大涨归因于更完整地利用了特征和更长的交互序列（这是作者的解释，未做归因实验）。

### 消融（排序，固定 480 token，batch 32k，超长左截断）

| 变体 | 说明 |
|---|---|
| Baseline | 同上文排序处理组（soft token 历史 + 全部特征） |
| WH_SID | 历史改回文本 SID |
| NO_FEAT | 去掉历史以外的所有传统 dense/sparse 特征 |
| WH_SID_NO_FEAT | WH_SID 且去掉所有传统特征 |
| NO_FEAT_STRICT | NO_FEAT 且历史 soft token 只含 SID + 频道 ID |

观察（只有图，无数值）：
- 特征齐全时，soft token 与文本 SID 没有明显差距；
- NO_FEAT_STRICT 优于 WH_SID_NO_FEAT：480 预算下 soft token 能放下 200 条历史，文本 SID 会被截断；
- NO_FEAT 优于 NO_FEAT_STRICT：往每个 soft token 里融入更多交互特征仍对 CTR 有帮助。

### 更长历史

历史从 200 扩到 500，新增 300 条按 10% 压缩比压成 30 个 soft token（prompt 比基线多 30 token），AUC **+0.08%**。

### 注意力可视化（附录 A）

- 文本 SID 模型：高频首位码（如 A1909）在整段历史上几乎不被注意，近一半文本 SID token 基本没有注意力；均值注意力高度稀疏，集中在少数 token 上，作者认为存在表示冗余。
- soft token 模型：所有 soft token 都有非零注意力，均值注意力图更稠密、更分散，不同头和层捕获互补信号。

## 思考与可参考价值

**这篇论文本质上是一份工业经验报告**：思路接近 CoLLM 的“协同 embedding → MLP → LLM token”，但推广到任意异构特征和长序列，并在 YouTube 规模上做了线上验证。贡献在于把这件事工程化、模块化，并给出“效率 → 更大 batch / 更长历史 → 质量”的证据链，而不在于方法新颖。

**对电商生成式推荐 / SID 的启发：**
1. 电商行为序列带有行为类型（点击/加购/下单）、价格、停留时长等丰富交互特征。“SID embedding + 行为特征 → MLP → 1 token/条”比把多位 SID 和特征全部文本化省得多，同样的上下文能装下 3-5 倍的历史。
2. 与 last100 + Q-Former 这类压缩方案同构。本文说明单条 1 token 的朴素 MLP 已经能和文本 SID 持平，二次压缩可以先试序列维 MLP 或每 K 条 attention pooling，作为 Q-Former 的轻量对照（推断）。
3. 用户/请求级特征做成前缀 soft token 并配合 prefix cache，对排序阶段多候选打分有直接的延迟收益。
4. 注意力图可以当诊断工具，检查文本 SID 首位码是否被忽略、注意力是否冗余。

**落地前要确认的事：**
- 新增的随机初始化模块需要约 1.5M 步才追平，要预留训练预算或设计热启动（例如用已有 SID embedding 初始化，推断）。
- 召回时输入是 soft token、输出仍是 SID 词表，两侧表示是否需要对齐，论文没有讨论。
- 召回对比中基线历史是单 token 哈希、人口属性仍是文本，处理组同时改了多处，+16.8% 难以拆分归因。
- 排序与消融只有曲线没有数值，MLP 结构等细节未披露，复现需要自己补实验：固定上下文预算，对比文本 SID 与 soft token。
- 新品冷启动下 soft token 的表现需要单独评估；1 天新鲜视频 +67.1% 是很强的信号，但机制没有拆解。
