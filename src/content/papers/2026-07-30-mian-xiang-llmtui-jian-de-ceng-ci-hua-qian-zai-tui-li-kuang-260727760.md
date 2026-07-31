---
title: Hierarchical Latent Reasoning for LLM-based Recommendation
title_zh: 面向LLM推荐的层次化潜在推理框架HiLaR
authors:
- Peiyu Hu
- Siying Gu
- Weihai Lu
- Zhuodong Liu
- Yuntian Tang
- Jiahao Liang
- Yiying Xie
- Jiang Rong
- Zhaokai Luo
- Zhiyong Wang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Xiaohongshu
- Peking University
- Beijing Jiaotong University
arxiv_id: '2607.27760'
url: https://arxiv.org/abs/2607.27760
pdf_url: https://arxiv.org/pdf/2607.27760
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · 层次化隐式推理
tags:
- LLM-based Recommendation
- Latent Reasoning
- Hierarchical Representation
- GRPO
- Process Reward
- Residual Quantization
one_liner: HiLaR 用残差量化和时间窗口监督构建粗到细用户偏好，对齐LLM潜在状态并以过程奖励优化层级贡献，在Amazon数据集上超越SOTA。
practical_value: '- 用户序列建模：借鉴时间窗口监督的残差量化，将用户历史按时间从远到近分层，构建从长期兴趣到短期意图的多粒度表示，可直接作为召回或排序阶段的特征。

  - LLM推理结构化：在推荐Agent中，可让LLM的中间隐藏状态对齐预训练的层次化偏好向量，使推理轨迹具有粗到细的结构，便于诊断与解释。

  - 过程奖励设计：利用下一物品预测的条件似然增益作为每步推理的奖励分量，结合GRPO优化多步潜在推理，为Agent的多步决策提供细粒度反馈，降低稀疏奖励问题。

  - 协同信号融入：在生成式推荐中引入冻结协同模型（如SASRec）的偏好分数作为RL奖励，弥补纯语义匹配的不足，可直接用于电商搜索召回的生成式模型。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有LLM推荐中，显式思维链推理开销大，而隐式推理方法（如LatentR3）将中间状态视为通用精炼步骤，忽略了不同状态对目标生成的贡献差异，且未充分利用用户历史中从长期兴趣到近期意图的多粒度偏好结构。为此，作者提出HiLaR，通过层次化潜在推理和层级感知强化学习来组织并优化推理过程。

**方法关键点**：
1) **时序引导的层次化量化**：将用户历史按时间顺序划分为K个窗口，用冻结LLM编码历史得到嵌入h_u后，使用K层残差矢量量化（RVQ）构建粗到细的偏好表示。第k级量化后累积嵌入e_{u,k}，并用对应的递进时间窗口（从全部窗口到最近窗口及目标物品）进行多标签BCE监督，迫使早期层级恢复广泛历史偏好，后期层级聚焦近期意图与目标。
2) **层次化潜在对齐微调**：在SFT阶段，为LLM引入K个连续潜在状态τ_k，通过可训练投影对齐到量化表示e_{u,k}，联合优化目标标题生成和层级对齐损失，使LLM获得粗到细的潜在偏好结构。
3) **层级奖励引导的GRPO**：采样G条潜在推理轨迹，每条轨迹生成标题。最终奖励融合精确匹配、前缀F1分数和协同过滤模型（SASRec）的偏好分。过程奖励包括：对齐余弦相似度、每层潜在状态的边际目标似然增益（ℓ_{g,k} - ℓ_{g,k-1}）。总奖励组合后，用GRPO进行策略优化，仅更新潜在推理模块和投影层。

**关键结果**：在Amazon Toys、CDs、Games、Instruments四数据集上，HiLaR对比序列模型（GRU4Rec、SASRec）、生成式模型（TIGER、RPG）、LLM推荐（AlphaRec、BIGRec、D3等）及隐式推理模型（LatentR3、VRec、FLR），采用Qwen2.5-1.5B骨干，在多数指标上取得最优。例如CDs上H@10达0.1484，Toys上H@10达0.1213，Instruments上H@10达0.1320。消融表明时序量化、层级对齐与GRPO及各项奖励均带来显著增益，历史越长增益越明显。推理开销仅略高于基础模型，远低于CoT。

**最值得记住的一句话**：用时间窗口监督的残差量化将用户偏好解耦为粗到细层次，并作为LLM隐式推理的落地靶向，过程奖励以每一步的似然增益度量贡献，实现更精细的轨迹优化。
