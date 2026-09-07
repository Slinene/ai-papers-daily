---
title: 'Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for
  LLM Agents'
title_zh: Trace2Tower：面向LLM Agent的转移感知多层级技能特征谱归纳
authors:
- Jiazheng Sun
- Boyu Yang
- Binhao Yuan
- Mingxuan Li
- Xin Peng
affiliations:
- College of Computer Science and Artificial Intelligence, Fudan University
arxiv_id: '2609.05261'
url: https://arxiv.org/abs/2609.05261
pdf_url: https://arxiv.org/pdf/2609.05261
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 经验学习 · 层级技能归纳
tags:
- LLM Agents
- Skill Hierarchy
- Spectral Clustering
- Experience Reuse
- Trajectory Mining
- Graph Contrastive
one_liner: 将Agent轨迹经事件抽象、成功/失败对比图与谱分解归纳为三层技能塔，ALFWorld成功率87.31%
practical_value: '- 把用户购物/搜索轨迹先按子目标切分为 canonical events 并做 typed arguments 去实体，可把不同商品、query
  实例对齐到同一行为单元；在电商埋点中可构建统一的 event graph。

  - 成功/失败对比图与参数自由的 failure suppression 变换 g(x,y)=x²/(x+y) 很有工程价值：只需成功/失败转移计数，不需要调权，能自动抑制仅在失败路径上高频但无转化贡献的行为。

  - 三层技能塔（action/procedure/strategy）对应电商可解释的交互链路：单品操作 → 购物流程（搜索-浏览-加购-支付）→ 意图达成策略；部署时按
  context 预算约束检索，可控制 prompt/上下文成本。

  - 上线后反馈驱动的图编辑（split/merge/promote/downweight）可在不重新训练/归纳的情况下修正技能结构，适合持续迭代的推荐/Agent
  系统。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现有 LLM Agent 经验复用多基于完整轨迹检索或扁平技能总结，忽略行为间的时序依赖和成功/失败条件拓扑。原始轨迹冗长、任务相关、含失败分支，直接复用易传播错误经验。因此需要从多样轨迹中提炼紧凑可靠的行为结构，保留有效决策模式，去除任务噪声和失败捷径。

## 方法关键点
- **事件抽象**：将连续步骤按局部目标切分为 canonical events，typed arguments 去实体，压缩实例级语言变化，同时保留原始事件顺序以估计转移。
- **转移感知 EigenTrace 图**：节点为 canonical events，有向边几何平均整合语义兼容、成功/失败转移依赖、结果兼容三个信号；edge mask 只保留观察到的转移，evidence strength 折扣弱证据。
- **对比谱分解**：用参数自由的失败抑制变换 `¯A = A_+² / (A_+ + A_-)` 抑制失败主导边；对称化后构建归一化拉普拉斯矩阵，按连通分量做特征分解，最大 eigengap 自动选择 procedure 数量，特征向量聚类成 procedure skills。
- **三层技能塔**：action 层为 canonical events，procedure 层为谱聚类结果，strategy 层由压缩 procedure 序列、SCC 折叠后保留成功支持的最大路径构建；部署时按预算约束检索，High-only 与 Full 两种策略。
- **反馈 refinement**：上线后支持 split/merge/promote/downweight 四类图编辑，无需重新归纳即可修正技能结构。

## 关键实验
在 ALFWorld 134 个 unseen 任务、WebShop 100 任务上，从 1240/400 条轨迹归纳技能。ALFWorld Full 达 87.31% 成功率、10.35 步、0.26 无效动作，显著优于 ExpeL 81.59、SkillX 78.61、No-Skill 46.27；WebShop exact success 50.67%。消融显示，去掉 transition 掉至 70.15%，去掉 outcome 或 contrastive 均掉至 73.88%。跨模型 GPT-5.4 Tower + Flash User 达 88.06%；反馈细化使 frozen Tower 从 80.42% 提升到 84.58%。

## 最值得记住的一句话
把成功/失败对比信号与时序转移显式建模，再用谱分解提取稳定行为模式，比仅按语义相似度积累技能更可靠。
