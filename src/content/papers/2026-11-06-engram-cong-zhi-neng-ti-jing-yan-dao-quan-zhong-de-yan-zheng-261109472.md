---
title: 'ENGRAM: From Agent Experience to Weights through Verified Consolidation'
title_zh: ENGRAM：从智能体经验到权重的验证式巩固
authors:
- Ruiyi Yang
- Zechen Li
- Lihuan Li
- Du Yin
- Hao Xue
- Flora D. Salim
affiliations:
- University of New South Wales
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2611.09472'
url: https://arxiv.org/abs/2611.09472
pdf_url: https://arxiv.org/pdf/2611.09472
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: LLM Agent 经验巩固与记忆释放
tags:
- Agent
- Memory Management
- Consolidation
- LoRA
- Skill Verification
- Retrieval
one_liner: 分离训练准入与记忆释放，用演示感知门控与验证门控将智能体经验选择性巩固为 LoRA 权重
practical_value: '- **技能级记忆路由 + LoRA 按需激活**：在电商导购/客服 Agent 中，可以按子技能（如商品参数理解、比价、售后政策）维护独立
  adapter。已验证的技能走纯权重推理，未验证技能继续走 RAG 检索，避免一刀切切换带来的性能抖动，同时降低平均输入 token 和调用次数。

  - **演示感知训练准入**：不必等模型对某任务达到 mastery 才学习，只要有足够的专家/教师成功轨迹即可纳入训练。这适合冷启动场景：用少量人工标注对话或高质量客服会话，直接对低
  mastery 技能做 LoRA 微调，快速补齐长尾能力。

  - **验证式记忆释放**：在决定删除/归档向量库或检索库中的历史经验前，先在 reserved probes 上对比“无检索的微调模型”和“带检索的基座模型”，同时满足相对提升和绝对性能下限才释放。这可以防止
  RAG 系统过早下线检索库导致知识遗忘，尤其适用于高频迭代的推荐/搜索 Agent。

  - **将经验组织成有类型的技能图**：用 ETG 记录技能、任务、经验、来源及依赖关系，训练和释放策略围绕技能粒度展开。可迁移到搜索推荐系统中，把用户反馈轨迹按意图、商品类目或
  query 类型组织，实现更细粒度的记忆管理和更新。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM Agent 通常同时使用外部检索和参数更新来利用历史经验。检索保留轨迹，但成本高；参数学习可摆脱检索，但如何判断模型已从经验中学会、何时可以安全删除外部记录并不清晰。仅基于学生 mastery 的准入会漏掉教师演示，训练后立即删除记忆又可能造成知识浪费。

**方法关键点**
- 将经验组织为 Engram Trace Graph (ETG)，按技能、结果、来源关联记录；每个技能有独立的训练准入和记忆释放决策。
- **演示感知准入**：技能被纳入训练需满足学生 mastery 达到阈值且有足够记录，或成功教师演示记录数达到 d_min。后者允许在 mastery 很低时利用高质量演示进行学习。
- **LoRA 训练**：在 ETG 上下文下，用有效动作轨迹对有监督目标训练低秩 adapter，训练格式与部署一致，不假设检索可以被移除。
- **验证门控释放**：保留部分 probes，比较候选模型无 episodic retrieval 与基座模型带检索的得分。释放需同时满足有效训练参与、探针数>0、相对得分差 ≥ δ、绝对得分 > α。只有通过验证的技能才释放外部记录；未通过的技能继续走检索，可单独启用 adapter+memory 配置。

**关键结果**
- 在 ALFWorld 上 ENGRAM 成功率 90.3%，超过 MAGE 87.3%、SkillRL 89.9%；WebShop 83.4% 接近 EDGE 82.6%；HotpotQA EM 54.6/F1 71.5，比 EmbQA 的 42.0/55.8 显著提升。
- 消融显示：演示感知准入、激活门控、推理期 ETG 均有贡献；冻结权重的 ETG 控制组分数明显更低。
- 600 条 HotpotQA 经验记录的技能级验证释放，可检索足迹减少 55.2%，保留 269 条；verified release 的 F1 为 70.9，接近 retain-all 的 71.1，显著优于 immediate release (66.8) 和 budget-matched random release (67.6)。
- 服务成本上，在 ALFWorld 中 ENGRAM 比 Base+ETG 减少 42.8% 输入 token 和 13.6% 模型调用；在 WebQuestions 上延迟降低 24.6%。

**最值得记住的一句话**：训练准入和记忆释放必须解耦，并且只有通过验证证明权重已经真正取代检索，才允许删除外部记忆。
