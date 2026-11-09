---
title: 'RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers'
title_zh: RuACT：恢复非活跃评分准则为自适应评论家与教师
authors:
- Yijun Li
- Zhengxi Lu
- Zhipiao Liu
- Jinzheng Yu
- Xutao Weng
- Jian Shao
- Yongliang Shen
affiliations:
- Zhejiang University
- Huawei
arxiv_id: '2611.09597'
url: https://arxiv.org/abs/2611.09597
pdf_url: https://arxiv.org/pdf/2611.09597
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: Rubric-based RL 训练优化
tags:
- RLVR
- Rubric-based RL
- Self-distillation
- Reward hacking
- LLM training
one_liner: 提出 RuACT，将 RL 中不可达与饱和 rubric 分别用作教师与评论家，恢复无效训练信号
practical_value: '- 在业务中若用 LLM rubric 做 reward，务必监控每个 rubric 在 rollout group 内的 pass
  rate，识别 unreachable/saturated 的无效维度；不要只是简单加权或丢弃。

  - 对 unreachable 的高标准 rubric（如合规/安全/风格约束），不要只靠 RL 探索：可以将其作为 teacher 信号做 reward-gated
  on-policy self-distillation，把条件直接注入 prompt/蒸馏，快速拉升满足率。

  - 对饱和的粗粒度 rubric（如“回答是否相关”），拆解为更细的 child rubrics，能更好地区分当前候选，提升 reward 与真实质量的 alignment；在电商文案/推荐理由/Agent
  多步任务中同样适用。

  - 在生成式推荐或 Agent 场景中，全局 rubric 常常过早饱和或长期不可达，可借鉴 parent-child 分解与共享权重的 critic 机制，保持密集、可学的奖励信号。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：Rubric-based RL 在 open-ended 任务中通过细粒度 rubric 提供可验证奖励，但在 group-relative optimization 下，不可达（unreachable）和饱和（saturated）rubric 使所有采样响应获得相同结果，无学习信号。在 Qwen3-4B 医疗训练中，60.88% 的 query-rubric 观测为 inactive。

**方法关键点**：两种 inactive 状态缺乏的监督不同：不可达 rubric 可通过在 prompt 中显式声明大幅提升满足率（1.13%→91.25%）；饱和 rubric 下响应质量仍有差异。RuACT 为两种 rubric 分配不同角色——Rubric as Teacher：将不可达 rubric 作为 privileged information，做 reward-gated on-policy self-distillation；Rubric as Critic：将饱和 rubric 分解为 child rubrics，在共享父权重的同时区分当前响应。

**关键结果**：RuACT 在四个医疗和科学基准上超越 GRPO、rubric reweighting 和 rubric-guided exploration，Qwen3-4B 全部领先，Qwen3-1.7B 平均最优；初始不可达 rubric 恢复率从 35.02% 提升至 42.86%，独立 rollout 上 reward-quality alignment 从 57.74% 提升至 60.77%。
