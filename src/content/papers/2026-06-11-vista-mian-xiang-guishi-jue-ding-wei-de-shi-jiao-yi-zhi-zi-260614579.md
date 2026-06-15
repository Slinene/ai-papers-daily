---
title: 'VISTA: View-Consistent Self-Verified Training for GUI Grounding'
title_zh: VISTA：面向GUI视觉定位的视角一致自验证训练框架
authors:
- Xinyu Qiu
- Yunzhu Zhang
- Heng Jia
- Shuheng Shen
- Changhua Meng
- Linchao Zhu
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2606.14579'
url: https://arxiv.org/abs/2606.14579
pdf_url: https://arxiv.org/pdf/2606.14579
published: '2026-06-11'
collected: '2026-06-15'
category: Agent
direction: GUI智能体视觉定位训练方法
tags:
- GUI Grounding
- GRPO
- Reinforcement Learning
- View Consistency
- Self-Verified Training
one_liner: 通过多视角组构建与自验证锚点，缓解GRPO在GUI定位中组内无相对优势的问题
practical_value: '- **GRPO组构建策略**：将单一实例的多视角裁剪作为一个组，强制模型学习视角不变性。类似思路可用于电商推荐系统，将同一商品的不同视图（如多角度图片、标题变体）构成对比组，提高模型对输入扰动的鲁棒性。

  - **自验证锚点机制**：在RL训练中动态加入oracle答案作为正则化项，仅在模型已产生高分rollout时激活，既避免策略坍塌为简单模仿，又稳定了短序列生成。该方法可迁移到其他基于RL的文本生成任务（如推荐理由生成、对话式推荐），以提升训练稳定性。

  - **目标保持裁剪增强**：通过裁剪确保目标区域可见且坐标精确映射，实现了语义等价但几何差异的输入增强。在电商场景中，可以类似地构造商品图像局部区域的正样本对，用于训练商品定位或热区预测模型。

  - **鲁棒性提升思路**：VISTA显著降低了预测翻转率（prediction flip rate），表明模型对输入变化更稳定。对于需要高可靠性的Agent系统（如自动化下单、客服），这种训练范式能减少因微小界面变化导致的误操作。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在GUI Grounding任务中应用GRPO时，rollouts均来自同一截图视角，导致困难样本上群体内全失败、简单样本上全成功，使相对优势信号消失，训练无效。
**方法**：提出VISTA框架，核心包括：(1) **视角一致性组构建**：对同一GUI实例生成多个目标保持的裁剪视图，保持目标元素可见并重映射边界框，形成语义等价但几何不同的输入组，使rollouts可跨视图比较；(2) **自验证跨视图锚点**：额外维护一个oracle答案，通过优势加权损失优化，但排除在组基线外，仅当模型产出最大奖励rollout时才激活，以此稳定训练而不退化为无条件模仿。
**结果**：在5个GUI Grounding基准上，VISTA显著提升Qwen3-VL多尺寸模型的准确率。ScreenSpot-Pro上4B/8B/30B分别从55.5/52.7/53.7提升至63.4/65.8/67.0，且在最差视角准确率和预测翻转率等鲁棒性指标上表现更优。
