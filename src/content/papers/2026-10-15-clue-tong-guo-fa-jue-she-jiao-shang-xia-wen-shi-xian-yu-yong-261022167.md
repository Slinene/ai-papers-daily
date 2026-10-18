---
title: 'CLUE: Uncovering Social Context for Pragmatic Understanding'
title_zh: CLUE：通过发掘社交上下文实现语用理解
authors:
- Chengfei Wu
- Zhaoqing Wu
- Dan Goldwasser
affiliations:
- Purdue University
arxiv_id: '2610.22167'
url: https://arxiv.org/abs/2610.22167
pdf_url: https://arxiv.org/pdf/2610.22167
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 训练模型发现对话社会线索用于语用理解
tags:
- GRPO
- reasoning
- pragmatics
- social context
- evidence grounding
- RL
one_liner: 用两阶段训练+GRPO奖励让模型自我发掘对话中的社会线索，准确率提升且推理 token 减少超 80%
practical_value: '- 可借鉴 Grounded Information Utilization 奖励设计：在对话理解、用户反馈归因等场景，要求模型的新推断必须引用具体交互证据，并惩罚冗余推理，可显著压缩推理
  token，降低线上成本。

  - 两阶段训练方案适合小样本业务任务：先用监督证据推理教会模型引用上下文，再用 GRPO 强化，类似客服对话意图消歧、评论情感归因等标注数据少的场景可以低成本迁移。

  - 推理 self-contained、不依赖外部 RAG 或知识库，适合低延迟 Agent 的对话理解模块，减少检索链路，同时输出可验证的证据引用。

  - 评估中加入推理 token 效率指标，避免只追准确率导致 CoT 过度生成；跨域跨语言 F1 提升 9.3% 的结果说明该训练方式有泛化潜力。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：理解对话常需结合说话人关系、预期与历史互动，但现有方法直接补充外部上下文，而这些信息可能已隐藏在对话中；关键是让模型自己找出支持判断的证据线索。

**方法**：CLUE 采用两阶段训练。第一阶段用监督证据推理，让模型学会引用与判断相关的具体对话内容；第二阶段用 GRPO 优化，奖励函数为 Grounded Information Utilization（IU_G），只奖励有证据支持的新社会推断，同时惩罚冗余推理 effort。推理时模型仅依靠当前交互自包含地给出解释。

**结果**：相比 Qwen 基础模型，CLUE 在域内平均加权 F1 相对提升 17.3%，域外提升 9.3%，5 个域外评测中 4 个 F1 更高；同时平均推理 token 减少超过 80%。人类评估显示，其解释更常锚定具体对话内容，引用的证据与人类选择的上下文更一致。
