---
title: 'EmbeddingGemma 2: Unified and Efficient Multimodal Representations'
title_zh: EmbeddingGemma 2：统一高效多模态表征模型
authors:
- Henrique Schechter Vera
- Sahil Dua
- Jovan Andonov
- Sara Smoot
- Sebastian Russo
- Ivan Llanos
- Max Matveev
- Jae Hyeon Yoo
- Kat Black
- Shih-Cheng Huang
affiliations:
- Google DeepMind
- Google
arxiv_id: '2610.37364'
url: https://arxiv.org/abs/2610.37364
pdf_url: https://arxiv.org/pdf/2610.37364
published: '2026-10-27'
collected: '2026-10-28'
category: Multimodal
direction: 多模态统一 embedding · 蒸馏与对比学习
tags:
- multimodal embedding
- contrastive learning
- distillation
- Matryoshka
- quantization
- retrieval
one_liner: 744M 多模态 embedding 模型，以多阶段课程训练在文本/视觉/音频基准上达到新 Pareto 前沿，支持量化与截断部署
practical_value: '- 统一商品多模态表示：图/文/视频/音频 natively 编码，适合电商搜索/推荐中的跨模态召回（如图搜商品、视频理解），避免先
  ASR/OCR 再文本 embedding 的管线损失。

  - 训练 recipe：先纯文本预微调（蒸馏）再多模态预微调（蒸馏），最后用对比 + spread-out + MRL 微调；加入 same-tower negatives
  和 Plackett-Luce listwise loss，有利于排序/检索任务。

  - 工程部署：用可调 vision token budget（70-1120）和 MRL 截断维度（768/512/256/128）做资源-质量 trade-off；QAT
  后 int4 量化在手机上 <600MB，可在端侧实时出 embedding。

  - 消融结论：多模态任务上 trainable vision encoder 比 frozen 大幅提升（MMEB-v2 52.27 vs 48.18）；native
  audio 比 ASR 提升 MSEB 69.54 vs 57.59，建议直接编码原始音频而非转写。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
现有文本 embedding 要处理音频/视觉数据，通常需要额外 ASR 或图像描述，既增加计算成本，又丢失细粒度视觉和非语言声音信号。CLIP/SigLIP 等虽能做跨模态对齐，但无法处理 mixed-modal 输入；而由 MLLM 改的 embedding 模型参数量动辄数十亿，不适合高吞吐、延迟敏感或端侧部署。

## 方法关键点
- **架构**：744M 总参数 = 271M 双向 transformer backbone + 167M vision encoder（ViT patch16）+ 305M audio encoder（conformer/USM）。模态编码器输出软 token，与文本 token 交错输入共享 backbone，支持按需只加载 text-only（271M）、vision-language（439M）或 audio-language（577M）。
- **简化 PLE**：去掉 Gemma 原有的专用 per-layer embedding lookup table，只用共享输入 token 的线性投影，既省参数又提升多模态质量。
- **三阶段课程训练**：text pre-finetuning（~300B tokens，蒸馏为主）→ multimodal pre-finetuning（~2T tokens，蒸馏）→ multimodal finetuning（~600B tokens，对比 + spread-out + MRL）。
- **损失函数**：NCE contrastive（in-batch/hard/same-tower negatives）+ Plackett-Luce listwise loss + spread-out regularizer（二阶矩项促进各向同性，利于 ANN 检索和量化）+ EmbedDistill 式 embedding matching。
- **部署友好**：Matryoshka 子维度 768/512/256/128；vision token budget 可调（70-1120）；QAT 后提供 int4 量化，Pixel 11 Pro 上 full multimodal 峰值内存 567MB。

## 关键实验
在 MTEB（多语言/英语/Code）、MMEB-v2、MIEB(lite)、MAEB、MSEB 等 7 个基准上建立新 Pareto 前沿。MTEB(Code) Mean(Task) 78.68（较上代 +9.92）；MMEB-v2 Mean(Task) 59.01，是榜单最小模型，超过部分 8B+ specialist；MIEB(lite) 60.17，比 sub-1B 最优高 +7.9；MAEB 49.87，接近 sub-1B 最优且 128 维超过所有其他 sub-1B 满维模型；MSEB(Retrieval) 69.54，native audio 比 ASR 提升 11.95。

## 最值得记住的一句话
多阶段课程（先文本预微调，再多模态蒸馏，最后对比微调）让 744M 模型在多个模态上达到新 Pareto 前沿，并通过可调视觉 token、MRL 截断和量化实现端侧部署。
