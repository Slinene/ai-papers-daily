---
title: 'From Relevance to Utility: Rubric Alignment in Yuanbao Search'
title_zh: 从相关性到效用：元宝搜索中的 Rubric 对齐
authors:
- Yu Lu
- Lixin Zou
- Yangqi Chen
- Hui Xu
- Qiaolin Xia
- Hao Wang
- Qianwen Ma
- Reed Li
- Shuang Zeng
- Haijin Liang
affiliations:
- Tencent Inc.
- Wuhan University
arxiv_id: '2611.22503'
url: https://arxiv.org/abs/2611.22503
pdf_url: https://arxiv.org/pdf/2611.22503
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Rubric 对齐的 Agentic Search 全链路优化
tags:
- Rubric Alignment
- Agentic Search
- Set-Level Utility
- GRPO
- Dual-Encoder
- LLM Ranker
one_liner: 用 query 专属 rubric 统一检索/排序/选择三阶段训练信号，将文档集效用对齐到 LLM 答案质量，线上端到端提升 8.52%。
practical_value: '- 借鉴 rubric 分解：把 query 级评估标准拆成正负准则，用 LLM 粗到细自动生成，作为检索/排序/选择统一监督标签，适合电商复杂
  query（如“2026年旗舰手机对比”）的召回与排序优化。

  - 轻量 labeler 蒸馏大模型 rubric 判断，以百万级标注成本解决点粒度训练数据问题；在电商商品/广告素材与 query 相关性标注中，可先用大模型标注小样本，再蒸馏小模型扩展到全库。

  - 选择阶段采用 GRPO+best-rollout distillation 双分支 RL：用组内最优 rollout 作为 token 级教师，稳定训练集选模型，适合商品组合推荐、广告位子集选择等稀疏奖励的组合优化场景。

  - 多任务 ranker 用共享 encoder+辅助 head，utility head 为主，辅助 loss 降权（0.5），可在电商多目标排序中复用，同时提升主目标并隐式建模其他信号。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：传统搜索引擎只优化单文档相关性排序，但 Agentic Search 中 LLM 需要从有限的文档集综合答案，评价标准转为文档集的效用（覆盖、无冲突、权威性等）。此前工作要么只优化选段模型，上游检索/排序仍用相关性训练，与下游答案质量不对齐。

**方法关键点**：
- 定义 query 专属 rubric：正准则带权重、负准则带扣分；粗阶段用三个不同 LLM 生成答案并提取候选维度，细阶段锚定 top-15 候选文档生成可验证子准则，保证区分度。
- 轻量 labeler 蒸馏大模型 rubric 判断：先 SFT，再用 GRPO 强化，输出 0-3 效用标签；这些标签用于监督检索与排序。
- 检索：Qwen3-Embedding-0.6B 双编码器，先 610M 在域对比预训练，再 utility 对齐微调（正样本 l>=2），使用 Matryoshka 表示。
- 排序：Qwen3-4B 多任务 ranker，共享 encoder 四个头（utility/authority/freshness/quality），focal pairwise loss，主 utility 头 + 辅助头降权。
- 选段：Qwen3-7B policy，双分支 RL：GRPO 处理优势 rollout，best-rollout distillation 将低于均值 rollout 拉向组内最优，奖励由 rubric-conditioned Pointwise-Ensemble Judge 给出。

**关键实验**：
- 离线：检索 Recall@1K 提升 11.2-14.2 点；排序 PNR 从 3.807 到 3.959（+4.0%）；选段 Utility 从 9.45 到 9.73（+3.0%）。
- 在线 A/B（5% 流量，约 280 万查询，14 天）端到端 GSB 提升 8.52%；其中 selection 单组件 +4.82%，ranking +3.94%，retrieval +0.40%。
- Rubric 与人类判断一致性从无 rubric 的 68.7% 提升到 79.3%。

**最值得记住的一句话**：把评价文档集质量的 rubric 转化为检索、排序、选择各阶段的训练信号，是让搜索全链路对齐 Agent 答案效用的关键。
