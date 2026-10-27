---
title: 'Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for
  Tool-Use Agents'
title_zh: Trajectory2Gym：面向工具使用智能体的决策锚定组合交互合成
authors:
- Yihao Hu
- Zhihao Wen
- Yitong Lin
- Siyuan Lu
- Pan Wang
- Wei Wu
- Jiang-Ming Yang
- Tao Lin
affiliations:
- Westlake University
- Ant International
arxiv_id: '2610.33568'
url: https://arxiv.org/abs/2610.33568
pdf_url: https://arxiv.org/pdf/2610.33568
published: '2026-10-23'
collected: '2026-10-27'
category: Training
direction: 工具使用 Agent 轨迹合成与 SFT
tags:
- Tool-Use Agents
- Trajectory Synthesis
- Decision Grounding
- SFT
- Compositional Coverage
- Multi-turn Interaction
one_liner: 通过构造组合交互并仅监督有可见历史依据的决策，大幅提升多轮工具使用智能体的 SFT 效果
practical_value: '- **决策级监督掩码**：训练工具使用智能体时，不要只按最终成功或 API 执行成功过滤轨迹。对每个 assistant 动作检查：参数是否来自决策时可见的上下文（如工具返回结果、用户确认），工具是否可见，以及是否满足工作流顺序。失败的调用保留为上下文但不参与模仿损失，避免模型学会利用
  collector 私有信息或错误捷径。

  - **定向合成欠支持依赖路径**：先统计现有轨迹池中组合结构的支持度（如“查询→错误→澄清→重试→确认→取消→更新”），再针对低于支持阈值的路径生成任务和初始状态。不要随机采样候选，否则稀有结构被漏掉的概率很高；可按模型尺度设定每个
  canonical path 的目标深度，小模型少重复，大模型多重复。

  - **父级归一化 SFT**：一条多轮交互可能被渲染成多行训练样例，若按行平均会让长交互主导损失。以语义交互为单位赋予相等权重，再在内部按目标 token 数分配，可防止长轨迹过拟合，提升多轮和状态依赖任务的稳定性（消融中单独贡献
  8.04 点）。

  - **成功只做 gate，不做 license**：在电商客服、订单处理等 Agent 场景，即使 API 执行成功，也可能包含错误目标或违反用户最新意图（如替换了已取消的商品）。将“成功”作为进入训练池的门槛，但不作为每个动作的监督许可；结合工作流顺序和用户确认来判定目标动作。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
工具使用智能体的训练通常以成功轨迹作为监督，但成功只证明 episode 结局正确，不保证每个被模仿的动作都有决策时可见信息支持。实际轨迹池中，40.9% 的候选最多只有两个监督决策，10.0% 在真实错误后有认证决策，导致多步依赖和恢复能力被严重欠采样。同时还存在执行成功但参数来自 collector 私有信息、或动作与用户最新确认冲突的情况。核心矛盾是：轨迹的教学价值取决于其实现的依赖关系与可见历史能证明的决策，而非最终结果。

**方法关键点**  
Trajectory2Gym 分三阶段构建训练数据：
1. **组合交互合成**：定义能力路径（如查找、错误、澄清、重试、订单读取、确认、取消、更新），针对支持度不足的路径生成请求与初始状态，由 teacher 在原生环境中执行，保证真实观察、状态变化和拒绝反馈。仅当路径中的动作-观察依赖出现在执行日志中才认证。
2. **决策锚定监督**：对每条日志构造学生可见上下文，仅监督同时满足三个条件的动作：本地执行有效、参数和工具由可见历史支持、满足工作流顺序。失败调用保留为上下文但不作为模仿目标，后续恢复动作才成为监督目标。
3. **结构支持学习**：按模型尺度为每个 canonical path 设定目标支持深度，选择轨迹覆盖能力路径；训练时采用父级归一化 SFT，以语义交互为单位赋权，避免长交互因渲染行数多而主导损失。

**关键实验**  
在 Tau1、Tau2、BFCL 三个基准上，对 Qwen3 五个尺度（1.7B 到 30B-A3B）做配对比较。三基准均值提升 16.9–29.8 个百分点，其中 Tau1+Tau2 均值提升 20–41 点，BFCL Overall 提升 3.35–11.93 点。增益集中在多轮和状态依赖任务：4B 模型在 Tau2 上达到 69.17，超过公开 30B-A3B 初始化的 28.33；8B 模型三基准均值 67.97，超过所有评估的公共 agent 训练 checkpoint（最高 57.17）。消融显示四个设计选择均正向，其中父级归一化单独增益最大（8.04 点）。

**最值得记住的一句话**  
成功应该 gate 监督，而不是 license 监督；真实错误属于上下文，不属于目标；结构支持是分配问题，而非数量最大化。
