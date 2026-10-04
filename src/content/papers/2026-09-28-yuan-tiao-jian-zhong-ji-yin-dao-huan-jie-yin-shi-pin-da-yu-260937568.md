---
title: 'Devils in Question Relay: Source-Conditioned Relay Steering to Mitigate Hallucinations
  in Audio-visual Large Language Models'
title_zh: 源条件中继引导缓解音视频大语言模型幻觉
authors:
- Yu Zhang
- Pingrui Zhang
- Xuefeng Bai
- Pengfei Zhang
- Yang Xiang
- Kehai Chen
affiliations:
- Harbin Institute of Technology, Shenzhen
- Peng Cheng Laboratory, Shenzhen
- Fudan University
arxiv_id: '2609.37568'
url: https://arxiv.org/abs/2609.37568
pdf_url: https://arxiv.org/pdf/2609.37568
published: '2026-09-28'
collected: '2026-10-04'
category: Multimodal
direction: 多模态LLM幻觉缓解 · 训练免干预
tags:
- AVLLM
- hallucination
- training-free
- steering
- source grounding
- multimodal
one_liner: 提出训练免方法SECRET，通过源条件中继引导抑制跨模态干扰，缓解AVLLM源混淆接地幻觉
practical_value: '- 训练免的表示引导（steering）思路可迁移到电商多模态场景（商品视频理解、直播切片审核、图文一致性校验）：对LLM内部问题表示做方向性修正，无需微调即可抑制无关模态干扰，快速上线。

  - 业务中跨模态冲突常见（如商品主图与描述不一致导致问答错误），可借鉴“源条件对比表示”：利用不同模态路径干预构造对比样本，用其表示差异引导原始状态，提升模型对指定源信息的遵循能力。

  - 路径干预分析定位干扰通路的方法，可用于诊断自有多模态Agent或推荐解释模型中的跨模态信息污染，为模型裁剪和推理优化提供依据。

  - 与RAG/推荐系统结合时，可对检索到的多模态候选做源条件重定向，避免LLM被无关信源带偏，提升生成结果的grounding可靠性。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：音频视觉大语言模型（AVLLM）存在源混淆接地幻觉——未使用模态的线索诱导出所需模态不支持的响应，影响真实场景可靠性。已有缓解方法缺乏对内部跨模态交互机制的理解。

方法关键点：通过路径干预和表示分析，发现一个 question-relay 机制：问题状态同时携带干扰线索与所需源证据，干扰模态到问题状态的连接是幻觉主要来源；切断干扰模态到问题状态的路径比切断到生成位置更能恢复正确 logit。基于此提出训练免方法 SECRET（SourcE-Conditioned RElay sTeering），利用不同模态路径干预产生的对比问题表示，将原始问题状态引导向所需源证据。

关键结果数字：在两个基准 CMM 和 AVHBench、三个 AVLLM 上，SECRET 一致优于先前训练免方法，相对基模型最高提升 +18.0 和 +7.1 个百分点；模态特定字幕生成实验进一步验证其对开放式生成的泛化能力。
