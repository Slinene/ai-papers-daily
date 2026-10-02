---
title: 'Not All Is Lost: Repairing Lossy User Preference States of Personalization
  Encoders'
title_zh: 并非全部丢失：修复个性化编码器中的有损用户偏好状态
authors:
- Parthiv Chatterjee
- Dhiraj Golhar
- Ummesalma Diwan
- Sourish Dasgupta
- Manjunath Joshi
- Tanmoy Chakraborty
affiliations:
- KDM Lab, Dhirubhai Ambani University
- LCS2 Lab, Indian Institute of Technology Delhi
- Dhirubhai Ambani University
arxiv_id: '2610.01270'
url: https://arxiv.org/abs/2610.01270
pdf_url: https://arxiv.org/pdf/2610.01270
published: '2026-10-01'
collected: '2026-10-02'
category: RecSys
direction: 推荐系统偏好状态事后校正
tags:
- Personalization Encoder
- State Repair
- Sequential Recommendation
- Frozen Host
- Temporal Correction
- Preference State
one_liner: 提出 REPAIR，利用冻结编码器缓存修复偏好状态，在不改编码器和任务头下提升推荐与个性化生成
practical_value: '- 对已部署的推荐模型，可在不重训编码器、不增加线上编码成本的情况下，插入轻量 REPAIR 模块，直接复用前向计算中已有的逐
  timestep 缓存，修复压缩后的用户偏好状态，提升 MRR/nDCG；实验显示仅微调任务头提升很小（如 Mamba4Rec +0.19 MRR），而修复状态本身能带来
  +3.96 MRR，说明瓶颈在状态压缩而非头部，排查效果时应优先检查状态表达。

  - 修复模块采用低秩可学习模式（K=128）和长/短/片段三时间基函数，是即插即用的工程组件；可借鉴其选择性写回与残差融合设计，控制线上额外延迟（论文报告延迟开销
  38-44%）。

  - 对于 LLM 个性化生成，可将修复后的状态映射为连续前缀喂给冻结 LLM，在 PerSEval 个性化指标上提升显著（IMPerSumm +25.23%），但通用生成指标变化不大，提示在评估个性化生成时需单独使用个性化敏感指标。

  - 训练目标中加入位置和源一致性辅助损失，可稳定修复模块对证据来源的追踪，在电商多行为序列建模中可借鉴该思路，让修复更可解释。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
个性化系统把用户交互历史压缩成任务面偏好状态，下游任务头只能看到这个压缩状态。但编码器前向计算中缓存的逐 timestep 表示仍可能保留有用证据，形成“可恢复性差距”。现有方法要么修改编码器内部表示，要么做去噪，但没有利用同一次前向计算的缓存来事后校正已形成的偏好状态。

**方法关键点**  
REPAIR 插入在冻结编码器和原任务头之间，不改编码器、不重跑输入。核心步骤：
1. 将压缩状态与缓存 timestep 表示投影到共同空间，计算 state-relative 残差；
2. 用可学习的低秩校正模式（仿 SVD 的 read-scale-write 结构，K=128）将残差压缩为紧凑坐标；
3. 通过长程、短程、片段式三个时间基函数视图解析时间证据，加权组合；
4. 选择性写回：按模式和时间步选取重要激活，经状态条件门控后残差融合回原状态；
5. 训练目标包含任务损失、位置分类损失、源一致性损失。对 LLM 宿主，将修复状态映射为连续前缀送入冻结解码器。

**关键实验与结果**  
在 MovieLens、PENS、MIND、Amazon Reviews 2023 四个数据集、12 个代表性宿主（GRU4Rec、SASRec、Mamba4Rec、NRMS、LSTUR、SigLIP2、OpenCLIP 等）上，仅训练 REPAIR、冻结编码器和任务头，所有宿主 MRR/nDCG@10 均提升，平均增益分别 +2.66/+2.63、+2.29/+2.16、+1.96/+3.08、+2.19/+2.55。其中 Mamba4Rec 在 MovieLens 上 MRR +3.96，而仅微调任务头只 +0.19。消融显示 K=128 最优，192 反而下降；联合三时间视图在 11/12 设置中最强，去掉时间分辨率甚至低于原冻结宿主。预头修复优于两种后头校正方法。个性化生成中 IMPerSumm 的 PerSEval 指标提升达 25.23%，而 ROUGE/METEOR 变化不大。

**最值得记住的一句话**  
偏好证据的可用性与下游使用是两回事——利用冻结编码器前向缓存进行紧凑、时间结构化的事后校正，就能在不重训编码器的情况下恢复被压缩丢失的偏好信息。
