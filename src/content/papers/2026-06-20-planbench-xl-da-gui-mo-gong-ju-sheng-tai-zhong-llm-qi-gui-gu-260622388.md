---
title: 'PlanBench-XL: Evaluating Long-Horizon Planning of LLM Tool-Use Agents in Large-Scale
  Tool Ecosystems'
title_zh: PlanBench-XL：大规模工具生态中LLM Agent长期规划评估基准
authors:
- Jiayu Liu
- Qihan Lin
- Cheng Qian
- Rui Wang
- Emre Can Acikgoz
- Xiaocheng Yang
- Jiateng Liu
- Zhenhailong Wang
- Xiusi Chen
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2606.22388'
url: https://arxiv.org/abs/2606.22388
pdf_url: https://arxiv.org/pdf/2606.22388
published: '2026-06-20'
collected: '2026-06-23'
category: Agent
direction: Agent 长期规划评估 · 大规模工具检索
tags:
- Tool-Use Agents
- Long-Horizon Planning
- Tool Retrieval
- Benchmark
- Blocking Mechanism
- Evaluation
one_liner: 在1665个工具的零售任务基准上，揭示LLM Agent在检索受限与动态阻塞下长期规划能力的严重退化
practical_value: '- 电商Agent常需在大量API/工具中选择与组合，本基准中的**迭代式工具检索-调用-发现子目标**范式可直接用于设计推荐/搜索Agent的规划流程，尤其需要将工具描述检索与规划解耦，避免一次性暴露全量工具。

  - 阻塞机制模拟了真实服务不可用、返回异常或误导性工具，建议在Agent开发中**注入工具调用异常处理与自适应模块**，如动态替换失败工具、延长尝试路径，并显式标记错误信号以降低恢复难度。

  - 实验发现Agent在缺乏明确错误信号时极易崩溃，值得在业务Agent中**强制要求工具返回标准化状态码与可读错误信息**，并训练模型利用这些信号重规划。

  - 该基准的“长期任务→子目标推断→中间证据收集”闭环，为电商场景中多步推荐（如先查用户画像→再查商品库存→组合优惠规则→生成推荐）提供了可测试的评价范式，可参照构建内部鲁棒性测试集。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM Agent评测基准多在完全可见的小型工具集上进行，忽略真实场景中工具数量庞大（如企业MCP服务器）、Agent需通过检索逐步发现可用工具，并应对工具失败、缺失等动态干扰。尤其在电商等长期任务中，Agent必须推断隐式子目标、按需调用工具并收集中间证据，现有基准无法衡量此类规划能力。

**方法**：构建PlanBench-XL——包含327个零售任务、1665个工具的多轮交互式基准。每个任务要求Agent通过检索关键字获取部分工具描述，调用工具后获得线索，再决定下一步检索与调用，直至完成最终目标。可选阻塞机制注入三种干扰：工具缺失、调用失败、无关干扰工具，迫使Agent动态检测故障并自适应恢复。在10个主流LLM上进行评估。

**关键结果**：大规模工具规划极具挑战，最强模型GPT-5.4在无阻塞下仅51.90%准确率，严重阻塞时骤降至11.36%。分析表明，缺乏显式错误信号或恢复路径较长时，Agent性能崩溃尤为严重。该基准成为诊断Agent长期规划与自适应能力的有效测试平台。
