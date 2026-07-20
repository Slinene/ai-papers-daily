---
title: 'Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video
  QA'
title_zh: 将视频搜索为树：自校正智能体实现长视频锚定问答
authors:
- Ce Zhang
- Ziyang Wang
- Yulu Pan
- Oluwatumininu Oguntola
- Pranav Wagh
- Qiyu Wu
- Hiromi Wakaki
- Mohit Bansal
- Gedas Bertasius
affiliations:
- University of North Carolina at Chapel Hill
- Sony
arxiv_id: '2607.16189'
url: https://arxiv.org/abs/2607.16189
pdf_url: https://arxiv.org/pdf/2607.16189
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 自我纠正树搜索智能体实现精准长视频QA
tags:
- Grounded Video QA
- Tree Search
- Self-Correcting Agent
- Hierarchical Search
- Reinforcement Learning
- Long Video Understanding
one_liner: 构建非均匀时间树并训练智能体通过显式回溯操作实现自纠正搜索，显著提升长视频问答与定位性能
practical_value: '- **长序列定位回溯机制可迁移**：电商场景中用户行为序列、商品介绍视频等长序列理解任务，可借鉴树形结构+显式回溯操作，使模型能从错误聚焦中恢复，精准定位关键片段（如商品使用痛点瞬间）。

  - **层次化搜索架构**：将长内容按语义边界预构建非均匀树，再训练智能体导航，可用于构建“商品视频智能导购”——用户提问时系统自动深入相关片段，并能回溯避免过早锁定错误区间。

  - **合成纠错轨迹训练范式**：通过故意构造走入错误分支再纠正的轨迹进行SFT+RL，可提升推荐Agent在复杂交互中的鲁棒性，使模型学会自我纠错，尤其适用于多轮对话式推荐。

  - **离散操作空间设计**：定义有限的原子操作（zoom_in/out/shift/answer），使策略学习更可控，可借鉴到面向搜索/推荐的Agent动作集设计，让模型在复杂检索环境中进行结构化探索。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有长视频锚定问答（Grounded LVQA）的智能体方法缺乏显式的从细粒度回到粗粒度的回溯能力，导致过早收敛且无法纠正早期错误。论文提出VideoTreeSearch（VTS），将任务建模为在自适应时间树上的迭代自校正搜索。

**方法关键点**：
- 基于视觉场景边界构建非均匀时间树，每个节点对应一个语义连贯的片段。
- 定义四个离散导航操作：zoom_in（深入子节点）、zoom_out（返回父节点）、shift（切换同级节点）和answer（输出答案及时刻），显式暴露回溯机制。
- 通过轨迹合成流水线生成包含故意走入错误分支再恢复的多步路径，用于监督微调，随后通过强化学习使用定位和答案准确率奖励进行策略优化。

**结果**：在CG-Bench上mIoU提升+12.5，Haystack-Ego4D上T-F1提升+7.4，均超越最强先验方法；迁移至通用长视频QA（Video-MME, MLVU, LVBench）准确率最高提升+7.1。消融证实自纠正层次搜索是增益核心，移除自适应下降或显式回溯均导致性能大幅下降。
