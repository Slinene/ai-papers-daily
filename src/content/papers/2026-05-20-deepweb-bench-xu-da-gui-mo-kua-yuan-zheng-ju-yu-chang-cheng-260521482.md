---
title: 'DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence
  and Long-Horizon Derivation'
title_zh: DeepWeb-Bench：需大规模跨源证据与长程推导的深度研究基准
authors:
- Sixiong Xie
- Zhuofan Shi
- Haiyang Shen
- Jiuzheng Wang
- Siqi Zhong
- Mugeng Liu
- Chongyang Pan
- Peilun Jia
- Baoqing Sun
- Xiang Jing
affiliations:
- Peking University
arxiv_id: '2605.21482'
url: https://arxiv.org/abs/2605.21482
pdf_url: https://arxiv.org/pdf/2605.21482
published: '2026-05-20'
collected: '2026-05-21'
category: Agent
direction: 深度研究智能体评估与诊断
tags:
- Deep Research
- Benchmark
- Agent Evaluation
- Multi-step Derivation
- Source Provenance
- Calibration
one_liner: 提出一个包含矩阵任务、溯源记录和校准维度的深度研究基准，揭示检索非瓶颈、推导与校准才是主要挑战。
practical_value: '- 电商/市场分析Agent构建：可复用矩阵任务格式（实体×分析维度）和四能力（检索、推导、推理、校准）设计，用于自动生成竞品报告或行业分析。

  - 信息抽取可靠性：引入源溯源等级（T1-T4）和跨源一致性检查，可作为电商知识库或RAG系统的证据可信度评估模板，减少幻觉。

  - 工程实现启发：发现检索并非瓶颈，应重点投入多步数值组合与校准逻辑，例如在推荐系统的归因分析或财务推演Agent中显式要求推导步骤。

  - 领域专长差异：模型在不同品类表现差异大（相关仅0.61），提示为细分场景（如新能源车、芯片）定制微调或专用提示链，而非通用方案。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：前沿深度研究产品（如OpenAI Deep Research、Claude Research）在现有基准上已接近饱和，难以区分真实能力。真实深度研究任务需要的不是单页查找，而是同时处理大量证据、跨源核对不一致数据，并进行多步定量推导。现有基准往往只覆盖其中一两个侧面，为此需要更综合、更难的新基准。

**方法关键点**：
- 任务设计：100个深度研究任务，覆盖科技、能源、消费等六个领域。每个任务以一个8×8矩阵呈现（8个可比实体 × 8个分析维度），要求智能体填充每个单元格的定量答案（精确值/范围/不可得）。
- 能力覆盖：8个维度按四类能力固定分配：1个检索（直接查找披露值）、4个推导（需多步组合计算，如营收分拆）、1个校准（跨源冲突处理与幻觉抗拒）、2个推理（情景外推/预期分析），推动难度超越单纯检索。
- 审计性保障：每个单元格配有参考答案、来源溯源等级（T1至T4，从正式监管文件到非正式来源）、跨源一致性标签（一致/分歧/单一），使评分可回溯至原始证据。
- 评估协议：9个前沿模型（包括GPT-5.5、Claude Opus 4.7、DeepSeek V4等）通过统一web搜索/浏览工具完成任务，每个任务限200次工具调用及30分钟。评分采用四级规则（1/0.5/0.25/0），自动评分器与人类标注一致性κ=0.82。

**关键结果**：
- 最强模型Codex CLI+GPT-5.5综合得分仅33.37%，最弱Kimi K2.6为16.79%，留有充足区分空间。
- 人工注释500个错误单元格发现：检索失败仅占12–14%，而推导不完整（31%强模型 / 24%弱模型）和幻觉精度（22%强 / 38%弱）占据超过70%。强模型更多在组合步骤出错，弱模型倾向臆造精确值。
- 模型间任务得分Spearman相关均值仅0.61，单任务得分标准差最高达18.8个百分点，显示明显的领域专长分化。

**核心发现**：深度研究能力的瓶颈不在检索，而在多步数值推导的准确性和面对信息缺失时的校准行为，为智能体优化指明了着力点。
