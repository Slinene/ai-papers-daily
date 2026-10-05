---
title: Collective Bias Mitigation via Model Routing and Collaboration
title_zh: 通过模型路由与协作实现集体偏见缓解
authors:
- Mingzhe Du
- Luu Anh Tuan
- Xiaobao Wu
- Yichong Huang
- Yue Liu
- Dong Huang
- Huijun Liu
- Bin Ji
- Jie M. Zhang
- See-Kiong Ng
affiliations:
- Nanyang Technological University
- National University of Singapore
- Harbin Institute of Technology
- King's College London
arxiv_id: '2610.03240'
url: https://arxiv.org/abs/2610.03240
pdf_url: https://arxiv.org/pdf/2610.03240
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: 多 LLM 协作路由去偏
tags:
- bias mitigation
- model routing
- multi-LLM collaboration
- fairness
- committee
- debate
one_liner: 提出 Collective Bias Mitigation，用多 LLM 路由与协作降低偏见，Committee 在 top-7 将年龄偏见从
  0.25 降至 0.10
practical_value: '- 在生成推荐文案、广告语、客服话术等 LLM 输出场景，可先对业务敏感维度（性别、年龄、地域、消费能力）做细粒度偏见评估，按问题类型路由到该维度偏见更低的模型或
  LoRA 专家，而不是全局换大模型。

  - 借鉴 Committee 拓扑：多个异构 LLM 对同一 prompt 生成候选，再用低成本聚合/仲裁模型投票或改写，能明显降低 biased 输出；线上可按
  top-k 控制成本，用较小 committee 在偏见与推理成本间取平衡。

  - Debating 拓扑适合高价值、低 QPS 场景（如公关文案、敏感 push 文案），让模型互相挑战后再产出；普通推荐解释或 query 改写可用 Committee
  的轻量投票。

  - 工程上把偏见分数作为模型路由特征：离线为每个模型×敏感属性×任务类型建立 bias profile，路由时查表选择，避免每次实时前向全部模型。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 在公共健康、金融、治理等场景会延续训练数据中的偏见；单个模型的 self-debiasing 依赖自身知识，难以纠正深层刻板印象。
方法：提出 CBM，核心不是训练新模型，而是学习细粒度模型行为并组织多个异构 LLM 协作。通过路由选择适合特定偏见上下文的模型，并用 Debating 与 Committee 两种拓扑促进知识共享：Debating 让模型互相挑战，Committee 用投票/仲裁生成更公平回答，可看成把去偏从单模型内省扩展为多模型集体决策。
结果：在多个偏见基准上显著优于单模型 baseline；top-7 Committee 将年龄偏见分数从 0.25 降到 0.10。Committee 在去偏效果与推理成本之间取得较好平衡，比 Debating 更省资源。
