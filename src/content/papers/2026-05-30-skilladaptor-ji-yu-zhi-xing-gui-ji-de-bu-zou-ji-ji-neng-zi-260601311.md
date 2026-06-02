---
title: 'SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories'
title_zh: 'SkillAdaptor: 基于执行轨迹的步骤级技能自我适应框架'
authors:
- Zhuoyun Yu
- Xin Xie
- Wuguannan Yao
- Chenxi Wang
- Lei Liang
- Xiang Qi
- Shumin Deng
affiliations:
- Zhejiang University
- Ant Digital Technologies, Ant Group
- Zhejiang University - Ant Group Joint Laboratory of Knowledge Graph
arxiv_id: '2606.01311'
url: https://arxiv.org/abs/2606.01311
pdf_url: https://arxiv.org/pdf/2606.01311
published: '2026-05-30'
collected: '2026-06-02'
category: Agent
direction: Agent技能自我适应 · 步骤级归因
tags:
- Skill Adaptation
- Step-level Attribution
- LLM Agents
- Training-free
- Failure Localization
one_liner: 提出训练免的步骤级失败归因与技能更新方法，在长程交互任务中稳定提升LLM Agent成功率。
practical_value: '- **细粒度故障定位与定向修复**：在业务中的多步 Agent（如客服导购、多工具编排）中，可借鉴 Localizer → Linker
  → Modifier 流水线，将失败归因到具体步骤和使用的技能片段，只修订或生成最小化改动，避免全轨迹更新带来的不稳定和过度泛化，提升迭代效率。

  - **资格验证门控防止技能退化**：Qualifier 模块通过重执行对比，仅当候选技能带来非负增益时才更新技能库，类似主动增量学习中的回测机制，可直接迁移到线上技能的自动化迭代中，防止错误技能污染下游任务。

  - **技能冗余控制与早期停止**：通过语义相似度阈值（θdup=0.95）过滤重复技能，并在技能库连续多变无效时提前停止迭代，减少了技能膨胀和计算开销，适合需要长期维护技能库的电商
  Agent 系统。

  - **OpenClaw 类框架的插件式集成**：方法设计为可插拔的适配器，可在不改变骨干模型和运行环境的前提下嵌入现有 Agent 框架，对已有产线改造代价小，适合在已有智能体底座上快速试验技能自适应能力。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent 在长程交互任务（如工具调用、网页操作）中常依赖外部可复用技能实现持续改善。现有训练免技能适应方法多基于完整轨迹或会话级反馈进行修订，缺乏细粒度失败归因，导致更新不稳定或改动过大，尤其在早期错误会污染后续步骤的长程场景下，信用分配问题严重。

**方法关键点**：提出 SKILLADAPTOR，一个训练免的步骤级技能适应框架，可在 OpenClaw 类 Agent 中即插即用。核心流程分三期：
- **初始化**：从成功轨迹蒸馏初始技能库。
- **执行与注入**：任务时用编码器检索并重排 top-k 相关技能，注入骨干预解决策。
- **失败轨迹适应**：
  - **归因（Attribution）**：Localizer 定位最早可操作的故障步（t*）并生成改进建议；Linker 估计相关技能的责任权重，并决策动作（修订现有技能或生成新技能）。
  - **修改（Modification）**：对最高权重技能进行定向改写，或基于故障上下文合成新技能，并通过语义相似度阈值（0.95）抑制冗余。
  - **资格验证（Qualification）**：在候选技能库与原库上重执行任务，仅当平均反馈指标非负时才提交更新，否则丢弃，有效防止不良技能进入库。
整个过程中骨干模型冻结，仅更新外部技能库，迭代至多 10 轮或连续 3 轮无变化提前停止。

**关键实验**：在 WebShop、PinchBench、Claw-Eval 三个 benchmark 上，以 Kimi-K2.5、GLM-5、GPT-5.2 为骨干，对比 Base、A-Mem、AWM、ExpeL、EvoSkill、OpenSpace 等基线。
- WebShop 上，所有模型成功率（Succ%）提升 1.7~2.3 个百分点，Score 最大提升 +2.3。
- PinchBench 上 Avg Score% 最大提升 +1.5，Claw-Eval 上 Avg Score 最大提升 +1.8。
- 消融表明去除 Localizer/Linker 或 Qualifier 后增益大幅下降，且仅靠初始技能库（无后续归因更新）几乎无增益，验证步骤级归因与资格验证的必要性。
- 适应轮次：75% 的通过资格验证更新集中在前 2 轮，后续轮次收益递减。

**核心结论**：精确的步骤级失败归因与带资格控制的定向技能更新，比技能库规模扩展或全轨迹反思更能稳定提升训练免 Agent 的性能。
