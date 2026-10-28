---
title: 'Memory Tax: Dissecting the Net Value of Agent Memory'
title_zh: 记忆税：剖析 Agent 记忆相对直接检索的净价值
authors:
- Xuan He
- Sining Zhoubian
- Ruozhen Yang
- Yuhao Wen
- Zhineng Wang
- Yuyang Hu
- Ke Yang
- Yuyu Zhang
- Ping Nie
- Jiawei Han
affiliations:
- University of Illinois Urbana Champaign
- Tsinghua University
- Renmin University of China
- Verdent.ai
- University of Waterloo
arxiv_id: '2610.34073'
url: https://arxiv.org/abs/2610.34073
pdf_url: https://arxiv.org/pdf/2610.34073
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent 记忆净价值与记忆税拆解
tags:
- Agent Memory
- RAG
- Memory Tax
- LLM Agents
- Evaluation
- Long-horizon
one_liner: 大规模评测发现多数 Agent 记忆系统不如 naive RAG，提出记忆收益与记忆税拆解净价值
practical_value: '- 在电商/推荐 Agent 的用户长期记忆、会话记忆或经验记忆项目中，先把 naive RAG 作为强制 baseline；很多专用记忆在
  retrieval-friendly 任务上会被简单 BM25+embedding+rerank 打败，若无法显著超过 RAG，就不值得上复杂记忆架构。

  - 保留一条从记忆回到原始日志/会话的“可恢复路径”：构建 memory 时同时从原始历史检索并联合 rerank，能补回构建阶段丢失或模糊的证据；实验中 SimpleMem
  加 src-aug 后 LongMemEval-s 准确率从 73.6 提升到 82.8，memory tax 从 12.0 降到 5.2。

  - 把“未来查询需求”当作隐式推荐问题：不要 AOT 全量预构建，利用用户历史兴趣/访问模式/偏好作为先验，选择性地对可能被未来 query 需要的信息做抽象与索引；这类似推荐系统中预估
  item/信息未来相关性。

  - 记忆系统要报告检索成本与原始 RAG 的 headroom；在电商/Agent 检索友好场景下，复杂记忆的增量收益有限，轻量或 JiT memory 可能是更高性价比的选择。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

长期 Agent 中记忆模块越来越复杂，但大多数工作只与其他记忆系统对比，很少把 naive RAG 作为 baseline。这导致“建记忆”的边际价值与检索本身的价值混在一起，净价值不清晰。

**方法关键点**

- 以 naive chunk-based RAG 为参照，将记忆的净价值拆为 **memory benefit** 和 **memory tax**：记忆系统解决了 RAG 未解决的 query 是收益，丢失/模糊了 RAG 已解决的 query 是税。
- 在 LongMemEval-s、PersonaMem-v2、MINT-Eval 三个个人 Agent 记忆 benchmark 上评测 flat、hierarchical、graph、trained policy 等代表性记忆系统，使用 Qwen3.5-4B、Qwen3.6-27B、GPT-5.6 Luna(low) 三个 backbone。
- 为公平比较，通过 Retrieval Scope 对齐 top-k 检索预算。
- 从 faithfulness、accessibility、robustness 和 benchmark headroom 四个维度解释 memory tax 来源：构建期信息丢失或扭曲、证据分散/稀释/改写导致更难检索、跨 backbone 更脆弱、部分 benchmark 中 naive RAG 已经接近上限。
- 将概念推广到 experiential memory 和 world-model memory，并提出 source-augmentation、recursive memory、面向未来需求的记忆构建等设计建议。

**关键结果**

在 LongMemEval-s 上，Qwen3.6-27B 的 RAG(2rd) 达到 81.4%，而 SimpleMem 仅 73.6%、OpenViking 58.8%；在 PersonaMem-v2 上 RAG(2rd) 为 48.7%，多数记忆系统低于或接近该值。加入 source-aug 后，SimpleMem 在 LongMemEval-s 上从 73.6 提升到 82.8，memory tax 从 12.0 降到 5.2。

**最值得记住的一句话**

记忆不是天然增益，而是对原始历史的双刃偏差；评估记忆系统时必须同时报告相对 naive RAG 的净价值和记忆税。
