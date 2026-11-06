---
title: Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO
title_zh: 拆解强到弱 OPD 相对 GRPO 的算力效率
authors:
- Zeyu Leo Liu
- Yang Li
- Bo Pang
- Emre Can Acikgoz
- Xuan-Phi Nguyen
- Anurag Koul
- Srijan Bansal
- Erik Nijkamp
- Shafiq Joty
- Semih Yavuz
affiliations:
- Salesforce AI Research
- UIUC
arxiv_id: '2611.08453'
url: https://arxiv.org/abs/2611.08453
pdf_url: https://arxiv.org/pdf/2611.08453
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LLM 后训练算力效率 · OPD/GRPO
tags:
- OPD
- GRPO
- distillation
- compute efficiency
- multi-teacher
- reasoning
one_liner: 系统对比 OPD 与 GRPO 的训练 FLOPs，证明仅自我 GRPO 教师可让 OPD 高效，多教师合并省 42% 算力
practical_value: '- 评估蒸馏/RL 训练效率时用 FLOPs 而非 GPU-hours 或 step 数，避免实现差异掩盖目标本身；在搜索推荐
  Agent 的 post-training 对比中可复用。

  - 多领域/多任务模型合并：不要联合 GRPO 训练所有任务，先按域独立训练 GRPO 专家，再用多教师 OPD 合并；蒸馏开销仅 5%-8%，总 FLOPs
  比 joint GRPO 省 42%（2 域）。适用于多场景推荐/多业务线模型融合。

  - 教师选择看 provenance：外部强 teacher 不一定好，可能引发长度膨胀和不稳定；用学生自身 GRPO checkpoint 作为 teacher（同源教师）更稳、更省，能恢复教师性能并可超越。业务上优先考虑从当前线上模型
  RL 微调得到教师，而非外部大模型。

  - 注意 OPD 的 response length inflation 和多样性坍缩风险，在生成式推荐/对话式 Agent 中需监控最大长度和重复行为。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：On-policy distillation (OPD) 通过冻结教师对每个 token 的密集监督训练学生，理论上比 outcome-reward GRPO 样本效率更高，尤其当学生难以找到正确答案时。但监督需要教师前向计算，更长响应进一步抬高成本。已有研究多用 GPU-hours 或 step 数报告优势，缺少匹配 FLOPs 的严格对比。

**方法关键点**：
- 统一按累计训练 FLOPs 跟踪 held-out 性能；GRPO 每 token 成本 10Ns，OPD 为 10Ns + 2Nt。
- OPD 目标为反向 KL top-k (k=16) 估计，基于学生自身 rollout；教师分为 external thinking、further-GRPO 思考模型、GRPO-trained base 模型，以及学生自身的 GRPO checkpoint（self-GRPO teacher）。
- 数据集覆盖数学（DAPO-Math-17K、DeepMath-103k）、代码（LiveCodeBench v1-v5、CodeForces）、知识（MMLU-Pro）和指令遵循（IFBench）；学生为 Qwen3-{1.7B,4B,8B} 和 Olmo-3-7B。
- 多教师 OPD 将每个域路由到对应的 self-GRPO 专家教师计算反向 KL。

**关键实验与结果**：
- 外部教师 OPD 在九轴消融和难度分层实验中均输给 GRPO，即使在最有利于 OPD 的学生零解、教师高解子集上也如此；且外部教师 OPD 出现严重的 response-length 膨胀和多样性问题。
- 使用学生自身 GRPO checkpoint 做教师时，OPD 在数学上以 50× fewer FLOPs 恢复教师精度（G=1），跨模型规模、代码域和模型家族复现；Olmo-3-7B 上学生甚至超越教师 11 个百分点（51% vs 40%）。
- 多域多教师 OPD：2 域蒸馏额外仅 5.2% FLOPs、4 域 8.0%；2 域总 FLOPs 比 joint GRPO 少 42.0%，并达到各专家性能；外部 8B 教师 OPD 在 4 域崩塌。

**最值得记住的一句话**：OPD 不是 GRPO 的直接替代，但它适合把多个同源 GRPO 训练出的专家合并成一个通用学生模型。
