---
title: 'From Volume to Value: Preference-Aligned Memory Construction for On-Device
  RAG'
title_zh: 从数量到价值：端侧RAG的偏好对齐记忆构建
authors:
- Changmin Lee
- Jaemin Kim
- Taesik Gong
affiliations:
- Ulsan National Institute of Science and Technology (UNIST)
arxiv_id: '2605.18271'
url: https://arxiv.org/abs/2605.18271
pdf_url: https://arxiv.org/pdf/2605.18271
published: '2026-05-18'
collected: '2026-05-21'
category: RAG
direction: 偏好对齐的端侧记忆构建与检索
tags:
- On-Device RAG
- User Preference
- Memory Construction
- Query Steering
- Personalization
- Privacy
one_liner: EPIC 框架通过筛选偏好相关数据并引导查询方向，在端侧实现 2404 倍内存压缩、20.17 个百分点的偏好遵循提升和 33 倍检索加速。
practical_value: '- **选择性记忆构建**：电商推荐系统可借鉴“只存偏好相关项”的思路，用用户偏好（如价格敏感、品牌偏好）过滤商品池，大幅缩减索引体积，同时保持推荐相关性。

  - **偏好对齐的检索引导**：在生成式推荐或对话 Agent 中，可在查询向量上叠加最匹配的偏好嵌入，增强检索结果与用户长期偏好的对齐，仅增加 0.18ms
  延迟。

  - **分级过滤流水线**：先使用轻量 Embedding 相似度做粗筛，再用 LLM 细粒度验证，平衡效率与精度；可迁移到商品候选集的粗排-精排流程，节省模型推理成本。

  - **偏好漂移适应**：端侧流式场景下，偏好的动态增删不会破坏索引，可直接更新偏好嵌入并检索，适合 Agent 长时对话中的兴趣追踪与实时调整。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：个人 AI 助手依赖端侧 RAG 实现隐私与低延迟，但设备内存有限，无差别索引会迅速耗尽存储，且传统检索结果容易忽略用户偏好（如忌海鲜却推荐寿司）。该工作提出：在资源受限的端侧，核心瓶颈不是“怎么用”个人信息，而是“存什么”——应优先保留与偏好相关的记忆。

**方法关键点**：
- **语义粗滤 (Semantic-Based Coarse Filtering)**：将数据项与用户偏好嵌入同一空间，用余弦相似度快速丢弃无关内容，保留至少与一个偏好匹配的项。
- **偏好对齐细验证 (Preference-Aligned Fine Verification)**：对粗筛结果使用语言模型做文本级验证，输出 Keep/Discard 决策、理由和精炼偏好子集；并为保留项生成“偏好条件指令”，说明在哪些偏好下如何使用该项。
- **指令中心记忆 (Instruction-Centric Memory)**：用指令嵌入索引原始内容，替换海量原始文本，大幅压缩存储，同时直接编码偏好使用方式。
- **偏好引导查询转向 (Preference-Guided Query Steering)**：检索时，查询嵌入主动向最相似偏好方向移动，使检索更可能命中偏好对齐的指令，仅增加可忽略的计算开销。

**关键结果**：在 PrefWiki、PrefRQ、PrefELI5、PrefEval 四个新构造的基准上，EPIC 与 NV-Embed-v2 等基线的标准 RAG、RAPTOR/HippoRAG 等索引增强 RAG、Pref-QR/PBR 等偏好条件 RAG 相比：内存用量平均降低 2404 倍，偏好遵循准确率最高提升 20.17 个百分点，检索延迟仅为最佳基线的 1/33。在 Jetson Orin Nano 8GB 端侧实验中，EPIC 在流式数据与偏好漂移下维持内存 <1MB、每查询 29.35ms 延迟，证明实际可部署。

**一句话记忆**：在端侧 RAG 中，用“偏好过滤 + 指令嵌入 + 查询转向”的组合，只保留与偏好相关的记忆条目，能以极小内存实现高精度、低延迟的偏好对齐生成。
