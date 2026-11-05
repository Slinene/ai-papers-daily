---
title: 'Think Less, Locally: Local Preference Learning for Reasoning Compression'
title_zh: 局部偏好学习实现推理压缩：少想一点，局部决策
authors:
- Muyao Yuan
- Liyan Xu
- Weizhan Zhang
- Muyan Jiao
- Jiangnan Li
- Jinchao Zhang
- Jie Zhou
affiliations:
- Xi'an Jiaotong University
- WeChat AI, Tencent Inc.
arxiv_id: '2611.04814'
url: https://arxiv.org/abs/2611.04814
pdf_url: https://arxiv.org/pdf/2611.04814
published: '2026-11-02'
collected: '2026-11-05'
category: Reasoning
direction: LLM 推理压缩 · 局部偏好学习
tags:
- Reasoning Compression
- DPO
- Chain-of-Thought
- Overthinking
- LLM Training
- Inference Efficiency
one_liner: LoCo 从模型自身轨迹检测过度思考状态，冻结前缀并重生成更短验证延续，用状态条件偏好对做 DPO，实现推理压缩
practical_value: '- 对电商/广告中的 LLM Agent、多步 RAG、推荐解释生成等场景，不必全局鼓励更短输出，而是识别「当前状态已足够回答」的局部停止点：从线上长轨迹中找过度思考段，冻结前缀、重生成更短且结果正确的延续，构造状态条件偏好对，训练模型在不损失准确率前提下提前收束，直接降延迟和
  token 成本。

  - 工程上可复用其自举数据构建方式：无需人工标注，用模型自身推理轨迹 + 最终答案校验正确性，配对「长 vs 短」同一中间状态续写，适合电商客服/导购中的多轮推理与意图澄清，降低训练数据成本。

  - 这种状态条件 DPO 比简单 SFT 更稳定，可作为已有 LLM 线上服务做推理长度压缩的轻量后训练方案；数学/代码领域训练可迁移到业务文本，适合先在小领域造数据再迁移到搜索
  query 规划、商品推荐解释等任务。

  - 若生成式推荐/候选生成链路包含「生成候选→校验→排序」等长 CoT，可把验证步骤视为可压缩过程，用局部偏好学习决定跳过哪些验证，平衡推荐质量与推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：大推理模型在数学、代码等任务上靠长 CoT 提高表现，但会持续思考到信息充分之后，带来解码延迟和推理成本。现有推理压缩多针对整条轨迹，忽略局部「当前状态是否还需要继续推理」的决策。

方法关键点：LoCo 先从模型自身生成轨迹中检测候选过度思考状态；对同一前缀冻结，从该状态重新生成更短且答案正确的延续，形成状态条件偏好对；再用 DPO 训练，让模型学会何时继续推理、何时停止，而不是简单全局缩短。训练数据完全来自自生成数学轨迹，无需人工标注。

关键结果：在 5 个数学和 3 个代码生成 benchmark 上，LoCo 将数学完成长度降低 41.7%–45.4%，代码降低 23.4%–36.3%，同时保持或提升准确率；代码所有 benchmark 的 AUC 最优。仅在数学数据训练即可迁移到代码生成，说明局部偏好学习跨域泛化能力强。
