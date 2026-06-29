---
title: 'ABACUS: Adapting Unified Foundation Model for Bridging Image Count Understanding
  and Generation'
title_zh: ABACUS：统一基础模型适配以实现图像计数理解与生成
authors:
- Anindya Mondal
- Sauradip Nag
- Anjan Dutta
affiliations:
- University of Surrey
- Simon Fraser University
arxiv_id: '2606.23835'
url: https://arxiv.org/abs/2606.23835
pdf_url: https://arxiv.org/pdf/2606.23835
published: '2026-06-21'
collected: '2026-06-29'
category: Multimodal
direction: 视觉语言模型统一理解与生成
tags:
- VLM
- Object Counting
- Image Generation
- GRPO
- Cycle-Consistency
- Unified Model
one_liner: 提出统一视觉语言模型 ABACUS，无需基准特定训练即可在多种计数任务和计数忠实图像生成上取得 SOTA
practical_value: '- 对于需要生成特定数量商品的电商场景（如促销图“5 件装”），可直接迁移 ABACUS 的计数忠实生成能力，确保图像内容与文案严格对齐。

  - 统一模型多任务设计思路可借鉴到推荐系统：用一个模型同时处理点击率预估、转化率预估、商品文案生成等任务，减少独立训练成本。

  - 循环一致性 GRPO 策略（理解分支自我批评生成结果）无需外部标注，可应用于推荐系统的生成式对话 agent 中，通过自我纠错提升回复事实性。

  - 自适应缩放与物体性图的局部感知机制，可类比到多模态召回，对 query 区域重点建模，提高细粒度检索准确率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：图像计数理解和计数忠实生成通常被独立研究，现有文本到图像扩散模型无法控制输出数量，而大 VLM 仅能给出粗粒度估计（如“>100”），且同一模型理解与生成之间存在鸿沟——能正确数出 4 个苹果的模型却无法生成恰好 4 个苹果。

**方法**：基于 3B 参数统一基础模型，提出三项关键创新：(1) **密度感知自适应缩放**——利用物体性图（objectness maps）进行空间定位，自适应裁剪高密度区域以提升细小物体计数精度；(2) **边界感知计数策略**——通过 GRPO 强化学习消除裁剪边界误差，训练模型学会当物体横跨边界时同时计算完整与部分实例；(3) **循环一致性 GRPO**——理解分支对生成分支的输出进行自我批评，无需外部标注即可缩小理解与生成间的差距。模型可处理物体计数、人群计数、指代表达计数和计数条件图像生成，所有任务使用统一文本提示，无需任何基准特定训练。

**关键结果**：在 7 个基准测试（包括生成和理解）上均达 SOTA，超越专用模型和更大参数量的通用模型，例如在 COCOnut、CrowdHuman 等数据集上明显优于现有方法。
