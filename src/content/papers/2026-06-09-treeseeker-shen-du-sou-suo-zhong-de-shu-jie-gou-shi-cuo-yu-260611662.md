---
title: 'TreeSeeker: Tree-Structured Trial, Error, and Return in Deep Search'
title_zh: TreeSeeker：深度搜索中的树结构试错与分支返回框架
authors:
- Zhuofan Shi
- Mingzhe Ma
- Lu Wang
- Fangkai Yang
- Pu Zhao
- Yiming Guan
- Youling Huang
- Wei Zhang
- Qingwei Lin
- Dongmei Zhang
affiliations:
- Microsoft
- East China Normal University
arxiv_id: '2606.11662'
url: https://arxiv.org/abs/2606.11662
pdf_url: https://arxiv.org/pdf/2606.11662
published: '2026-06-09'
collected: '2026-06-13'
category: Agent
direction: Agent深度搜索的树结构试错与预算分配
tags:
- Deep Search
- Tree Search
- UCB
- Agent
- Trial-and-Error
one_liner: 提出TreeSeeker，通过树结构分支状态和文本UCB操作控制实现深度搜索的受调试错与预算重分配
practical_value: '- **多路径搜索控制**：在需要多步信息收集与证据整合的代理任务（如电商导购助手、事实核查）中，可为每个候选方向（查询、来源、假设）维护独立分支状态，利用进度、冲突和失败线索动态分配搜索预算。

  - **文本UCB预算分配**：通过大语言模型对候选操作（利用/探索/剪枝）进行语义评分（价值、不确定性、风险），无需精确数值奖励即可实现探索-利用-剪枝决策，适合开放域搜索任务。

  - **记忆压缩与锚点保留**：TreeMem将长历史压缩为分支局部状态，同时保留叶踪迹作为短期锚点，可有效控制上下文长度并保持决策连贯，适用于长对话或长搜索轨迹的代理。

  - **操作级决策简化空间**：将预算分配抽象为利用、探索、剪枝三种操作，避免细粒度路径评分，降低组合空间，提高大语言模型决策的稳定性和效率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：深度搜索代理面临早期方向不确定性，贪婪跟随当前最佳方向可能持续扩展弱路径，而无纪律的探索会浪费预算。亟需受控的试错机制，在多个候选方向间动态分配搜索预算。

**方法关键点**
- **TreeSeeker框架**：将搜索过程组织为树结构状态，每个子目标维护一棵搜索树，分支代表不同的查询、来源或假设。
- **TreeSearch控制层**：使用操作级文本UCB规则，从TreeMem状态中估计价值（Value）、不确定性（Uncertainty）和风险（Risk），对每个子目标输出EXPLOIT（利用前景分支）、EXPLORE（探索不确定替代）或PRUNE（剪枝并返回早期分支点）决策。
- **TreeMem记忆层**：为每个分支存储压缩状态，包括证据、冲突、进度与失败线索，并保留最新叶踪迹作为短期锚点，使决策可比较不同方向、识别失败尝试并回退。
- **算法流程**：规划代理分解问题为子目标DAG并初始化候选路径；每轮根据依赖关系构建前沿，对活跃目标应用文本UCB决策；执行动作（搜索/浏览）或剪枝，更新TreeMem；定期汇总压缩；最终合成答案。

**关键实验**
- **数据集**：XBench-DeepSearch全量，BrowseComp及BrowseComp-ZH各随机抽样100例。
- **对比底线**：Flash-Searcher（最直接树结构搜索基线）、IterResearch、Tongyi-DeepSearch等开源系统，以及闭源模型参考。
- **主要结果**：使用gpt-5.2主干，TreeSeeker在XBench-DS达56.3，BrowseComp达47.0，BrowseComp-ZH达43.0，均优于所评测开源基线。与Flash-Searcher相比提升5.6点，且总token和工具调用更低。消融实验：移除文本UCB下降4.3点，禁用探索与剪枝下降8.3点，移除叶踪迹下降5.0点，验证了各组件必要性。操作频率分析显示，文本UCB使利用与探索更平衡（51.4% vs 43.4%），剪枝占比5.2%。

**核心贡献**：显式维护树结构分支状态并通过文本UCB进行操作级预算分配，为深度搜索提供了一种不依赖数值奖励的试错与回退框架，性能优于固定调度的并行搜索。
