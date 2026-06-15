---
title: 'StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance'
title_zh: StreamMemBench：面向未来辅助的个人Agent记忆流式评估基准
authors:
- Guanming Liu
- Yuqi Ren
- Hansu Gu
- Peng Zhang
- Weihang Wang
- Jiahao Liu
- Ning Gu
- Tun Lu
affiliations:
- Fudan University
- Amazon
arxiv_id: '2606.14571'
url: https://arxiv.org/abs/2606.14571
pdf_url: https://arxiv.org/pdf/2606.14571
published: '2026-06-12'
collected: '2026-06-15'
category: Agent
direction: Agent记忆评测 · 流式未来辅助
tags:
- memory evaluation
- personal agent
- streaming benchmark
- evidence reuse
- future-oriented assistance
- lifelog
one_liner: 提出首个从流式观察到任务复用全链路诊断Agent记忆行为的基准，揭示存储与利用的鸿沟
practical_value: '- 在设计电商/推荐Agent的记忆模块时，不能仅关注存储准确率，需要构建“证据存储→初始任务使用→反馈修正→跨任务复用”的端到端评测链路，否则高存储命中率可能掩盖低效的任务应用

  - 反馈的即时修正与长期固化是两回事：很多系统能在同轮中根据反馈修正回复，但无法将修正经验沉淀到记忆供后续任务调用，应在记忆更新机制中增加“经验整合”步骤（如prompt
  template、mem-skill等）

  - 随着会话或行为流变长，Agent的证据使用能力可能持续衰减，建议在线上监控中引入分段能力漂移指标，而不仅看全局平均

  - 构建记忆评测数据时，可借鉴“证据锚点”方法，从真实行为流中抽取关键事实并关联到后续需要该事实的任务，避免合成数据集中的信息泄露与表面合理性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
个人Agent的记忆不仅需要存储用户偏好和历史，更要能将观察到的信息转化为未来任务的辅助，但目前大多数记忆评测只孤立测试对话回忆或任务提升，忽略了从流式观察到未来辅助的完整路径。实际应用中，Agent需要从自我中心流（egocentric streams）中识别有用证据、用于当前任务，并固化反馈为后续可复用的经验，而现有系统往往“存而不用”。  

**方法**  
- 基于EgoLife生活日志构建证据锚点（evidence anchor）：从5分钟片段中抽取用户特异性证据，并生成两条依赖同一证据但场景不同的任务查询（初始任务和后续任务）  
- 评测轨迹包含四个关键节点：证据保真度（Fidelity，检查记忆是否存储证据）、初始证据使用（IEU，是否用证据回答初始任务）、反馈整合（FI，对修正反馈是否能临场修正）、后续复用（FUR，后续任务中是否复用修正后的经验）  
- 通过用户模拟器给出自然反馈并评判，所有得分均由多数投票决定，避免信息泄露，保证查询不直接暴露证据  

**关键实验与结果**  
在8个记忆系统（RAG、Mem0、EverMemOS、A-Mem、MemOS、MemoryOS、MemSkill）和两个LLM骨干（DeepSeek-V4-Flash、Gemini-3-Flash）上评测：  
- 高Fidelity并不保证高IEU和FUR，例如A-Mem和MemoryOS的Fidelity达100%，但IEU仅34.9%/23.9%，FUR 64.9%/61.9%  
- 多数系统FI高于FUR，表明能临场修正却无法转化为长期复用，MemOS尤为突出（FI 77.2% vs. FUR 3.9%）  
- 随着流长度增加，RAG的IEU从早期到晚期明显下降，但FI和FUR可能回升，暴露出单一全局指标无法反映能力漂移  
- 故障模式分析显示，不同系统的崩溃点不同：有的在记忆形成，有的在初始使用，有的在修正巩固  

**核心结论**  
记忆应被评判为是否支撑未来的有用行为，而不仅是存储的信息量。StreamMemBench通过追踪“观察→存储→初始使用→反馈修正→后续复用”的完整体现了这一理念。
