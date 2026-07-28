---
title: 'LaRec: Unleashing LLM-based Latent Reasoning for Generative Recommendation'
title_zh: LaRec：释放大模型隐式推理能力的生成式推荐框架
authors:
- Yu Xia
- Zihan Lin
- Wei Yang
- Rui Zhong
- Cheng Chen
- Huan Ren
- Yao Hu
affiliations:
- University of Chinese Academy of Sciences
- Xiaohongshu
arxiv_id: '2607.24617'
url: https://arxiv.org/abs/2607.24617
pdf_url: https://arxiv.org/pdf/2607.24617
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 隐式推理与强化对齐
tags:
- Latent Reasoning
- Generative Recommendation
- LLM
- RL-tuning
- Step-level Alignment
- Personalized Exploration
one_liner: 通过步骤级对齐与过程方向对齐提供细粒度隐式监督，结合个性化高斯混合引导的 RL 探索，实现高效且多样的生成式推荐
practical_value: '- **隐式推理的步级对齐迁移**：用强LLM生成目标导向的CoT，将各步隐状态作为教师信号对比学习，可复用于电商搜索query理解、用户偏好挖掘等任务，用少量隐式token替代显式推理，显著降延迟。

  - **过程方向对齐损失**：约束隐状态演化方向逐步骤指向目标item语义向量，防止“语义空转”。此设计可直接用于生成式召回模型，提升多步推理的语义连贯性。

  - **个性化锚定探索**：基于用户历史交互物品嵌入构建高斯混合分布，采样作为初始隐状态扰动，有效限制RL探索范围，避免崩溃。适合需要可控多样性的广告文案生成、push推送选词等场景。

  - **两阶段训练范式（预训练对齐 + GRPO RL微调）**：复合奖励（命中+语义相似度）提供密集学习信号，对LLM-based推荐系统的多路径探索对齐具有工程参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有LLM推荐多采用显式CoT，虽可解释但产生冗长推理文本，导致在线延迟不可接受。隐式推理（latent reasoning）用少量连续隐向量替代文本步骤，理论上能平衡效果与效率，但面临两大挑战：① 中间隐状态缺乏细粒度监督，仅依赖最终推荐标签的稀疏信号，优化困难；② 确定性映射限制了多样性，难以捕获用户多兴趣。为此，LaRec提出隐式预训练+个性化RL微调的两阶段框架。

**方法关键点**  
1. **隐式预训练**  
   - *步骤级对齐*：用强LLM基于用户历史交互和目标item生成反向CoT，提取各步隐状态作为教师信号；以InfoNCE损失拉近对应隐式状态，提供稠密监督。  
   - *过程方向对齐*：要求隐状态更新方向逐步指向目标item的语义嵌入，通过余弦一致性损失防止“语义空转”。  
2. **个性化RL微调**  
   - *个性化引导分布*：用用户历史物品的标题嵌入建立高斯混合分布，采样作为初始隐状态扰动，实现“锚定探索”，避免盲目随机噪声导致的推理崩溃。  
   - *GRPO对齐*：对采样的多条推理路径计算复合奖励（命中+语义相似度），组内归一化计算优势，更新策略。  
3. **推理效率**：仅用K个隐式token（K=6），解码延迟接近无推理方法，远低于显式CoT。

**关键结果**  
在Amazon Toys、Instruments、MovieLens和工业数据集上，LaRec全面超越GRU4Rec、SASRec、BERT4Rec、ReaRec、TallRec、D3、TrackRec、LatentR3等基线。以Industry为例：H@5 0.3033（+4.6%），H@10 0.4090（+1.7%）；推理延迟仅0.67s（显式CoT需3.92s）。消融验证步骤级对齐、方向对齐、个性化引导分布均显著贡献。此外，模型规模增大带来持续增益，步数在6步时最优。
