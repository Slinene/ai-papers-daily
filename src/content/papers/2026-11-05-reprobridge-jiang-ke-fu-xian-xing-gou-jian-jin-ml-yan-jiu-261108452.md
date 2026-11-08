---
title: 'ReproBridge: Building Reproducibility into ML Research Artifacts'
title_zh: ReproBridge：将可复现性构建进 ML 研究工件
authors:
- Yubo Wang
- Rui Meng
- Jaehyun Nam
- Tomas Pfister
- Jinsung Yoon
affiliations:
- University of Waterloo
- Google
arxiv_id: '2611.08452'
url: https://arxiv.org/abs/2611.08452
pdf_url: https://arxiv.org/pdf/2611.08452
published: '2026-11-05'
collected: '2026-11-08'
category: Agent
direction: Agent 构建可复现实验工件
tags:
- reproducibility
- coding agent
- benchmark
- artifact
- experiment reproduction
- LLM
one_liner: 用 agent workflow 沉淀复现过程为标准化工件，使编码代理复现成功率从76.4%升至92.6%并降本19.7%
practical_value: '- 可把模型/策略实验的复现流程沉淀为标准化 artifact：refined codebase、environment setup、experiment
  launchers、reproduction guide，减少团队内不同成员或 agent 重复排障；对电商搜索/推荐中频繁复现 baseline 的场景尤其省时。

  - 在 agent workflow 中增加独立 Auditor 校验执行证据，避免主 agent 自报成功；业务中可要求 agent 提交日志、diff、输出文件等证据后再进入下一阶段，提升可靠性。

  - 标准化 artifact 能把不同 LLM 模型的成功率差距从 21.6pp 缩到 3.9pp，同时 API 花销降 19.7%；说明在内部给 agent
  提供清晰的上下文、依赖和运行说明，比单纯换更强模型更能稳定提效降本。

  - 消融显示 code 和 environment 组件损失最大，因此优先维护可运行的训练/推理代码与锁定依赖环境，是对复现性收益最高的投入。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：复现 ML 实验需要从论文、代码和衍生材料中重建缺失细节；编码 agent 的成败往往取决于补全隐含信息，而非原始 artifact 是否公开。问题在于，是否保存恢复出的过程和决策能提升后续独立复现。

方法：定义标准化 artifact 组成：refined codebase、environment setup、experiment launchers 和 reproduction guide。设计 ReproBridge agent workflow 自动构建这些工件，并构建 ReproBridge-Bench：36 篇论文、387 个实验、1029 个任务，每任务锚定 5 个人工验证参考分数。实验让 agent 在全新 session 中分别基于 raw code 或 refined artifact 尝试复现，独立 Auditor 检查执行证据。

结果：四个模型下，refined artifact 将平均复现成功率从 76.4% 提升到 92.6%，下游 API 花费平均降低 19.7%；跨模型成功率差距从 21.6 个百分点收窄到 3.9 个百分点，四个模型平均成功率均超 90%。消融中删除任一组件都会降低成功率，code 和 environment 删除损失最大。结论是保存执行知识能帮助即使原始代码成功率较低的模型更可靠地复现实验，且 API 成本更低。
