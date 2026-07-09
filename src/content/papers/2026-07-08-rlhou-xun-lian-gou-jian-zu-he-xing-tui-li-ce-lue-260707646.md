---
title: RL Post-Training Builds Compositional Reasoning Strategies
title_zh: RL后训练构建组合性推理策略
authors:
- Azwar Abdulsalam
- Nishil Patel
- Andrew Saxe
affiliations:
- Gatsby Computational Neuroscience Unit, UCL
arxiv_id: '2607.07646'
url: https://arxiv.org/abs/2607.07646
pdf_url: https://arxiv.org/pdf/2607.07646
published: '2026-07-08'
collected: '2026-07-09'
category: Reasoning
direction: RL后训练组合推理策略机制
tags:
- Reinforcement Learning
- Compositional Reasoning
- Post-training
- Rejection Fine-tuning
- Symbolic Reasoning
- Transformers
one_liner: RL后训练能将基础模型的原始技能组合为新的高级推理策略，而拒绝微调易陷入停滞。
practical_value: '- 在需要多步推理的业务场景（如 Agent 自动构建搜索策略、多跳问答、动态推荐流程），采用 RL 后训练比拒绝采样微调更可能组合出高级策略，可复现性地提升难以通过采样突破的任务成功率。

  - RL 探索的选择性很关键：RFT 常生成无效捷径，而 RL 能集中探索有效且可复用的结构。实践中可借鉴引入过程监督或结构先验来过滤无效探索，提升训练效率。

  - 预训练阶段的技能组织方式直接影响后训练的组合能力：在电商/推荐模型中，若预训练只堆砌原始特征交互，RL 难以将其组合为可靠推理；应在预训练时通过课程或任务设计让模型先掌握可被压缩的原子过程。

  - 组合策略出现具有阶段性（先强化原语，再发现组合），提示我们可以在 RL 早期加入辅助奖励或先验来加速这一过程，例如在 Agent 训练中先强化基础工具调用，再组合成复杂工作流。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：探究 RL 后训练是否仅仅放大基座模型中已有的原始技能，还是能够将多种原始技能**组合成新的高级推理策略**。

**方法**：在一个完全可观测的**重写语法环境**中，先让 Transformer 在原始符号重写链上预训练，然后用仅有二元最终答案奖励的轨迹推理任务进行 RL 后训练，并对比**拒绝微调 (RFT)**。所有生成的重写均可审计。

**关键结果**：
- RL 解决了大量预训练模型即便高预算采样也极难解决的 held-out 问题，而 RFT 早期提升后即**陷入停滞**。
- 轨迹分析揭示 RL 通过**阶段性组合机制**重组原始能力：先**强化原始规约**，再**发现有效组合过程**（包括顺序组合和并行组合），这些组合过程并非孤立样本，而是被**重用并巩固为稳定套路**。
- RL 与 RFT 的关键差异在于**选择性**而非探索量：RFT 产生大量无效的捷径式重写，RL 则将探索集中于**有效的可复用结构**。
- 预训练消融表明，组合策略的出现不仅取决于对原始符号的曝光，更依赖于预训练是否已将原始能力组织成可供 RL 后期压缩的**规约程序**。
