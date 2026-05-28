---
title: 'Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini'
title_zh: Gemini Embedding 2：原生多模态统一嵌入模型
authors:
- Madhuri Shanbhogue
- Zhe Li
- Shanfeng Zhang
- Gustavo Hernández Ábrego
- Shih-Cheng Huang
- Aashi Jain
- Daniel Salz
- Sonam Goenka
- Chaitra Hegde
- Ji Ma
affiliations:
- Google
arxiv_id: '2605.27295'
url: https://arxiv.org/abs/2605.27295
pdf_url: https://arxiv.org/pdf/2605.27295
published: '2026-05-25'
collected: '2026-05-28'
category: Multimodal
direction: 多模态统一嵌入 · 跨模态检索
tags:
- Multimodal Embedding
- Cross-modal Retrieval
- Video Retrieval
- Audio Retrieval
- MMTEB
- MRL
one_liner: 基于 Gemini 构建的多模态统一嵌入模型，在文本/图像/视频/音频及交叉任务上达到 SOTA，并展现强零样本域泛化。
practical_value: '- **原生多模态避免级联损失**：音频直接编码方案比 ASR → 文本嵌入领先 +3.6 mrr@10，跨语言场景更达 +5.0。电商语音搜索（如智能客服、语音评论检索）可直接复用，省去
  ASR 链路。

  - **交织输入支持复杂搜索意图**：模型可接受“图片+文本”或“视频片段+关键词”的组合 query，实现更精准的跨模态检索。在产品推荐中，用户可上传商品图加“类似款但更休闲”的文字，提升搜索命中。

  - **多阶段多任务训练 + Model Soup 平衡通用与领域**：PFT → FT → Model Soup 的配方可迁移至业务自有数据，少量领域数据 fine-tune
  后通过 soup 恢复通用性，避免 Catastrophic Forgetting。适合电商垂直品类或 Agent 特定工具检索微调。

  - **MRL 多维度输出**：单模型支持 768、1536、3072 维，实际部署可按成本/延迟选维度，无需重新训练。推荐系统可用低维向量做召回，高维做精准排序。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
当前多模态嵌入模型多采用双塔后期融合架构（如 CLIP），难以处理交错输入（interleaved）且未充分利用模态间交互。业界亟需一个能统一映射文本、图像、视频、音频及任意组合至同一语义空间的模型，以支撑多模态搜索、推荐、RAG 等复杂应用。

## 方法关键点
- **架构**：以 Gemini 为基础模型，使用双向注意力 Transformer，对令牌序列做 mean pooling 后经线性投影至 3072 维。利用 MRL 同时优化 768、1536、3072 维。
- **训练**：多任务多阶段对比学习（噪声对比估计损失，含 in-batch negatives 及 hard negatives）。第一阶段 Pre-Fine-Tuning (PFT) 用大 batch 噪声数据适配编码；第二阶段 Fine-Tuning (FT) 加入多模态任务并精调 batch size；第三阶段 Model Soup 融合不同 FT 检查点。
- **数据**：覆盖文本、代码、图像、视频、音频的单模态、交叉模态及多模态任务。利用 Gemini 合成高质量伪标签数据（如代码检索任务提升+15.8）。
- **原生模态处理**：视频采样 1 fps 最多 32 帧；音频直接输入，无需 ASR 转录。

## 关键结果
在 MSCOCO 文本→图像 R@1 达 62.9，Flickr30k 图像→文本 R@1 97.4；MTEB 多语种 69.9，代码 84.0，双项超越前代文本版及竞品。视频检索 Vatex NDCG@10 68.8，YouCook2 52.5。文档检索 ViDoRe V2 64.9。零样本域泛化：天文、显微镜、食谱等专用数据集大幅领先 CLIP、SigLIP 等。音频检索 MSEB 上原生音频比 ASR 方案 mrr@10 高 3.6 点。

## 一句话
“Gemini Embedding 2 不再只是多模态‘对齐’，而是通过原生交织处理和多任务训练，将全模态语义真正统一进一个向量空间，使零样本跨域检索成为可能，这为下一代多模态搜索与推荐提供了基座。”
