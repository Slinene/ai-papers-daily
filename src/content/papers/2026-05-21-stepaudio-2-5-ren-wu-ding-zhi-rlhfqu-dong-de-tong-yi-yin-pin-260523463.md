---
title: StepAudio 2.5 Technical Report
title_zh: StepAudio 2.5：任务定制RLHF驱动的统一音频语言基础模型
authors:
- Bin Lin
- Bo Zhao
- Boyong Wu
- Chao Yan
- Chen Wu
- Cheng Yi
- Chengyuan Yao
- Daijiao Liu
- Fei Tian
- Feng Tian
affiliations:
- StepFun
arxiv_id: '2605.23463'
url: https://arxiv.org/abs/2605.23463
pdf_url: https://arxiv.org/pdf/2605.23463
published: '2026-05-21'
collected: '2026-05-25'
category: Multimodal
direction: 音频语言统一建模 · 任务定制RLHF
tags:
- unified audio-language model
- RLHF
- ASR
- TTS
- real-time interaction
- post-training
one_liner: 用任务定制RLHF和专用解码，使单一音频模型在ASR、TTS和实时交互上达到专用系统水平
practical_value: '- **任务定制RLHF范式可迁移**：不同业务（搜索/推荐/对话）可共享一个多模态基座，通过定义场景专属的reward函数实现差异化对齐，避免维护多套模型。

  - **可验证多token解码提效**：ASR采用的verifiable multi-token decoding，在生成式推荐（如Semantic ID逐token生成）中可设计验证器并行检验并及时剪枝，加速推理。

  - **实时交互的生成式奖励建模**：电商客服Agent可借鉴其生成式RM，在RLHF中同时优化延迟、人物一致性与回答质量，低成本实现端到端对话调优。

  - **任务差异归结为数据与优化目标**：该方法强调多模态对齐后，任务只需差异化的数据和优化目标，启发电商场景下文本-商品embedding对齐后，用指令微调/RL解决搜索、描述生成等多任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有统一音频语言模型在自动语音识别（ASR）、文本到语音（TTS）和实时口语交互上仍难以匹敌专用系统，需探索使单一基座内化不同任务目标的路径。  
**方法**：核心思路是，一旦文本与音频共享多模态表示空间，任务差异便可归结为数据构造、优化目标和解码约束的不同。StepAudio 2.5 将后训练范式从标准监督学习升级为**任务定制的RLHF**，作为定义复杂优化目标的主要机制，并辅以专用解码策略。具体地：ASR分支通过**可验证多token解码**提高转录效率，解码时并行验证多个token并早期截断；TTS分支采用**基于偏好的RLHF**和上下文丰富的监督，实现可控、富有表现力的合成；实时分支利用**生成式奖励建模**在RLHF框架下优化低延迟和人物一致性对话。  
**结果**：在标准基准上，StepAudio 2.5 在ASR、TTS和实时交互三个方向上均达到或超越专用系统的最优性能，证明单一音频语言基础能成功内化语音理解、生成和实时交互的差异化部署目标。
