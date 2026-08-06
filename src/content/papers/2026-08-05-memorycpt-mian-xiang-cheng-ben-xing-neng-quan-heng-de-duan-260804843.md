---
title: 'MemoryCPT: An End-to-End Agent Memory Framework for Cost-Performance Trade-off'
title_zh: MemoryCPT：面向成本-性能权衡的端到端Agent记忆框架
authors:
- Songxin Lei
- Kun Ouyang
- Weilin Ruan
- Yuqian Wu
- Zhijiang Guo
- Yushi Sun
- Fugee Tsung
affiliations:
- 香港科技大学
- 香港科技大学(广州)
- 腾讯LIGHTSPEED STUDIOS
- 香港中文大学
arxiv_id: '2608.04843'
url: https://arxiv.org/abs/2608.04843
pdf_url: https://arxiv.org/pdf/2608.04843
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent记忆优化 · 成本与性能权衡
tags:
- agent memory
- cost-performance trade-off
- distillation
- GRPO
- RRF
- QPC
one_liner: 通过离线蒸馏记忆构建 + 在线GRPO摘要优化，在长对话问答中同时提升答案质量并大幅降低推理成本
practical_value: '- **离线记忆构建与在线检索分离**：将记忆压缩为可复用的片段（episodic + semantic），整体记忆构建成本可以在多次查询间摊销，适合电商Agent持续对话或长期用户画像维护，避免每次请求重复处理全量历史。

  - **RRF融合稠密与稀疏检索**：在商品知识库或用户行为记忆中，结合 embedding 和 BM25 两种信号做初步召回，再用 LoRA 摘要器压缩，能有效降低下游
  LLM 的 token 消耗——可直接用于客服意图识别或推荐语生成前的背景筛选。

  - **GRPO 训练成本感知摘要策略**：用加权奖励（F1 + token节省）训练摘要模型，使 agent 学会“用最少且最关键的上下文回答问题”。在电商搜索结果摘要生成或广告文案自动适配中，可以借鉴此方法，在字数限制下优化信息含量。

  - **QPC 指标量化智能密度**：在评测推荐解释、Agent 回答或 query 扩展时，除看准确率，也应关注单位推理成本的产出，便于在工程上做模型选型与预算控制——尤其是当需要高频调用大模型时。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
长对话 Agent 需要从大量历史中提取关键证据，但现有记忆管道多依赖手工启发式及多次 LLM 调用，导致推理成本高且冗余上下文多。缺少端到端可训练框架，既要压缩历史构建记忆，又要在线按需检索与压缩，且需显式优化成本-性能权衡。

**方法关键点**  
- **两阶段可训练流水线**：离线 **Query-Agnostic Distillation (QAD)** 将模块化记忆构建链路（分段、生成片段、合并、语义提取）蒸馏到 LoRA-A，训练时使用教师推理轨迹（reasoning trace），学生输出结构化 JSON；在线 **Query-Aware Retrieval and Summarization (QAR)** 先通过 RRF 融合稠密嵌入与 BM25 进行粗检索，再用 LoRA-B 摘要器生成查询相关摘要。  
- **GRPO 训练摘要策略**：状态 = 查询 + RRF 候选，动作 = 摘要 token 序列，奖励 = α × F1 + (1-α) × (1 - 归一化成本)，用组相对优势优化 LoRA-B。  
- **成本建模**：在线成本计入摘要器和下游 QA 模型的 token 费用，训练时代理信号归一化至 [0,1] 与 F1 对齐。  
- **评价指标 QPC**：F1 / 平摊总成本，衡量单位推理成本的答案质量。

**关键结果**  
在 LoCoMo 和 LongMemEval 上，使用 Qwen2.5-7B 做记忆处理、Qwen3-14B 做最终 QA。MemoryCPT (α=0.8) 取得 LoCoMo F1 0.479 / Judge 0.755 / Cost 4.31 ×10⁻⁴ USD / QPC 0.111，相比 BudgetMem 成本降低近 7 倍，QPC 提升 9 倍以上；比 No-Memory 的 F1 提升 50%，成本下降 61%。消融实验显示去掉精炼摘要（FS）后，Cost 从 4.31 升至 8.35，QPC 从 0.111 降至 0.053，说明成本感知的 GRPO 摘要是实现权衡的核心。检索深度分析表明 top-20 情节+top-50 语义回忆已近最优，继续增加会引入噪声。

**最值得记住的一句话**  
“MemoryCPT 表明，将记忆构建拆分为离线蒸馏与在线成本感知摘要，并联合训练，能让长对话 Agent 在极低成本下获得高质量回答——关键不是追求最高 F1，而是最大化每美元的信息产出。”
