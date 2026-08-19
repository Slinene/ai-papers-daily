---
title: 'Once Generated, Ranked: End-to-End Generative Slate Recommendation with Unified
  Semantic-Collaborative IDs'
title_zh: 一经生成即为排序：统一语义-协同ID的端到端生成式Slate推荐
authors:
- Yang Hu
- Jiayi Guo
- Jingui Ma
- Ning Li
- Jiangling Qin
- Yanming Li
- Yang Deng
- Xiaoshuang Chen
- Kaiqiao Zhan
affiliations:
- Kuaishou Technology
- Peking University
- Nanjing University
arxiv_id: '2608.17613'
url: https://arxiv.org/abs/2608.17613
pdf_url: https://arxiv.org/pdf/2608.17613
published: '2026-08-18'
collected: '2026-08-19'
category: GenRec
direction: 生成式推荐 · Semantic ID · Slate推荐
tags:
- Generative Recommendation
- Semantic ID
- Slate Recommendation
- Preference Alignment
- CountSketch
- Listwise Planning
one_liner: 提出OGR框架，融合推荐感知SID构建与列表级偏好规划，端到端生成有序slate并提升在线指标
practical_value: '- SID构建：TUSID用CountSketch压缩局部共现并做置信度融合，避免显式物品共现矩阵，适配亿级物品库；电商/广告可借鉴此方式将语义（多模态/属性）与协同信号统一到层次SID，尤其利用B/C类属性刻画供给与需求。

  - 生成式slate架构：GL2P将列表规划与SID解码流水线化，推理深度从O(KD)降至O(K+D)，吞吐量提升约2.4x且NDCG更高；实时推荐场景可参考该解耦与并行策略，缓解自回归生成延迟。

  - 偏好对齐：SPA用主奖励+辅助奖励的符号一致性校准，冲突时只保留主信号，再叠加PPO-clip与KL约束；LLM推荐微调可复用此保守策略，防止对齐后遗忘曝光分布或产生退化。

  - 训练监督：同时使用曝光顺序和反馈排序序列进行监督，增强对用户偏好的学习但保留对展示分布的拟合，可迁移到列表重排或生成式重排模型训练。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：传统slate推荐是“先生成后排序”的级联，候选池受限且各阶段目标不一致；生成式推荐（SID）虽然端到端，但SID构建缺乏推荐感知语义和局部协同，且NTP损失与slate整体效用错位。

方法关键点：
- **TUSID**：两阶段统一SID构建。用MLLM提取细粒度语义，编码品牌/类别/B-tags/C-tags属性，交叉注意力门控融合；用SASRec损失做推荐感知。协同注入采用Signed CountSketch压缩局部共现，得到协同嵌入，通过置信度感知权重（基于distinct users）与语义表示拼接，再RQ-KMeans量化。
- **GL2P**：列表级偏好规划。规划器自回归生成每个位置的偏好向量，SID解码器基于该向量逐token生成SID，规划与解码流水线并行，串行深度从O(KD)降为O(K+D)。监督同时使用曝光序列和反馈排序序列。
- **SPA**：slate级偏好对齐。候选rollouts后，主奖励（有效观看/点赞）和辅助奖励（多样性）经符号一致性校准；用PPO clip和KL散度保守更新规划器和解码器，防止偏离参考策略。

关键结果：在工业数据集和KuaiRec上，OGR的NDCG@5相对最佳基线提升48.2%和27.2%；在线A/B测试中有效观看提升1.120%，评论/点赞/转发均有提升；效率上较生成式基线Beam模式吞吐量提升2.43x和2.49x。

最值得记住的一句话：生成式推荐并非必须逐项串行生成，通过列表规划与解码流水线可以同时获得列表级依赖和低延迟。
