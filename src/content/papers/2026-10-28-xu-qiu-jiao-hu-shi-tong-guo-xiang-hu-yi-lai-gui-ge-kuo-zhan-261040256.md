---
title: 'When Requirements Interact: Scaling Long-Horizon Coding via Interdependent
  Specifications'
title_zh: 需求交互时：通过相互依赖规格扩展长程编码
authors:
- Yishuo Cai
- Minzheng Wang
- Liang Zhao
- Linghao Zhang
- Lei Li
- Shicheng Li
- Xu Sun
- Fuli Luo
affiliations:
- LLM Core, Xiaomi
- Peking University
- University of Hong Kong
arxiv_id: '2610.40256'
url: https://arxiv.org/abs/2610.40256
pdf_url: https://arxiv.org/pdf/2610.40256
published: '2026-10-28'
collected: '2026-11-03'
category: Training
direction: 编码代理 · 规格合成与强化学习
tags:
- Code Agent
- Specification Synthesis
- Reinforcement Learning
- Benchmark
- Long-Horizon Coding
one_liner: CodeSpecWeave 合成带相互依赖规格的任务并用 RL 训练编码代理，显著提升长程开发表现
practical_value: '- 任务设计上，可构造具有相互依赖约束的合成任务（例如同时满足相关性、多样性、商业指标约束），迫使模型进行联合推理，避免退化为简单清单，提升生成式推荐或
  query 推荐策略的鲁棒性。

  - 数据质量保障上，借鉴 review agent 审计多条 solution trajectories 的做法：在离线样本生成或评估中，用多个模型交叉验证候选输出的合理性和正确性，过滤隐藏缺陷或误判，提高训练数据可靠性。

  - 训练范式上，在仿真环境或历史日志中合成带多目标约束的任务，用强化学习优化策略模型，使其在复杂业务约束下（如用户体验与商业收入平衡）学习长期收益。

  - 评估体系上，构建包含多维规格的基准，揭示模型在处理相互依赖约束时的能力边界，指导针对性迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：真实软件开发中，编码代理需满足多维度任务规格（接口兼容性、错误处理等），且不能破坏已有依赖。现有任务合成缺少数量和多样性的规格，常偏重主要目标而忽略复杂约束。直接添加规格易使任务退化为琐碎清单，验证相互依赖的规格又可能漏掉隐藏缺陷或错误拒绝有效方案。

**方法关键点**：CodeSpecWeave 框架，基于真实开发者种子，由 synthesis agent 迭代生成耦合的任务需求和可执行测试；review agent 审计多个模型的 solution trajectories 以保证测试可靠性。

**结果**：构建 4,670 个训练任务，覆盖 2,865 个仓库。在这些任务上做强化学习，在 DeepSWE-v1.1 上性能显著超越基线和现有基线。另构建 CodeSpecWeave-Bench 基准，含 100 任务、1,044 规格，清晰区分前沿模型，揭示处理相互依赖工程约束仍有很大空间。
