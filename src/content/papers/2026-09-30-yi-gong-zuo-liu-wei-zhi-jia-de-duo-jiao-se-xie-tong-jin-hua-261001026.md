---
title: It Takes Workflows to Evolve Better Workflows
title_zh: 以工作流为支架的多角色协同进化框架 FLOWRIGHT
authors:
- Xuehang Guo
- Haoyu Wang
- Haifeng Chen
- Yangyi Chen
- Zhenhailong Wang
- Qingyun Wang
affiliations:
- William & Mary
- NEC Corporation of America
- University of Illinois Urbana-Champaign
arxiv_id: '2610.01026'
url: https://arxiv.org/abs/2610.01026
pdf_url: https://arxiv.org/pdf/2610.01026
published: '2026-09-30'
collected: '2026-10-02'
category: MultiAgent
direction: 多智能体工作流协同进化与训练
tags:
- Multi-Agent
- Workflow Optimization
- Reinforcement Learning
- Credit Assignment
- LLM
- Data Hardening
one_liner: 提出FLOWRIGHT，将工作流作为统一harness，通过分层结构感知奖励实现多角色自进化与共进化，无需额外模型或标注
practical_value: '- 将推荐/搜索链路建模为工作流，用统一的业务指标作为 harness 同时训练召回、粗排、精排、重排等多角色策略，避免各环节独立优化导致的不一致；工作流生成器和执行器共享同一奖励信号，可实现端到端协同进化。

  - 借鉴结构感知信用分配：从执行 trace 中提取每个角色失败的节点比例作为轻量惩罚项，无需额外 reward model 或人工标注，即可在联合训练中定位责任，降低多智能体
  RL 的信用分配成本。

  - 采用数据硬化策略构造工作流级任务：将简单 query 或单步任务组合成需要多源信息聚合、长上下文推理的复杂任务，防止训练信号退化为单一 agent 主导，更有效地激发多
  Agent 协作。

  - 测试时 meta-distillation：将线上成功的工作流模板蒸馏为 few-shot prior，通过上下文学习快速适应新场景，避免在线梯度更新，适合电商大促、突发
  query 等动态环境。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
复杂任务需要多智能体工作流协作，但现有方法通常只训练工作流生成器，其他执行或构建 agent 保持固定；同时工作流结果只有一个稀疏分数，难以定位失败责任；此外常用基准过简单，单 agent 即可解决，无法体现工作流增益。这些问题限制了工作流整体优化空间。

**方法关键点**  
- **工作流作为 harness**：上游生成工作流图，下游执行并评分，该评分同时用作评估指标、训练信号和测试时目标，所有角色共享这一统一信号。
- **结构感知信用定位**：从执行 trace 中识别每个角色负责的失败节点，按失败节点占该角色总节点的比例给予惩罚，无需额外模型、标签或执行。
- **分层奖励**：奖励由格式、有效性、执行、答案正确性和结构信用五项加权组成，将稀疏结果转化为密集反馈，其中有效性贡献最大。
- **四种进化模式**：单角色自进化、agent-skill 协同进化、上下游协同进化、多智能体协同进化；多角色共进化形成互惠课程，每个角色的行为塑造其他角色的训练分布。
- **DATAWRIGHT 数据硬化**：通过组合子任务、增加难度、跨文档捆绑等策略，将单 agent 数据集转化为工作流级任务，提升训练和评估难度。
- **测试时 meta-distillation**：将成功经验蒸馏为 reusable prior 和 few-shot 案例，无需更新权重即可提升新任务性能。

**关键实验**  
在 12 个数据集、7 个领域、44 个评估 arm 上，Qwen3.5-4B/9B 等模型。未训练的 FLOWRIGHT 相比单 agent 基线提升至少 +11.39%；训练后多智能体共进化整体提升 +5.03%，单角色自进化 +2.83%，agent-skill 协同 +4.06%；测试时 5-shot meta-distillation 提升 +2.58%，与训练结合后 +3.21%。消融显示分层奖励中有效性贡献 +2.07~+2.29%，信用项再加 +0.69~+0.75%；动态 pool 按需增长提升 +4.83%。

**最值得记住的一句话**  
共享 harness 与结构感知信用分配让多角色工作流在不增加额外模型或标注的情况下实现协同进化，而数据硬化是释放工作流增益的关键前提。
