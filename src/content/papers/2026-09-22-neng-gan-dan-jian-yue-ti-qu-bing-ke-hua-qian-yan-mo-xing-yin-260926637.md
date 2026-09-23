---
title: 'Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought
  in Frontier Models'
title_zh: 能干但简约：提取并刻画前沿模型隐藏的思维链
authors:
- Xiaoyu Luo
- Tao Ren
- Wenrui Yu
- Xiao Li
- Qiongxiu Li
- Johannes Bjerva
affiliations:
- Department of Computer Science, Aalborg University
- Department of Electronic Systems, Aalborg University
- Seafill
arxiv_id: '2609.26637'
url: https://arxiv.org/abs/2609.26637
pdf_url: https://arxiv.org/pdf/2609.26637
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: LLM 隐藏思维链提取与推理结构刻画
tags:
- Chain-of-Thought
- reasoning extraction
- frontier models
- token efficiency
- interpretability
one_liner: 通过标准 API 注册自定义工具诱导闭源模型外化中间推理，发现提取推理匹配原生 CoT 且 Astra 拥有 token 高效的有向推理
practical_value: '- 在 Agent 或推荐链路中用闭源 LLM 且需审计中间决策时，可通过标准 API 注册一个轻量自定义工具（如 `think(step)`）诱导模型外化推理；先在开源模型上对照原生
  CoT 验证外部化痕迹性能一致，避免只得到事后合理化。

  - 评估 query 推荐、文案生成、排序解释等 LLM 任务时，除最终准确率外引入 token 效率、推理步骤类型、推理树等指标：关注模型是否提前锁定正确轨迹、把简单步骤内化，从而选择更适合线上、成本更低的模型。

  - 多 Agent 或生成式推荐 pipeline 中对中间推理做结构化记录，用于错误归因和可追溯性，防止正确答案来自错误推理；高风险策略如营销文案、价格解释尤其适用。

  - 不要用 trace 长度作为推理质量代理：更强模型可能话少但关键，应关注有效推理步骤密度和正确轨迹选择早晚。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：闭源前沿模型隐藏原始 CoT，只暴露最终答案或粗粒度摘要，导致无法验证推理质量，也无法区分正确结论是来自可靠推理还是偶然/伪推理。

方法关键点：通过标准 API 注册一个简单自定义工具，诱导前沿模型将中间推理外部化；先在开源模型上对比提取的推理与原生 CoT，确认其不是事后合理化；再扩展到闭源前沿模型（包括 GPT-6 Astra），在竞赛数学、科学、代码生成任务上评估。进一步从 token 效率、推理步骤类型、诱导推理树三个维度刻画推理结构。

关键结果：提取的推理性能与原生 CoT 匹配，并显著超过无推理基线；不同模型在外部化、压缩和组织推理上存在系统性差异；Astra 表现出 token 高效的有向推理，更早选择正确轨迹，基础步骤在内部解决，只外部化关键推理步骤。
