---
title: 'OmniScope: Modality-Decoupled Token Compression for Omnimodal Large Language
  Models'
title_zh: OmniScope：面向全模态大语言模型的模态解耦Token压缩
authors:
- Jinsen Su
- Yongdong Luo
- Yuexiao Ma
- Yibo Hu
- Meiguang Jin
- Xiaowu Zheng
affiliations:
- Xiamen University
- Alibaba Group
arxiv_id: '2607.23193'
url: https://arxiv.org/abs/2607.23193
pdf_url: https://arxiv.org/pdf/2607.23193
published: '2026-07-27'
collected: '2026-08-02'
category: Multimodal
direction: 全模态LLM推理加速 · 模态解耦压缩
tags:
- Token Compression
- OmniLLM
- Modality Decoupling
- Video Understanding
- Inference Acceleration
- Cross-Modal Salience
one_liner: 训练无关的模态解耦压缩框架，解决音视频跨模态显著度错配，实现高效全模态推理
practical_value: '- 模态解耦思想可迁移到多模态推荐：在视频+音频+文本场景下，不同模态对点击/转化的贡献峰值可能不同时，应独立计算各模态token显著性再融合，避免跨模态指导遗漏关键信息。

  - 训练无关压缩框架可直接嵌入已部署的多模态大模型，不增加微调成本；根据内容复杂度动态分配各模态token预算，适合工程化轻量实现。

  - anchor-delta视觉剪枝策略保留全局上下文与时序变化，可用于商品展示视频或直播帧采样，保留关键变化帧的同时降低token数。

  - 音频按秒合并的冗余去除方法可应用于直播语音或客服会话的压缩，减少后续模型输入长度，提升吞吐。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：全模态LLM（如Qwen2.5-Omni）同时处理音视频，现有token压缩方法通常假设跨模态显著度一致，用一模态指导另一模态的保留。但观察发现，同一查询下音频与视频的相关性峰值时刻常不一致，激进压缩时易丢弃回答关键线索。

**方法**：提出OmniScope，训练无关的模态解耦框架。以查询为共享语义锚点，分别估计音频和视频的显著性；分配模态特定token预算；视觉token使用anchor-delta策略剪枝，保留全局上下文和时序变化；音频token按秒合并以降低冗余并保持时序连续性。

**结果**：在四个音视频基准和两个规模的Qwen2.5-Omni上，OmniScope在所有压缩设置下平均准确率最优。25%总体token保留率时，实现最高3.53倍prefill加速、>15% GPU内存节省，平均准确率仅下降0.35点，验证了“共享查询、独立显著度估计”的设计原则。
