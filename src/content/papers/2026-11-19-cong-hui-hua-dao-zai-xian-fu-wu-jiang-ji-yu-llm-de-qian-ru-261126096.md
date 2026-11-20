---
title: 'From Sessions to Serving: Integrating LLM-Based Embeddings into Retrieval
  for Production Content Recommendation'
title_zh: 从会话到在线服务：将基于 LLM 的嵌入集成到生产内容推荐检索中
authors:
- Zhixiong Hu
- Meng Li
- Maggie Zhang
- Deborshi Goswami
- David Bailey
- James Bradley
affiliations:
- Autodesk
arxiv_id: '2611.26096'
url: https://arxiv.org/abs/2611.26096
pdf_url: https://arxiv.org/pdf/2611.26096
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: LLM 嵌入增强召回阶段用户表示
tags:
- LLM Embeddings
- Retrieval
- Session Representation
- Nearline Serving
- Two-Tower
- Production RecSys
one_liner: 将预训练 LLM 会话/历史嵌入作为用户塔辅助特征，配合近线异步刷新，在 Autodesk 内容推荐召回中验证增量提升
practical_value: '- 在双塔召回的用户塔中，把 LLM 生成的会话/历史语义嵌入作为辅助特征，与已有 ID 序列编码器并行拼接，可以低成本复用预训练模型增强
  recall，无需替换主模型。

  - 近线异步刷新用户向量：将 LLM 推理和序列聚合放在近线链路，主服务只读取缓存向量，解决 LLM 延迟与实时性矛盾，适合电商高频行为下的用户兴趣即时更新。

  - 会话级嵌入能捕捉用户短期意图（如浏览某类商品/内容），历史级嵌入则建模长期偏好；两者结合可提升对异构候选内容（商品、文章、视频等）的匹配能力。

  - 在多内容类型全目录上做消融验证 LLM 特征增量价值，可以作为在业务中引入 LLM 语义信号的评估范式，减少上线风险。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：大型市场网站内容推荐面临候选内容高度异构（客户故事、产品页、行业页、学习内容等），用户行为稀疏且快速变化，检索阶段对用户兴趣的表示质量成为瓶颈，仅靠下游排序难以弥补。

**方法关键点**：系统 LSER 从预训练 LLM 中导出会话级和历史级嵌入，将其作为用户塔的辅助特征，与已有可学习序列编码器拼接使用，不替换原有双塔结构。为保证实时性，构建近线服务路径，异步刷新序列和 LLM 派生用户向量，主推荐服务直接消费缓存向量，规避 LLM 在线推理延迟。

**关键结果**：在 autodesk.com 完整多内容类型目录上的消融实验表明，加入 LLM 派生嵌入可带来稳定的增量模型性能提升；生产级近线刷新链路验证了该方案的技术可行性。
