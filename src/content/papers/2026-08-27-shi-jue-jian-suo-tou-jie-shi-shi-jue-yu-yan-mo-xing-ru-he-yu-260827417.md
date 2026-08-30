---
title: 'Retrieval Heads Meet Vision: Uncovering How VLMs Locate and Extract Visual
  Information'
title_zh: 视觉检索头：揭示视觉语言模型如何定位与提取视觉信息
authors:
- Chanho Park
- Daehyeon Choi
- Jihyun Lee
- Minhyuk Sung
affiliations:
- KAIST
- Independent Researcher
arxiv_id: '2608.27417'
url: https://arxiv.org/abs/2608.27417
pdf_url: https://arxiv.org/pdf/2608.27417
published: '2026-08-27'
collected: '2026-08-30'
category: Multimodal
direction: VLM 可解释性 · 视觉检索头
tags:
- Vision-Language Models
- Interpretability
- Attention Heads
- Visual Grounding
- Causal Analysis
one_liner: 发现 VLMs 中稀疏且因果的视觉检索头，负责将文本描述 grounding 到图像区域
practical_value: '- 业务中用到 VLM（如商品图问答、广告素材理解）时，可通过 mask 少量 VRHs 快速验证定位能力是否关键，或做推理时的受控干预，提升输出可信度。

  - 头打分方法（输出 token 对 GT 区域的 attention 求和）可作为诊断工具，评估多模态模型在特定业务数据上的视觉 grounding 质量，识别失败案例是模型定位偏差还是高层推理问题。

  - VRHs 跨模型迁移（共享 LLM 主干）意味着可以在一个 VLM 上发现关键头，再迁移到同主干的其他 VLM，降低重复分析成本，用于模型压缩或推理加速。

  - 整体上是机制解释的学术贡献，直接迁移到电商推荐/搜索系统还需结合具体业务数据做适配，不建议直接照搬。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLMs 能根据文本定位图像区域并提取视觉证据，但内部机制尚不明确。受 LLMs 中 retrieval heads 的启发，作者探究 VLMs 是否具有类似的视觉检索机制。

**方法**：提出 Visual Retrieval Heads (VRHs)，一个小而因果的注意力头子集。为识别 VRHs，作者将现有头部评分方法统一到一个设计空间，涵盖 query token 选择、key 聚合方式和跨样本聚合。实验表明，从输出预测 token 打分，并对 ground-truth referent 区域求和，最能可靠地识别因果头。

**结果**：在 11 个 VLMs 和 5 个 referring-expression 基准上，VRHs 仅占约 1.7-2.6% 的注意力头，但 masking 前 20 个 VRHs 可使 grounding 准确率下降最多 80 个百分点，而随机 masking 影响甚微。VRHs 不仅复现了文本检索头的因果-稀疏-通用三元组特性，还展现出新性质：跨视觉参考任务泛化（在属性、空间、计数和视觉数学基准上仍具因果性）；功能特异性（破坏定位但保持输出格式）；架构共享性（在共享 LLM 主干但视觉编码器、投影器、指令微调不同的 VLM 间因果迁移）。
