---
title: How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt
  Structure
title_zh: LLM 推断提示词结构的评估结论可复现性审计
authors:
- Dipankar Sarkar
affiliations:
- Skelf Research
arxiv_id: '2609.30074'
url: https://arxiv.org/abs/2609.30074
pdf_url: https://arxiv.org/pdf/2609.30074
published: '2026-09-24'
collected: '2026-09-26'
category: Eval
direction: LLM 评估排名可复现性审计
tags:
- LLM evaluation
- reproducibility
- rank stability
- prompt structure
- bootstrap
- model ranking
one_liner: 自审计 8 个开源 LLM 的 prompt 结构推断评估，发现排名仅底部稳定，小样本评估可能过度确定性
practical_value: '- 内部 LLM 评估（如生成式推荐里的 Semantic ID 提取、query 解析、prompt 结构推断）不要只看平均排名的表格，必须补充
  bootstrap 排名稳定性；业务上若只根据顶部模型排名做流量分配或 A/B 决策，可能选中的是噪声上的赢家。

  - 温度为零不意味着确定性，同一输入多次调用可能返回不同结构；在关键抽取或推理链路中增加重复运行、记录原始输出，用一致性投票或阈值过滤，不要依赖单次输出。

  - 模型 API 端点可能在几周内撤回或改变，线上效果会漂移；工程上应固定模型版本或内部部署，并在评估报告中记录 measurement date 和模型 revision，保证可追溯。

  - “可复现”不等于“准确”：模型输出自一致不能替代与 ground-truth 的对比，尤其在 prompt 结构推断等任务中，要额外做人工标注一致性验证。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 系统评估通常在小 prompt 集上取平均后排名，但这类表格的置信度存疑。论文以 LLM-based prompt-structure inference 为案例，对评估本身进行自审计。

方法关键点：使用 8 个开源模型（5 个家族，8B-675B），禁用缓存，持久化 293 个原始中间表示。首先测量相同调用的结构一致性，再通过 joint cluster bootstrap over prompts 检验排名稳定性，比较不同重复 campaign 合并规则的敏感性，并将推断结构与 ground-truth 标注对照。

关键结果：相同调用下节点集 Jaccard 均值从 0.39 到 0.96，72% 的 prompt-model cell 从未 node-set-perfect。排名底部最稳定：最差的两个模型在 99% 和 86% 的 bootstrap 复制中保持排名，中间四个仅 27%-48%，顶部两个各 68%，说明表格能可靠识别最差模型，但不能可靠识别最佳模型。两种同样合理的合并规则改变了 8 行中的 4 行，研究级 headline 移动 7 个百分点。与 ground-truth 的对比显示可复现性不能解读为准确性。此外，8 个端点中有 4 个在测量后 10 周内撤回，研究无法按原样重跑。结论：小样本 LLM 评估可能显得比证据支持的更确定，建议报告 rank stability、per-cell provenance、敏感性比较、原始输出和测量日期。
