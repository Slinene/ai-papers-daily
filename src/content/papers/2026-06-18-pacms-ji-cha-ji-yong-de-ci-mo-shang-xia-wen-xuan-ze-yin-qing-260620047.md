---
title: 'PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents'
title_zh: PACMS：即插即用的次模上下文选择引擎，提升长会话LLM Agent问答
authors:
- Manu Ghulyani
- Arunabh Singh
- Karan Bharadwaj
- Ankit Nath
- Suranjan Goswami
affiliations:
- Nasiko
arxiv_id: '2606.20047'
url: https://arxiv.org/abs/2606.20047
pdf_url: https://arxiv.org/pdf/2606.20047
published: '2026-06-18'
collected: '2026-06-19'
category: Agent
direction: Agent 上下文管理 · 次模优化
tags:
- context-management
- submodular-optimization
- LLM-agents
- memory
- pluggable-engine
- facility-location
one_liner: 提出基于设施选址次模函数的上下文选择方法，在保持回忆的同时将LLM Agent端到端QA准确率提升8~12个点
practical_value: '- **电商对话Agent的长上下文管理**：电商客服、导购Agent的会话会累积商品信息、用户意图、工具调用结果，PACMS的做法可直接移植：将所有来源（记忆、对话、API响应）统一为一个候选池，每次模型调用时根据最新查询做子模覆盖选择，优先保留与当前需求最相关的信息，丢弃冗余。

  - **推荐解释/文案生成中的上下文压缩**：在生成推荐理由或广告文案时，需从大量用户行为、商品属性中筛选关键句，可使用类似设施选址覆盖的贪心选择，在 token
  预算内最大化覆盖相关属性，同时自动剔除重复表述。

  - **插件化设计支持策略A/B测试**：PACMS将上下文选择实现为可替换的引擎插件，通过本地HTTP服务暴露接口，支持多种策略（PACMS、MMR、top-k、last-k）。这种做法可直接照搬，让搜索推荐Agent的上下文组装逻辑与主框架解耦，便于线上快速切换和效果评估。

  - **工程优化技巧**：嵌入向量缓存常驻服务、失败时回退到简单策略（soft fail）、成本感知的贪心近似，这些实现细节对构建稳定低延迟的在线服务具有参考价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM Agent 在长会话中会积累大量上下文（对话历史、持久记忆、工具调用输出），很容易超出模型的 token 预算。主流的最近性截断是主题盲目的，它会丢弃旧但相关的事实，却保留最近但不相关的噪声。现有的 RAG 或压缩方法要么只关注外部检索，要么是查询无关的有损压缩，没有在提示组装的那一刻，从整个候选池中按相关性进行筛选。因此，需要一个预算感知、查询相关且能自动剔除冗余的上下文选择策略。

## 方法关键点
- **选择目标**：将候选池中的所有项目（记忆条目、对话轮次、工具输出）加权为查询相关的覆盖问题，采用设施选址（facility-location）次模函数，最大化覆盖所有查询相关区域，同时惩罚冗余。
- **算法**：使用 CELF 懒惰贪心，在 token 预算约束下获得常数因子近似解。与 MMR 的成对惩罚不同，PACMS 的覆盖奖赏是对整个候选池求和，并由每个目标项的相关性加权，因此更具全局视野。
- **系统集成**：作为 OpenClaw Agent 框架的可插拔上下文引擎，通过本地 FastAPI 服务（/select）提供选择功能，嵌入向量缓存在服务生命周期内保持温热，避免冷启动；失败时自动回退为最近性截断。
- **多策略对比**：内置了 PACMS、top‑k、MMR、last‑k、RAG 五种策略，共享嵌入和 token 估计，确保差异仅来自策略本身。

## 关键实验
在 LongMemEval 的 100 个问题上注入模板冗余（R=0,2,4,8），评估不同预算（20%, 45%, 70%）下的证据轮次-回忆和端到端 QA 准确率。
- 证据回忆：低预算（20%）时 PACMS 不及 top‑k，但在 45% 和 70% 预算下，PACMS 与 MMR 追平并最终超越 top‑k（如 R=8, 45% 预算时 PACMS 0.972 vs top‑k 0.940）。
- **核心结果**：在 45% 预算、R=2 的 QA 测试中，PACMS 以 52.0% (GPT-5-mini) 和 68.0% (GPT-5.4-mini) 的准确率领先所有预算约束方法，比 MMR 分别高出 8 和 12 个百分点，甚至比 evidence recall 更高的 top‑k 也高出 2~4 个百分点。这表明设施选址覆盖生成的下游阅读器更容易提取的提示，而不是仅仅恢复证据。
- 最近性截断在冗余下崩溃（各预算下 last‑k 接近 0），且更强的阅读器也无法弥补其错误选择。

**值得记住的一句话**：查询感知的全局覆盖选择比成对去重更能让模型从长上下文中高效提取答案——PACMS 在证据回忆与 MMR 持平的情况下，将端到端 QA 准确率最高提升 12 个点。
