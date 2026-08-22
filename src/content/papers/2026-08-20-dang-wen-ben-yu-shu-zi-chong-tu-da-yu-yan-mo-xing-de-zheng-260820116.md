---
title: 'When Text and Numbers Disagree: Evidence Arbitration in Large Language Models'
title_zh: 当文本与数字冲突：大语言模型的证据仲裁研究
authors:
- Mattia Carletti
- Edward Phillips
- Fredrik K. Gustafsson
- Patitapaban Palo
- Lei Clifton
- Danielle Belgrave
- Xiao Gu
- David A. Clifton
affiliations:
- Department of Engineering Science, University of Oxford
- Nuffield Department of Primary Care Health Sciences, University of Oxford
- GlaxoSmithKline
- Oxford Suzhou Centre for Advanced Research, University of Oxford
arxiv_id: '2608.20116'
url: https://arxiv.org/abs/2608.20116
pdf_url: https://arxiv.org/pdf/2608.20116
published: '2026-08-20'
collected: '2026-08-22'
category: Reasoning
direction: LLM 异质证据冲突仲裁与推理偏差
tags:
- LLM
- Evidence Arbitration
- Tool-augmented Decision
- Numerical Reasoning
- Conflict Resolution
- Benchmark
one_liner: 系统研究 LLM 在文本与数值证据冲突时的仲裁行为，发现启发式偏向与外部工具过度依赖
practical_value: '- 在 Agent/RAG 工具调用链中，若检索或数值 API 返回与上下文文本冲突，不要默认模型能正确仲裁。建议在 LLM 前增加显式证据对齐/冲突检测模块：将数值序列与文本摘要对齐到统一
  schema，并标记冲突供模型或规则处理。

  - 模型对外部工具输出存在过度依赖，即使与直接上下文冲突也倾向采信工具结果。工程上可对工具输出注入置信度/新鲜度信号，并强制模型在生成最终答案前输出每路证据的可靠性判断，作为中间推理步骤。

  - 显式可靠性提示效果弱于时间 recency 提示，提示词中“最新数据优先”可能比“高可靠来源优先”更有效；业务中实时转化率等时间敏感特征与历史统计冲突时，应更重视
  recency 信号而非依赖模型自行权衡。

  - 可构建合成冲突测试集（用隐变量生成两种模态，再制造仅一个模态对齐 ground truth）用于上线前评估 LLM 在风控、广告竞价、推荐解释等场景下的证据整合鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
LLM 越来越多用于工具增强决策，但不同证据源（文本摘要、数值观测、外部工具输出）经常互相冲突。模型如何在这些证据间仲裁直接决定下游决策质量。  

**方法关键点**  
构建受控合成 benchmark：用隐风险轨迹同时生成数值时间序列和自然语言摘要，可精确构造冲突——仅有一个证据源与 ground-truth 对齐。设计允许独立操纵模态、时间近因、来源可靠性和证据出处。在多个开放权重指令微调模型上测试。  

**关键结果**  
仲裁行为系统化而非随机：模型表现出明显的文本/数字偏好；对时间近因的遵循比显式可靠性提示更一致；即使外部预测与直接上下文证据冲突，模型也会过度依赖外部预测。  

**结论**  
当前 LLM 在整合异质证据时采用启发式仲裁策略，暴露了 tool-augmented 决策系统的失败模式。
