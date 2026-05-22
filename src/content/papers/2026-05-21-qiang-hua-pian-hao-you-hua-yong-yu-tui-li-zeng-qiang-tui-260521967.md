---
title: Reinforced Preference Optimization for Reasoning-Augmented Recommendations
title_zh: 强化偏好优化用于推理增强推荐
authors:
- Jingtong Gao
- Zeyu Song
- Chi Lu
- Xiaopeng Li
- Derong Xu
- Maolin Wang
- Peng Jiang
- Kun Gai
- Qingpeng Cai
- Xiangyu Zhao
affiliations:
- City University of Hong Kong
- Kuaishou Technology
arxiv_id: '2605.21967'
url: https://arxiv.org/abs/2605.21967
pdf_url: https://arxiv.org/pdf/2605.21967
published: '2026-05-21'
collected: '2026-05-22'
category: RecSys
direction: 生成式推荐 · 推理增强
tags:
- LLM
- Reasoning
- GRPO
- CoT
- RLVR
- Recommendation
one_liner: 解耦LLM推理与推荐head，用GRPO+可验证奖励优化CoT质量，实现检索精度与推理可解释性双提升
practical_value: '- **推理与检索解耦**：采用LLM生成文本级CoT，专用Rechead做item检索，避免直接微调LLM隐藏状态破坏推理能力，适合工业推荐中LLM作为上游理解模块，下游用已有高精度检索模型承接。

  - **轻量级推理融合头**：Rechead用小型句子编码器+Transformer+软门控嵌入CoT，可过滤噪声，可作为排序模型的辅助特征；在线上部署时，只需将LLM生成的CoT/Answer转成稠密向量注入排序模型，已获得1.348%收入提升。

  - **RL多目标奖励设计**：格式、NDCG、CoT语义一致性、压缩率、熵差组合奖励驱动GRPO，可借鉴到对话式推荐或Agent推理链优化，尤其熵奖励能促进生成高信息密度token。

  - **两阶段迭代训练**：先冻结LLM训Rechead，再冻结Rechead用RL调LLM，避免非平稳奖励，适合业务上微调LLM时已有稳定评分器（如精排模型）的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM推理能力（CoT）能提升推荐的解释性和准确性，但直接将LLM隐藏状态与推荐目标联合优化会破坏推理连贯性，而生成式方法存在文本与item ID的语义鸿沟。现有的推理增强推荐面临推理保持、任务对齐、噪声过滤三重挑战。

**方法关键点**：
- 两阶段迭代框架：阶段一冻结LLM，训练Rechead（由文本编码器、Transformer、软门控组成），以CoT和Answer作为辅助信号，用对比学习预测下一个item；阶段二冻结Rechead，用GRPO优化LLM，通过格式、NDCG准确性、CoT质量（语义一致性、压缩率、熵）组合奖励引导。
- Rechead采用自适应门控机制控制CoT贡献，当Answer不可靠时回退到历史建模，有效过滤噪声推理。
- CoT质量奖励中引入熵差（E20% − Eµ）鼓励高信息密度token，减少冗余。
- 模型使用Qwen3-0.6B，用负采样+交叉熵损失训练Rechead，GRPO更新LLM。

**关键结果**：
- 在Amazon Musical Instruments、CDs、Video Games三个数据集上，RPORec的H@10比最强基线分别提升9.43%、28.57%、5.52%；在稀疏的CDs上提升尤为显著。
- 消融显示去除CoT、Rechead或整个阶段二均导致大幅性能下降，各奖励项均有贡献，一致性奖励影响最大。
- 在线A/B测试（40M用户、2.1B曝光）实现收入+1.348%、广告主价值+1.058%。

**一句话记忆**：用RL让LLM的推理成为可被专用head利用的文本特征，而非直接输出结果，从而兼顾推理的完整与检索的精准。
