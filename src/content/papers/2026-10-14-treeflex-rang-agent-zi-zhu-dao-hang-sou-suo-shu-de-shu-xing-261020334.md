---
title: 'TreeFlex: Agents Navigating Their Own Search Trees'
title_zh: TreeFlex：让 Agent 自主导航搜索树的树形搜索框架
authors:
- Dongzhuo Li
- Fangzhou Cheng
- Weiwei Li
- Kevin Han
- Haixu Ma
- Zhongchang Sun
- Ruiyi Li
- Serena Li
- Xiangjun Fan
- Lizhu Zhang
affiliations:
- Meta AI
arxiv_id: '2610.20334'
url: https://arxiv.org/abs/2610.20334
pdf_url: https://arxiv.org/pdf/2610.20334
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 策略引导的树搜索与 RL
tags:
- Tree Search
- GRPO
- Agent
- Long-Horizon
- Checkpoint
- SWE-bench
one_liner: TreeFlex 让同一 LLM 在 Reflection 与 Execution 间切换，自主选择保存的中间状态继续搜索，并用树感知 GRPO
  训练，在深度研究和 SWE 上显著超越 ReAct 与 FoldAgent
practical_value: '- 对于多轮推荐/搜索 agent，维护一个显式状态树（候选 query、商品集合、对话状态），让模型自己决定回溯或分支，可避免线性上下文被低质量探索路径污染。工程上可以像
  TreeFlex 一样用“卡片”摘要表示节点，Reflection 角色只看摘要选点，Execution 角色只加载所选路径的详细上下文，既省 token 又保留全局视野。

  - Tree-aware GRPO 的训练方式值得复用：把一次树搜索视为一个 rollout，每个输出只在其生成时的上下文上计算损失，而不是拼接所有分支后训练，这样能避免训练与推理分布不一致，且无需树形
  attention mask。这对任何多路径决策 RL（如对话策略、搜索链路优化）都适用。

  - 过程惩罚设计（如失败调用 -1、超出当前指令范围的操作 -0.2）比单纯最终奖励更能约束 agent 行为；业务上可以针对推荐 agent 的无效工具调用或偏离当前用户意图的探索给予轻量负奖励，避免盲目分支。

  - 资源效率：TreeFlex 用更多推理换取准确率，但在相同采样数下优于重复采样 baseline；因此，在允许高延迟的场景（如深度研究型推荐、复杂用户意图解决），增加可控分支回溯比单纯增加样本量更有效。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长程 agent 任务（深度研究、软件工程）中，标准 ReAct 将所有历史塞进单一线性上下文，废弃尝试和离题观察占据容量，降低推理质量。显式树搜索虽能保留多个中间状态，但如何选择下一个节点通常依赖固定遍历顺序或节点评分，无法结合节点与后续计划。TreeFlex 让同一个模型在全局摘要（Reflection）与局部执行（Execution）间切换，自主决定在哪保存的状态上继续工作。

**方法关键点**：
- 搜索树节点保存父节点、指令、模型撰写的卡片、上下文状态和环境快照（如仓库）。Reflection 仅看所有节点的卡片，选择节点并给出新指令；Execution 恢复该节点路径的上下文，执行领域工具，最后 checkpoint 或 commit 提案；Reflection 批准提案则结束搜索。无固定遍历顺序或节点分数。
- 训练用 Tree-aware GRPO：将一次完整搜索视为一个 rollout，每个模型输出只在它实际生成时的上下文上计算损失，恢复的上下文只作输入并 mask。奖励为任务级二元奖励加上过程惩罚（失败调用 -1、深度研究中超出指令的操作 -0.2）。损失聚合对比 token/block/rollout mean，主结果用 rollout mean λ=0。
- 在 BrowseComp-Plus（深度研究）和 SWE-bench Verified（软件工程）上评估，使用相同 active-context 限制。

**关键实验**：
- 深度研究：Qwen3-4B RL 后，TreeFlex 达到 48.8% Mean@8、66.0% Pass@8，显著高于 flatReAct（41.5/56.0）和 FoldAgent（42.8/55.3）；在 hard questions 上从 3.9% 提升到 13.4%。相同样本和检索调用下也优于重复采样的 baseline。
- SWE-bench Verified：从 Qwen3.5-9B 训练后，TreeFlex 解决 54.9% 的任务，显著高于 FoldAgent（43.3%）及 step-wise 变体（45.2%）。
- 代价：TreeFlex 使用更多生成 token 和推理时间，但在相同资源限制下仍优于 baseline。

**最值得记住的一句话**：让模型在全局摘要和局部执行之间切换，自主管理搜索 frontier，而不是预设树搜索规则，是长程 agent 突破线性上下文瓶颈的有效途径。
