---
title: 'PredAct-Bench: Benchmarking Tool-Augmented Dialogue under Controlled Tool
  Noise'
title_zh: PredAct-Bench：在可控工具噪声下评测对话智能体
authors:
- Abdulrahman AlRabah
- Xiaocheng Yang
- Dilek Hakkani-Tür
- Abdussalam Alawini
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2608.02372'
url: https://arxiv.org/abs/2608.02372
pdf_url: https://arxiv.org/pdf/2608.02372
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 工具增强对话 · 人机信任校准
tags:
- Tool-Augmented Dialogue
- Trust Calibration
- Human-AI Collaboration
- Longitudinal Reasoning
- Benchmark
one_liner: 提出首个在预测工具噪声下评估对话智能体的基准，发现LLM过度依赖工具而人类能更校准地采纳建议
practical_value: '- **信任校准指标可迁移**：RAIR/RSR 指标不依赖特定领域，可直接用于评估推荐解释或对话推荐场景中用户对AI建议的适当依赖程度，帮助诊断过度信任或忽视问题。

  - **工具噪声注入方法论**：在对话推荐系统中，可以像 PredAct-Bench 一样只对某些工具（如预测评分）注入可控噪声，而保持事实查询类工具准确，以此评估系统在噪声下的鲁棒性和用户行为变化。

  - **多轮验证对话设计**：所采用的“初始决策-工具对话-最终决策”流程可借鉴到电商Agent中，让用户先看推荐理由再通过追问验证（查历史、反事实），减少盲目采纳有噪声的推荐。

  - **人类行为基线参考**：论文显示人类会花更多时间、问更少但更有针对性的问题，这提示在设计推荐对话Agent时，不应追求短平快的交互，而应鼓励用户提出证据整合类问题以校准信任。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现实中的任务型对话系统常依赖统计预测工具（如风险评分、点击预测），这些工具输出带有噪声，但现有基准普遍假设工具完美，忽略了人类决策者在与Agent交互时如何校准信任。本文以教育领域为测试床，构建了首个在受控工具噪声下评测预测性对话智能体的基准，旨在暴露LLM在纵向推理、多轮交互和噪声条件下的实际决策行为。

**方法关键点**：
- 构建两个数据集：OULAD（真实成绩轨迹）和 PREDACT-CS（60门CS课程的真实最终成绩+合成周评分轨迹），模拟学期中预测学生是否挂科的场景。
- 工具集包含4类12个工具：确定性查找（查成绩、课程大纲）、反事实模拟（假设剩余作业得分）、k-NN预测（概率工具，输出预测等级和置信度）、干预建议生成。仅对预测工具注入可控噪声，准确率设为40%~80%五档。
- 对话流程分三阶段：① Agent自动展示高风险学生及置信度；② 教师（人或LLM扮演）给出初始flag/no-flag决策；③ 教师通过多轮对话向助手追问证据，最终修正决策。
- 评估指标：决策F1（初始与最终）；新引入的RAIR（当教师初始错、Agent正确时，教师转向Agent的比例）和RSR（教师初始正确、Agent正确时，教师坚持己见的比例），用于度量多轮对话中的信任校准。
- 13个LLM担任“教师”角色（7个闭源、6个开源），助手固定为GPT-4o Mini，完成1300次完整对话；另招募13位真人讲师进行对照实验。

**关键结果**：
- 随着工具准确率从40%升至80%，LLM教师的F1在PREDACT-CS上从36升至73，在OULAD上从26升至45，说明工具质量直接影响决策质量。
- 11/13的LLM模型RAIR<0.20、RSR>0.97，表现为过度依赖工具输出，对话不但未纠正错误反而导致10个模型F1下降（最大降幅11点）；而人类RAIR=0.63、RSR=0.88，处于校准象限。
- 行为分析显示人类每轮对话耗时更长、提问更少但问题类型更多样（偏好证据聚合而非单一查询），决策更审慎。

**一句话**：**当工具不可靠时，LLM代理倾向于“盲目跟从”而不是“选择性验证”，这一行为模式与人类形成鲜明对比。**
