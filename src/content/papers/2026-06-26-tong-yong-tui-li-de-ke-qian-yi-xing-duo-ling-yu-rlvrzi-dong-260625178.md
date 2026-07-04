---
title: 'Transferability for General Reasoning: An Automated Curriculum for Multi-Domain
  RLVR'
title_zh: 通用推理的可迁移性：多领域RLVR自动课程学习
authors:
- Yongjin Yang
- Jiarui Liu
- Yinghui He
- Lechen Zhang
- Bernhard Schölkopf
- Zhijing Jin
affiliations:
- University of Toronto
- Carnegie Mellon University
- Princeton University
- University of Illinois Urbana-Champaign
- Max Planck Institute for Intelligent Systems
arxiv_id: '2606.25178'
url: https://arxiv.org/abs/2606.25178
pdf_url: https://arxiv.org/pdf/2606.25178
published: '2026-06-26'
collected: '2026-07-04'
category: Training
direction: 跨领域迁移感知课程 · RLVR
tags:
- RLVR
- curriculum learning
- gradient alignment
- multi-domain reasoning
- bandit
- transferability
one_liner: 提出Transfer-Aware Curriculum (TAC)，利用梯度投影对齐自动选择能促进跨领域迁移的训练领域
practical_value: '- 在多任务推荐或跨场景排序中，借鉴梯度投影对齐度量任务间迁移性，动态调整训练数据采样权重，避免领域不均衡导致头部任务垄断。

  - 在LLM微调业务中，用在线bandit策略融合局部学习进度与跨域迁移信号，无需人工设计课程，且计算开销极小（<1%），适合工程落地。

  - 可利用RL训练已产生的优势函数和投影梯度，不必额外构造监督信号，降低实现复杂度。

  - 实际场景中，若领域间存在正向迁移（如通用语义理解可为多个下游任务带来增益），TAC思路可扩展至多领域对话、多意图排序等场景，提升整体性能。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多领域RLVR（数学、编程、科学等）的训练数据采样通常固定或人工调参，未考虑跨领域迁移能力差异。现有基于可学性（learnability）的课程仅追随当前进步最快的领域，却忽略了其对其他领域的帮助，可能导致训练不均衡和负迁移。

**方法**：提出Transfer-Aware Curriculum (TAC)，一种在线bandit课程。为每个领域计算两个信号：①局部可学性——用各领域的平均优势值衡量当前学习进度；②跨领域迁移性——利用GRPO步骤中已算出的投影梯度，估计该领域更新对其他领域损失的影响（梯度对齐度）。当前领域的最终得分为这两项的组合。采样权重按softmax分布动态调整，实现自动课程。整个过程复用RL训练已有计算，墙钟时间开销<1%。

**结果**：在六领域推理套件上，TAC在Qwen3-1.7B和Llama3.2-3B上均达到最佳宏观平均准确率，超越比例随机采样、人工设计课程及learnability-only bandit，较后者高出最多2.8个百分点（相对提升10%）。消融实验表明，去除迁移项后性能急剧下降；在数据极度不均衡的混合训练下，TAC仍保持鲁棒，而learnability-only方法会过度偏向优势领域。
