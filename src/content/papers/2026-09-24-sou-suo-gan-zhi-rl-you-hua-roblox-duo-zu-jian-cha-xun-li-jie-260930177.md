---
title: Search-Aware Reinforcement Learning for Multi-Component Query Understanding
  in Roblox Game Search
title_zh: 搜索感知 RL 优化 Roblox 多组件查询理解
authors:
- Nayoung Choi
- Shengjian Chen
- Xiaokai Wei
- Wenzheng Zhang
- Daiyao Yi
- Rachit Pareek
- Vincent Su
- Michelle Gong
- Jinho D. Choi
affiliations:
- Emory University
- Roblox Corporation
arxiv_id: '2609.30177'
url: https://arxiv.org/abs/2609.30177
pdf_url: https://arxiv.org/pdf/2609.30177
published: '2026-09-24'
collected: '2026-09-25'
category: QueryRec
direction: 生成式Query理解·搜索感知RL
tags:
- Query Understanding
- Search-Aware RL
- RLAIF
- GR-DPO
- LLM Distillation
- Production Search
one_liner: 蒸馏+搜索感知RL，按查询组件给 live search reward，2B/4B小模型超过大模型教师并提升下游搜索
practical_value: '- 对电商/广告搜索 query 理解，可直接复用「一个生成模型输出多组件 JSON 计划 + 每个组件按线上搜索反馈单独给 reward」的框架；SFT
  先用大模型蒸馏保证 schema 正确，再上 RL，能训出满足线上延迟的小模型。

  - 用于 query 扩展/改写：给每个 fanout query 单独跑线上检索，计算 LLM-judged NDCG，并加搜索重叠 + 词面重叠惩罚，能有效抑制冗余扩召回；这个打分公式可直接迁移到电商搜索的
  query expansion / 推荐 query 生成。

  - 多 reward 场景优先用 offline groupwise preference（GR-DPO），而不是 on-policy GRPO；因为组件 reward
  存在可逃逸的 N/A（intent=none、不生成 fanout），on-policy 会学歪，而固定池 offline 更稳定。若必须 on-policy，需加最低生成约束或强制覆盖。

  - 不需要人工标注的 reward 全部来自 live 引擎 + LLM judge，但 train/eval 要用不同 version judge，避免过拟合
  judge；线上 shadow 部署后可用行为 GT 持续评估。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Roblox game search 的 query understanding（QU）需要输出结构化 JSON，包含 intent、normalized_query、fanout_queries、negative_terms、attributes 等组件，直接驱动下游 retrieval/rerank。静态标签训练无法感知组件与搜索引擎的真实交互，而单一端到端 reward 在多组件场景存在信用分配不足，因此需要 search-aware 且组件分解的 RL 信号。

### 方法关键点
- 两阶段范式：SFT 蒸馏（teacher LLM -> Qwen3.5 2B/4B，LoRA），再用 RL 优化。
- QU 输出为 JSON，组件字段与搜索机制耦合：intent 选路由，normalized_query/fanout_queries 做语义匹配，attributes/negative_terms 做过滤和重排。
- 七项 reward：r_fmt、r_search、r_norm、r_int、r_fan、r_attr、r_neg；全部不依赖人工标签，由 live 搜索执行 + LLM judge 评分；N/A 组件不计入均值聚合。
- r_fan 对每个 fanout lane 计算 NDCG，并扣掉与 normalized-query/其他 lane 的搜索重叠和词面重叠；r_attr 按 11 个 attribute slot 算 F1；r_neg 检查排除词。
- RL 算法对比：offline DPO/GR-DPO 稳定；on-policy GRPO 会利用逃逸口（intent=none、不生成 fanout），GDPO 虽消除但排名退化。采用 GR-DPO，每 query 从 SFT 策略预采样 8 个 completions，组内 reward 排序构造 soft preference。

### 关键实验
数据 16,100 条：7,624 真实日志（有行为 GT）、2,650 catalog 合成、5,826 attributes 合成；split 7:1:2；RL 只用 2,000 条固定池。SFT 将 format validity 从 0.1%/0.8% 提到 98.9%/99.3%。RL 后 Qwen 4B NDCG@20 从 45.2 到 54.1（+8.9），MRR@20 从 42.1 到 50.9（+8.8），超过 teacher 的 39.5/36.6；2B 同样提升。单 reward 只能到 NDCG@20 50.6，低于复合 reward 的 54.1。线上 2B 模型 p50<200ms、p99<400ms，QPS 比 teacher 高 6 倍以上。

### 最值得记住的一句话
把 QU 的每个结构化组件当独立 operational unit，用 live search 结果给每个组件单独 LLM-judge reward，而不是一个端到端 reward，能让小模型超过大 teacher，并把下游 NDCG@20 推高 8.9 点。
