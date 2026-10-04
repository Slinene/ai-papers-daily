---
title: 'Every Ablation Is a Dose: Counterweights and the Semblance of Self-Repair'
title_zh: 消融即剂量：抵消权重与自修复的假象
authors:
- Areeb Ahmad
- Pratinav Seth
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2610.02173'
url: https://arxiv.org/abs/2610.02173
pdf_url: https://arxiv.org/pdf/2610.02173
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: 模型可解释性 · 自修复机制
tags:
- self-repair
- mechanistic interpretability
- ablation
- counterfactual
- affine law
one_liner: 提出自修复源于消融前已有的反事实增益，组件响应服从仿射定律并可由固定权重预测
practical_value: '- 在 LLM 推荐 / Agent 的模块消融中，不要只看“删掉某个 LoRA / 记忆模块后指标变化很小”就认为该模块不重要；自修复会掩盖因果贡献。可把干预强度连续化（如缩放隐藏状态
  λ），拟合 E_r(λ)=own_r+γ_rλ，用斜率而非二进制消融判断真实作用。

  - 若你的业务要对 LLM 中的风险 / 偏见子模块做 unlearning 或 circuit 剪枝，先测量下游单元的 γ_r 符号与幅度；固定权重可预估哪些单元会抵消删除信号，避免越高删、下游补偿越大。

  - 对于 Agent 多模块 pipeline，当移除某工具 / 检索模块后整体效果“没掉”，要区分是模块没用还是其他模块在补偿；建议用多档剂量干预（0, 0.25,
  0.5, 1, 2 等）替代单点消融，找出剂量 - 响应曲线，定位真实瓶颈。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：语言模型消融后，下游组件常表现出调整与补偿，即“自修复”。此前系统性研究认为该现象噪声大、未必有单一机制。本文主张它有一个统一解释：修复增益在消融前已经存在。

**方法关键点**：把任意对因果重要组件的干预看作反事实对比强度 λ 轴上的点；传统消融只是该轴上未校准的点。细粒度单元 r 的因果修复响应服从仿射定律 E_r(λ)=own_r+γ_rλ，其中斜率 γ_r 是固定系数，符号决定该单元是抵消还是强化被移除信号。可通过固定权重预估 γ_r 大小。

**关键结果**：在 factual-verdict 任务上，覆盖 Gemma、Qwen、LLaMA、Mistral 四个不同家族模型，识别出 MLP 神经元、OV 神经元、奇异方向等组件，81 个下游方向中 68 个遵循仿射定律。在 GPT-2 Small 的 IOI 电路中，干预可到达的 10 个 head 中 7 个遵循该定律，且全部为 counterweight。因此，看似自修复的现象，实际是 counterweight 在对比信号到达核心时执行其常规操作。
