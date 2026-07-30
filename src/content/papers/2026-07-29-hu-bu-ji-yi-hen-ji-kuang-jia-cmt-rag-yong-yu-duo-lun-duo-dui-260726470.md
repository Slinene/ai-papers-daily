---
title: 'CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG'
title_zh: 互补记忆痕迹框架 CMT-RAG：用于多轮多跳对话 RAG
authors:
- Lang Zhou
- Yingjian Chen
- Shuxuan Li
- Kun-Yu Lin
- Zhilin Zhao
affiliations:
- 中山大学
- 深圳循环智能研究院
- 香港大学
arxiv_id: '2607.26470'
url: https://arxiv.org/abs/2607.26470
pdf_url: https://arxiv.org/pdf/2607.26470
published: '2026-07-29'
collected: '2026-07-30'
category: RAG
direction: 对话记忆与检索协同 · 子问题级 trace
tags:
- multi-turn RAG
- trace-based memory
- SSM
- DAG
- conversational QA
- reasoning
one_liner: 用子问题级记忆痕迹对齐对话记忆与检索，通过 SSM+DAG 实现跨轮依赖跟踪和证据复用
practical_value: '- **子问题级记忆单元设计**：在电商对话推荐或搜索中，可借鉴 trace 结构（子问题、关键词、依赖、证据 ID），将用户意图分解为可检索的细化单元，避免全文历史重放导致的上下文稀释。

  - **依赖图驱动的证据复用**：每次对话轮次通过 DAG 节点链接前序推理步骤，直接复用之前检索到的段落 ID，减少重复检索，提升长对话的响应速度与一致性，适合多轮商品对比或参数补充场景。

  - **SSM 生成器替代 Transformer 重编码**：使用 Mamba-2 维护回合级隐状态，将推理时延降低近一半，适合对延迟敏感的在线服务；同时通过课程学习
  + DPO 微调适配特定下游 Reader，可落地到需要结构化计划生成的 Agent 工作流中。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
多轮信息寻求对话需要同时处理多跳推理和跨轮依赖，但现有 RAG 系统通常仅维持对话历史、改写 query 或非结构化摘要，无法精确复用前面的推理步骤和证据，导致模型需要重复检索或丢失关键上下文。本文核心直觉是将对话记忆与检索对齐，把对话上下文表示为子问题级的推理痕迹（trace），让系统能够直接在需要时找回之前的检索单元。

**方法**  
- **互补记忆框架 CMT-RAG**：包含运行时记忆（SSM 状态空间模型）和持久记忆（会话级 DAG）。SSM 基于 Mamba-2，利用其循环状态捕获局部话语连续性，避免全历史重编码。  
- **结构化痕迹生成**：每轮由 SSM 生成若干 trace draft，每个 draft 包含分解后的子问题、trace 关键词及对先前 traces 的依赖列表。  
- **证据解析与复用**：通过依赖边和关键词匹配，从 DAG 中获取历史 trace 的证据 ID，并与当前子问题检索的新证据合并，形成紧凑的段落集合，供下游无状态 Reader 回答问题。  
- **训练**：三阶段课程学习（单轮→短对话→长对话）+ DPO，用复合奖励（最终答案 F1 + 子问题匹配 F1）对齐 trace 生成与检索推理目标。  
- **基准 MuMu-QA**：基于 MuSiQue 构造，显式标注子问题级跨轮依赖和证据，涵盖短/长/超长对话（最大 67 轮）。

**实验**  
在 MuMu-QA 长对话 split 上，CMT-RAG（Qwen3-32B Reader）获得 41.73 EM / 55.63 F1，比最强分解/会话 benchmark 高 5–9 点 EM；所需段落数从 20 降至约 14。SSM 生成器比同规模 Pythia-2.8B Transformer 方式减少 48.4% 端到端时延。消融显示 DAG 在长对话（16–67 轮）中贡献逐步增大，而 SSM 状态维持在所有长度段都贡献突出。跨基准迁移到 RECOR/HotpotQA 等仍保持竞争力。

**一句总结**  
将对话记忆单元从“文本块”升级为“可检索、可链接的子问题痕迹”，是提升多轮多跳 RAG 效率与准确性的关键设计。
