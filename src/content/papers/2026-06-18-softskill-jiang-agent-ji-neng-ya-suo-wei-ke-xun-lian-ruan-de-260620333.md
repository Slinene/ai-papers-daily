---
title: 'SoftSkill: Behavioral Compression for Contextual Adaptation'
title_zh: SoftSkill：将 Agent 技能压缩为可训练软前缀的行为适应方法
authors:
- Xijia Tao
- Yihua Teng
- Xinyu Fu
- Ziru Liu
- Kecheng Chen
- Yuzhi Zhao
- Suiyun Zhang
- Rui Liu
- Lingpeng Kong
affiliations:
- The University of Hong Kong
- Huawei Research
- City University of Hong Kong
- Huazhong University of Science and Technology
arxiv_id: '2606.20333'
url: https://arxiv.org/abs/2606.20333
pdf_url: https://arxiv.org/pdf/2606.20333
published: '2026-06-18'
collected: '2026-06-19'
category: LLM
direction: LLM 推理行为压缩与自适应
tags:
- Soft prompt tuning
- Prompt compression
- Agent skill
- Behavioral compression
- Qwen
- Prefix tuning
one_liner: 用可训练软前缀压缩长 Markdown 技能，以 32 个虚拟 Token 替代数百上千 Token，提升 QA 和数学任务准确率。
practical_value: '- 推荐/搜索场景中常需长文本策略指令（如多路召回规则、排序准则），可借鉴 SoftSkill 将其压缩为可训练 soft prefix，大幅降低推理时的上下文长度和
  KV cache 开销。

  - Agent 执行复杂任务时，若技能描述过长，可预先训练任务专属的 latent prefix 来注入行为先验，提升 Agent 遵循流程的稳定性和效率。

  - 工程上采用冻结基座模型、仅训练少量虚拟 Token 的方法，避免全参数微调，部署时只需替换短 prefix，实现低成本多技能热切换。

  - 实验中长度仅 32 的 soft prefix 即大幅超越长 Markdown 提示，说明压缩技能表示本身具有强正则化效果，可迁移用于压缩推荐解释、搜索引导等长文本上下文。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：当前 Agent 技能常以自然语言 Markdown 文件存储，推理时需模型重新解读长文本才能转化为行为，效率低且易受上下文长度限制。本文探索能否将技能初始化为一小段连续向量（soft skill），通过冻结基座模型训练一个可微调的 soft delta，从而用极短虚拟 Token 编码行为先验。

**方法**：提出 SoftSkill，基于冻结的 LLM 在目标技能相关语料上做下一 token 预测，微调少量可学习的前缀嵌入（长度 32）。这些 soft prefix 作为隐式行为先验在推理时前置，完全替代冗长的 Markdown 指令。实验覆盖单轮问答和 Agent 多步执行两种设定。

**关键结果**：在 Qwen3.5-4B 上，32 长度的 SoftSkill 相比无技能提示，在 SearchQA、LiveMath、DocVQA 上分别提升 8.3、42.1 和 1.3 个准确率点；相比使用完整 Markdown 技能的 SkillOpt 方法，在 SearchQA 和 LiveMath 上分别再提升 5.2 和 12.5 个点，同时将上千 Token 压缩至 32 个虚拟 Token。Agent 场景中，稀疏轨迹模仿能提供有用信号，但对长程行为压缩仍不鲁棒。
