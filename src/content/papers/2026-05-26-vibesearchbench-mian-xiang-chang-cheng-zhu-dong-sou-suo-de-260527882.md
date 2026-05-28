---
title: 'VibeSearchBench: Benchmarking Long-horizon Proactive Search in the Wild'
title_zh: VibeSearchBench：面向长程主动搜索的渐进式意图评测基准
authors:
- Xiaohongshu Inc
affiliations:
- Xiaohongshu Dots Studio
- Unipat AI
arxiv_id: '2605.27882'
url: https://arxiv.org/abs/2605.27882
pdf_url: https://arxiv.org/pdf/2605.27882
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: 长程主动搜索 · 渐进式意图澄清
tags:
- VibeSearch
- Search Agent
- Multi-turn Interaction
- Knowledge Graph Evaluation
- Benchmark
one_liner: 提出VibeSearch范式与VibeSearchBench基准，通过多轮渐进式用户模拟与图匹配评估揭示当前模型主动搜索能力严重不足。
practical_value: '- **电商搜索体验升级**：VibeSearch 的“模糊意图→多轮渐进澄清”恰好对应电商中消费者“不确定想买什么→通过浏览交互逐步明确需求”的典型行为，可直接将
  VibeSearchBench 中的用户角色设计与渐进式意图触发机制迁移到电商搜索 Agent 的评测与训练中，驱动从被动答询到主动引导的范式转变。

  - **知识图谱评测框架复用**：图匹配评测不依赖固定 schema，能客观度量检索结果对复杂实体关系的覆盖。在生成式推荐或商品知识库问答中，可借鉴此方式评测输出结构化信息的精确度与召回率，避免自由文本评测的不稳定性。

  - **Agent 交互成本诊断**：实验表明，过多工具调用与上下文压缩反而损害性能（如 GPT-5.4 存在“冗长输出→上下文溢出→信息丢失→重复搜索”的恶性循环）。在构建电商客服或购物助手
  Agent 时，应监控 #Asst/#User 比值与压缩频率，寻找资源消耗与性能的 sweet spot，避免盲目堆叠多步推理。

  - **记忆与子代理机制的实际效果**：OpenClaw 的 local/lifelong memory 与 sub-agent 并未显著提升 VibeSearch
  性能，说明现有架构增强不能弥补模型本身在长文本整合与意图追踪上的缺陷。这提示在业务中若遇到类似多轮复杂任务，应优先投入提升基座模型的上下文理解能力，而非过度依赖外部记忆工程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有搜索 Agent 基准在短文本、单轮、固定输出格式下已取得高分，但真实用户仍反馈“答非所问”。根本原因是用户无法一次性完整描述需求，而是通过多轮对话逐步澄清模糊意图，这一过程被称为 VibeSearch。已有基准无法复现这种双向收敛的交互模式，导致评测与体验严重脱节。

**方法关键点**  
- **VibeSearchBench 数据集**：200 个中英双语任务，覆盖 20 个领域，分专业版 (VibeSearch-Pro) 与日常版 (VibeSearch-Daily)。每个任务包含一个用户角色 (Persona) 和一个无模式知识图谱作为真值 (G*)，平均含 298 个三元组。  
- **渐进式用户模拟器**：基于角色定义多个触发式信息披露阶段，仅当 Agent 主动提及或完成特定里程碑时才解锁下一层需求；模拟器以 LLM 为后端，持续给予反馈与追问压力。  
- **图匹配评测**：要求 Agent 输出预测知识图谱，使用 LLM-as-judge 判断每个真值三元组是否被覆盖，支持语义等价、包容、组合推导等，计算三元组级别的精确率、召回率与 F1。

**关键实验结果**  
在 7 个前沿模型（含 Claude Opus 4.6、GPT-5.4 等）上测试，ReAct 与 OpenClaw 两个框架下最好 F1 仅 30.30（Claude Opus 4.6），所有模型均在 33 以下。错误分析揭示三大瓶颈：  
- 上下文压缩导致信息丢失，压缩轨迹 F1 下降 8–12 点；  
- 无模型能触及用户模拟器的结束信号，意图挖掘效率低下；  
- 输出知识图谱结构扁平，缺少层级关系，出现大量无效元数据或主观臆断。  
OpenClaw 的子代理、本地记忆、终身记忆消融均未带来显著提升，说明能力短板在模型本身而非框架层面。

**核心结论**  
当前最先进的 LLM Agent 在需要持续主动挖掘用户意图、整合分散信息并构建结构化知识的长程搜索任务上，表现与真实需求相距甚远，亟需模型对长上下文融合与精细意图建模的根本性突破。
