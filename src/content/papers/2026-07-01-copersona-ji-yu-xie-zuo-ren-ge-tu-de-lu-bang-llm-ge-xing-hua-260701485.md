---
title: 'CoPersona: Collaborative Persona Graphs for Robust LLM Personalization'
title_zh: CoPersona：基于协作人格图的鲁棒 LLM 个性化
authors:
- Yangtian Zhang
- Leyao Wang
- Hiren Madhu
- Ngoc Bui
- Walter Roznyatovskiy
- Rex Ying
affiliations:
- Yale University
- Samsung
arxiv_id: '2607.01485'
url: https://arxiv.org/abs/2607.01485
pdf_url: https://arxiv.org/pdf/2607.01485
published: '2026-07-01'
collected: '2026-07-04'
category: LLM
direction: LLM 个性化 · 图协作消偏 · 多面建模
tags:
- LLM Personalization
- Graph Neural Networks
- Collaborative Filtering
- Facet Disentanglement
- Retrieval-Augmented Generation
- Cold Start
one_liner: 通过构建多面相似度图来借力行为相似的同伴，缓解因用户历史稀疏与偏斜导致的个性化生成冷启动
practical_value: '- **面对用户历史稀疏的场景**：可用协同的思路，从行为相似的同伴那里“借”信号补全用户的弱项维度，而不是仅在自身上检索。

  - **Facet 解耦与多面图构建**：先无监督地归纳出全局人格面（如评论中的 tone、主题偏好、价值观），再按面分别建相似度图，可避免全局相似度带来的噪声。该思路可直接用于品评文案生成、商品推荐理由个性化等任务，按“写作风格”“价格敏感度”等维度对用户分层。

  - **双分支推理架构**：非参分支提供可解释的文本范例，供 LLM 作为上下文；参数分支通过可靠性门控在图上游走补全弱置信度面的向量，再压缩成软提示 token
  注入 LLM，两者互补。实际工程中可按资源拆解：低成本场景只用检索范例，高成本场景加训软提示。

  - **可靠性标签与门控**：为每个用户每面的摘要打分（none/weak/moderate/strong），在图传递时根据可靠性加权，避免低质量信息污染。类似地，在
  Agent 协作中可按证据强度对同伴信号加权，降低幻觉。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 个性化常用记忆‑检索管线，但真实用户历史往往稀疏且偏斜（例如只覆盖了“类型偏好”，而“写作语气”证据缺失）。这导致在测试 query 需要弱支持维度时，模型输出失准。为此，论文引入协同过滤思想：通过借用行为相似用户的信号来补全弱面。

**方法关键点**
- **Facet 解耦与归纳**：从全量用户资料中聚类，用 LLM 对比簇间差异，自动归纳出 3‑6 个可解释的人格面（如 Emotional Engagement、Critical Tone），再为每位用户每面生成摘要、支持引用和可靠性标签。
- **多面相似度图**：按每个面分别计算余弦相似度，构建 multiplex 用户‑用户图，每层仅在最相似的 top‑K 邻居间保留边，并用可靠性加权边。
- **双分支推理**：(1) **非参分支**从图中取回面一致的邻居摘要与范例文本，作为可读上下文；(2) **参数分支**执行可靠性门控的图消息传递：根据自面置信度插值自身嵌入与邻居聚合嵌入，经跨面自注意力后压缩为固定长度的软提示 token，微调时以 LoRA 注入 LLM。
- **训练时**，BM25 检索自史与邻居范例构成文本上下文，与软提示 token 拼接后喂给 LLM，用负对数似然优化。推理时使用缓存的软提示和检索结果。

**关键结果**
- 在 Amazon Reviews 的 Books、Movies & TV、CDs & Vinyl 三个类别上，CoPersona 全面超越 RAG、PAG、DPL、DEP 等基线。以 7B 模型为例，Books 上 ROUGE‑1 达 0.395（DEP 0.362），BLEU 达 15.47（DEP 12.34）。
- 消融表明，拿掉参数分支（仅保留检索）造成 BLEU 下降 4.13，拿掉非参分支下降 2.17，双分支互补明显。
- 稀疏尾部数据（Video Games、Musical Instruments、Sports & Outdoors）上依然稳定最优，LLM‑as‑Judge 评估在 Authenticity 和 Practical Details 维度得分显著更高。

**核心金句**：不是从所有用户中粗略地借用，而是按面精细地对齐，让 LLM 知道“在这一点上，可以看看那些相似的人” —— 这正是稀疏历史下个性化的一条实用出路。
