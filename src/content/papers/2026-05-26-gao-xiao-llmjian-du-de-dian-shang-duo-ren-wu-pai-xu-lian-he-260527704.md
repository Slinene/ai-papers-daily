---
title: Joint Optimization of Relevance and Engagement in Multi-Task Ranking for E-Commerce
  with Efficient LLM Supervision
title_zh: 高效LLM监督的电商多任务排序：联合优化相关性与参与度
authors:
- Luming Chen
- Jiaqi Xi
- Raghav Saboo
- Kenny Chi
- Martin Wang
- Sudeep Das
- Danny Nightingale
- Aditya Dodda
- Elyse Winer
- Akshad Viswanathan
affiliations:
- DoorDash Inc.
arxiv_id: '2605.27704'
url: https://arxiv.org/abs/2605.27704
pdf_url: https://arxiv.org/pdf/2605.27704
published: '2026-05-26'
collected: '2026-05-28'
category: RecSys
direction: 多任务排序 · 序数相关性 · LLM监督
tags:
- multi-task learning
- e-commerce search
- relevance ranking
- LLM supervision
- ordinal relevance
- value model
one_liner: 用LLM离线生成三级序数相关性标签，通过序数头融入多任务排序价值函数，实现相关性与参与度的可控权衡
practical_value: '- **高质量相关性监督的规模化方案**：使用大量人审数据 + 行为信号审计/校正（如高转化但人为标为不相关的样本用大LLM复核），再微调轻量LLM（GPT-4o-mini）批量生成亿级序数标签。标签分布需对齐线上真实比例以稳定分类行为。可直接复用到商品搜索/推荐的粗排或召回训练。

  - **序数头 + 统一价值函数实现可控权衡**：预测 p(r≥1) 和 p(r≥2) 并求和作为期望相关性标量，与 CTR/ATCR/CVR 预测通过可调权重组合成最终排序分。权重可作为线上配置项，通过小权重的相关性分量就能大幅提升语义匹配，而几乎不损伤转化。

  - **单模型多目标集成，无额外推理成本**：相关性头与参与度塔共享底层特征，复用 embedding 查找和特征加工，不增加在线延迟。这种“离线用 LLM，在线纯模型”的思路适合高
  QPS 的电商场景。

  - **标签生成流水线含 Q2T 模型辅助审核**：当人审与 LLM 复审冲突时，用 Query-to-Taxonomy 模型判断商品类别是否匹配，以此选择采用更高或更低标签。这种“规则
  + 模型”融合的清洗方法可借鉴到自家标注流程中。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索排序若仅优化 CTR/ATCR/CVR 等参与度信号，会引入流行度偏差和价格锚定偏差，导致语义不相关但热门的商品排在前面，损害搜索体验。引入语义相关性作为优化目标面临监督信号缺失：人工标注昂贵且难以覆盖长尾，行为信号有偏。LLM 虽能生成高质量相关性判断，但直接用于在线推理成本过高。本文旨在将 LLM 监督高效地融入多任务排序，实现相关性与参与度的联合优化与可控权衡。

### 方法
1. **LLM 离线标签生成**：收集 60 万人工标注，用行为信号（高转化但人为标无关）触发大 LLM（GPT-4o）复审，再结合 Query-to-Taxonomy 模型裁决冲突，形成高置信度训练集。微调 GPT-4o-mini，为超 1 亿 query-item 对生成三级序数标签（无关/中等相关/强相关），三类准确率 89%，1-差准确率 98%。
2. **多任务排序模型**：共享底层（包含 query/item/交互特征）后接多个任务塔，新增序数相关性头预测 p(r≥1) 和 p(r≥2)，求和作为期望相关性标量 ˆs_rel。与 CTR/ATCR/CVR 预测通过线性加权组合成最终排序分（超参 𝛼,𝛽,𝛾 控制权衡）。
3. **序数建模**：采用累积概率形式 p(r≥k) 保留序数结构，优于 softmax 分类和 MSE 回归。

### 关键结果
- 离线：序数模型在相关性 NDCG@10 上达到 0.962，远超仅参与度基线（0.812），且参与度指标持平。仅作辅助任务不直接用于评分时提升甚微。
- 在线 A/B：ATCR 提升 1.16%，CVR 提升 1.10%，GOV 提升 0.50%，均统计显著。
- 权衡曲线：序数头在相关性-转化 NDCG 曲线上 Pareto 最优，小权重的相关性分量即可大幅提升语义质量。

### 一句话
将 LLM 生成的精细序数相关性监督通过概率累积头融入多任务价值函数，可在不增加在线负担下实现相关性与参与度的显式调控与双赢。
