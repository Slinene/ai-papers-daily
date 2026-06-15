---
title: 'HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry'
title_zh: HarnessX：可组合、自适应、可进化的 Agent 运行时脚手架工厂
authors:
- Tingyang Chen
- Shuo Lu
- Kang Zhao
- Weicheng Meng
- Hanlin Teng
- Tianhao Li
- Chao Li
- Xule Liu
- Jian Liang
- Zhizhong Zhang
affiliations:
- Darwin Agent Team
arxiv_id: '2606.14249'
url: https://arxiv.org/abs/2606.14249
pdf_url: https://arxiv.org/pdf/2606.14249
published: '2026-06-11'
collected: '2026-06-15'
category: MultiAgent
direction: Agent 多智体协作优化
tags:
- Agent Harness
- Self-Evolution
- Multi-Agent
- GRPO
- AEGIS
- RL
one_liner: 将 Agent 运行时脚手架抽象为一等公民，通过模块化处理器、进化引擎与协同训练实现自动优化，在多基准上平均提升 14.5%
practical_value: '- **模块化处理器架构**：将 Agent 行为拆解为上下文组装、工具生态、内存策略、控制流等九维处理器，通过 hook 和替换代数实现可组合、可替换的运行时。电商推荐、对话
  Agent 可根据场景（搜索、推荐、售后）快速组装不同的 prompt/工具组合，无需重复开发。

  - **Trace 驱动的自适应优化**：AEGIS 引擎将执行轨迹、验证分数转化为进化信号，自动调整 Agent 的 prompt、工具选择与交互流程。在电商场景中，可将用户反馈（点击、转化）作为
  reward，让 Agent 在线自动优化推荐话术、多步检索策略，且通过变体隔离避免多任务间相互干扰。

  - **跨策略版本协同训练**：利用不同脚手架版本产生的轨迹进行 GRPO 训练，任务级分组计算 group-relative advantage，让模型内化多种策略的优点。可用于训练电商
  Agent 从混合策略数据（如不同召回/排序规则）中学习最优决策，突破固定策略的限制。

  - **共享回放缓冲区的经济性**：Harness 进化与模型训练复用同一批 rollout 轨迹，仅增加一次前向缓存和梯度计算，无额外环境交互成本。对于需要频繁迭代的线上
  Agent 系统，该方法以较低算力开销实现智能化升级。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现代 AI Agent 的性能严重依赖运行时脚手架（harness）——决定模型如何观察、推理和行动的一套 prompts、工具、内存与控制流。但现有脚手架多由人工定制且静态不变，模型升级或任务变化时需逐个重写，且运行产生的丰富轨迹数据极少被系统性反哺优化。该文认为，将脚手架视为可组合、可进化的第一等对象，是提升 Agent 能力、避免单纯依赖模型缩放的另一条可行路径。

**方法关键点**：
- **Harness 组合层**：定义 typed 处理器，挂载到生命周期 hook 上，通过替换代数实现类型安全的即插即用。梳理出九维行为空间（模型选择、上下文组装、内存管理、工具生态、执行环境、评估奖励、控制安全、可观测性、训练桥接），每个维度对应一类处理器。
- **AEGIS 进化引擎**：将脚手架进化映射为强化学习（状态=配置，动作=类型编辑，反馈=轨迹+验证分），通过四阶段管道（Digester 压缩轨迹、Planner 构建适应地貌、Evolver 生成候选、Critic 防御奖励黑客）进行 trace 驱动优化。引入确定性门控和 seesaw 约束防止灾难性遗忘，变体隔离解决异构任务间的冲突。
- **脚手架-模型协同进化**：共享 replay buffer 累积多版本轨迹，采用跨版本 GRPO：同一任务的所有轨迹（无论由哪个脚手架产生）分为一组，计算 group-relative advantage，训练模型内化成功策略。模型更新与脚手架进化复用同一批数据，无额外 rollout 成本。

**关键结果**：
- 在 ALFWorld、GAIA、WebShop、τ3-Bench、SWE-bench Verified 五个基准上，对 Claude Sonnet 4.6、GPT-5.4、Qwen3.5-9B 三种任务 Agent 进行最多 15 轮进化，平均性能提高 +14.5%，最高 +44.0%（Qwen3.5-9B 在 ALFWorld）。
- 增益与基线负相关：较弱模型获益更大，表明进化补足了其行为缺陷；强模型增益小但未见退化。
- 变体隔离消融在异构 GAIA 基准（GPT-5.4）上恢复稳定提升（+13.6%），避免单脚手架进化的停滞。
- 协同进化相比纯脚手架进化额外带来 +4.7% 的增益。

**一句话**：脚手架的设计和进化本身就是与模型训练同等重要的优化杠杆，模块化架构与 trace 反馈闭环可以持续挖掘 Agent 系统的潜能。
