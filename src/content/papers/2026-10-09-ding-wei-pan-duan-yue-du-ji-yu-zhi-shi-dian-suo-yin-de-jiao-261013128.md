---
title: 'Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index
  for Open-Domain Multimodal Document QA'
title_zh: 定位、判断、阅读：基于知识点索引的角色专用工具智能体用于开放域多模态文档问答
authors:
- Wenlin Lin
- Fanzhe Wei
affiliations:
- Metask Lab
arxiv_id: '2610.13128'
url: https://arxiv.org/abs/2610.13128
pdf_url: https://arxiv.org/pdf/2610.13128
published: '2026-10-09'
collected: '2026-10-12'
category: MultiAgent
direction: 角色分工的多 Agent 文档 QA
tags:
- Agentic RAG
- Multimodal QA
- Tool Agents
- Role Specialization
- Document QA
- Knowledge Graph
one_liner: 按任务拆分搜索与阅读智能体、代码强制第二跳，在三个文档 QA 基准上显著超越现有系统
practical_value: '- 搜索与阅读工具物理隔离：在电商商品库/文档客服 Agent 中，可把「找商品/找片段」和「读详情/规格」拆成两个 agent，Reader
  不挂搜索工具，避免模型无限搜而不读；论文显示单 agent 全工具且双倍轮数反而低 1.9 F1。

  - 类型化证据池：多模态业务里图片/表格在文本排序中分数低容易被淘汰；建议按 text/image/table/example 分池并各自设 cap，每次搜索保护
  top-K，合并所有搜索的排名，这能显著保住图表证据。

  - 代码级桥接判断：不要靠模型自己发现缺少第二跳文档；在检索后加一个固定 prompt 检查是否覆盖所有 hop，缺失则定向补搜 1-2 次。在 MultiHop-RAG
  上这是最大单项提升来源，「all evidence found」从 50.6% 升到 65.1%。

  - 轮次预算观察：4+4 后基本平台，延迟主要随模型调用数而非语料规模增长；工程上可设 Locator/Reader 为 cap 上界，让模型提前停，保证首 token
  快。对需要多跳属性补全的推荐解释/导购 Agent 有直接可复制性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：开放域多模态文档问答既要从数千 PDF 中定位证据，又要深度阅读表格/图片；单智能体手握所有工具时会偏好继续搜索而非阅读，因为搜索有即时新结果，阅读没有。KnowForge 主张设计单元是“任务”而非“轮次”。

方法关键点：
- 离线构建混合检索索引：文档转 Markdown 并切分为 text/image/table/example 片段，图片表格由 VLM 生成描述，抽取原子知识点和类型化关系，BM25+稠密检索融合。
- Locator：仅能搜索/枚举，最多 L 轮，物理隔离阅读工具。
- Bridge judge：代码调度，Locator 停止后检查是否覆盖所有 hop；缺失则执行 1-2 次定向补搜，强制第二跳。
- Typed evidence pool：合并所有搜索排名，30K token 上限，按图片 3K/表格 3K/示例 2K 分池，避免文本把图表挤出。
- Deep Reader：仅能阅读（fragment_context/read_media/media_context），最多 R 轮，无搜索工具。
- Synthesizer + format checker 输出基准规定格式。

关键实验：在 M3DocVQA 全量（2441 问/3368 PDF）上 F1 47.5，比 M3DocRAG 36.5 高 11.0，比同索引基线 40.4 高 7.1；换 DeepSeek-V4-Flash 达 53.5。MultiHop-RAG accuracy 73.5，超过 GraphRAG 71.2 与 GPT-4 baseline 56.0。MMLongBench-Doc 上同样 3B active 模型从 34.8 提到 47.0，比肩 GPT-4o 读页图 46.3。消融：Deep Reader 在三个语料分别值 3.8/9.8/0，跟着视觉证据比例走；单智能体全工具且双倍轮数反而低 1.9；混合检索 +2.5，图扩展中性；轮数在 4+4 出现台阶后平台。

最值得记住：文档 QA Agent 的单元应是 job 而非 round；用物理不相交的工具集把“找”和“读”分开，并用代码强制补跳，才能让模型真正读图表而不是继续搜。
