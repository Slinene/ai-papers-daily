---
title: 'HARNESS-LM: A Three-Phase Training Recipe for Harnessing SLMs in Sponsored
  Search Retrieval'
title_zh: 'HARNESS-LM: 赞助搜索检索下SLM的三阶段训练配方'
authors:
- Vipul Gupta
- Shikhar Mohan
- Lakshya Kumar
- Pranjal Chitale
- Nikit Begwani
- Amit Singh
- Manik Varma
affiliations:
- Microsoft AI India
arxiv_id: '2605.23572'
url: https://arxiv.org/abs/2605.23572
pdf_url: https://arxiv.org/pdf/2605.23572
published: '2026-05-22'
collected: '2026-05-25'
category: RecSys
direction: 赞助搜索检索 · 知识蒸馏与模型压缩
tags:
- Dense Retrieval
- Knowledge Distillation
- Structured Pruning
- Sponsored Search
- Dual Encoder
- SLM
one_liner: 通过教师训练、ℓ2对齐和对比细化，将大检索模型能力迁移到轻量级在线查询编码器，并实现27×延迟降低与线上收益提升。
practical_value: '- **三阶段解耦训练范式**：广告检索或推荐召回场景可先训练一个不受延迟约束的强教师（大模型、多模态特征或LLM增强特征），再用ℓ2回归将轻量级查询塔对齐到教师查询空间，最后用业务数据对比微调，获得接近教师精度且满足在线延迟的模型。

  - **ℓ2对齐简单有效**：无需标注数据，利用大量无监督查询日志即可将大模型的几何结构迁移到小模型，避免复杂的对比蒸馏损失或核对齐，在电商搜索、推荐序列等海量无标签语料上极易落地。

  - **逐步剪枝再对齐**：借鉴Ministral 3的级联压缩思路，逐层/逐FFN维度剪枝后重新对齐，可系统探索延迟-质量帕累托前沿；如从28层剪至4层仅损失1.1%精度，获得6×延迟缩减，适合需要多档位部署（如GPU/CPU）的业务场景。

  - **对比细化恢复剪枝损失**：冻结教师文档编码器后，用业务正负样本单独微调查询编码器，能有效弥补因压缩引起的精度下降（剪枝4层模型提升2.7 P@100），可作为快速迭代的轻量适配手段。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：赞助搜索系统依赖高吞吐的第一阶段检索器，在线查询编码器受严格延迟约束（<15ms）。当前SLM大模型（如Qwen3-Embedding-8B）虽在检索基准上表现强劲，但在线部署成本过高。作者观察到查询端与文档端存在天然不对称性：文档可离线预计算大模型向量，而查询必须在线实时计算，因此需要将大模型的检索能力迁移到轻量级查询编码器，同时复用高质量的离线文档索引。

**方法关键点**：
- **Phase 1 教师训练**：放松生产约束，用大容量SLM（Qwen3-4B/8B）和/或仅离线可用的丰富特征（如GPT生成的查询扩展）训练高性能教师检索器，采用Qwen3对比损失（混合in-batch、same-tower和hard negatives）。
- **Phase 2 查询对齐**：用无监督ℓ2回归将紧凑学生查询编码器（Qwen3-0.6B）的表示对齐到冻结教师查询空间，使其在检索时可直接与教师文档编码器计算内积。此阶段仅使用无标注查询文本，无需配对标签。
- **可选逐步剪枝**：采用结构化剪枝移除Transformer层和FFN隐藏单元，通过“剪枝→再对齐”循环将学生模型压缩至4层/190M参数，保障性能平缓下降。
- **Phase 3 对比细化**：冻结教师文档编码器，使用有监督对比学习（Qwen3 loss）单独调整学生查询编码器，聚焦边界区分和与固定文档空间的适配，进一步提升精度。

**关键实验**：
- 在Bing Ads内部评测集（230K查询，4700万广告）上，Qwen3-8B教师达到P@100=64.8；对齐后的Qwen3-0.6B+CR达64.3，几乎持平；剪枝至4层（190M参数）后为63.1，在线A100 GPU延迟从186ms降至6.8ms（27×加速），吞吐量超6800 queries/sec。
- 线上A/B测试显示收入提升1%，展示量+0.38%，点击量+0.4%，且不回退率与缺陷率无劣化。
- 相比直接不对称微调基线，HLM提升8.1-9.6 P@100，说明解耦训练显著优于端到端联合优化。

**最值得记住的一句话**：通过解耦任务适应、表示转移和在线效率，简单的ℓ2对齐配合后续对比细化即可大幅回收大模型质量，并实现极低延迟服务。
