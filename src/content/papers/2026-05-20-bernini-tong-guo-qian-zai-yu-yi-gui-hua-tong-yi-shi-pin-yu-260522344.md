---
title: 'Bernini: Latent Semantic Planning for Video Diffusion'
title_zh: Bernini：通过潜在语义规划统一视频生成与编辑
authors:
- Bernini Team
- Chenchen Liu
- Junyi Chen
- Lei Li
- Lu Chi
- Mingzhen Sun
- Zhuoying Li
- Yi Fu
- Ruoyu Guo
- Yiheng Wu
affiliations:
- Bytedance
arxiv_id: '2605.22344'
url: https://arxiv.org/abs/2605.22344
pdf_url: https://arxiv.org/pdf/2605.22344
published: '2026-05-20'
collected: '2026-05-24'
category: Multimodal
direction: 视频生成 · 语义规划
tags:
- Video Generation
- Diffusion Models
- Multimodal LLM
- Semantic Planning
- SA-3D RoPE
- Editing
one_liner: 将 MLLM 语义规划与 DiT 像素渲染解耦，模块化组合实现高效视频生成与编辑
practical_value: '- 模块化生成框架：将视频生成拆分为语义规划（MLLM）与像素渲染（DiT）两个独立模块，可在电商商品视频生成中复用预训练 MLLM
  的视觉理解能力，降低渲染器迭代成本。

  - 语义级接口设计：使用 ViT embedding 作为中间表示，让规划与渲染仅需轻量联合训练，适合业务中快速适配新的编辑需求，如虚拟试穿、商品展示变换。

  - SA-3D RoPE 位置编码：处理多帧、多视角输入时，段感知的 3D 旋转位置编码可迁移至多模态推荐中的视频理解编码器，提升长序列时空表征。

  - 推理链引入生成：在规划器中加入 chain-of-thought ，能将复杂编辑指令分解为中间步骤再生成语义计划，可借鉴到 Agent 的视觉生成任务，提高指令遵循性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态大语言模型（MLLM）善于跨模态语义推理，扩散模型能生成逼真视频，但两者结合通常繁琐。论文提出以“语义”为接口，让 MLLM 做高层规划、扩散模型做像素渲染，从而保留各自预训练优势且训练高效。

**方法**：Bernini 框架包含两个核心模块：
- **MLLM Planner**：接收文本/图像/视频输入，通过 chain-of-thought 推理后，直接预测目标视频的语义表示（ViT embedding 空间）。
- **DiT Renderer**：以语义计划、文本特征和源 VAE 特征为条件，生成目标视频。编辑时还引入源 VAE 细节以保持背景一致。
模块独立预训练，仅需少量联合微调。为处理多视觉输入，设计了 Segment-Aware 3D Rotary Positional Embedding (SA-3D RoPE)，对每段（如源视频、参考图）施加独立 3D 位置编码，再按段位置注入顺序信息。

**结果**：在多项视频生成与编辑基准上取得 SOTA，Bradley-Terry 对战评分 1044，胜率 56.3%，仅低于 HappyHorse-1.0，但高于 Wan2.7 等模型。在包含复杂编辑指令的测试中表现出强泛化性，表明 MLLM 的预训练理解有效转化为了生成能力。
