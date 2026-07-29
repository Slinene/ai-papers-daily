---
title: 'A New Role for Relevance: Guiding Corpus Interaction in Agentic Search'
title_zh: 相关性新角色：引导智能搜索中的语料交互
authors:
- Jiangnan Li
- Yuqing Li
- Mo Yu
- Jinchao Zhang
- Jie Zhou
affiliations:
- Tencent
- Institute of Information Engineering, CAS
arxiv_id: '2607.24223'
url: https://arxiv.org/abs/2607.24223
pdf_url: https://arxiv.org/pdf/2607.24223
published: '2026-07-26'
collected: '2026-07-29'
category: Agent
direction: 相关性引导的语料库交互代理
tags:
- Relevance-Aware Search
- Agentic Search
- Ripgrep
- Coarse-to-Fine Guidance
- Search Convergence
- Dense Retrieval
one_liner: RARG 将检索相关性转化为 grep 遍历的文档顺序与匹配片段重排信号，以更少交互步数提升搜索收敛效率
practical_value: '- **把相关性当作执行先验，而不是证据通道**：在电商搜索 Agent 中，可以用稠密检索对商品池做文档级排序，让 grep/关键词匹配按此顺序遍历，使高相关商品优先被检索，减少无效扫描。

  - **提供入口点初始化加速收敛**：为 Agent 提供少量 top 相关段落作为启动线索，避免冷启动时的盲目搜索，可类比在推荐对话系统中先给出若干候选商品摘要，快速进入验证阶段。

  - **匹配级重排弥补文档级排序的粒度不足**：当关键词匹配输出被截断时，用嵌入模型对匹配片段重排，使埋在低排名文档中的关键信息也能暴露给 LLM，可在商品标题/详情片段高频匹配的场景下保留重要长尾证据。

  - **利用工具设计约束引导模型行为**：通过引入 `embed_recall` 工具和 scope 文件，将多步检索显式化为有序管道，避免模型滥用耗时的全量遍历命令（如
  `ls`/`find`），该模式可用于约束 Agent 在大量候选中进行有序探索。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**  
检索增强生成（RAG）用相关性排名提供 top-k 文档，但文档级相关性与证据可用性并不等价，多跳推理或精细定位时，关键线索可能被截断或埋没。直接语料交互（DCI）允许 grep 式特设搜索，但缺乏全局优先级，搜索结果出现晚、收敛慢。既有改进用检索先缩小搜索空间，却未在交互中继续利用相关性信号。本文提出让相关性贯穿交互执行：决定 grep 扫描文档的顺序，并重排匹配输出以控制 LLM 可见片段，从而加速搜索收敛。

**方法关键点**  
- **文档级相关性注入**：新增 `embed_recall` 工具，接收 Agent 生成的查询，将排序后的文档路径写入 scope 文件；要求 cat scope 后按顺序执行 `rg -j1`，强制单线程顺序扫描，使高相关文档的匹配优先出现。  
- **入口点初始化（RARG+）**：从 scope 的 top 文档中抽取段落，用嵌入模型评分，选出 top-10 相关段落作为提示，为 Agent 提供起始搜索线索。  
- **匹配级重排（RARG++）**：捕获 scope 查询与 rg 模式的关键词，拼成重排查询，对 rg 的宽匹配池（M=500）做嵌入排序，只展示 top-m，防止无关匹配挤占预算，并让低排文档中的关键段落有曝光机会。  
- **上下文管理**：截断单工具结果，保留最近 40 条工具结果，其余替换为占位符，维持有限上下文窗口。

**关键实验**  
在 BrowseComp-Plus（100 查询，100K 文档）上：GPT-5.4-mini 下 RARG++ 准确率 84%，较 RISE 和 DCI 的 78% 提升 6 个百分点，平均工具调用 23.9 次，而 DCI 需 99.1 次；扩展到 1M 文档时，RARG++ 仍保持 79%，较 RISE-BM25 高 10 个百分点。在推理密集型 BRIGHT 检索中，RARG+ nDCG@10 平均 53.36，优于专项检索代理 NeMo（52.89）。行为分析证实：文档级排序使命中集中在前排，匹配重排则从低排文档回收证据。
