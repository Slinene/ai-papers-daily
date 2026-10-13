---
title: 'Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction'
title_zh: 学习在何处注入新用户轮次以重定向 LLM 推理自纠正
authors:
- Jiwon Jeon
- Myungsik Cho
- Jeonghye Kim
- Youngchul Sung
affiliations:
- KAIST
arxiv_id: '2610.13672'
url: https://arxiv.org/abs/2610.13672
pdf_url: https://arxiv.org/pdf/2610.13672
published: '2026-10-09'
collected: '2026-10-13'
category: Reasoning
direction: LLM 推理自纠正 · 干预位置学习
tags:
- Self-Correction
- LLM Reasoning
- Intervention
- MLP Head
- No Fine-Tuning
one_liner: UPTURN 用 130K 参数头学习失败推理的干预位置，以新用户轮次注入纠正指令，无需微调即提升数学推理准确率
practical_value: '- 在对话式推荐/搜索 Agent 的 multi-step 推理或工具调用失败时，可训练轻量 MLP 头（冻结 encoder）从若干候选
  step 中选一个「重试起点」，只保留前缀、重新生成后缀，避免整轮重跑；该头只以最终任务成功（如是否下单/点击）做弱监督，不需要过程标注。

  - 干预时把纠错指令作为新的 user turn 注入，而不是拼在原生成文本里 inline 注入；在固定生成预算下，角色转换更容易改变模型后续生成分布，这对包含
  system/assistant/user 轮次的搜索推荐多轮对话尤其适用。

  - 该框架与现有 RL（如 GRPO）和 self-correction 正交，可在强化学习后的 policy 上叠加，作为推理时纠错模块，适合业务中不重训大模型、只加小模型控制干预时机的低风险上线方式。

  - 但注意其训练信号只有 final-answer correctness，对没有明确二元成功信号的推荐场景（如点击/转化稀疏）需要重新设计 reward，迁移价值主要在「何时重试」的选择器+「新
  user turn」重定向技巧。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 自回归推理中单步错误会传播，内部自纠正不可靠甚至降低表现；现有训练方法需要微调 LLM 生成修订或反馈，成本较高。

**方法关键点**：UPTURN 将纠正拆成「在哪干预」和「如何重定向」。训练一个 130K 参数的 MLP head 放在冻结 encoder 上，仅用最终答案正确性作为弱监督，从失败 rollout 中学习选择保留前缀的位置。重定向环节发现：在固定生成预算下，将同一指令 inline 注入原解码序列会被模型「吸收」而难以改变推理轨迹；改为作为新的 user turn 注入则能有效改变模型后续生成。因此 UPTURN 不微调 LLM，只保留选中的前缀、注入一个指令作为新 user turn，再重新生成后缀。

**结果**：在 4 个 reasoners 和 6 个数学基准上，平均准确率相对 32-rollout baseline 全部提升，提升幅度从 +9.4 到 +24.5 个百分点；在匹配纠正预算下优于 self-correction 和 reflection-token injection 基线，能跨 reasoner 迁移到 GPQA-Diamond 而无需重训，并与 GRPO 和 self-correction 方法互补。
