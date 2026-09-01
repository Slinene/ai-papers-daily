---
title: 'CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product
  Ads Retrieval'
title_zh: CAMIE：面向 Snap 动态商品广告检索的协同参与多模态商品嵌入
authors:
- Xiaodong Liu
- Siman Wang
- Congfei Zhang
- Hsiang-wei Chao
- Xiao Bai
- Wen Zhang
- Jingxiao Ma
- Zhe Liu
- Yunzhi Zhou
- Yajun Wang
affiliations:
- Snap Inc.
arxiv_id: '2608.30255'
url: https://arxiv.org/abs/2608.30255
pdf_url: https://arxiv.org/pdf/2608.30255
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 多模态商品嵌入 · 协同参与对比学习召回
tags:
- co-engagement
- multimodal embeddings
- item-to-item retrieval
- LLM-MLLM
- contrastive learning
- production ads
one_liner: 用用户旅程中的共同参与对微调 LLM/MLLM 骨干，得到统一多模态商品嵌入并上线 Snap DPA
practical_value: '- **用共同参与 pair 替代内容相似度监督**：在电商/广告 I2I 召回中，从用户 Session 或归因窗口挖掘共现商品对（view/click/加购/购买均可），用对称
  in-batch InfoNCE 微调商品编码器，比单纯内容相似度更贴近转化目标。业界常纠结“只保留高意图事件”，但该文证明：全漏斗事件带来的训练规模增益（+8.9%
  R@10）大于只保留加购/购买的事件纯度增益（+1.6%），可优先保规模。

  - **一个 checkpoint 服务多模态 / 纯文本 / 纯图片三种召回面**：通过 renderer 控制字段（image/title/brand/description/category），同一个
  MLLM 骨干能同时支持多模态和文本检索。在 Snap 场景文本-only 仅比专用文本微调差 1.1pp R@10，可直接替换独立文本编码器；但纯图片 serving
  明显弱于专门视觉塔，电商图像替代类召回建议保留专用 image encoder。

  - **行为监督的增益大于骨干升级**：对照实验表明，在相同的 co-engagement pair、目标函数、负样本、LoRA 设置下，SigLIP2 和 CLIP
  双塔也能达到接近 CAMIE 的召回水平，说明业务里如果已有轻量双塔，优先把训练信号换成共同参与 pair，比急着换 LLM 骨干收益更稳；MLLM 的增量主要在文本侧和训练
  headroom。

  - **工程部署可复用**：离线用 512 维 embedding，线上截取前 128 维匹配现有 ANN 索引，控制索引成本；对百万级商品目录用 10M 训练对即可达到较好效果，训练规模扩展到
  100M 对进一步提升，适合电商场景逐步扩量。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生产级 item-to-item (I2I) 检索普遍存在两个问题：一是视觉、文本、多模态编码器各自为政，多套召回链路和 ANN 索引割裂；二是内容-only 训练只学内容相似，不学用户真实共同互动行为，导致召回与下游转化不一致。Snap 动态商品广告（DPA）需要一个能同时服务多模态、纯文本、纯图片的统一商品编码器，并用共同参与信号对齐推荐空间。

## 方法关键点
- **数据构造**：从 30 天用户旅程中挖掘无向共同参与商品对，包含 view/click/加购/购买事件，采用 7 天半衰期时间衰减权重，每用户最多采 2 对，并要求 EXACT match 归因、非空标题图片、相同广告主、一级类目一致。
- **模态感知编码**：将商品渲染为 image/title/brand/description/category 的输入序列；训练时多用多模态，serving 可通过不同 renderer 切到文本-only 或图片-only。
- **网络与训练**：使用 Qwen3-VL-Embedding 2B 作为骨干，冻结骨干 + LoRA（r=32, α=64）在 attention 投影 + 可训练 projection head；采用对称 in-batch InfoNCE 目标，跨设备收集负样本，512 维 embedding。
- **ANN 服务**：离线对目录商品编码建索引，在线通过 seed item 的 embedding 做一次 ANN top-K 查询，保持与传统 I2I 相同的延迟。

## 关键结果
- 离线：CAMIE 在 R@10 上达到 137.7%（相对 Qwen3-VL-Embedding 2B pretrained 的 100%），超过最强商用多模态 embedding Gemini Embedding 2 约 6%；同一 checkpoint 文本-only 服务比专用文本微调仅差 1.1pp。
- 归因：在相同数据、损失、负样本和训练步数下，SigLIP2 和 CLIP 双塔与 CAMIE 拉到 5.5pp 内，证明 co-engagement 监督是主要增益来源；MLLM 的额外优势主要在文本侧和训练更长时的 headroom。
- 在线 A/B：CAMIE 替换多模态 I2I_MM 编码器，CTR +0.390%、CVR +10.832%；替换文本 I2I_TEXT 编码器，CTR +18.958%、CVR +13.12%；整体 DPA 流量 CVR +1.911%、CTR +0.211%。

## 最值得记住的一句话
行为监督（共同参与 pair）而非骨干架构，买走了大部分质量提升；MLLM 的真正价值在于用同一个 checkpoint 同时服务多模态和文本召回面。
