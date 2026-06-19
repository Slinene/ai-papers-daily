---
title: 'RODS: Reward-Driven Online Data Synthesis for Multi-Turn Tool-Use Agents'
title_zh: RODS：奖励驱动的在线数据合成用于多轮工具使用智能体
authors:
- Ruishan Fang
- Siyuan Lu
- Chenyi Zhuang
- Tao Lin
affiliations:
- Ant Group
- Zhejiang University
- Westlake University
- Shanghai Innovation Institute
arxiv_id: '2606.19047'
url: https://arxiv.org/abs/2606.19047
pdf_url: https://arxiv.org/pdf/2606.19047
published: '2026-06-16'
collected: '2026-06-19'
category: Agent
direction: Agent 动态数据合成 · 能力边界检测
tags:
- GRPO
- multi-turn tool use
- data synthesis
- curriculum learning
- replay buffer
- agentic RL
one_liner: 利用GRPO中进度奖励方差作为能力边界检测器，动态合成多轮变体解决静态数据信号耗竭，以约20倍更少数据达到大规模离线合成水平
practical_value: '- **能力边界检测的复用**：在训练对话推荐或搜索Agent时，可直接用RL的进度奖励方差识别高梯度区域，无需额外推理，用于动态筛选或重放样本。

  - **结构化同构重采样**：保持任务图结构（如API依赖拓扑、对话状态转移）不变，仅替换场景实体与叙述，生成大量语义连贯的边界样本，可迁移到对话推荐的多轮数据增广中。

  - **动态缓冲管理**：随着策略迭代，退役已掌握或过难的任务，始终保持训练池处于高方差区域，可借鉴到推荐系统RL训练的样本生命周期管理，避免过时数据稀释梯度。

  - **多智能体合成流水线**：Planner + Executor + Rewrite + Critique 的流水线设计可直接用于自动生成高质量多轮对话训练数据，减少人工标注，适用于电商客服、语音助手等场景。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
多轮工具使用智能体的RL训练面临数据稀缺与静态数据集信号枯竭的双重挑战：高质量多轮标注数据极少（如BFCL V3仅800条），且随着模型能力提升，原本有区分度的样本逐渐被掌握，导致梯度方差消失，训练效率骤降。

## 方法
RODS 提出一个闭环数据合成框架，将训练与生成紧密耦合：
- **边界检测**：利用GRPO中进度奖励（Progress Reward）的rollout方差作为零成本能力边界探测器，将任务划分为已掌握、边界、困难三区，选中处于边界的高方差种子。
- **技能对齐合成**：五阶段多Agent流水线——①Planner基于种子设计同构API依赖图与叙述；②Executor在仿真环境中实例化并自动修复执行错误；③Rewrite全盘重写多轮用户查询，保证跨轮语义连贯；④Critique严格质量审查，循环修正；⑤可选的对抗增强注入模糊/缺失参数。整个过程保持任务结构复杂度不变，只变换场景实体。
- **动态重放缓冲**：按类型配额采样边界种子，新合成数据在epoch边界分阶段注入，避免梯度震荡；同时三级淘汰机制（燃烧过滤、边界漂移驱逐、方差优先修剪）持续淘汰已掌握或过难的任务，保持池内样本始终处于高梯度区域。

## 实验
在BFCL V3多轮测试集上，以Qwen3-4B-Instruct为基模型，起始仅400个人工种子，活跃池～800样本，RODS取得56.00%整体准确率，显著优于固定数据RL（50.00%）与环境增强EnvTuning（50.50%），与使用17K离线合成数据的FunReason-MT-4B（56.50%）相当，数据效率提升约20倍。消融实验证实连贯重写（-5.13%）和边界检测（-4.75%）贡献最大，且方差峰值在边界区约2倍。

## 要点
“在哪里合成数据”比“合成多少”更重要——在模型能力边界上动态生成少量高质量样本，比大规模盲目静态合成更高效。
