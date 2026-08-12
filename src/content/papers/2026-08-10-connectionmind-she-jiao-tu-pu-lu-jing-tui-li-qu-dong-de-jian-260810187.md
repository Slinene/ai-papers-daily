---
title: 'ConnectionMind: Leveraging Social Networks and Large Language Models for Personalized
  Recommendation at Meta'
title_zh: ConnectionMind：社交图谱路径推理驱动的LLM推荐框架
authors:
- Haoyu Han
- Yuming Liu
- Lei Huang
- Lizhu Zhang
- Jiliang Tang
- Xiangjun Fan
affiliations:
- Michigan State University
- Meta Platforms, Inc.
arxiv_id: '2608.10187'
url: https://arxiv.org/abs/2608.10187
pdf_url: https://arxiv.org/pdf/2608.10187
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 社交推荐 · 图路径推理 · LLM策略
tags:
- Social Recommendation
- Graph Reasoning
- LLM Policy
- Reinforcement Learning
- Path Exploration
- Teacher-Student Distillation
one_liner: 将社交推荐形式化为异构图上的路径探索，LLM策略选择性发现证据路径，在Meta线上提升观看时长0.43%
practical_value: " - **异构社交关系显式建模**：将用户、物品、创作者、群组等纳入统一异构图，定义多种关系类型，把推荐转化为路径发现。电商可引入用户-好友、店铺关注、购物群等关系，生成可解释的推荐路径。\n\
  \ - **SFT+RL两阶段训练范式**：SFT用历史最短路径做行为克隆，RL采用规则化奖励（格式、F1、路径shaping）优化全局推荐质量。该奖励设计（尤其用子图内可达正样本的F1作为奖励）可直接用于需要序列决策的推荐场景。\n\
  \ - **Teacher–Student混合推理架构**：高活用户用LLM直接推理，普通用户通过知识蒸馏到轻量GNN，兼顾推理能力与毫秒级延迟。对于需要大模型推理但性能受限的场景极具参考价值。\n\
  \ - **多模态→紧凑文本的预处理流**：视频经OCR、ASR、VidLLM转换为文本摘要，供LLM高效处理。类似流程可用于商品的多模态信息（描述、图片、视频）的文本化，降低LLM推理成本。"
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
社交平台（如Meta）的用户行为高度受社交关系影响，但传统推荐方法将社交信号压缩为稠密向量，丢失了哪些关系在特定上下文中真正起作用的可解释性与选择性。ConnectionMind 提出将推荐建模为在异构社交-item 图上的路径推理问题，利用LLM的策略能力显式发现从用户到候选物品的证据路径。

## 方法关键点
- **异构图构建**：节点包括用户、创作者/页面、物品；边类型有好友、相似用户、关注、群组、分享、发布、同看、语义相似等，带有时戳和权重。
- **路径探索推荐**：从目标用户出发，LLM策略在采样的局部子图上逐步扩展路径，每一步输出继续扩展的路径和已到达的物品-路径对。最终输出物品集和对应的证据路径。
- **两阶段训练**：
  1. SFT：从历史交互中提取用户到正样本的最短路径作为监督，训练策略生成关系一致的路径。
  2. RL：采用GRPO，奖励由格式合规、最终推荐F1（基于子图内可达正样本）、以及每一步是否向正样本靠近的分层shaping奖励加权组成。
- **生产部署**：Teacher-Student混合推理，高活用户直接走LLM，普通用户用蒸馏后的轻量GNN模仿路径发现逻辑，控制延迟。

## 关键结果
- 公开数据集 Delicious 和 Foursquare 上，ConnectionMind (3B) 的 Recall@5 分别达到 0.0343 和 0.0818，显著优于所有GNN、扩散、LLM基线（如MHCN 0.0230、BIGRec 0.0039）。
- 线上A/B测试：曝光多样性 +0.33%，视频观看时长 +0.43%，视频会话数 +0.22%，均统计显著。
- 消融显示，无任务训练的原LLM几乎零召回，SFT大幅提升，RL进一步带来增益。
