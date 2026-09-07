---
title: Latent-Aligned Reasoning for Multimodal Recommendation
title_zh: 潜在对齐推理用于多模态推荐
authors:
- Jiarui Jin
- Anyang Ji
affiliations:
- Xiaohongshu Inc.
- Nanjing University
arxiv_id: '2609.04645'
url: https://arxiv.org/abs/2609.04645
pdf_url: https://arxiv.org/pdf/2609.04645
published: '2026-09-04'
collected: '2026-09-07'
category: Multimodal
direction: 多模态推荐 · VLM 潜在推理与双对齐
tags:
- Multimodal Recommendation
- Latent Reasoning
- Cross-modal Dilution
- VLM
- Contrastive Learning
- Item Embedding
one_liner: 提出 LARK 两阶段潜在推理框架，用视觉与推理文本双重对齐缓解多模态推荐中的跨模态稀释，在 Amazon 与工业数据集上一致超越 baseline
practical_value: '- 离线 item encoder 部署：用 VLM 对商品图/文离线生成 embedding 并预存向量索引，线上只训练 DeepFM/LightGCN/SASRec
  等轻量模型，把多模态推理成本完全移出 serving 路径；该论文在百万级商品上验证了此 decoupled 设计的可扩展性。

  - 用 Swing 相似度构造 item-item 对比学习正样本，比随机负样本更符合电商协同信号，能显著提升长尾商品表示；已有 Swing 的电商场景可直接替换为
  InfoNCE 的正样本源。

  - 若业务需要在 VLM 内做多步推理，可采用 latent tokens + 双对齐：用 frozen vision encoder 做 patch-wise
  对齐保留视觉信息，用 stop-gradient CoT hidden states 对齐保留推理语义；掩码图像 50% 可防过拟合像素级细节。

  - 超参参考：latent token 总数 16（4 组×4）、损失权重 0.1、对比温度 0.07 在多个数据集稳健；3B 参数 VLM 即可超越 7B NoteLLM-2，说明结构设计比模型规模更关键。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多模态 VLM 在推荐中能统一视觉和文本理解，但多步 CoT 推理会使视觉和文本信号逐步衰减——论文称之为 cross-modal dilution。推荐场景要求最终输出 dense item embedding，没有自回归刷新信号的机会，因此该问题尤为严重。

**方法关键点**  
- 两阶段架构：阶段 1 learnable latent tokens 与多步 CoT 交错；latent mode 用 hidden state 反馈避免离散化瓶颈，语言段用 teacher forcing 生成 CoT。  
- 双对齐：阶段 1 用 frozen vision encoder 对 latent 特征做 patch-wise alignment（L_vision）保存视觉细节；阶段 2 经 Bridge MLP 投影后用 Swing 挖掘的 item-item 正样本做 InfoNCE 对比学习（L_i2i），并将中间特征与阶段 1 CoT hidden states 的 stop-gradient 均值对齐（L_text）锚定推理语义。  
- 训练目标联合 L_cot、L_vision、L_text、L_i2i；VLM 用 Qwen2.5-VL-3B，mask ratio 0.5，latent tokens 16，Swing top-K=10。

**关键结果数字**  
在 Amazon Baby/Sports/Clothing 和百万级 In-House 数据集上，LARK 在所有指标上超越 SOTA。In-House 上 LARK LightGCN R@20=0.0548，比 AlignRec 提升 10.0%；Baby 上 R@20=0.1148。特征替换实验中，MMGCN 接入 LARK embedding 后 R@20 提升 13.9%（Baby）和 15.1%（Sports），长尾商品增益最大。消融显示去除 latent reasoning 使 R@20 下降 17.4%，去除 L_text 降 8.4%，去除 L_vision 降 5.5%。

**最值得记住的一句话**  
跨模态稀释是 VLM 多步推理推荐中的核心瓶颈，用 latent tokens 做视觉 checkpoint 并与推理文本对齐，能显著提升 item 表示质量并迁移到任意下游推荐模型。
