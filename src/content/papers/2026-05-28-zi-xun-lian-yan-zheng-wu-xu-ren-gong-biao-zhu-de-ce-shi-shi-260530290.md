---
title: Self-Trained Verification for Training- and Test-Time Self-Improvement
title_zh: 自训练验证：无需人工标注的测试时与训练时自我改进
authors:
- Chen Henry Wu
- Aditi Raghunathan
affiliations:
- Carnegie Mellon University
arxiv_id: '2605.30290'
url: https://arxiv.org/abs/2605.30290
pdf_url: https://arxiv.org/pdf/2605.30290
published: '2026-05-28'
collected: '2026-05-29'
category: Reasoning
direction: 推理模型自我改进 · 验证器训练与蒸馏
tags:
- self-verification
- on-policy distillation
- verifier-in-the-loop training
- test-time compute scaling
- LLM reasoning
one_liner: 利用参考答案蒸馏验证器，同时提升推理模型在测试时迭代精炼和训练后独立表现
practical_value: '- **验证器训练范式**：当直接评价生成结果困难时，可引入参考答案作为特权信息，用 on-policy 蒸馏训练一个无条件验证器，避免人工标注反馈质量。电商搜索中，可类似地利用点击/成交数据作为“参考答案”训练查询质量判别器。

  - **弱到强验证**：实验证明 1.7B 的 STV 验证器配合 8B 生成器可匹敌 8B 自验证，适合资源受限场景。在多智能体系统中，可用小模型作为仲裁者或反馈提供者，节省推理成本。

  - **生成器反馈训练 (ViL)**：在验证器反馈下继续 RL 训练生成器，不仅能提升多轮对话效果，还能让模型首轮回答质量大幅提升（+30%）。可迁移到对话式推荐或
  agent 工具调用，用自我反馈数据突破 RL 平台期。

  - **防止奖励黑客**：STV 缓解了验证器分数虚高但准确率停滞的问题，通过精确率-覆盖率曲线诊断验证器校准。对推荐系统中的 RL 排序或生成模型，可借鉴该思路监控并校准
  critic 或 reward model。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：推理模型的测试时自我修正（如 verifier-refinement loop）和训练时自我提升（如自训练）都受限于验证器质量：未训练的验证器常给出模糊反馈或错误接受错误解。训练验证器需要精细的反馈信号，但直接让模型定位自身错误十分困难。本文发现一个不对称性——模型无法独立发现错误，但若获得参考答案，就能通过对比找出错误。由此提出自训练验证（STV），利用这个有监督信号训练无条件验证器。

**方法关键点**：
- 构建“教师”验证器：输入问题、生成解和参考答案，输出判决+自然语言反馈。
- 用 on-policy 蒸馏（JS 散度）训练学生验证器模仿教师分布，避免 SFT 的分布偏移。
- 额外加入判决准确率 RL 奖励。
- 进一步提出 verifier-in-the-loop 训练（ViL）：用训练好的 STV 验证器在多轮 refinement 中对生成器进行 RL 训练，生成器学习利用反馈改进。

**关键结果**：
- 在 DAPO 数学题（含 pass@1=0 的最难子集）上，STV 验证器将最终轮 pass@1 提升约 2×，远超仅做判决 RL 或 meta-verifier RL 的基线。
- 在 SciKnowEval 科学推理任务上，pass@1 从 1.5% 升至 21.0%（14 倍），超过 30 倍大的模型。
- ViL 训练后，生成器首轮 pass@1 提升 30% 相对值，即使移除验证器也保留增益，突破普通 RLVR 平台期。
- 验证不上限多样性：pass@k 在最初 10 轮整体上升，精炼优于重采样。

**核心洞察**：更好的验证器不仅让测试时精炼更可靠，还能作为反馈源训练出更强的生成器，形成迭代自我改进闭环。
