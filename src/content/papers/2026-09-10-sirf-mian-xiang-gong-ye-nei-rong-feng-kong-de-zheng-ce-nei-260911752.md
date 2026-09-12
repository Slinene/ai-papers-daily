---
title: 'SIRF: A Spec-Internalized Risk Foundation Model for Industrial Content Risk
  Control'
title_zh: SIRF：面向工业内容风控的政策内化风险基础模型
authors:
- Suwan Wu
- Yumeng Lin
- Pengcheng Yuan
- Xiaolong Jiang
affiliations:
- Xiaohongshu Inc.
- Tianjin University
arxiv_id: '2609.11752'
url: https://arxiv.org/abs/2609.11752
pdf_url: https://arxiv.org/pdf/2609.11752
published: '2026-09-10'
collected: '2026-09-12'
category: LLM
direction: 内容风控 · 政策内化基础模型
tags:
- Content Risk Control
- Foundation Model
- Continued Pretraining
- Policy Internalization
- Low Latency
one_liner: 通过约70M token小规模CPT将复杂政策内化到8B模型，在verdict-only低延迟下将Black Recall@P95提升15.1pp
practical_value: '- 政策/规则内化到模型权重而非仅用RAG或prompt，适合高精度+秒级延迟场景：电商/广告审核、平台治理可参考EntiGraph+MAGA
  rewriting+账号级CoT自动合成领域规则语料，对底座做几十M tokens小规模CPT再SFT，在verdict-only输出下获得提升，避免检索延迟。

  - 同源对照实验值得借鉴：控制变量隔离CPT贡献，只让policy-grounded CPT一个因素变化，避免把能力提升误归于SFT或提示词，适合业务团队做严格归因。

  - verdict-only+logprob可落地为树模型裁决层：模型输出logprob作为置信度，高精度自动处置，边界样本交给树模型校准，可恢复误伤样本；电商处罚/营销触达等高风险场景可复用该部署结构。

  - 规则频繁变更时，用低成本合成语料+小规模CPT迁移到新场景，能大幅降低误伤率；对电商季节性/区域合规策略更新有直接迁移价值。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：工业内容风控的关键约束不是平均准确率，而是在高精度和秒级延迟下能自动处置多少风险。账号级风险识别面临上百条政策、异构多源特征、秒级全账号视角判定，且业务策略频繁变化。

**方法**：SIRF将平台复杂政策通过EntiGraph、MAGA rewriting和账号级CoT自动合成CPT语料，无需额外人工标注；用继续预训练把政策内化到8B模型权重，再SFT为verdict-only低延迟输出。同源对照中，Qwen3-8B-SFT与SIRF-8B-SFT注入相同政策、输出形式一致，唯一差异是policy-grounded CPT，从而归因内化收益。

**结果**：SIRF-8B-SFT达到71.3% Black Recall@P95，比基线提升+15.1pp，仅用约70M CPT tokens且不损害通用能力；在logprob可用模型中达到或超过更大系统。线上部署为树模型裁决层，误伤样本恢复增加20%；迁移到冻结场景相对误伤率降低约70%。
