---
title: 'Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and
  Cannot Do'
title_zh: 看轻，想重：多模态思维链推理的能与不能
authors:
- Zhuoran Jin
- Kejian Zhu
- Hongbang Yuan
- Yupu Hao
- Pengfei Cao
- Yubo Chen
- Kang Liu
- Jun Zhao
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2606.22565'
url: https://arxiv.org/abs/2606.22565
pdf_url: https://arxiv.org/pdf/2606.22565
published: '2026-06-20'
collected: '2026-06-25'
category: Multimodal
direction: 多模态思维链评估与视觉推理分析
tags:
- multimodal chain-of-thought
- visual reasoning
- evaluation
- perception tasks
- reasoning models
one_liner: 系统评估多模态思维链推理，揭示其在感知任务中的反效果与视觉推理瓶颈
practical_value: '- 在电商多模态推荐或购物Agent中，涉及商品图片的视觉接地、目标计数等感知任务时，应谨慎使用思维链推理（CoT），以免性能下降；可按任务类型选择性开启，只在需要复杂分析（如多张图片对比、穿搭推理）时启用慢思考。

  - 对于多图像推理（如商品相似度对比、场景理解），CoT可能有效，但模型会出现‘看轻’现象——视觉反思随推理步骤减弱。可设计显式回看机制，例如在每个推理步骤后重新编码图像特征，或插入视觉锚点提示，强制模型持续关注视觉信息。

  - 选用开源多模态推理模型时，不要仅凭数学或科学推理榜单决定，需额外评估其在基础感知任务（如对象定位、属性识别）上的表现，因现有模型常过度拟合数学任务而牺牲通用视觉能力。

  - 构建多模态Agent时，可将推理流程解耦为轻量级视觉感知与重型语言推理，但需引入外部视觉校验模块，防止因‘想得过重’而忽略图像细节，提升最终决策可靠性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：思维链（CoT）在纯文本推理上效果显著，但在多模态场景下的作用仍不明朗，需系统探究其适用范围与失效原因。

**方法**：在12个多模态任务（涵盖视觉接地、物体计数等感知任务，以及数学、科学、多图像推理等推理任务）上，全面评估14个非推理模型与8个推理模型的CoT效果，对比有无CoT的性能差异，并分析推理过程中的语言与视觉反思模式。

**关键发现**：
1. CoT不是免费午餐：在感知任务上，CoT反而降低性能（如视觉接地、物体计数）；在推理任务上（数学、科学、多图像推理）则有效。
2. 开源多模态推理模型整体提升有限：虽在数学推理上提升明显，但因过度侧重数学训练，牺牲了更广泛的视觉理解能力，导致总体性能仅边际改善。
3. 视觉推理是核心瓶颈：模型表现出‘看轻想重’模式——语言反思（口头分析）在推理过程中时有回升，而视觉反思持续衰减，说明当前多模态CoT无法维持深度的图像内省。

这些发现指出，多模态CoT擅长语言推理链，但视觉能力的深层利用仍是待解难题。
