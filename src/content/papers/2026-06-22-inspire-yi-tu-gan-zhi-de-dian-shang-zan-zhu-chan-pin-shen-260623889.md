---
title: 'INSPIRE: Intent-aware Neural Sponsored Product Retrieval for E-commerce'
title_zh: INSPIRE：意图感知的电商赞助产品神经检索框架
authors:
- Shasvat Desai
- Hong Yao
- Utkarsh Porwal
- Kuang-chih Lee
affiliations:
- Walmart Global Tech, USA
arxiv_id: '2606.23889'
url: https://arxiv.org/abs/2606.23889
pdf_url: https://arxiv.org/pdf/2606.23889
published: '2026-06-22'
collected: '2026-06-24'
category: RecSys
direction: 意图感知检索 · 赞助搜索
tags:
- intent-aware retrieval
- sponsored search
- knowledge distillation
- LoRA
- bi-encoder
- grocery e-commerce
one_liner: 通过多LLM共识生成结构化意图标签，蒸馏轻量模型并注入双编码器，显著提升购物搜索中隐式意图的检索质量
practical_value: '- 意图弱监督标注管道：用多个大模型（如Gemma、LLaMA、Qwen）生成结构化意图，交叉共识后蒸馏到小模型（Phi-4-mini
  + LoRA），可直接复用于商品理解或query解析。

  - 意图增强检索双编码器：将预测的意图字段（品牌、口味、饮食偏好等）拼接到query/item文本后训练，用cosine regression + MNR loss联合优化，能有效抑制“语义相似但意图冲突”的bad
  case，适合迁移到召回或相关性排序。

  - 工程部署思路：离线用vLLM批量推断所有item的意图并存入索引，线上对高频query做缓存增强，新增的query使用轻量模型实时预测，平衡效果与延迟。

  - 评估协议：用级联相关模型（Gemma-1B→2B→LLaMA-3 8B）自动标注QIP相关度分数，结合用户行为信号作为训练监督，可减少人工标注成本，在自有数据集上复用。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：Walmart 的生鲜杂货搜索中，大量查询包含未明说的饮食限制（gluten-free、dairy-free）、品牌认知或烹饪类型等隐式意图。传统语义匹配容易检索出字面相似但意图冲突的商品（如搜“paella rice”返回Arborio米），导致用户体验与广告主投放回报双输。赞助位有限，对意图精度要求更高。

**方法**：
1. **意图标注生成**：从生产日志挖掘失败QIP，用Gemma-27B、LLaMA-3.1-8B、Qwen3-8B等教师模型生成结构化意图字段（brand, dietary_preference, flavor, cuisine_type 等），通过交叉模型共识（token overlap>0.5或embedding cos>0.3）保留高置信标签，并用GPT-4.1二次验证。
2. **蒸馏部署**：用共识标签对 Phi-4-mini-instruct 做 LoRA SFT（lr=4e-4, 3 epochs），得到可规模化推断意图的学生模型，在商品端P/R均超0.95，查询端P=0.91/R=0.93。
3. **意图增强检索**：将预测意图字段拼接到原始query/item文本后，训练MiniLM双编码器，损失=MultipleNegativesRanking + cosine regression（目标为相关度+行为信号混合评分）。

**关键结果**：在12000个混合流量查询的离线评估中，意图感知模型相较基线：Avg relevance@10 +2.38%，Precision@1 +4.2%，NDCG@10 +2.64%；"Embarrassing"结果（严重不匹配）减少50%。案例显示添加意图字段后，原先被错误排高的冲突商品得分被明显压低。计划后续上线A/B测试。
