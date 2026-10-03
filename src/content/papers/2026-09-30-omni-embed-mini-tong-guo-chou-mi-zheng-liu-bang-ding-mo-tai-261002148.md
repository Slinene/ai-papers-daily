---
title: 'Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation'
title_zh: Omni-Embed-Mini：通过稠密蒸馏绑定模态而不遗忘
authors:
- Mohammed Irfan Kurpath
- Jaseel Muhammad Kaithakkodan
- Sahal Shaji Mullappilly
- Ivan Laptev
- Hisham Cholakkal
affiliations:
- Mohamed Bin Zayed University of Artificial Intelligence
arxiv_id: '2610.02148'
url: https://arxiv.org/abs/2610.02148
pdf_url: https://arxiv.org/pdf/2610.02148
published: '2026-09-30'
collected: '2026-10-03'
category: Multimodal
direction: 多模态嵌入蒸馏与对齐
tags:
- Multimodal Embedding
- Distillation
- SigLIP
- LoRA
- Matryoshka
- Hard Negative Mining
one_liner: 0.9B 参数多模态嵌入模型，冻结文本塔、用稠密 caption 自身嵌入作教师，在不退化文本检索下对齐六模态
practical_value: '- 多模态向量召回：把商品图片、视频、ASR 文案、详情页等映射到同一余弦空间，可实现自然语言 query 直接检索图片/视频/富文档，直接用于电商搜索、广告创意匹配、内容推荐。

  - 冻结文本塔防退化：现有文本 embedding 服务（如商品描述召回）扩展多模态时，可完全冻结文本编码器，只对非文本模态编码器加轻量 projector 和
  phased LoRA，避免线上文本检索指标下滑，工程上更安全。

  - 用稠密 caption 做教师信号：用多模态 LLM 离线为图片/视频/音频批量生成 dense caption，再以文本塔 embed caption 作为学生对齐目标，无需单独训练教师模型，成本低且几何空间天然一致。

  - 在线混合 hard negative miner：随着 encoder 更新逐步 sharpen 负样本，可结合 ANN 检索召回困难负样本，提升对比学习区分度，适合电商多模态检索中的难例挖掘。

  - 0.9B 小模型即可覆盖六模态，2.3B 变体接近闭源 gemini-embedding-2，适合业务落地部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：文本嵌入模型扩展到新模态通常会损害文本检索质量，而现有多模态嵌入模型往往靠数十亿参数弥补。该工作旨在不更新任何文本侧参数的前提下，把文本、语音、音频、图像、视频、富文档六种模态映射到同一共享余弦空间，并保持文本检索能力不退化。

**方法关键点**：
- 教师信号无需独立嵌入模型：每个媒体样本配有稠密级联 caption，教师目标就是冻结骨干自身对 caption 的 embedding。因为教师和学生共享同一骨干权重，几何空间完全一致。
- 非文本模态编码器上只加轻量 projector 和分阶段 LoRA adapter，文本塔 bit-identical 冻结。
- 训练损失为 Matryoshka SigLIP 对比损失，配合在线混合 hard-negative miner，负样本随编码器提升不断 sharpen。
- 2.3B 变体通过替换为原生视觉-语言骨干即可复用同一训练配方。

**关键结果**：
- 0.9B 模型文本权重与骨干 bit-identical，文本检索不回归：MTEB-v2 BEIR-8 nDCG@10 保持 49.57。
- 扩展到五种额外模态，模型尺寸比所有对比的开源 omni embedder 小约 2.7~9.5 倍。
- 2.3B 变体与闭源 gemini-embedding-2 竞争，整体模态平均指标略胜。
