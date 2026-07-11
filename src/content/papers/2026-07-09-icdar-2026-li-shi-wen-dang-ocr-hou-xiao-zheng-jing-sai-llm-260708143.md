---
title: ICDAR 2026 HIPE-OCRepair Competition on LLM-Assisted OCR Post-Correction for
  Historical Documents
title_zh: ICDAR 2026 历史文档 OCR 后校正竞赛：LLM 辅助方法评估
authors:
- Maud Ehrmann
- Emanuela Boros
- Juri Opitz
- Andrianos Michail
- Florian Wagner
- Simon Clematide
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL)
- University of Zurich
arxiv_id: '2607.08143'
url: https://arxiv.org/abs/2607.08143
pdf_url: https://arxiv.org/pdf/2607.08143
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: LLM 辅助 OCR 后校正 · 历史文档多语言基准
tags:
- OCR post-correction
- LLM
- historical documents
- multilingual benchmark
- evaluation
one_liner: 组织多语言历史文档 OCR 后校正竞赛，评估 LLM 在不同噪声和语言下的校正能力与过校正风险。
practical_value: '- 论文面向数字人文领域，与电商/推荐系统的直接关联度较低。

  - 可借鉴的思路：利用 LLM 对搜索 query 或商品描述中的 OCR/文本噪声进行后校正，提升索引与召回质量；采用检索导向评估而非逐字匹配来贴合实际搜索场景。

  - 低噪声环境下 LLM 过校正的发现提醒，在生成式推荐文案纠错时需控制模型改写自由度，避免引入新错误。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：大规模历史文档数字化中存在大量遗留 OCR 错误，重扫成本高。LLM 为后校正带来机遇，但其跨语言、跨文档类型和噪声水平的有效性及幻觉风险尚不明朗。

**方法关键点**：组织 ICDAR 2026 HIPE-OCRepair 竞赛，提供统一的多语言（英、法、德）历史报纸和印刷品数据集（17-20 世纪）。参与者收到段落级噪声 OCR 文本，不提供原始图像，需输出校正版本。评估采用检索导向指标（而非字符级严格匹配），模拟数字馆藏搜索和访问的真实场景。

**关键结果**：四支队伍提交系统，涵盖零样本提示、持续预训练与微调。结果表明：LLM 辅助系统能显著提升 OCR 质量，但表现因数据集、语言和噪声程度而异；低噪声输入上普遍出现过校正问题，强调需要超越字符错误减少的评估视角。竞赛数据集、评分器和流程均已公开发布。
