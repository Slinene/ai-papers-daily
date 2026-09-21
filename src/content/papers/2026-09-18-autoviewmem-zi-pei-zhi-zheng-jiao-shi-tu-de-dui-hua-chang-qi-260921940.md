---
title: 'AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term
  Memory'
title_zh: AutoViewMem：自配置正交视图的对话长期记忆框架
authors:
- Zijie Cao
- Xijun Qu
- Zhicheng Gu
- Xiaoshu Chen
- Duanyang Yuan
- Yanning Hou
- Sihang Zhou
- Jianxing Gong
- Jian Huang
- Yang Mei
affiliations:
- National University of Defense Technology
arxiv_id: '2609.21940'
url: https://arxiv.org/abs/2609.21940
pdf_url: https://arxiv.org/pdf/2609.21940
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 长期记忆 · 多视图写入组织
tags:
- long-term memory
- multi-view memory
- retrieval
- LLM agents
- DPP
- memory consolidation
one_liner: 在写入时用自配置低重叠语义视图组织长期对话记忆，使简单 top-K 检索即可稳定找到相关证据
practical_value: '- 对电商导购 / 客服 Agent 的用户长期记忆，不要把所有对话日志压成一个 embedding；可借鉴 AutoViewMem
  用多个语义视图（如偏好、预算、物流、售后、家庭结构）在写入时抽取结构化字段，降低后续检索的语义干扰。

  - 视图选择可用 DPP 做低重叠、多样化的轻量 schema 选择：每 N 个会话块让 LLM 候选生成视图，再用同一 dense encoder 嵌入并选
  top-K，工程成本可控，且能动态适应用户专属画像。

  - 检索评估必须按 provenance / 证据 ID 去重，否则同一证据在不同视图下重复命中会虚高；落地时给每条记忆打 timestamp、view tag、source
  span ID，便于审计、回滚和线上诊断。

  - 离线 consolidation 可用 embedding 相似度构图 + LLM 裁决合并冗余，但要保留 provenance 并谨慎处理时间版本与冲突；可异步执行，不改变在线检索链路，适合
  Agent 长期记忆增量化维护。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机

长期对话中，偏好、事件、约束、时间更新等异构信息往往混合在同一条 span 里。若把这种混合内容写入单一表示，语义无关信息会在相似度检索时互相干扰，导致 top-K 检索出现盲区，相关证据排不上来。AutoViewMem 认为，检索失败不只是粒度问题，更是表示组织问题：应把语义解耦从检索时前移到写入时。

## 方法关键点

- 定义「视图」为轻量 schema：包含名称、槽位、抽取模板，用于指导 LLM 从对话中抽取结构化记忆。
- 在线阶段：每 50 个 chunk 让 LLM 提出 10 个候选视图；用同一 dense encoder 嵌入后，通过 DPP 选择 K=10 个低重叠、互补的视图，再扩展 top-30 邻居并总结为 canonical 抽取指令。
- 写入阶段：对每个 chunk 按活跃视图分别抽取事实，仅当证据与该视图相关时才写入；同一证据可投影到多个视图，但每条记忆带 view tag、timestamp、provenance。
- 检索阶段保持简单：单一向量索引、标准 top-K dense retrieval，不引入路由或迭代检索；评估时按 provenance identity 去重。
- 离线 consolidation：先 hash 去重，再以 cos≥0.9 构图聚类，由 LLM 按 Containment / Complementarity / Independence 三种关系裁决是否合并，提升紧凑性与一致性。

## 关键实验

在 LoCoMo 1,540 问题与 PersonaMem-32k 589 选择题上，用 Qwen3-8B / 14B 评测。LoCoMo 8B 下 AutoViewMem 总体 Judge 0.837，14B 下 0.853，超过 A-mem、Mem0、MemGAS、MemoryBank 等外部记忆基线；PersonaMem-32k 14B 下总体准确率 69.10，比最强基线 A-mem 高 5.77 分，比 Full-History oracle 高 13.92 分。消融显示：去掉多视图仅保留结构化抽取，Judge 降至 0.774；去掉 consolidation 后 no-positive rate 从 5.14% 升至 9.83%，说明多视图组织与冗余清理都很关键。

最值得记住的一句话：在 Agent 长期记忆中，把语义解耦从检索时前移到写入时，用低重叠多视图组织证据，才能让简单 top-K 检索稳定命中相关记忆。
