---
title: 'Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled
  Cross-Encoders and Agentic VLMs'
title_zh: 检索-匹配-升级：VLM蒸馏交叉编码器与Agentic VLM商品链接
authors:
- Jian Wang
- Steven Xu
- Sanjyot Thete
- Maryam Barouti
- Tom Tang
- Elaine Wu
- Charu Sareen
- Kyle MacDonald
affiliations:
- DoorDash Inc.
arxiv_id: '2608.25037'
url: https://arxiv.org/abs/2608.25037
pdf_url: https://arxiv.org/pdf/2608.25037
published: '2026-08-25'
collected: '2026-08-27'
category: Agent
direction: 商品实体解析 · 检索-匹配级联
tags:
- entity resolution
- product linking
- cross-encoder
- VLM distillation
- agentic VLM
- adaptive cascade
one_liner: 用VLM共识标签蒸馏轻量交叉编码器，并把困难尾部升级给自托管Agentic VLM，实现按难度路由的商品链接
practical_value: '- 难度路由级联：用 cheap text-only cross-encoder 产出 calibrated score，设 HIGH/LOW
  双阈值，只把 MEDIUM 升级给昂贵 VLM；成本差可达 4 个数量级，端到端覆盖从 68.1% 提升到 77.1%。

  - 标签飞轮：dual-VLM consensus 自动生成训练标签（保留 87% 一致、丢弃 13% 不一致），5.3M 标签替代 40k 人工标注，放大 130×；业务上可先让闭源
  VLM 产生伪标签，再用 ops 审计校准。

  - 特征工程与修复：原始 barcode digits 直接进 cross-encoder 比 [BARCODE_MATCH] 标志更好（+0.8pp F1），但需防
  rare collision：用 barcode dropout + name-similarity guardrail + 合成同 barcode 冲突 name
  对，再以 guardrailed teacher 蒸馏学生，把 stress audit R@P98 从 0.200 拉到 0.768。

  - Agent 部署与评测：自托管 open-weight MoE VLM 替代 closed frontier，同精度成本 1/7，recall 仅 -4pp；通过
  MCP 解耦 search backend、限制 tool loop ≤4 轮、加同零售商证据/空搜索 inconclusive addenda 稳定行为；同时主动构造对抗性子分布，补足
  held-out 看不到的稀有失败。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Marketplace 商品链接是把商户 SKU 映射到 canonical catalog 商品的实体解析任务，直接影响下游搜索、推荐、广告的 item 信号干净度。规模达到数十亿商户记录 vs 数千万 canonical 商品，噪声、多品类、多语言；统一用重型多模态模型太贵，轻量模型又处理不了困难尾部，因此需要按难度路由的计算级联。

## 方法关键点
- 三阶段级联：检索（text/image/GTIN ANN 融合，top K=20）→ 轻量 ModernBERT-base text-only cross-encoder（150M）→ agentic VLM。Cross-encoder 输出 calibrated score，按双阈值分 HIGH 自动接受、LOW 自动拒绝、MEDIUM 升级。
- 标签：用 dual-VLM consensus 构造 5.3M 训练 pairs，保留两个 VLM 一致 87%，丢弃 13% 不一致，取代 40k 人工标注，扩大 130×。
- Agent：自托管 open-weight MoE VLM Qwen 3.6 35B-A3B FP8，支持图片和网页搜索，最多 4 轮 tool loop，输出 JSON 决策；search backend 通过 MCP 解耦。
- 成本阶梯：cross-encoder 1x，open-weight agent ~7,000x，closed frontier VLM ~50,000x；仅 MEDIUM 升级。

## 关键实验
- 检索 dedup-slice recall 93.06%，加 BM25 到 94.10%，换 Gemini Embedding 2 到 94.27%；image 单通道仅 0.40%，基本无唯一增量。
- Cross-encoder held-out 6k：AP 0.964，F1 0.896，R@P98 77.05%；ops-certified audit 24k 中 HIGH band auto-accept 43.7% @98% precision，95% barcode-matched true links 进 HIGH。
- Agent vs 人类操作员在 hard medium-confidence 上：accuracy +13.7 pp，recall +18.5 pp，precision +4.7 pp（p<0.0001）；open vs closed 在 98% precision 下 recall 88% vs 92%，成本 1x vs 7x。
- 端到端生产覆盖：cheap stage 单独 68.1%，升级 agent 后 77.1%，+9.0 pp。
- 对抗性审计：barcode collision stress audit，raw barcode tokens R@P98 0.200 → dropout+guardrail+distillation 0.768。

## 最值得记住的一句话
用双 VLM 共识自动产标签、把昂贵推理蒸馏进 cheap cross-encoder、只把困难中间带升级给 agent，是规模化商品链接的可持续路径；同时必须构造对抗性子分布，才能暴露聚合指标看不到的稀有失败。
