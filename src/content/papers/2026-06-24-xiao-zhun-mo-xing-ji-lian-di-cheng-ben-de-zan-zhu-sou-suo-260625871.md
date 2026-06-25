---
title: 'AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation
  in Sponsored Search'
title_zh: 校准模型级联：低成本的赞助搜索相关性离线标注
authors:
- Md Omar Faruk Rokon
- Shasvat Desai
- Hong Yao
- Kuang-chih Lee
affiliations:
- Walmart Global Tech
arxiv_id: '2606.25871'
url: https://arxiv.org/abs/2606.25871
pdf_url: https://arxiv.org/pdf/2606.25871
published: '2026-06-24'
collected: '2026-06-25'
category: Eval
direction: 离线标注 · 模型级联 · 按类校准
tags:
- Model Cascade
- Confidence Calibration
- Relevance Annotation
- Sponsored Search
- LLM Fine-Tuning
- Cost Efficiency
one_liner: 将精度与成本解耦：领域微调提供近20点精度提升，校准级联再节约一半计算量
practical_value: '- 自动标注管线设计：先部署小模型 (Cross-Encoder) 处理绝大多数简单样本，仅对低置信度实例级联到更大 LLM，可在保持精度的同时节省约
  50% 推理成本，适合大规模 query-item 相关性标注。

  - 按类校准优于全局校准：对每个预测类别分别拟合 isotonic 回归，能够修正类别特异的过/欠置信，提升级联路由的准确性 (+0.6pp)；在分类器置信度用于触发不同策略时，推荐采用
  per-class 校准。

  - 模型规模与数据预算的联合规划：小模型（如 DeBERTa）学习曲线饱和早，大模型（8B）能持续从更多数据中获益；可根据标注预算将难例递交给大模型，最大化样本效率。

  - 输入模板的严格一致性：微调后的分类头对 prompt 格式极度敏感，细微变化会导致精度下降 10–15 个点；生产环境必须固化模板并与训练时完全对齐。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
赞助搜索中，query-product 相关性标注是排序模型训练、NDCG 评估与故障排查的基石，但人工标注昂贵（$0.50/条，日产 3000 条，5 天周转）且覆盖有限。现成 LLM（GPT-4 仅 68% 准确率）远达不到人工一致性 89%，而直接级联这类模型会继承其精度上限。该工作从问题本质出发：**精度与成本是两个可以独立优化的维度**——先通过领域微调大幅提精度，再用校准级联降成本，从而构建一套高质、可扩展的离线标注流水线。

## 方法关键点
1. **三级微调模型序列**：由小到大排列为 DeBERTa-v3-base Cross-Encoder（184M）、Gemma‑2B（LoRA）和 LLaMA‑8B（LoRA），均在 120 万条电商 query-title 对上微调，采用分类头输出 5 类相关性的置信度。
2. **逐类 isotonic 校准**：针对每个预测类别独立拟合单调校正函数，矫正类别特异的过/欠置信，使路由决策更可靠，相较最强全局校准再提升 0.6 个百分点。
3. **置信度级联 + 集成兜底**：从最廉价的 Cross-Encoder 开始，若校准置信度超过阈值则直接输出，否则依次递进到 Gemma 和 LLaMA；最终仍无法判定的样本进入多数投票，平局时偏向高相关度标签。

## 关键实验结果
- 微调后的三类模型准确率分别达 87.5%、88.2% 和 88.9%，对比 GPT-4 的 68.2% 有 >19 点的绝对提升。
- 校准级联达到 **89.1% 的准确率**，同时相比全用 LLaMA-8B 节省 **50.1% 的计算成本**；Cross-Encoder 承担 74.5% 的样本且该部分准确率 91.2%。
- 消融实验表明：微调贡献约 20 点精度，级联在成本减半下精度仅微降 0.7 点，逐类校准再带来 0.9 点（相对未校准级联）的增益，三个模块呈正交叠加。
- 生产部署已处理 **1.5 亿+ 次标注**，平均周转从 5 天缩短到 **1–3 小时**，支撑训练数据制备、NDCG 评估等多个离线场景。
