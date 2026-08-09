---
title: 'Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation
  Routing for Web Agents'
title_zh: 路由在最需要时最难学：Web Agent 表征路由的界限
authors:
- Jiaming Wei
- Zekun Wu
- Adriano Koshiyama
- Maria Perez-Ortiz
affiliations:
- University College London
- Holistic AI
- UCL Centre for Artificial Intelligence
arxiv_id: '2608.06171'
url: https://arxiv.org/abs/2608.06171
pdf_url: https://arxiv.org/pdf/2608.06171
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent 表征路由与成本优化
tags:
- routing
- web agents
- observation modes
- cost-quality tradeoff
- label noise
- representation selection
one_liner: 多观察模式的路由收益被重运行噪声夸大，弱智能体因标签不足难以学习路由
practical_value: '- 多表征系统（如文本+图像+融合）可借鉴路由思路：按任务特征动态选择最优表征，但需注意重运行噪声（12-14%）会夸大收益，评估时务必用足够重复实验校准。

  - 当基础智能体成功率低时，路由训练样本极少（路由标签源自智能体自身成败），此时应先提升智能体核心能力再引入路由，避免“鸡生蛋”困境。

  - 成本-质量权衡策略可直接复用：仅将基础模式无法解决的任务发送到最强模式，可在不降低成功率前提下节省 9.5-30.6% 成本，适合电商 Agent 多级调用（如廉价
  KV cache vs 完整生成）。

  - 任务文本作为零成本路由规则（如关键词过滤）效果有限且脆弱，建议谨慎使用，优先构建基于置信度的级联路由。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
Web Agent 常用文本（a11y tree）、截图或融合表征，但不同任务的最优观察模式可能不同。能否动态路由以提升性能与成本？  
**方法**  
在 VisualWebArena 和 WebArena 的 8 个站点-模型组合（cells）上测量 6 种观察模式，分析模式互补性、重运行噪声（同模式同任务重跑结果变化 12-14%），计算理想路由（oracle）收益和成本界。随后测试 5 种路由策略（模式选择、何时用强模式、基于任务文本的零成本规则、置信度级联、成本分层），评估是否稳健优于固定最佳模式。  
**关键结果**  
1. 重运行噪声使 oracle 收益膨胀，实际可实现的改进为：仅将未解决任务发送到最便宜模式，成本节省 9.5-30.6% 而成功率不变。  
2. 所有路由策略均未稳健击败固定最优模式，仅在数据最稀疏的 cell 有脆弱优势。  
3. 核心障碍：路由监督信号来自智能体自身决策，智能体越弱（成功率低），路由可用的标签越少，而恰是这些场景路由最急需。标签供给与路由机会相关性达 0.95，更强的基础智能体可能逆转此结论。
