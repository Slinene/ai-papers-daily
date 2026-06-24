---
title: 'Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for
  Agentic Experience Learning'
title_zh: 逃离自我确认陷阱：执行-蒸馏-验证的智能体经验学习框架
authors:
- Shiding Zhu
- Yudi Qi
- Yajie Wang
- Jiaze Li
- Chao Song
- Yaorui Shi
- Yibo Miao
- Hanqi Gao
- Kai Zhang
affiliations:
- Zhejiang University
- Tsinghua University
- Northwestern Polytechnical University
- University of Science and Technology of China
- Shanghai Jiaotong University
arxiv_id: '2606.24428'
url: https://arxiv.org/abs/2606.24428
pdf_url: https://arxiv.org/pdf/2606.24428
published: '2026-06-22'
collected: '2026-06-24'
category: MultiAgent
direction: 多智能体协作经验构建
tags:
- Self-Confirmation Trap
- Multi-Agent
- Experience Learning
- Memory
- Agent Self-Evolution
- Long-Horizon Tasks
one_liner: 通过多智能体异构执行、第三方对比蒸馏与共识验证，将经验学习从自反思循环重构为协作过滤，可靠抑制错误记忆污染
practical_value: '- **经验构建的去偏设计**：在电商Agent（如导购助手、客服Agent）的经验积累中，直接套用单智能体自总结容易把错误但自洽的交互流程当成成功案例写入记忆，导致后续任务复用错误策略。可借鉴EDV的**第三方蒸馏**：用另一个模型（或不同prompt的同一模型）对比多个并行执行轨迹，生成候选经验，减少执行者中心化的总结偏差。

  - **共识验证提升记忆质量**：在广告出价Agent或搜索推荐Agent的记忆更新时，引入**执行者集体投票**的默认拒绝机制，只有获得全体执行者一致认可的经验才进入共享记忆，部分认可则存入私有记忆。这能有效过滤幻觉与噪声，特别适用于无明确ground-truth的开放域任务。

  - **异构执行增加探索多样性**：实际业务中可部署多个不同模型（或同模型不同温度）对同一任务并行产生候选轨迹，而非简单增加重试次数。这样做能暴露不同的成功与失败模式，为后续经验提取提供更丰富的对比素材，类似推荐系统中的多样性采样。

  - **能力矩阵与分层记忆**：维护一个动态能力矩阵，记录各Agent擅长哪些任务类型；推理时先按任务匹配最适求解器，再从共享记忆和私有记忆中逐级检索。这种轻量级的路由+记忆分层模式可直接移植到多模型协同的推荐Agent系统，几乎不增加在线推理成本，却显著提升检索命中率和经验利用率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM智能体依赖经验学习实现自我进化，但现有方法多采用单体闭环：同一智能体执行、总结、记忆，导致“自我确认陷阱”——错误但自洽的轨迹被误判为成功经验存入记忆，并通过后续检索复用逐步放大错误。在开放世界环境下，根本原因是执行与评估角色耦合，缺乏独立验证。因此，如何提升经验构造本身的可靠性成为关键瓶颈。

**方法关键点**：
- **EDV框架**：将经验学习分解为三个阶段：**Execute**—从异构模型池随机抽取多个智能体并行探索同一任务，产生多样化候选轨迹；**Distill**—指定独立的第三方蒸馏智能体对多条轨迹执行对比分析，提炼候选经验，避免执行者自总结的视角偏见；**Verify**—原执行组对候选经验进行共识投票（采用严格默认拒绝策略），只有全体一致认可的经验进入共享记忆，部分认可则写入对应私有记忆，其余丢弃。
- **记忆与推理**：维护**共享记忆库**（普适经验）和**私有记忆库**（个性化经验），并基于蒸馏过程中的表现统计构建**能力矩阵**，记录各模型擅长任务类型。推理时先用能力矩阵匹配最佳求解器，再分层检索共享/私有记忆辅助决策。
- **实现细节**：使用MiniMax-M2.1、Mimo-V2-Flash、GLM-4.7-FP8三个异构模型；执行阶段温度越高以鼓励探索；检索基于Qwen3-Embedding-4B余弦相似度，共享库阈值0.8，私有库阈值0.85。

**关键实验结果**：
- 在长程基准τ²-bench（航空、零售、电信三个域）上，EDV平均Pass@1达86.6，显著优于单模型无记忆（76.4-79.6）、ReasoningBank（79.0-81.9）和推理时路由（83.5）。Mind2Web跨任务/跨网站/跨域泛化中，EA、AF1、SSR等均稳定超越基线；MMTB多工具评测总分58.10，同样最高。
- 人工审核EDV产生的记忆，在正确性（4.41 vs 3.72）、可操作性（4.32 vs 3.58）、特异性（4.27 vs 3.64）上全面领先ReasoningBank，噪声分数从1.21降至0.63。
- 故意在记忆库注入10%自洽错误经验，RB性能从82.5骤降至77.2，验证了自我确认陷阱的现实危害。
- 消融实验证明：异构执行+第三方蒸馏+共识验证缺一不可；能力矩阵和分层记忆分别带来2.0和2.7-2.9分的增益，且二者均无额外在线开销。

**核心洞见**：记忆质量比数量更重要——可靠的经验学习不仅需要更丰富的记忆，更需要严格的构造和验证流水线。
