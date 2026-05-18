---
title: A Cross-Modal Prompt Injection Attack against Large Vision-Language Models
  with Image-Only Perturbation
title_zh: 仅图像扰动的跨模态提示注入攻击大视觉语言模型
authors:
- Hao Yang
- Zhuo Ma
- Yang Liu
- Yilong Yang
- Guancheng Wang
- JianFeng Ma
affiliations:
- Xidian University
arxiv_id: '2605.16090'
url: https://arxiv.org/abs/2605.16090
pdf_url: https://arxiv.org/pdf/2605.16090
published: '2026-05-15'
collected: '2026-05-18'
category: Multimodal
direction: 多模态模型安全与对抗攻击
tags:
- prompt injection
- LVLM
- cross-modal
- adversarial perturbation
- security
- multimodal
one_liner: 首次实现仅通过图像扰动同时操控LVLM对视觉和文本输入的跨模态提示注入
practical_value: '- 用于多模态推荐系统安全性测试：可借鉴跨模态攻击思路，验证模型是否容易被图像扰动误导，影响图文推荐的一致性。

  - 扰动预算分配策略（距离语义区域越远，扰动越小）可用于视觉模型可解释性分析或对抗训练，提升推荐模型对噪声的鲁棒性。

  - 层选择揭示多模态融合发生在模型中部，可指导多模态推荐模型的结构设计，将融合模块放在中间层而非最后一层。

  - 隐藏状态空间优化思路可迁移到多模态Agent的对抗样本生成或鲁棒性增强训练中。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有大视觉语言模型（LVLM）的提示注入攻击只能沿单模态传导，无法实现跨模态操控，即图像注入仅影响视觉解释，文本注入仅影响文本解释。

**方法**：提出CrossMPI，仅通过扰动图像实现跨模态提示注入，使模型对视觉和文本输入均做出攻击者期望的解释。核心创新有三：1）将扰动优化目标从视觉嵌入空间（约10^5参数）转向模型隐藏状态空间（约10^7参数），扩大可操控的多模态信息流；2）提出层选择策略，首次发现对LVLM提示扰动最优的层位于模型中部而非最后一层，以约束优化参数空间；3）设计距离递减扰动预算分配，像素离语义关键区域越远，扰动预算越小，从而约束图像扰动空间。

**结果**：在多个LVLM（如LLaVA、BLIP-2）和数据集上，CrossMPI的跨模态操控成功率显著高于基线方法，同时保持图像扰动不可见。消融实验验证了中部层选择和距离递减预算分配的关键作用。
