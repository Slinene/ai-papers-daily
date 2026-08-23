---
title: 'Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio
  Learners'
title_zh: 聆听向前：下一 Patch 嵌入预测实现可扩展音频学习器
authors:
- Umberto Cappellazzo
- Xubo Liu
- Stavros Petridis
- Maja Pantic
affiliations:
- Imperial College London
- University of Surrey
arxiv_id: '2608.19863'
url: https://arxiv.org/abs/2608.19863
pdf_url: https://arxiv.org/pdf/2608.19863
published: '2026-08-19'
collected: '2026-08-23'
category: Other
direction: 自监督音频表征 · 下一 patch 预测
tags:
- Self-Supervised Learning
- Audio Representation
- Autoregressive Prediction
- Next Patch Embedding
- Causal Transformer
- Spectrogram
one_liner: 用因果 Transformer 预测下一 patch embedding，极简自监督在音频任务达到 SOTA
practical_value: '- 用户行为序列预训练可借鉴 NAPE 的「下一 embedding 预测」：将行为序列切块后，用因果 Transformer
  预测下一步用户/item embedding，配合 stop-gradient 避免表征坍塌，无需构建离散 Semantic ID 或重建 item 特征，大幅降低工程复杂度。

  - 现有推荐 SSL 常依赖对比学习+掩码重建+teacher-student 等多重目标，NAPE 证明仅自回归前向预测 + stop-gradient 即可学出强表征，可作为轻量预训练
  baseline，减少超参调优和训练成本。

  - 因果掩码天然适配流式增量训练，适合电商/广告的实时序列建模；同时自回归预测下一 embedding 可直接作为在线学习辅助任务，无需等待完整序列即可更新表征。

  - log-mel patch 切分思路可迁移到商品多模态序列（如短视频帧、商品描述片段），统一用预测下一 patch embedding 做跨模态预训练，简化多模态对齐流程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：音频自监督学习（SSL）近年性能提升依赖于越来越复杂的预训练配方，例如重建解码器、声学 tokenizer、student-teacher 蒸馏、辅助正则化损失。相比之下，语言和视觉领域最有效的表示学习正转向极简的自回归预测：从历史上下文预测下一个元素，无需人工设计代理任务。音频的时序结构使预测下一 patch embedding 天然适配。

**方法关键点**：提出 NAPE（Next-Audio-Patch-Embedding prediction），将 log-mel 频谱图划分为 patch，输入因果 Transformer，仅预测每个下一 patch 的连续 embedding。训练信号只有两个：因果掩码（causal masking）保证只看到过去，stop-gradient 防止表征坍塌。整个框架刻意保持极简，避免重建 decoder、离散 tokenizer、student-teacher 结构以及任何辅助正则化损失。

**关键结果**：在 6 个音频与语音基准上，NAPE 在多个任务 fine-tuning 达到 state-of-the-art，模型规模从 small 到 large 扩展性能一致；线性 probing 同样取得有竞争力的结果。无需显式监督，attention 模式自发呈现结构化特征。
