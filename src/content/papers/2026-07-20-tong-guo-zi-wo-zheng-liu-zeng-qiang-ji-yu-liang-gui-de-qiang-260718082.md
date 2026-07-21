---
title: Enhancing Rubric-based RL via Self-Distillation
title_zh: 通过自我蒸馏增强基于量规的强化学习
authors:
- Mingxuan Xia
- Yuhang Yang
- Chao Ye
- Shuai Zhu
- Shenzhi Yang
- Guangcheng Zhu
- Yuhang Zhang
- Cheng Peng
- Haobo Wang
- Siqing Wang
affiliations:
- Zhejiang University
- ByteDance
arxiv_id: '2607.18082'
url: https://arxiv.org/abs/2607.18082
pdf_url: https://arxiv.org/pdf/2607.18082
published: '2026-07-20'
collected: '2026-07-21'
category: Training
direction: Rubric-based RL 训练优化
tags:
- Rubric-based RL
- Self-Distillation
- On-policy
- Token-level Advantage
- Training Efficiency
one_liner: 用 on-policy 自我蒸馏同时解决 rubric RL 的未被探索准则和压制准则问题，消除训练推理不匹配
practical_value: '- 当使用 rubric-based RL 训练对话/推荐 Agent 时，可借鉴 CriPO 的自我蒸馏框架：对训练中从未满足的准则，构造一个注入准则提示的
  teacher 模型，用局部 forward-KL 损失将缺失行为蒸馏到当前策略，无需在推理时引入额外引导，避免 train-inference mismatch。

  - 针对 scalar reward 聚合导致部分准则信号被压制的问题（如推荐理由生成中某维度得分高但总分低），可识别与压制准则相关的 token，将其 token-level
  advantage 翻转为正值，保留被全局奖励淹没的细粒度模式，提升策略学习效率。

  - 实现上，两个 self-teacher 均从当前策略加载参数（on-policy），工程简单，且实验中只需约一半训练步数即超越基线，适合资源敏感的业务场景快速迭代。

  - 该方法不依赖外部模型或数据，仅利用 rollout 样本和准则元信息，可直接集成到现有 GRPO/PPO 训练框架中，对推荐系统的多目标/多准则 RL 对齐具有参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：基于量规的强化学习（rubric-based RL）在开放式任务中训练 LLM 时面临两大问题：一是未被探索准则（Unexplored Criteria, UC）——训练中没有任何 rollout 满足的准则，梯度信号缺失；二是压制准则（Suppressed Criteria, SC）——部分 rollout 满足但被 scalar reward 聚合赋予非正优势值，导致有用模式被抑制。现有方法通过外部引导增强探索，却引入训练-推断失配。

**方法关键点**：提出 **CriPO**，通过 on-policy 自我蒸馏同时解决 UC 和 SC，无需外部引导。对 UC：从当前策略构造一个注入准则信息的 self-teacher，计算局部 forward-KL 损失，将缺失行为蒸馏进策略。对 SC：构造一个 counterfactual self-teacher，用于在负优势 rollouts 中定位与准则相关的 token，将其 token-level 优势翻转为正值，保留被压制的模式。整个过程完全 on-policy，无推断时修改。

**关键结果**：在医学和科学基准上，CriPO 一致优于基础 rubric RL 方法，且仅需约一半优化步数（约 2× 更少）即达到更强最终性能。分析显示超 57% 样本存在 SC，平均每样本 1.8 个压制准则，CriPO 有效减轻了这两类失效模式。
