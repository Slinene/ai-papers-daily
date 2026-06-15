---
title: Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling
title_zh: 知识图谱增强的记忆检索实现长上下文建模
authors:
- Ghadir Alselwi
- Basem Suleiman
- Hao Xue
- Shoaib Jameel
- Hakim Hacid
- Flora D. Salim
- Imran Razzak
affiliations:
- University of New South Wales
- Hong Kong University of Science and Technology (Guangzhou)
- University of Southampton
- Technology Innovation Institute
- Mohamed Bin Zayed University of Artificial Intelligence
arxiv_id: '2606.14047'
url: https://arxiv.org/abs/2606.14047
pdf_url: https://arxiv.org/pdf/2606.14047
published: '2026-06-12'
collected: '2026-06-15'
category: LLM
direction: 长上下文建模 · 动态知识图谱增强记忆检索
tags:
- memory-augmented
- knowledge graph
- long-context
- R-GCN
- multi-modal memory
- efficient retrieval
one_liner: 构建动态上下文知识图谱，融合结构、语义与上下文记忆，长文本困惑度降8.5%且内存效率提升2-2.5倍
practical_value: '- **多记忆银行与融合检索**：可借鉴其 contextual/semantic/structural 三组记忆并行检索并学习融合权重的设计，在电商会话或
  Agent 长程对话中将短期键值对、长期语义块与图谱关系嵌入混合，提升对“同一设备、不同状态”等实体级依赖的检索精度。

  - **动态知识图谱构建流水线**：NER + 关系抽取 + 实体合并 + 置信度过滤的在线构图方法，能迁移至商品知识库、故障诊断等场景，实时将用户描述的设备、错误码、操作链抽成结构化关系，辅助对话
  Agent 理解因果链条。

  - **图-文跨模态融合**：利用 R-GCN 编码结构嵌入再与 LM 文本嵌入做交叉注意力融合，可参考用于推荐系统中物品画像的增强——将商品知识图谱的拓扑信息与文本描述对齐后作为
  item 表征，改善冷启动或跨领域推荐。

  - **内存与延迟的折中分析**：论文量化了实时构图带来的延迟成本（比纯记忆检索高约2倍），但内存节省显著；对离线可预计算场景（如固定文档集），可先构图再供线上使用，启发式地平衡精度与吞吐，适合电商推荐离线索引生成。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：长上下文语言建模的核心痛点不是上下文窗口长度，而是跨越数千 token 后仍能追踪实体状态和因果关系的结构理解。现有记忆增强检索方法仅依赖语义相似度，无法区分“同一打印机”的初始化故障和后续无关错误码，导致检索精度不足。静态知识图谱方法又无法适应领域特定的动态实体。因此需要一种能在推理时从输入文本中动态构建知识图谱、并将图结构信息融入记忆检索的框架。

**方法关键点**
- **动态知识图谱构建**：推理时用 BERT-large 做 NER，BERT-base 做关系抽取（TACRED 微调），在局部窗口中提取五种实体类型和七种关系类型；通过字符串和嵌入相似度合并重复实体，置信度加权过滤噪声，形成上下文相关的知识图谱。
- **图增强嵌入生成**：用 R-GCN 编码图谱结构得到实体结构嵌入，再与来自底层 LM 的文本嵌入（实体上下文池化）做交叉注意力融合，产出既含语义又含拓扑关系的最终实体表示。
- **三记忆银行架构**：维持上下文记忆（key‑value 对，从 LM 中间层抽取）、语义记忆（BGE‑M3 嵌入的文本块，FAISS 索引）和结构记忆（上述融合实体嵌入），通过可学习权重融合三个检索引擎的信号，注入 LM 的检索因果注意力层。
- **多任务训练**：语言建模、知识图谱链接预测、检索排序损失和跨模态对齐四目标联合微调，LoRA 适配 OpenLLaMA‑3B。

**关键实验**
- 数据集：SlimPajama (84.7K 训练样本) 微调，WikiText‑103、PG‑19、Proof‑Pile 评估。
- 对比模型：MemLong、ERMAR、LongLLaMA、LongLoRA、YARN、Phi3‑128k 等。
- 主要结果：在 WikiText‑103 上，KGERMAR 在 1K~16K token 长度下困惑度显著低于所有同规模记忆增强模型（7.74/7.25/7.20/7.14 vs. ERMAR 的 8.42/7.61/7.62/7.80）；内存峰值仅为 ERMAR 的 2–2.5 倍低（32K 时 14.51 vs 22.87 GB）；ICL 五任务平均准确率最高（4‑shot 78.6%，20‑shot 81.2%）。延迟因实时构图增加约 2 倍，但延迟方差更小且随长度近线性增长。

**核心结论**：动态上下文知识图谱提供的结构信号能有效弥补纯语义检索的不足，以可控的延迟代价换来长上下文建模精确度和内存效率的显著提升。
