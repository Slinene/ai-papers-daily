---
title: 'Knowing What to Solve Before How: Preplan Empowered LLM Mathematical Reasoning'
title_zh: 先理解再求解：预计划增强的LLM数学推理框架
authors:
- Shaojie Wang
- Liang Zhang
affiliations:
- Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2605.30245'
url: https://arxiv.org/abs/2605.30245
pdf_url: https://arxiv.org/pdf/2605.30245
published: '2026-05-28'
collected: '2026-05-29'
category: LLM
direction: LLM推理范式·规划与预计划
tags:
- Preplan
- Plan-based Reasoning
- GRPO
- Mathematical Reasoning
- Chain-of-Thought
one_liner: 在问题→计划→CoT之间插入显式的“预计划”阶段，明确分析问题类型与陷阱，并通过防剧透过滤与复合奖励保证计划真正遵循预计划，在不增加推理开销下提升数学推理性能。
practical_value: '面向电商/推荐/Agent从业者的可借鉴点：

  - **在Agent规划中引入显式意图分析阶段**：类似于预计划，在生成执行计划前，先让模型分析用户意图、可用工具、约束和潜在陷阱，再输出具体步骤；可参考论文中“先what后how”的范式分离设计，减少规划错误。

  - **用防剧透过滤器清洗训练数据**：当需要为推理或规划链条生成中间分析数据时，可使用规则化spoiler-score检测器过滤掉“把答案/推导提前泄露”的低质量样本，保证中间分析只停留在高层策略而非具体计算。

  - **设计复合奖励让中间输出被真正使用**：对于多阶段的生成（如推荐理由→候选生成→排序），可在RL训练时引入“前后一致性奖励”，强制模型生成的理由真正被下游模块遵循，而非装饰性文本。

  - **零额外推理开销的高阶组织**：PPC范式表明，增加结构化的前序分析不会膨胀总token数，反而因减少了后续推理的试错而更高效；这给多阶段生成系统（如多Agent推理链）提供了设计信心：引入规划摘要层可能整体提速。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
现有基于计划的推理方法（如Plan-Tuning、PTA-GRPO）遵循“问题→计划→CoT”范式，其计划和执行阶段都在回答“如何求解”，而“求解什么”（如识别问题类型、可用的工具、边界条件和常见陷阱）则完全隐式化。诊断表明，大量错误源于对“求解什么”的理解失败，而非计算错误。这揭示了一个范式空缺：需要在“如何求解”之前显式建模“求解什么”。  

**方法关键点**  
- **三阶段推理范式**：提出PPC（Preplan-Plan-CoT），引入“预计划”（preplan）阶段，围绕问题类型、工具、约束和陷阱进行分析，不涉及具体推导或计算，形成“问题→预计划→计划→CoT”新流程。  
- **防剧透的数据构建**：采用三阶段合成管道生成训练数据（预计划→计划→执行），并通过规则化的spoiler-score检测（基于推导短语、等式密度、长公式、答案泄露等6项信号）过滤掉含有“剧透”或“泄露”的预计划，确保预计划停留在高层分析。  
- **复合GRPO奖励**：在强化学习阶段设计四项组合奖励：部分正确结果奖励（基于路径接近度）、计划-预计划一致性奖励（由冻结的LLM评委评判策略对齐度）、结构格式检查以及预计划风格惩罚（复用spoiler-score），强制模型生成的计划真正遵循预计划。  

**关键结果**  
在Qwen3-4B、Qwen2.5-7B、Qwen2.5-Math-7B、Llama3.1-8B四个骨干模型上，于AIME25、Minerva-Math、OlympiadBench、MATH-500、GSM8K五个基准测试中，PPC在39/40个指标上取得最佳结果，maj@16和pass@16分别平均提升+2.23和+3.06。消融实验证实三项奖励成分的叠加贡献。推理效率方面，PPC在MATH-500上的平均生成token数低于标准CoT和PTA-GRPO，表明结构化预分析能减少冗余探索，未增加推理成本。
