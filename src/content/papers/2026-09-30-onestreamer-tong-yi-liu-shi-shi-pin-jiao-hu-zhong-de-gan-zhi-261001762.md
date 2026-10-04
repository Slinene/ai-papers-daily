---
title: 'OneStreamer: Unifying Perception, Memory, and Proactive Response in Streaming
  Video Interaction'
title_zh: OneStreamer：统一流式视频交互中的感知、记忆与主动响应
authors:
- Xiangyu Zeng
- Yuandong Yang
- Zhiqiu Zhang
- Yuhan Zhu
- Xinhao Li
- Qingyi Si
- Dingyu Yao
- Changlian Ma
- Haoran Chen
- Xinyu Chen
affiliations:
- NJU
- PJLAB
- JD
- SJTU
- USTC
arxiv_id: '2610.01762'
url: https://arxiv.org/abs/2610.01762
pdf_url: https://arxiv.org/pdf/2610.01762
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 流式视频LLM主动记忆与响应
tags:
- streaming video
- LLM
- memory
- proactive generation
- multimodal
- training
one_liner: 通过共享主动生成过程联合学习证据记录与任务响应，形成可复用事实记忆且不牺牲实时感知
practical_value: '- **实时用户行为流中的记忆机制**：可借鉴 PHCM 思路，让 LLM 在用户会话中持续生成结构化摘要（如兴趣点、关键事件），作为可复用记忆补充最近窗口的原始行为，无需回溯全部历史即可回答后续
  query 或做动态推荐。

  - **状态监督稀疏化**：PSTL 只对状态变化和状态持续的代表性 token 施加监督，减少重复无动作状态的负样本主导，适合序列推荐中的用户状态建模，降低标注成本并提升训练效率。

  - **流式数据合成**：该论文的数据合成管道强调输出内容与时序必须与当前可用证据对齐，避免信息泄露；在搜索推荐 Agent 的模拟数据生成中同样重要，确保生成样本符合在线实时约束。

  - **主动生成作为统一接口**：将感知、记忆和响应整合到同一个生成任务中，可指导设计电商 Agent，使模型在浏览/对话过程中持续产生可复用的中间记录（意图、属性），服务于后续推荐和问答。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：流式视频 LLM 需要在不知道未来任务相关性的情况下保留证据，并在足够证据出现时及时响应。核心挑战是形成可复用的事实记忆，同时不损害实时感知能力。

**方法关键点**：OneStreamer 通过共享的主动生成过程联合学习 query-independent 的证据记录与任务响应。其 Proactive Hierarchical Caption Memory (PHCM) 生成时间对齐的局部细节 caption 和已完成事件摘要；训练时用流式 caption 目标监督对已观测视频前缀的解释。推理时模型生成的记录补充最近的视觉窗口，提供可复用事实上下文而无需重访历史视觉特征。Proactive State Transition Learning (PSTL) 通过保留所有输出锚点的监督并选取代表性状态变化/持续 token，缓解重复等待状态的主导问题。另构建流式数据合成管道，对齐输出内容与时序与可用证据，得到 OneStreamer-1M 数据集，包含超过 100 万条记录。

**关键结果**：4B 模型在 8 个流式视频理解基准上均优于对比方法。消融显示保留生成 captions 提升历史 QA 且不降低实时感知；PSTL 只监督 27.5% 的标注状态 token 即优于 dense state supervision。
