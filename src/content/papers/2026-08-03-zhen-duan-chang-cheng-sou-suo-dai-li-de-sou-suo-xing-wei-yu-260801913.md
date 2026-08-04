---
title: Diagnosing Search Behavior and Failure Modes in Long-Horizon Search Agents
title_zh: 诊断长程搜索代理的搜索行为与失败模式
authors:
- Qi Liu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2608.01913'
url: https://arxiv.org/abs/2608.01913
pdf_url: https://arxiv.org/pdf/2608.01913
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 搜索代理行为诊断与失败分析
tags:
- Search Agent
- Failure Analysis
- Retrieval Gap
- Utilization Gap
- Evidence-Driven Stopping
- Trajectory Diagnosis
one_liner: 通过轨迹级诊断揭示搜索努力与答案质量弱相关，证据检索召回率才是核心，失败可拆分为检索缺口与利用缺口
practical_value: '- **用累积证据召回率替代搜索步数作为健康指标**：在构建电商问答Agent或深度搜索产品时，监控“已检索到的黄金证据占比”远比统计搜索次数更能预测回答准确性。可嵌入评估链路，实时判断搜索质量。

  - **实施基于证据增量的动态停止策略**：研究发现77–94%的搜索步骤未带来新证据，有用证据集中在早期。可在Agent中增加模块，当连续K步未检索到新证据或已达累积证据阈值时自动终止搜索，减少尾部浪费和上下文溢出。

  - **区分检索侧与利用侧失败，定向修复**：错误答案可分为“从未找到证据”（检索缺口）和“找到证据但回答错”（利用缺口）。在迭代优化时，前者应改进查询改写与探索策略，后者应加强证据验证与答案归因。不同Agent的缺口比例差异大，需按诊断施治。

  - **上下文管理优先处理搜索摘要流**：搜索片段占用了大部分上下文（66–85%），远高于访问内容。可引入摘要去重、按轮次老化旧摘要、限制保留摘要数量等机制，防止旧信息淹没后续推理。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
深度搜索代理通过多步检索与推理回答复杂问题，但当前评估只看最终答案正确率，忽略了轨迹内部的低效与失败根源。区分“有效搜索”与“盲目搜索”对于提升系统效率与问题诊断至关重要。

**方法关键点**  
- 在 BrowseComp-Plus 固定语料库上，所有代理共享同一检索器和工具接口（ReAct 框架），隔离行为差异。  
- 利用人工标注的文档级相关性判断（qrels），逐步度量检索证据的累积召回率、新证据增量，划分步骤为productive/redundant/unproductive。  
- 将错误分为**检索缺口**（黄金证据从未被检索）和**利用缺口**（证据被检索但答案仍错）。  
- 对比六种代理（三个中等规模、三个前沿规模），分析查询改写、搜索量、上下文消耗与准确率的关系。

**关键实验与结果**  
- 在 BrowseComp-Plus 上，搜索量与准确率几乎无关（r=0.16），但累积证据召回率与准确率强相关（r=0.99）。  
- 77–94% 的搜索步骤未增加新证据，有用证据多在早期步骤中出现，后续多为浪费尾部。  
- 检索缺口在所有代理中占比51–64%，但个别代理利用缺口占优（如 Kimi K2.6 达52%），相同准确率的代理缺口分布可能相反。  
- 重复查询是低效的强信号；强代理查询更精简，倾向于并行批处理且极少重复。  
- 在开放网络 BrowseComp 上结论一致：准确率由证据充分度决定，而非搜索量。

**核心洞察**  
*更好的搜索不在于更深，而在于更有方向：早期命中证据并适时停止，远比追加无效搜索重要。*
