---
title: Gemma 4 Technical Report
title_zh: Gemma 4 多模态模型：高效推理与编码器自由架构
authors:
- Gemma Team
- Sherif El Abd
- Vaibhav Aggarwal
- Robin Algayres
- Alek Andreev
- Olivier Bachem
- Ian Ballantyne
- Cormac Brick
- Victor Cărbune
- Michelle Casbon
affiliations:
- Google DeepMind
arxiv_id: '2607.02770'
url: https://arxiv.org/abs/2607.02770
pdf_url: https://arxiv.org/pdf/2607.02770
published: '2026-07-01'
collected: '2026-07-09'
category: LLM
direction: 多模态 LLM 与推理效率优化
tags:
- Gemma 4
- Multimodal
- MoE
- Thinking Mode
- QAT
- Encoder-Free
one_liner: 开源密集与 MoE 多模态模型，集成思维链、长上下文压缩与量化，在多项基准上以小参数量匹配大模型
practical_value: '- **长上下文 KV 缓存优化**：采用 5:1 局部/全局注意力比、p‑RoPE 位置编码、键值重用 (keys as values)，全局
  KV 缓存减少 37.5%，可直接用于推荐系统的长序列用户行为建模，降低推理显存。

  - **量化感知训练 (QAT)**：提供 int2/int4 混合权重量化版本，搭配 fp16 激活时块级缩放，大幅降低部署内存与延迟；特别适合电商中端侧部署的排序或生成式推荐模型。

  - **多 Token 预测草稿头 (MTP)**：轻量自回归头跨注意主模型 KV 缓存，支持任意草稿长度；可迁移到对话式搜索/推荐 Agent，加速多轮生成响应。

  - **编码器自由多模态架构**：12B 模型直接用线性投影处理原始音频和图像块，省去专用编码器，简化多模态融合管线；在商品图像+语音评价的场景可尝试单一 LLM
  统一提取特征，降低工程复杂度。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
开源大模型越来越需要高效的多模态理解和复杂推理能力，同时要适配从边缘设备到云端的多样硬件。Gemma 4 旨在在不增大参数量的前提下，通过架构创新和训练优化，让中小模型在 STEM、多模态和长文本任务上达到甚至超越更大的开源模型。  
**方法关键点**  
- **架构家族**：密集模型 2.3B/4.5B/12B/31B 和 MoE 模型 26B‑A4B (3.8B 激活)。E2B/E4B 使用逐层嵌入减少有效参数。  
- **思维模式**：输出前生成推理轨迹，提升数学和编程类任务表现。  
- **长上下文效率**：局部/全局注意力比例 5:1（2.3B 为 4:1），全局层用 p‑RoPE (p=0.25) 并重用键作为值，共享部分 KV 缓存，全局 KV 缓存体积降低 37.5%。  
- **量化感知训练**：支持移动端混合量化 (int2/int4) 和 Q4_0，前端冻结时块级缩放保证 fp16 数值稳定。  
- **多 Token 预测草稿头**：4 层 Transformer 交叉关注主模型 KV 缓存，增量生成草稿 token；对 E2B/E4B 用 top‑k 聚类减少词汇表投影的开销到 d×4096。  
- **编码器自由架构 (仅 12B)**：移除视觉 (550M) 和音频 (305M) 编码器，用单层 matmul (35M) 投影 48×48 图像块，音频分 40ms 块直接投影，配合 2D 位置嵌入保留空间信息。  
- **预训练与后训练**：数据截至于 2025‑01，26 万 SentencePiece 词表，蒸馏与指令微调加入思考模式控制、函数调用格式。  
**关键结果**  
- Arena 人类评估：Gemma 4 31B Elo 1451，在密集开源模型中最优，26B‑A4B 1438，与 17‑49B 激活的 MoE 大模型相当。  
- 静态基准：31B 在 AIME 2026 无工具 89.2、LiveCodeBench 80.0、GPQA Diamond 84.3；E2B 在多个任务上接近 Gemma 3 27B，但参数量仅 1/10。  
- 视觉：高分通过 InfographicVQA 92.0、MATH‑Vision 85.6；音频：FLEURS ASR 误词率 0.075 (E4B)、12B 无专用编码器仍达 0.063。  
- 长文本：RULER 32k 准确率 95.2‑97.3，128k 仍保持 86.6‑96.4；LOFT 128k 召回 66.4、MTOB 整书翻译质量大幅领先 Gemma 3。  
“一句话”：Gemma 4 通过对注意力机制、内存管理、量化和模态融合的系统性重设计，让中小模型在复杂推理与多模态任务上能够以小博大，实质降低了先进 AI 的部署门槛。
