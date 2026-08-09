---
title: 'CLIP-CC-Bench: Evaluating Paragraph-Level Video Descriptions in Video-Language
  Models'
title_zh: CLIP-CC-Bench：评估视频语言模型的长段落描述能力
authors:
- Mukhtiar Ali
- Harsh Dubey
- Sugam Mishra
- Chulwoo Pack
affiliations:
- South Dakota State University
arxiv_id: '2608.04302'
url: https://arxiv.org/abs/2608.04302
pdf_url: https://arxiv.org/pdf/2608.04302
published: '2026-08-05'
collected: '2026-08-09'
category: Eval
direction: 视频语言模型评估 · 长文本生成
tags:
- Video-Language Models
- Long-Form Video Description
- Evaluation Benchmark
- Embedding Ensemble
- Semantic Matching
one_liner: 提出首个面向段落级长视频描述的评估基准，通过嵌入模型集成与粗细粒度匹配衡量生成质量
practical_value: '- **嵌入模型集成评估法**：用多个 LLM 作为评判器的思路可直接迁移到电商商品描述、推荐理由、广告文案等生成任务的离线评估，避免单一嵌入模型带来的评分偏差，提升评估鲁棒性。

  - **粗细粒度语义匹配**：粗粒度匹配确保主题一致性，细粒度匹配捕捉细节忠实度，这种分层评估方式可用于 Agent 回复、搜索结果摘要等长文本生成场景，快速定量诊断生成质量。

  - **Borda 聚合排名**：当需要从多个评测指标或多个评判器综合对比模型时，Borda 计数法提供了一种简单稳定的排名聚合方案，适合在业务模型选型或线上
  A/B 评估中引入。

  - **长文本评估基准构建**：从原始内容切分、专家撰写参考到标准化评估脚本的完整流程，可复用到电商直播切片描述、商品讲解视频摘要等垂直域的长文本生成评估任务中。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有视频语言模型评估局限于短视频片段和单句匹配，无法衡量模型生成长段落级描述的准确性、完整性与连贯性，亟需一个面向长视频描述能力的基准。

**方法关键点**：
- 从5小时电影中切分出90秒片段，为每段撰写专家级段落参考描述，构建CLIP-CC-Bench。
- 评估协议采用五个先进LLM嵌入模型（如CLIP、LLM-based embedder）的集成，通过粗粒度语义匹配（主题级对齐）和细粒度语义匹配（细节忠实度）双维比较生成描述与参考描述。
- 对17个主流视频语言模型进行测评，使用Borda计数聚合各评判模型给出的排名，并分析评判间一致性与bootstrap排名稳健性。

**关键结果**：
- 集成嵌入评估显著降低单模型偏差，评判间一致性高，排名在bootstrap下稳定。
- 发布标准化评估脚本、模型输出及聚合工具，支持可复现。
- 该框架填补了段落级长视频描述评估的空白，可扩展至其他长文本生成任务。
