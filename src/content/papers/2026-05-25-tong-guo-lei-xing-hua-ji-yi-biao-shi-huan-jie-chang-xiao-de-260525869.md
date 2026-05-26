---
title: Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation
title_zh: 通过类型化记忆表示缓解长效Agent中的溯源-角色坍缩
authors:
- Zhengda Jin
- Bingbing Wang
- Jing Li
- Ruifeng Xu
- Min Zhang
affiliations:
- Harbin Institute of Technology, Shenzhen
- The Hong Kong Polytechnic University
- Shenzhen Loop Area Institute
arxiv_id: '2605.25869'
url: https://arxiv.org/abs/2605.25869
pdf_url: https://arxiv.org/pdf/2605.25869
published: '2026-05-25'
collected: '2026-05-26'
category: Agent
direction: 长效Agent记忆组织 · 类型化记忆原子
tags:
- Long-Term Memory
- Agent Memory
- Source Monitoring
- Typed Memory Atoms
- Provenance-Scoped
one_liner: 提出类型化记忆中间表示 MEMIR，以记忆原子分离证据、线索与事实，实现溯源监控的结构化
practical_value: '- **记忆原子分层存储**：将对话历史拆分为证据 Span、线索（句柄/时间/枢轴）和事实 Claim，避免不同角色信息混杂。在电商对话或购物助手中，可分别存储用户偏好事实、原始对话片段和时间锚点，提升事实追踪与更新。

  - **类型约束投影**：检索命中的非事实原子（如 Span）必须通过关联 Claim 进入候选，间接阻断虚假事实的生成。适用于 RAG 或 Agent 场景，只让被证据支撑的声明影响答案，减少幻觉。

  - **溯源范围利用**：通过粗到细排序和选择，仅将 Claim 及其溯源闭包（证据 + 线索）作为“事实接口”输入给答案模型，强制模型在证据范围内生成，并在证据不足时明确拒绝回答。可迁移至生成式推荐，将商品属性类声明与其来源证据打包，提升推荐解释性和防幻觉能力。

  - **认知记忆设计借鉴**：明确区分外部感知与内部推理，避免将系统推断当作用户提供的事实。在多轮交互中可用于甄别用户真实陈述与模型猜测。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有长程记忆系统（如 RAG 代理）将历史交互压缩为扁平文本存储，丢失了信息的来源（谁说的、何时说的）和认知角色（是观察的事实还是推理出的内容），导致**溯源-角色坍缩**：检索到的碎片可能被错误合并、重复计数或当作独立事实使用。例如，回答“Joanna 写了多少剧本”时，扁平记忆将不同时期的提及视为独立对象而造成计数错误。因此，需要一种结构化的记忆表示，将来源监控（source monitoring）作为显式约束。

**方法**
MEMIR 将记忆构建为**类型化记忆原子**，包括：页面（Page）与跨度（Span）作为原始证据；句柄（Handle）、时间（Time）、枢轴（Pivot）作为检索线索；声明（Claim）是唯一承载事实的原子，且必须有支持它的证据 Span；检索视图（Retrieval View）连接原子供检索。记忆写入阶段，LLM 从对话中抽取线索并生成声明，同时严格约束每个声明必须由至少一个 Span 支撑。检索时，**多路原子投影**结合 BM25（浏览视图）与稠密检索 BGE-M3（在声明和 Span 上），然后通过**类型约束投影**将所有命中原子映射到关联的声明原子，形成候选束。每个束包含声明、聚合检索分数和溯源闭包（证据+线索）。**溯源范围利用**阶段，先粗排（RRF 分数）选出 top-M 候选束，再用交叉编码器 reranker（bge-reranker-v2-m3）精排，最后由 LLM 选择器挑出最多 X 个束（标记为 direct 或 support），构建标准化事实接口（声明文本 + 时间线索 + 角色）供答案模型生成；若证据不足，则回答“证据不足”。

**实验结果**
在 LoCoMo（10 组长对话，1540 题）和 BEAM-100K（20 组 100K token 对话，400 题）两个长程记忆基准上，MEMIR 均优于主流基线（Zep、Mem0、NEMORI、SimpleMem 等）。LoCoMo 上，单跳、时间、开放域 F1 分别提升 1.9、3.1、1.4 点（GPT-4.1-mini）；BEAM-100K 上平均 Judge 分数达 48.26，比最佳基线 SimpleMem 高 7.6 点，在矛盾解决、知识更新、多会话推理等任务上优势显著。消融实验证实，移除声明原子、线索原子、类型约束投影或候选束均导致性能下降。超参数分析建议每页约 12 个声明、预排序池 32、最终选择 6 个束为较优配置。

**一句话**
可靠的长程记忆不只靠检索，更需要显式划分证据来源与事实授权，MEMIR 通过原子化类型表示将这一理念落地。
