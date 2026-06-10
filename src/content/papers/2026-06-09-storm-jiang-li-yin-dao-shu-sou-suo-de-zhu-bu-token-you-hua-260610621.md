---
title: 'STORM: Stepwise Token Optimization with Reward-Guided Beam Search'
title_zh: STORM：奖励引导束搜索的逐步 token 优化查询扩展
authors:
- Arthur Satouf
- Giulio D'Erasmo
- Yuxuan Zong
- Habiboulaye Amadou Boubacar
- Pablo Piantanida
- Benjamin Piwowarski
affiliations:
- MILA – Quebec AI Institute & ILLS
- Université Paris-Saclay & CentraleSupélec & CNRS
- Air Liquide
- Sorbonne Université & ISIR & CNRS
- Sapienza, University of Rome
arxiv_id: '2606.10621'
url: https://arxiv.org/abs/2606.10621
pdf_url: https://arxiv.org/pdf/2606.10621
published: '2026-06-09'
collected: '2026-06-10'
category: QueryRec
direction: 查询改写与词汇扩展 · 奖励引导束搜索
tags:
- Query Rewriting
- Beam Search
- Lexical Expansion
- Self-Supervised
- BM25
- Reward Guidance
one_liner: 将检索奖励转化为 token 级信号，通过奖励引导束搜索训练 LLM 生成高效关键词，在不改变索引下大幅提升 BM25
practical_value: '- **奖励信号粒度下放**：将检索质量指标（如 nDCG）转化为 token 级反馈，在生成过程中实时剪枝，解决序列级奖励延迟与稀疏问题。这一思路可直接用于电商搜索/推荐中的
  query 改写、标题优化、对话式 Agent 的关键词生成，用业务指标（CTR、转化率）替换 nDCG 即可训练。

  - **低成本高效重写**：STORM 训练的 LLM 输出短关键词串，推理延迟接近 BM25，适合在线实时场景。电商搜索可部署为轻量级改写模块，不增加检索延迟，却显著提升召回与相关性。

  - **自监督训练摆脱人工标注**：无需人工改写对，只需相关性判断或近似信号（如点击日志、伪标签）。可借鉴其利用交叉编码器伪标签蒸馏到生成式改写器的方法，在标注稀缺的电商场景快速冷启动。

  - **多语言零样本迁移**：仅用英文 MS-MARCO 训练，即可迁移到多语言 BM25 索引，效果超越专用多语言稠密检索器。对跨国电商平台，可简化多语 query
  改写部署，无需额外训练。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
词汇不匹配严重限制稀疏检索（BM25）效果，现有 LLM 重写器（如 HyDE、MuGI）生成冗长伪文档，解码与检索成本高，且仅获得序列级奖励信号，难以分辨哪些词真正提升检索。强化学习类方法（如 QUESTER）同样面临延迟反馈和探索效率低的问题。  

**方法关键点**  
- **奖励引导的束搜索（reward-guided beam search）**：在每一步生成时，对当前候选序列用 BM25 索引打分，保留高奖励分支，将检索奖励转化为 token 级剪枝信号，集中探索检索有效词汇。  
- **自监督训练框架**：借鉴 GCN，用 BM25 的 nDCG 作为判别器，训练 LLM 以最小化 KL 散度。提议分布由 ε-混合（ε 核采样 + (1-ε) 束搜索中选最高奖励序列）组成，通过重要性采样更新策略，无需人工改写。  
- **奖励函数设计**：nDCG@100（用交叉编码器伪标签代替稀疏 MS-MARCO 标签）、文档频率惩罚（避免高频泛词）、对数似然长度正则，共同引导生成高质量关键词。  
- **推理高效**：生成约 32-128 tokens 的逗号分隔关键词串，用 BM25 索引一次检索，延迟极低。  

**关键实验**  
- 数据集：MS-MARCO 训练（~80k 查询），评估涵盖 TREC DL 19/20、MS-MARCO Dev、BEIR 12 集合、MIRACL 18 语言。  
- 基线：BM25、RM3、SPLADE-v2、Qwen3 上的 HyDE/MuGI/W2P/QUESTER，以及 GPT-4.1 上的多个重写器。  
- 结果：STORM-8B 在 BEIR 平均 nDCG@10 达 47.5，超过所有同尺寸 LLM 重写器，并比 GPT-4.1 最强基线高 0.3；在 MIRACL 上零样本迁移平均 48.4，超越专用多语言稠密检索器 mColBERT。推理延迟仅 4.4 秒（8B）且检索时间与 BM25 持平。
