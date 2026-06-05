---
title: 'Agent Memory: Characterization and System Implications of Stateful Long-Horizon
  Workloads'
title_zh: 智能体记忆：长时状态工作负载的特性与系统启示
authors:
- Yasmine Omri
- Ziyu Gan
- Zachary Broveak
- Robin Geens
- Zexue He
- Alex Pentland
- Marian Verhelst
- Tsachy Weissman
- Thierry Tambe
affiliations:
- Stanford University
- Independent Researcher
- MICAS, KU Leuven
- Massachusetts Institute of Technology
arxiv_id: '2606.06448'
url: https://arxiv.org/abs/2606.06448
pdf_url: https://arxiv.org/pdf/2606.06448
published: '2026-06-04'
collected: '2026-06-05'
category: Agent
direction: 智能体记忆系统设计与部署特征分析
tags:
- Agent Memory
- Systems Characterization
- LLM Serving
- RAG
- Profiling
- Memory Management
one_liner: 首次系统表征智能体记忆工作负载，揭示构建成本主导生命周期，并提出面向部署的十项建议。
practical_value: '- 业务选型时不能只看准确率，需将构建成本、查询延迟、存储增长、能耗等系统指标纳入决策。

  - 将记忆构建作为后台批处理任务，与在线查询分离调度，避免抢占GPU资源影响延迟；根据范式选择合适的批大小。

  - 长生命周期智能体必须引入主动裁剪/遗忘策略，否则存储和token成本会非线性增长；使用合并式记忆系统可抑制膨胀。

  - 根据业务场景的查询频率和历史稳定程度选择记忆范式：高查询率、稳定历史选重构建轻查询系统（如Mem0）；持续流入、低查询率选轻构建系统（如BM25）。

  - 部署LLM控制流的记忆系统时，必须设置最大工具调用轮次或超时，防止检索/构建尾部延迟不可控。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
大模型智能体在长时交互中需要跨会话持久化并检索记忆，已有多种记忆系统方案（平面RAG、结构增强、智能体控制流等），但缺乏系统层面的特征分析。现有评估仅关注下游准确率，掩盖了它们在构建成本、查询延迟、存储增长和能耗上的巨大差异，而这些差异将决定大规模部署的可行性与成本。

## 方法
1. **系统分类**：将智能体记忆系统归入四种范式——长上下文记忆（用上下文保存历史）、平面RAG记忆（无LLM参与，仅分块索引）、结构增强RAG记忆（LLM提取事实/摘要，分为仅追加和可合并子类）、智能体控制流（LLM决定读写时机和工具调用）。选取10个代表性系统（long_context、BM25、embedRAG、GraphRAG、HippoRAG v2、Mem0、SimpleMem、A-Mem、Letta、MIRIX）进行表征。
2. **剖析工具**：构建分阶段探测框架，记录构建、检索、生成阶段的token量、LLM/embedding调用次数、延迟、GPU利用率、功耗等，并区分远程API和本地vLLM部署。
3. **基准测试**：在MemoryAgentBench（多任务长时记忆评估）和MemoryArena（依赖多会话任务）上测试，控制关键变量，如统一生成LLM和嵌入模型，本地实现以测量硬件开销。

## 关键实验与结果
- **构建成本主导**：对于LLM参与的记忆系统，构建耗时为分钟到数小时（SimpleMem约3.9h，Letta约13.3h），能耗远超300次查询的总和。能量/正确答案比值跨系统差超47倍（BM25 ~4.1kJ，Letta ~185.9kJ）。
- **构建工作负载特征**：构建以预填充和嵌入为主，解码token占比中位数仅4.6%。嵌入调用模式分两大阵营：结构化追加系统（GraphRAG等）批量嵌入，合并式/智能体系统（Mem0、MIRIX等）逐条嵌入，造成不同的GPU流量模式。
- **构建–服务–准确率前沿**：没有系统在三个轴同时最优。BM25构建极快、查询慢但综合准确率55.8%，Mem0查询最快（2.2s）但构建耗时长且准确率低（26.8%）。在MemoryAgentBench各类别下，强项各有侧重，ICL和冲突任务差距明显。
- **构建LLM缩放受限**：对于有严格输出协议的系统（如MIRIX），使用过小LLM会导致存储损坏，失效；无硬协议的系统（GraphRAG等）可平滑降级准确率。
- **新鲜度-延迟权衡**：连续会话场景下，构建时间若超过会话间隔，同步调度导致用户可见延迟，异步调度则引入记忆过时。范式IV系统会话构建延迟从秒级到百秒级，BM25仍是毫秒级。
- **存储与成本增长**：单用户历史1M token时，存储差约9倍（~6 MB到~62 MB），但LLM token成本差距更大：智能体系统（Letta、A-Mem）因每次写入都要查询并更新已增长存储，token成本随历史长度超线性增长。
- **尾部延迟**：由LLM决定何时停止检索/构建的系统尾部更宽（p95/p50达3.9–5.9倍），需要迭代上限保护。

## 核心结论
智能体记忆系统不能仅凭准确率选型——其构建代价、查询开销和存储增长构成多目标规划问题，部署时须根据工作负载的写入频率、历史稳定性和延迟SLO匹配不同范式，并将构建与查询分离调度，设置强制遗忘机制以控制长期成本。
