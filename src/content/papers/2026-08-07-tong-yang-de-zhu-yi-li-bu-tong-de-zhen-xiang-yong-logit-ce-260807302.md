---
title: 'Same Attention, Different Truths: Put Logit-Lens over Visual Attention to
  Detect and Mitigate LVLM Object Hallucination'
title_zh: 同样的注意力，不同的真相：用Logit-Lens检测和缓解LVLM物体幻觉
authors:
- Zichuan Wang
- Songlin Yang
- Bo Peng
- Zhenchen Tang
- Yang Li
- Beibei Dong
- Jing Dong
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Science
- Hong Kong University of Science and Technology
arxiv_id: '2608.07302'
url: https://arxiv.org/abs/2608.07302
pdf_url: https://arxiv.org/pdf/2608.07302
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态幻觉检测与缓解
tags:
- LVLM
- Object Hallucination
- Logit Lens
- Visual Attention
- Detect-Mitigate
one_liner: 发现物体幻觉并非视觉注意力不足，而是注意力区域无法解码为目标token，提出训练免的检测-缓解框架，取得SOTA。
practical_value: '- 在电商图片描述生成或视觉问答中，可借鉴 Logit Lens 检验高注意力区域是否真正解码为目标商品token，快速定位幻觉来源，无需额外训练。

  - 根据幻觉成因分类处理：对于视觉不确定性（相似物体混淆），通过屏蔽高注意力区域（HARM）强制模型重新聚焦；对于上下文先验（强共现偏见），采用视觉证据增强解码（VEED），提高生成可靠性。

  - 训练免的 Detect-Mitigate 框架可以直接嵌入现有 LVLM 推理流程，低成本提升生成质量，对 Agent 中视觉模块的可信输出有实用价值。

  - 注意力图可视化结合 token 解码一致性检查，可以作为一种离线诊断工具，用于发现商品描述生成中的常见幻觉模式，进而优化数据或 prompt。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：大型视觉语言模型（LVLM）常出现物体幻觉，即描述图像中不存在的物体。以往工作归因于视觉注意力不足，但本文发现真实物体和幻觉物体在模型中层至顶层都获得同等强度的视觉注意力，核心问题不是注意力强度，而是注意力区域的可解码性。

**方法关键点**：
1. 使用 Logit Lens 解码高注意力区域的视觉特征，发现真实物体区域可正确解码为目标 token，幻觉物体区域则不能。
2. 据此识别两种幻觉机制：(a) 视觉不确定性：由语义相似或易混淆区域触发，屏蔽这些区域可消除幻觉；(b) 上下文先验：由强共现偏见触发，即使屏蔽最初关注区域，幻觉仍存在且注意力会漂移到其他区域。
3. 提出训练免的 Detect-Mitigate 框架：Logit-Lens 一致性检查检测幻觉；对视觉不确定性幻觉使用高注意力区域屏蔽（HARM）；对上下文先验幻觉使用视觉证据增强解码（VEED）。

**关键结果数字**：在多个幻觉基准上（如 POPE、MMHal-Bench 等）达到 SOTA，无需额外训练，取得显著提升。
