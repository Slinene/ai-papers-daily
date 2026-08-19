---
title: Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation
title_zh: 基于图结构在线难度估计的高效RLVR调度
authors:
- Zhizhao Liu
- Zhiliang Tian
- Xi Wang
- Zhihua Wen
- Yihang Xiong
- Zhiquan Lai
- Dongsheng Li
affiliations:
- PDL Lab, College of Computer Science and Technology, National University of Defense
  Technology
arxiv_id: '2608.17941'
url: https://arxiv.org/abs/2608.17941
pdf_url: https://arxiv.org/pdf/2608.17941
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: RLVR 自适应样本调度
tags:
- RLVR
- difficulty estimation
- graph propagation
- online variational inference
- sample scheduling
- reasoning
one_liner: 提出图结构化在线难度估计器，共享相邻样本rollout反馈以缓解冷启动与滞后
practical_value: '- 推荐系统冷启动与稀疏反馈：借鉴图结构上共享反馈的思路，对冷门 item/user 通过语义或行为相似图传播邻居的交互信号，缓解新
  item 无曝光或曝光少的估计偏差，类似 GraphSAGE/标签传播，但这里用在线变分状态估计更平滑。

  - Agent 任务调度中的预算分配：在 multi-agent 或工具调用场景，可按任务难度与相关性构建任务图，用 Beta-Binomial 聚合同一难度状态的任务执行结果，动态决定给哪些任务更多推理步数或工具预算，避免统一预算浪费在简单任务上。

  - 训练样本重要性采样：电商搜索/推荐模型训练时，可以利用模型当前 loss/奖励作为反馈，通过图传播估计样本难度或信息量，对高难度但可学习样本提高采样权重或增强次数，对简单样本降权，提升样本效率。

  - 在线均值场变分可复用于实时点击率预估中的 item/user 状态更新：将曝光/点击反馈按状态聚合，用先验鼓励相似 item 同状态，在线更新难度或价值估计，适合流式场景无批量重训练。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

## 动机
RLVR 依赖昂贵的 rollout 探索来提升 LLM 推理能力，但统一分配探索预算对不同难度样本低效：简单样本冗余，困难但有学习价值的样本探索不足。现有自适应调度依赖难度估计，专用探测额外生成开销大，基于历史的方法面临冷启动、反馈滞后，且忽略样本间关系。

## 方法关键点
- 构建难度感知样本图：基于语义与推理相似性连接样本，引入潜在难度状态，并用 Potts 先验鼓励相邻样本共享同一状态。
- 状态级 Beta-Binomial 模型：聚合同一状态下样本的 rollout 成功/失败结果，估计状态难度。
- 在线均值场变分：随新 rollout 反馈到达，持续更新潜在状态分配与状态级难度，无需专用探测，缓解冷启动与 staleness。
- 可插拔集成：可嵌入样本选择型或 rollout 分配型 RL 调度器，实现难度自适应探索。

## 关键结果
在多个基座模型、RL 调度器和 benchmark 上，在匹配 rollout 预算下，该框架相较基线取得更好性能，验证了图结构共享反馈对难度估计和调度效率的提升。
