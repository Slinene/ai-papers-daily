---
title: 'Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating
  Agents in Dynamic Adversarial Environments'
title_zh: AnTrap：评估Android GUI Agent对运行时异常的鲁棒性基准
authors:
- Guo Gan
- Yilun Zhao
- Cong Chen
- Jinbiao Wei
- Tingyu Song
- Zheyuan Yang
- Lin Fu
- Hong Zhou
affiliations:
- Zhejiang University
- Yale University
- Tongji University
- University of Chinese Academy of Sciences
arxiv_id: '2608.24099'
url: https://arxiv.org/abs/2608.24099
pdf_url: https://arxiv.org/pdf/2608.24099
published: '2026-08-24'
collected: '2026-08-27'
category: Agent
direction: GUI Agent 鲁棒性评估与对抗训练
tags:
- GUI Agents
- Robustness
- Adversarial Evaluation
- GRPO
- Benchmark
one_liner: 提出AnTrap基准系统注入动态对抗扰动，揭示GUI Agent普遍脆弱并区分可学习与推理瓶颈异常
practical_value: '- 将线上 Agent 可能遇到的弹窗、误操作、状态死锁等异常抽象为分层陷阱（State/Thinking/Action/Round），在部署前构建对抗测试集做压测，提前暴露脆弱环节。

  - 用 GRPO 在含陷阱环境中训练可修复大部分单步状态/动作层异常，适合作为上线前的鲁棒性微调步骤；但状态死锁等深层上下文陷阱无法仅靠环境训练解决，需要额外引入记忆、回溯或规则兜底机制。

  - 借鉴其“保持任务可解”的扰动构造管道：在业务环境中注入异常时保留原始任务可达性，避免测试集失真，从而准确度量鲁棒性而非任务难度。

  - 对电商推荐 Agent，可将广告弹窗、支付中断、页面跳转异常等作为 State 层扰动，将模型选错工具或遗漏步骤作为 Thinking/Action 层陷阱，系统化定位故障来源。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Android GUI Agent 实际部署时会频繁遇到运行时异常（如应用内广告弹窗、误操作、上下文死锁），但现有基准缺乏对这类动态异常的鲁棒性系统评估。

**方法**：提出 AnTrap 基准，将真实世界异常按四层分类（State、Thinking、Action、Round），细化为十个子类，并设计构造管道在保留任务可解性的同时注入对抗性扰动。评估 16 个领先 GUI 模型，并在原始环境与对抗环境中进行 GRPO 训练，以区分环境可学习异常与推理瓶颈异常。

**关键结果**：所有模型均对动态异常表现出普遍脆弱性，最强模型性能也显著下降。单步 State 和 Action 层陷阱通过对抗强化学习可大幅修复，但 State deadlock 等深层上下文陷阱暴露内在推理限制，仅靠陷阱环境训练无法解决。
