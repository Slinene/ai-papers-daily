---
title: Offline-to-Online Creative Optimization with Generative Models and Adaptive
  Testing
title_zh: 从离线到在线：用生成模型与自适应实验优化广告创意
authors:
- Kevin Lee
- Benjamin Letham
- Zhiyuan Jerry Lin
- Elodie Samson
- Eric Onofrey
- Poppy Zhang
- Shawndra Hill
- Eytan Bakshy
affiliations:
- University of Michigan
- Meta
arxiv_id: '2607.23696'
url: https://arxiv.org/abs/2607.23696
pdf_url: https://arxiv.org/pdf/2607.23696
published: '2026-07-26'
collected: '2026-07-28'
category: RecSys
direction: 广告创意优化与自适应实验设计
tags:
- creative optimization
- generative AI
- adaptive testing
- multi-armed bandit
- ranking model
- inference-time critic
one_liner: 用历史A/B数据训排序模型引导创意生成，结合自适应在线实验筛选，AI最佳创意较人工最优提升45%
practical_value: '- **历史实验数据用于生成引导**：将历史 A/B 测试中的创意比较数据训练 Bradley‑Terry 排序模型，在推理时作为“批评者”指导
  LLM 生成变体，而不是直接用排序模型选 Top1 部署。这种用法可迁移到电商商品标题、推送文案的批量生成与筛选。

  - **候选集召回 > 单点精度**：离线评价模型时，改用 Recall@k（如 Top‑30 石板对高表现创意的召回率）取代 Top1 准确率，更适应“生成→在线实验筛选”的两阶段范式。可借鉴到搜索词推荐、广告文案生成的离线评估中。

  - **自适应实验降低试错成本**：在线阶段采用 Thompson 采样的分批自适应实验，能快速识别强势创意并将流量从弱臂移开，相比固定均匀分配可降低约 66%
  的探索遗憾。在电商/广告多臂测试预算有限时，这种批量自适应分配可直接复用。

  - **生成迭代火候控制**：推理时对生成候选只做一次排序再精炼即可获得最大提升，进一步迭代会过拟合到排序模型。在类似“文本梯度优化”的营销文案自动生成中，控制一轮精炼是工程上的有效经验。'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
生成式 AI 使广告创意海量生成成为可能，但可靠评估仍依赖在线实验，可供测试的创意数量（slate 大小）受限，形成了评估瓶颈。如何利用历史 A/B 测试数据，引导生成模型产出高潜力候选集，再由在线实验高效筛选，成为关键问题。

**方法关键点**  
- **离线排序模型训练**：从历史随机实验内提取创意对比对（𝑦𝐴≻𝑦𝐵），训练 Bradley‑Terry 排序模型（基于 Llama‑3.2‑1B+LoRA），用作推理时批评者。  
- **排序指导的生成与精炼**：给定人工种子创意，先让 LLM 生成 5 个变体，用排序模型打分排序；再基于排序结果提示 LLM 生成 5 个新变体（仅一轮精炼），最后合并、去重、重排，形成候选 slate。整个过程冻结生成模型，无需微调。  
- **在线自适应筛选**：使用分批 Thompson 采样实验在线测试 slate，动态把流量分配给当前最优或可能挑战 leader 的创意，快速识别胜者并降低弱创意消耗的流量。
- **评估侧重召回而非精度**：离线评价模型时关注候选集能否“包含”高表现创意 (Recall@k)，而非预测哪个创意一定最优。

**关键实验结果**  
- 主实验：50 臂（10 人工 + 40 AI 精炼），AI 最佳创意的打开率比人工最佳高 **45.1%**。  
- 在线实验结果：排序模型预测的 Top‑1 创意实际仅排第 43 名，但其 Top‑30 石板覆盖了 6 个超过最佳人工创意的变体中的 5 个 (Recall@30 = 83%)。  
- 两个附加实验（推送通知、另一促销邮件）同样验证了 AI 精炼创新领先趋势，提升分别达 **46.7%** 和 **36.2%**。  
- 模拟显示，将 slate 从 Top‑10 扩大到 Top‑30 并配合 Thompson 采样，可使“选中创意超过最佳人工”的概率从 0 上升到 1，且探索遗憾较固定均匀分配 + 只选人工最强创意降低 **66%**。  

**核心启示**：排序模型不应直接挑选唯一赢家，而应帮助生成一个“包含赢家”的候选石板，再让在线自适应实验完成最后的精确选择。
