---
title: 'When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time
  Scaling'
title_zh: 更多采样为何有害：测试时缩放的模态上限与相关性上限
authors:
- Yong Yi Bay
- Kathleen A. Yearick
affiliations:
- University of Illinois at Urbana-Champaign
arxiv_id: '2606.28661'
url: https://arxiv.org/abs/2606.28661
pdf_url: https://arxiv.org/pdf/2606.28661
published: '2026-06-26'
collected: '2026-07-03'
category: Reasoning
direction: 推理时采样效率上限与停止策略
tags:
- test-time scaling
- sampling strategy
- modal ceiling
- correlation ceiling
- effective sample size
- identifiability gap
one_liner: 揭示测试时缩放中盲目增加采样次数无法持续提升答案选择准确率，提出模态上限与相关性上限，并给出有效样本数作为停止信号。
practical_value: '- 在基于 LLM 的推荐生成（如推荐理由、Query 改写）中采用多数投票时，利用模态上限确定最优采样规模，避免冗余推理成本。

  - 评估生成式推荐模型时，将 pass@k（覆盖率）与业务指标（选择准确率）解耦，监控 identifiability gap，指引优化重点从生成转向答案识别。

  - 在在线推理中计算有效样本数，作为动态停止采样的信号，实现自适应计算预算控制。

  - 为提升 Agent 决策或链式推理的可靠性，应优先投资于验证器或置信度估计器，弥补识别瓶颈，而非单纯扩大采样次数。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：测试时缩放通常靠反复采样提升正确覆盖率，但部署系统只能选择一个最终答案，而选择机制（如投票）存在上限，导致覆盖率持续上升而实际准确率停滞的“可识别性差距”。需要找到采样次数的有效边界。

**方法关键点**：定义**模态上限**：多数投票结果在数十次采样后即稳定；**相关性上限**：评估分数所需采样数更少，因样本间存在内部相关。引入**有效样本数**的概念，通过设计效应和同类相关系数量化新增样本带来的独立信息量，当有效样本数达饱和时采样应停止。

**关键结果**：在典型数学推理任务中，多数投票准确率在 ~30-50 次采样后即达模态上限，继续采样至数千次无提升甚至下降；相关性上限出现更早。瓶颈在于识别正确答案的能力，而非生成能力。
