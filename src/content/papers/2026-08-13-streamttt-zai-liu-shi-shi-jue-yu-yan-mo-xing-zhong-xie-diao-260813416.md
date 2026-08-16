---
title: 'StreamTTT: Reconciling Real-Time Perception and Long-Term Memory in Streaming
  VLMs'
title_zh: StreamTTT：在流式视觉语言模型中协调实时感知与长期记忆
authors:
- Joya Chen
- Zeyun Zhong
- Mike Zheng Shou
affiliations:
- National University of Singapore
- Karlsruhe Institute of Technology
arxiv_id: '2608.13416'
url: https://arxiv.org/abs/2608.13416
pdf_url: https://arxiv.org/pdf/2608.13416
published: '2026-08-13'
collected: '2026-08-16'
category: Multimodal
direction: 流式视觉语言模型 · 快速权重记忆
tags:
- Streaming VLM
- Long-term Memory
- Fast Weights
- Real-time Perception
- Video QA
one_liner: 提出StreamTTT将长程历史写入在线更新的快速权重，缓解流式VLM感知与记忆的权衡
practical_value: '- **长期记忆外部化**：把长程历史压缩到在线更新的快速权重（fast weights）中，避免全部塞入Transformer上下文造成注意力稀释，类似推荐系统中将用户长期兴趣建模在外部参数，短期会话保持滑动窗口。

  - **滑动KV cache只留近期证据**：在实时推荐/流式用户行为建模中，可以只保留最近交互的KV缓存，将长历史沉淀到可更新的小网络，实现低延迟实时推理。

  - **在线更新参数替代全量缓存**：快速权重在线更新机制类似TTT，对用户兴趣漂移建模可尝试用小参数在线学习历史，避免维护超长序列。

  - **混合训练数据构造**：联合离线长视频QA与实时QA训练，启发在电商推荐中混合长期历史序列和实时行为数据进行联合优化，提升长期记忆与实时感知的平衡。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：流式VLM在处理实时视频流时面临感知-记忆权衡：保留短上下文可提升当前场景感知，但牺牲长期记忆；扩充历史上下文又会导致注意力稀释，损害实时理解。

**方法关键点**：
- 将长程历史写入在线更新的快速权重（fast weights），存储在注意力上下文之外，避免占用有限上下文窗口。
- 保留短滑动KV cache专门处理近期证据，减轻注意力稀释。
- 联合训练：使用离线长视频QA和一个新构造的实时QA语料进行优化。

**关键结果数字**：
- 在OVO-Bench上，StreamTTT-4B的实时感知比SimpleStream-4B高1.4点，backward tracing高3.7点。
- 在StreamingBench的Real-Time Visual Understanding (RTVU)子集上，StreamTTT-4B与更大的SimpleStream-8B保持竞争力。
