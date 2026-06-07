---
title: 'AdaCodec: A Predictive Visual Code for Video MLLMs'
title_zh: AdaCodec：面向视频 MLLM 的预测性视觉编码
authors:
- Haowen Hou
- Zhen Huang
- Zheming Liang
- Qingyi Si
- Chenglin Li
- Shuai Dong
- Kele Shao
- Ruilin Li
- Dianyi Wang
- Nan Duan
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- JD.com
arxiv_id: '2606.02569'
url: https://arxiv.org/abs/2606.02569
pdf_url: https://arxiv.org/pdf/2606.02569
published: '2026-05-31'
collected: '2026-06-07'
category: Multimodal
direction: 多模态大模型 · 视频压缩编码
tags:
- predictive coding
- video MLLM
- visual token compression
- adaptive GOP
- motion-residual encoding
one_liner: 将视频帧编码为自适应 I/P 帧：高预测代价的参考帧保留全量 tokens，中间帧压缩为紧凑 P-tokens，在 1/7 视觉 token
  预算下保持甚至超越基线准确率，并大幅降低延迟。
practical_value: '- 对于多模态购物推荐或直播商品理解场景，可借鉴自适应 I/P 帧选择机制，对关键帧保留全量视觉 token，非关键帧仅传输变化信息，大幅降低视频
  token 开销，减少推理时延和成本。

  - P-tokenizer 将运动向量和残差编码为紧凑 token 的思路，可复用于商品视频的理解前端，在不损失太多有效信息的前提下压缩 token 序列长度，提升多模态模型的吞吐。

  - 基于预测代价的自适应 GOP 构造策略，可推广至其他序列建模任务（如用户行为序列），用动态关键点替代均匀采样，平衡信息密度与计算预算。

  - 整体方案提供了一种视频 MLLM 的视觉接口设计范式，类似视频压缩中的 I/P 帧思想，可直接用于 Agent 或 RAG 场景中对长视频的实时理解与检索。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频多模态大模型（video MLLM）对逐帧独立编码，大量视觉 token 重复帧间共有内容，造成严重的计算和内存冗余。 

**方法**：
- 将视觉接口设计为预测性编码（predictive visual code），自适应划分视频为图像组（GOP）。
- 为每帧计算预测代价 `pcost`，高于阈值时将其作为 I-frame，用 ViT 编码为全量 256 tokens；否则作为 P-frame，由 P-tokenizer 提取运动向量和重建残差，压缩为 16-token 的紧凑表示。
- 该自适应 I/P 选择使得模型仅在场景无法被上下文良好预测时才发送完整参考帧，其余仅发送帧间变化。

**关键结果**：
- 在 11 个基准上，与 Qwen3-VL-8B 逐帧基线相比，匹配视觉 token 预算时 AdaCodec 全面优于基线；仅使用 1/7 的 token（32k vs 224k），在长视频基准上已超越基线，在通用视频基准上也匹配甚至小幅提升平均分。
- TTFT（首 token 延迟）从 9.26 秒降至 1.62 秒，端到端延迟从 11.18 秒降至 3.20 秒，同时准确率整体不降。
