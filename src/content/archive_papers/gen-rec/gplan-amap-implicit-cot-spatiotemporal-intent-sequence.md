---
title: "Generative Spatiotemporal Intent Sequence Recommendation via Implicit Reasoning in Amap"
authors: "Sicong Wang, Ruiting Dong, Yue Liu, Bowen Zheng, Jun Meng et al. (10 人)"
affiliation: "高德地图 AMAP × 阿里巴巴集团"
date: "2026-05"
venue: "RecSys 2026"
topic: gen-rec
topic_name: 生成式推荐
topic_icon: 🎯
idea: "把首页推荐从“逐个打分卡片”改成“生成一条带参数的工具调用序列（意图流）”，定义 GSISR 任务：序列要逻辑连贯且在时空约束下物理可执行。GPlan 用渐进式隐式 CoT 蒸馏（PICD）把 Qwen3-235B 教师的结构化推理按块压进每块 3 个保留 latent token，配合与压缩课程绑定的两段式学习率 CALR；再用时空反事实 DPO（SC-DPO）只扰动时间/位置构造双向偏好对，并以 anchor/gap/center 正则把偏好限制为“随上下文切换”而非“全局压低负样本”。"
paperUrl: https://arxiv.org/abs/2605.28888
codeUrl: https://github.com/alibaba/GPlan
tags:
- "Intent Sequence Planning"
- "Implicit CoT Distillation"
- "Counterfactual DPO"
- "LBS / Map Recommendation"
- "Latent Reasoning Tokens"
unverified: false
---
## 核心思路

高德首页的 agent 会根据用户画像、历史和时空上下文调用打车、目的地探索、本地生活等工具，结果以卡片序列展示。作者认为真实需求是**意图流**（跨城：打车→酒店入住→附近餐饮→回酒店），而不是相互独立的卡片。因此他们定义了 **GSISR（Generative Spatiotemporal Intent Sequence Recommendation）**：生成一条有序的、带参数的工具调用序列 Y=(a1,...,an)，ai=(工具 vi, 参数 pi)。后续意图可以引用前序意图的参数（例如打车的目的地会成为后面“酒店附近餐饮”的中心点），整条序列要逻辑连贯，并且在时空约束下可执行。

论文的例子：用户已订 B 城酒店，15:00 刚落地 B 城机场。GPlan 输出“打车去酒店→入住提醒→酒店附近餐饮→酒店附近休闲→全城景点”；列表式基线前两步相同，但第三步起仍以机场为中心推附近餐饮/景点，随后退化成公交、天气这类通用卡片。

直接上 LLM 有两个问题：CoT 时延太高，以及“时空幻觉”（计划不可执行）。GPlan（Guess What You Plan）对应两个模块：

- **PICD（Progressive Implicit CoT Distillation）**：按块把教师的结构化 CoT 压进保留的 latent token，小模型保留规划逻辑，但不用解码长文本。
- **SC-DPO（Spatiotemporal Counterfactual DPO）**：只扰动时间/位置构造反事实上下文，用双向偏好对和带正则的 DPO 训练模型在上下文变化时改计划。

## 整体实现思路

三阶段流水线：

1. **HITL 数据合成**：日志触发 → 专家校准 1000 条种子 → Qwen3-235B-A22B few-shot 生成“推理 R + 意图序列 Y” → 三级规则过滤 → 10 万训练 / 1000 测试。
2. **PICD**：Qwen3-1.7B/4B 学生先学全文本 CoT，再按 CONTEXT → STRATEGY → STEP_1 → ... 的顺序逐 epoch 把块替换为 3-token latent 三元组，最终输出“latent think token + JSON 意图序列”。学习率用 CALR 两段式调度。
3. **SC-DPO**：从 PICD-CALR checkpoint 出发，用反事实上下文对做 1 epoch 偏好对齐。

训练目标是标准自回归 MLE：θ* = argmax Σ_(x,Y)∈D Σ_l log P(y_l | y_<l, x; θ)，x=(u, H, s)。计划最多 9 个意图（训练、评估、线上一致）。

## 子模块实现（可复现细节）

### 1. HITL 数据合成与规则过滤

- 先从大规模日志中提取**高价值触发**，即暗示多步服务需求的日志模式，例如跨城到达、进行中的打车/酒店订单。
- 高德领域专家对清洗后的轨迹做逻辑校准，得到 **1000 条“Intent–Environment–Logic”种子三元组**。
- 教师 Qwen3-235B-A22B 以种子为 in-context 示例，在用户画像 u 和时空上下文 s 条件下自回归生成结构化推理 R 和意图序列 Y。
- 规则过滤器（任一层失败即丢弃）：
  - 格式：JSON 可解析，计划长度合法；
  - schema：工具必须属于固定工具库，必填参数齐全，枚举字段取值合法；
  - 逻辑不变量：每个参数引用都要解析到序列中更早的 producer 意图；互斥出行类意图有数量上限（例如每条序列最多一次打车）。
- 过滤掉 **28.9%**，最终得到 10 万训练、1000 测试。评估时，同一过滤器也作为所有模型输出的最低合法性检查。

### 2. PICD：Latent 多 token 推理脚手架

教师 CoT 的结构：

```
<THOUGHT>
<CONTEXT>分析当前上下文与潜在需求</CONTEXT>
<STRATEGY>基于上下文制定计划核心策略</STRATEGY>
<STEP_1>分析首要意图</STEP_1> ... <STEP_n>解释第 n 个意图</STEP_n>
</THOUGHT>
```

- 每个完整语义块替换为 **K=3** 个保留词表 token，只保留外层 `<THOUGHT>...</THOUGHT>`：Φ(R) = <THOUGHT> C S T1 ... T|Y| </THOUGHT>。
- C=(c_a,c_b,c_c) 对应 `<THOUGHT_CONTEXT_*>`，S 对应 `<THOUGHT_STRATEGY_*>`，T_i 对应 `<T_i_*>`。这些 token **区分类型且与位置绑定**，块被压缩后内部的 XML 标签也一起删掉。
- K=3 的理由：一个 STEP 块要同时编码工具选择、参数赋值和与前一意图的关联；CONTEXT/STRATEGY 块要容纳时空情境和高层规划理由。K 作为固定架构选择，不当超参调。
- 块数 **B = 2 + |Y|**，按样本动态跟踪，不 pad。

### 3. 前向渐进压缩 + CALR

- 设 b(e) 为第 e 个 epoch 开始时已压缩的前导块数，训练分三阶段：b=0 时为全文本 CoT；0<b<B 时前 b 块是 latent，其余仍是文本；b≥B 时全隐式。因为 B 随样本变化，短计划的样本更早进入全隐式。
- **非平稳问题**：b 增大时，学生要学会 latent token 编码了哪些被删掉的语义。余弦衰减会在 latent 结构学会之前就把 LR 降下来，导致三元组重复、缺 token、乱序；恒定 LR 能稳住结构，但缺少一个低 LR 阶段来精修 JSON 计划。
- **CALR**：g(t) 为第 t 步计划压缩的块数。
  - g(t) ≤ B* 时：η = η_struct = 5e-6（结构习得）
  - g(t) > B* 时：η = η_polish · cosine(t − t*)，η_polish = 1e-6（语义精修）
  - B* = 9，取训练集 B 的 p90，保证 LR 下降时大多数样本至少见过一次全隐式前缀。
- **分节归一化 loss**：L = (L_cot + L_json) / 2，两项各自在活跃 token 上求均值，避免 CoT 文本变短后 JSON 部分的权重漂移。
- 训练 13 个 epoch，主干为 Qwen3-1.7B / 4B。

### 4. SC-DPO：时空反事实偏好对齐

**构造样本对**：对每个锚样本构造原上下文 x 和反事实上下文 x'。两者共享用户画像、长期行为摘要和主历史，只在时空变量上不同：当前时间、当前位置、当前城市、工作日/周末、节假日。各自配一条教师生成且通过过滤的计划。样本对**双向**使用：在 x 下 y+ 为 chosen、y− 为 rejected；在 x' 下反过来。关键在于 y− 只是“与当前上下文不匹配”，本身并不是低质量计划。

**损失**（π_ref 为 SFT 模型，β_DPO = 0.20）：

- r+ = β (log πθ(y+|x) − log π_ref(y+|x))，r− 同理
- L_DPO = −log σ(r+ − r−)
- 参考锚：L_anchor = max(0, δ − r+)²，δ = 0，即 matched 回复的似然不能低于 SFT
- 有界 margin：gap = r+ − r−，L_gap,ℓ = max(0, γℓ − gap)²，L_gap,h = max(0, gap − γh)²，[γℓ, γh] = [0.10, 0.20]
- 居中漂移：center = (r+ + r−)/2，L_center = (center − m)²，m = 0
- 总损失：L = L_DPO + 5·L_anchor + 10·L_gap,ℓ + 2·L_gap,h + 3·L_center

训练配置：从 PICD-CALR checkpoint 初始化，1 epoch，lr = 2e-7（常数，warmup 比例 0.03）。

### 5. Latent-Valid 诊断

输出要算合法，须满足：只有一个 THOUGHT 块；latent token 按 C, S, T1..T|Y| 的顺序排列，无重复、无乱序；没有残留的原始 XML 标签；步数等于 JSON 计划长度。这个诊断能抓到只看 JSON 指标时发现不了的失败。

## 实验设置与结果

- 数据：高德 GSISR，10 万训练序列 + 1000 测试序列。
- 基线：SASRec、BERT4Rec、ReaRec、P5、TIGER。基线只用历史意图序列（P5 额外用画像和时空上下文），而且不生成参数槽，所以 Table 1 只在**工具层面**评估。
- 指标：Acc@1（首意图，首页 UI 最看重）、NDCG@3、NES = 1 − D(Ŷ,Y*)/max(|Ŷ|,|Y*|)，D 为加权编辑距离（增删 1.0，换工具 1.0，同工具换参数 0.3）。
- LLM judge：GPT-4o，温度 0，只看上下文和候选计划，不看目标。在 Flow / Logic / Spatiotemporal 三个维度上各打 1–5 分，“安全但通用”的计划默认给 3 分。

**主结果（Table 1）**

| 方法 | Acc@1 | NDCG@3 |
|---|---|---|
| SASRec | 36.1 | 0.5865 |
| BERT4Rec | 37.4 | 0.5973 |
| ReaRec | 42.9 | 0.6442 |
| P5 | 43.5 | 0.6581 |
| TIGER | 44.2 | 0.6647 |
| GPlan-1.7B | 60.5 | 0.7450 |
| GPlan-4B | **62.7** | **0.7759** |

**训练策略消融（Table 2，Qwen3-4B）**

| 方法 | Acc@1 | NDCG@3 | NES | Flow | Logic | ST | Overall |
|---|---|---|---|---|---|---|---|
| Direct-SFT | 61.2 | 0.7591 | 0.6210 | 3.37 | 3.43 | 3.49 | 3.43 |
| CoT-SFT | 62.3 | 0.7785 | 0.6354 | 3.53 | 3.61 | 3.64 | 3.60 |
| PICD | 62.6 | 0.7726 | 0.6290 | 3.56 | 3.62 | 3.69 | 3.62 |
| PICD + SC-DPO | 62.7 | 0.7759 | 0.6365 | 3.58 | 3.59 | 3.75 | 3.64 |

**LR 调度消融（Table 3）**

| 调度 | Acc@1 | NDCG@3 | NES | Latent-Valid |
|---|---|---|---|---|
| Cosine-LR | 62.4 | 0.7652 | 0.6259 | 0.0 |
| Constant-LR | 62.1 | 0.7575 | 0.6216 | 1.0 |
| CALR | 62.6 | 0.7726 | 0.6290 | 1.0 |

**DPO 损失消融（Table 4）**

| 后训练 | Acc@1 | NDCG@3 | NES | ST | Overall |
|---|---|---|---|---|---|
| PICD | 62.6 | 0.7726 | 0.6290 | 3.69 | 3.62 |
| + Vanilla DPO | 62.1 | 0.7484 | 0.6158 | 3.60 | 3.51 |
| + SC-DPO | 62.7 | 0.7759 | 0.6365 | 3.75 | 3.64 |

**推理时延（Table 5，2×H20，QPS=10，贪心解码）**

| 规模 | Direct-SFT | CoT-SFT | PICD |
|---|---|---|---|
| 1.7B | 299 ms | 1.06 s | 366 ms |
| 4B | 437 ms | 1.85 s | 503 ms |

4B 下 PICD 比 CoT-SFT 快 3.7 倍。

**线上 A/B**：GPlan-1.7B 对比现网 CTR 排序模型，跑 14 天。通用切片占首页 5% 流量（约 600 QPS），UV-CTR **+0.87%**；跨城切片另占 5% 流量（只含有异地出行上下文的用户），UV-CTR **+1.04%**。

## 思考与可参考价值

**结果要怎么读**

- 主表 18.5pp 的优势需要打折：基线不看画像和时空上下文（P5 除外），模型容量也差很多；训练和测试目标又大多由同一个教师生成。离线指标主要衡量的是“复刻教师”的程度。缺一个“同样输入、同样 LLM、直接列表式输出”的强基线。
- PICD 的离线效果和 CoT-SFT 基本持平（NDCG@3 和 NES 反而略低）。它的价值在于时延：1.85s 降到 503ms，同时 judge 分不掉。和 Direct-SFT 比，Acc@1 +1.4pp、judge Overall +0.19，代价是多 67ms（4B）。
- SC-DPO 在 label 指标上只有 0.1pp 级别的变化，主要信号是 judge ST 分 3.69→3.75，没有报告方差和显著性。反过来看，Vanilla DPO 让 NDCG@3 从 0.7726 掉到 0.7484，这个对照更有说服力：在反事实负样本上直接跑 DPO 会伤害 SFT 学到的能力。
- Cosine-LR 的 Latent-Valid 为 0.0，但任务指标还不错。这说明模型绕开了预期的 latent 接口，靠别的路径拼出了 JSON。只看 JSON 指标的话，会误以为隐式推理在起作用。

**对电商生成式推荐 / SID 的启发**

1. **think 块压缩**：如果 SID 生成前先输出 think 块，可以借鉴“结构化 CoT 分块 → 每块 K 个类型化保留 token → 前向逐块压缩”的做法。它只扩词表，不改推理引擎，比 Coconut 式的隐状态回填更容易部署。上线前要监控 latent 结构合法率。
2. **课程训练配学习率**：目标随压缩课程变化时，LR 切换点要跟课程进度（这里是 p90 块数）对齐，而不是按 epoch 数固定。这个原则适用于任何渐进式蒸馏或压缩。
3. **分节归一化 loss**：一条样本里同时有长度会变的推理段和输出段时，两段分别取均值后再等权相加，防止输出段权重被稀释。
4. **场景敏感性对齐**：电商的时段、地域、大促和非大促都可以套 SC-DPO：只改场景变量构造反事实，双向偏好，加上参考锚、有界 margin 和居中漂移，避免把“换个场景就是对的推荐”当成全局负例压低。
5. **组合推荐**：把“参数化意图序列 + 规则过滤器”用于搭配购、行程化导购或 agent 多工具推荐，同一个过滤器既做训练数据清洗，也做线上兜底（推断）。

**采纳前要核对**：教师标签和真实点击/成交是否一致；在同等输入下，与强 LLM 列表式基线的差距；K=3、B*=9、正则权重的敏感性（论文没给）；latent token 合法率在线上分布漂移下是否稳定；线上 +0.87% 对比的是 CTR 排序模型，展示形态是否完全一致论文没说清楚。
