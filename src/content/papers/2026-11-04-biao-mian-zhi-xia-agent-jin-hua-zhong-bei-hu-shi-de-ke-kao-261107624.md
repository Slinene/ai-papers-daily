---
title: 'Beneath the Surface: What We Overlook When We Talk About Agent Evolution'
title_zh: 表面之下：Agent 进化中被忽视的可靠性与迁移性
authors:
- Xiaobo Wang
- Zimu Wang
- Siyu Ye
- Jiaqi Li
- Min Tang
- Jun Bai
- Yuling Shi
- Ruobing Wang
- Jingjing Zhang
- Chaofan Wang
affiliations:
- University of Science and Technology of China
- University of California, Berkeley
- Simple Agent Lab
- Beijing Institute for General Artificial Intelligence
- Shanghai Jiaotong University
arxiv_id: '2611.07624'
url: https://arxiv.org/abs/2611.07624
pdf_url: https://arxiv.org/pdf/2611.07624
published: '2026-11-04'
collected: '2026-11-09'
category: Agent
direction: Agent 自我进化评估与审计
tags:
- Agent Evolution
- Self-Improvement
- Evaluation
- Reliability
- Transferability
one_liner: 系统评估 Agent harness 进化发现高分伴随任务覆盖丢失与成本上升，EvoAudit 将诊断转为修订后最优
practical_value: '- 在推荐/搜索的 LLM Agent 自动调优（如 prompt 改写、策略搜索、多智能体分工）中，不要只看聚合分数；维护任务/slice
  级别的覆盖矩阵，监控旧能力是否退化，把“能力覆盖保持”加入停机与选模标准，避免高分但丢核心任务。

  - 对进化流程做组件干预：固定 select/analyze/mutate/gate 的其余部分，单独对比某个模块改动，同时保留 admission 回放记录，不要把严格
  admission 淘汰的候选直接丢弃，后续组合可能产生增益。

  - 上线前同时评估可靠性与部署成本（latency/token），论文显示多数可靠性提升伴随成本增加；业务中应设置成本约束下的 Pareto 搜索，不盲目选择最高分配置。

  - 跨域迁移时先做分域覆盖回归，通用任务场景 coverage 容易下降；例如从服饰域进化出的推荐 Agent 策略迁移到美妆域前，需重放原目标域任务集，不能只凭源域得分。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent harness evolution 在固定模型权重下通过修改外部系统实现递归自我改进，但常见评估只盯 benchmark 分数，少有人验证高分是否真正可靠、高效、可迁移。

**方法关键点**：评估四种进化方法在多种 harness、通用与编码任务上的表现；通过重复评估、受控 agent 扩展、组件干预与 admission replay，分析任务覆盖变化，EvoAudit 将这些诊断转化为对 select、analyze、mutate、gate 四个组件的修订。

**关键结果数字**：所有 16 个进化 agent 都获得未覆盖任务同时丢失已覆盖任务；一个通用任务案例可靠性上升 5.2 分却丢失 10 个已覆盖任务；多数可靠性提升伴随部署成本增加；specific changes 单独优于 generic reminders，但组合后收益可能反转；最高分 agent 在四个候选池中均未带来最大平均改进；更严格的 admission 会淘汰有用替代方案；迁移时通用目标任务覆盖通常下降，编码目标在仅外层 harness 条件下上升。EvoAudit 取得 best performance。
