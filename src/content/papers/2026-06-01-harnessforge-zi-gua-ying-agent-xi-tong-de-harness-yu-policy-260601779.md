---
title: 'HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems'
title_zh: HarnessForge：自适应 Agent 系统的 Harness 与 Policy 联合进化
authors:
- Mingju Chen
- Can Lv
- Guibin Zhang
- Heng Chang
- Shiji Zhou
affiliations:
- Beihang University
- Tsinghua University
arxiv_id: '2606.01779'
url: https://arxiv.org/abs/2606.01779
pdf_url: https://arxiv.org/pdf/2606.01779
published: '2026-06-01'
collected: '2026-06-09'
category: Agent
direction: Agent 系统 harness–policy 协同进化
tags:
- harness-policy co-evolution
- meta-adaptation
- LLM agents
- tool use
- LoRA
- Pareto selection
one_liner: 通过 harness–policy 对协同进化实现 LLM agent 系统的元适应，解决执行结构与推理策略兼容性问题
practical_value: '1. **业务 Agent 的联合迭代范式**：将电商客服或推荐 Agent 拆解为 Harness（任务分解、工具接口、记忆模块）与
  Policy（推理行为），通过故障诊断改进 Harness，再用成功轨迹训练 Policy，闭环提升系统整体兼容性。

  2. **低成本 Policy 对齐**：复用同一批 rollout 数据同时完成 Harness 筛选和 Policy 训练，避免额外数据采集成本，适用于在线业务快速迭代。

  3. **资源受限下的适配策略**：保持基座模型不变，仅训练轻量 LoRA 适配器，使模型对齐不同 Harness 的执行约定，适合在算力有限时动态切换任务范式。

  4. **多目标 Pareto 筛选机制**：在 Harness 候选评估中同时考虑任务效果、token 消耗和延迟，可迁移到推荐 Agent 的架构搜索，平衡收益与成本。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent 在跨异构任务（工具调用、检索问答、状态交互）时，固定系统难以通用。现有方法或优化外部工作流（Harness），或仅强化内部推理策略（Policy），忽略了两者的兼容性：更强的 Harness 可能超出模型执行能力，更强的 Policy 可能受限于不合适的执行接口。因此需要系统级的元适应，将 Agent 视为 Harness–Policy 耦合对，进行联合进化。

**方法关键点**  
- **Harness–Policy 对建模**：Harness = {Planning, Action, Memory} 定义执行结构，Policy 为适配该 Harness 的轻量 LoRA 适配器。
- **故障引导的 Harness 定制**：通过 rollout 诊断将失败归因到 Planning/Action/Memory，利用历史存档中的帕累托优案例生成改进报告，并产生若干新 Harness 候选，经多目标 Pareto 筛选（效果、token 成本、延迟）选出幸存 Harness。
- **Harness 条件化的 Policy 对齐**：复用筛选阶段产生的成功轨迹，将其解码为步骤级监督数据，训练新的 LoRA 适配器，使 Policy 对齐特定 Harness 的执行范式，无需额外 rollout。
- **迭代协同**：每轮交替进行 Harness 进化和 Policy 进化，逐步提升匹配度。

**关键实验结果**  
在 ToolHop、SearchQA、RestBench-TMDB、API-Bank 四个基准上，使用 Qwen3-4B 和 Qwen3-8B 作为基座，HarnessForge 平均超过最强基线 3.56%，TMDB 成功率最高提升 12.0%，API-Bank 准确率平均提升 4.96%。消融表明去掉 Harness 或 Policy 进化均导致显著下降，且轮次越深耦合越重要。兼容性矩阵显示匹配对（对角线）性能远优于交叉组合，验证了协同进化产生配适增益。Rollout 效率分析表明，相比纯 RL 策略训练，HarnessForge 在相同预算下处于 Pareto 前沿。

**一句话结论**：有效的 Agent 系统适应必须联合优化执行 Harness 与推理 Policy 的兼容性，而非单独改进任一组件。
