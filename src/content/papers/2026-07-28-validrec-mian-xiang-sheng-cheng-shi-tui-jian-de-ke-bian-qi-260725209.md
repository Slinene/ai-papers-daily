---
title: 'VaLiDRec: Variable-Length LLM-Aligned Semantic IDs for Generative Recommendation'
title_zh: VaLiDRec：面向生成式推荐的可变长LLM对齐语义ID
authors:
- Shutong Qiao
- Wei Yuan
- Tong Chen
- Hao Wang
- Quoc Viet Hung Nguyen
- Hongzhi Yin
affiliations:
- University of Queensland
- Computer Network Information Center, Chinese Academy of Sciences
- Griffith University
arxiv_id: '2607.25209'
url: https://arxiv.org/abs/2607.25209
pdf_url: https://arxiv.org/pdf/2607.25209
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 可变长语义ID
tags:
- Generative Recommendation
- Semantic ID
- LLM
- Variable-Length
- Token-Set Prediction
- Cold-Start
one_liner: 从LLM原生词表直接构建可变长语义ID并用并行token集预测替代自回归，实现高效语义对齐的生成式推荐
practical_value: '- **直接利用LLM原生词表构建物品语义ID**：不依赖量化码本，从物品标题/描述中基于token重要性（隐状态范数+IDF）和贪心剪枝选取关键词，形成可变长token集。电商业务可直接复用此方法为商品生成紧凑、语义对齐的ID，用于搜索、推荐或冷启动表示。

  - **并行token集预测替代自回归生成**：推理时仅需一次LLM前向传播计算所有候选token的得分，再聚合到item级，彻底消除beam search。线上推荐可借鉴该非自回归架构，实现87倍以上的推理加速，大幅降低RT和资源消耗。

  - **Graph-aware软提示注入协同信号**：用GraphSAGE在物品转移图上聚合邻居，生成用户行为序列的连续提示向量。该方法可嵌入现有电商推荐pipeline，将交互图信息提炼为可学习的prompt，增强LLM对用户行为模式的理解，尤其利于稀疏场景和冷启动。

  - **SID构建中的碰撞处理与语义质量约束**：通过功能权重引导的token扩展和频率后缀消歧，保证ID唯一性；同时用语义相似度阈值控制剪枝终止，平衡紧凑性与保真度。该思路可用于商品表示的去重、规范性控制，或为多模态物品生成高质量特征码。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有生成式推荐中的语义ID（SID）多采用聚类/量化得到定长人工码，与LLM词表割裂、语义不可解释，且固定长度不适应物品语义复杂度。同时自回归生成SID带来高延迟和beam search开销。本文提出VaLiDRec，直接从LLM原生词表构建可变长SID，并利用并行token集预测实现高效、语义对齐的生成式推荐。

**方法关键点**：
1. **可变长SID构建**：从物品元数据文本出发，经LLM tokenization后计算token重要性（隐状态范数×IDF），构建候选池；再通过语义质量感知的贪心剪枝，在质量阈值约束下迭代去除非核心token，使ID长度自适应语义复杂度；最后通过碰撞感知扩展与功能权重驱动的替换解决冲突，并以频率后缀消歧。
2. **推荐模型**：利用GraphSAGE在物品转移图上聚合邻居，生成recency加权池化的用户行为提示向量；LLM（Llama-3.2-1B）通过LoRA微调，仅更新语义token嵌入。训练目标融合token集预测损失、item级排序损失与对比对齐损失，实现协同信号注入与语义一致性。
3. **推理加速**：将推荐转化为单次LLM前向计算所有候选token得分，再按item的SID token聚合得到排序分数，彻底免除自回归和beam search。

**关键结果**：在Amazon四领域（Luxury, Scientific, Instruments, Arts）上，VaLiDRec全面超越GRU4Rec、SASRec、TIGER、LC-Rec、RPG等基线，Luxury上Recall@20提升12.4%，Arts上NDCG@20提升超22%。零样本冷启动场景下Recall@100与NDCG@100分别较最强基线提升2.5%和5%。与LC-Rec相比，推理速度提升87.49倍（仅需0.078秒/实例）。消融实验表明Graph-aware软提示贡献最大，SID refinement次之。
