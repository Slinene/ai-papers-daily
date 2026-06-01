---
title: 'SAGE: A Novelty Gate for Efficient Memory Evolution in Agentic LLMs'
title_zh: SAGE：一种用于智能体 LLM 记忆高效演化的新颖性门控
authors:
- Sijia Wang
- Dhanajit Brahma
- Ricardo Henao
affiliations:
- Duke University
arxiv_id: '2605.30711'
url: https://arxiv.org/abs/2605.30711
pdf_url: https://arxiv.org/pdf/2605.30711
published: '2026-05-29'
collected: '2026-06-01'
category: Agent
direction: Agent 记忆写端控制 · 新颖性检测
tags:
- Memory Evolution
- Novelty Detection
- Agentic LLM
- vMF
- Write-side Control
one_liner: 用 von Mises-Fisher 密度估计为智能体记忆演化构建轻量新颖性门控，仅将不确定案例交给 LLM 合并，显著降低写入成本。
practical_value: '- **记忆写入的轻量决策层**：电商 Agent 需要持续更新用户偏好、商品特征等长期记忆，可以借鉴 SAGE 的 vMF 密度估计门控，用闭式得分快速判定新信息是
  ADD / NOOP，仅对边界案例调用 LLM，大幅降低在线写入成本。

  - **自适应阈值跟踪存储密度**：推荐系统的知识库（如用户兴趣表示）会动态增长，可采用基于 PCA 投影体积的密度代理自动调整阈值，避免固定阈值在稀疏/密集状态下过松或过严，该方法无需后端大模型即可实现。

  - **模块化预过滤插件**：SAGE 展示的二进制 NOOP 门可作为现有记忆框架（如 A-Mem、Mem0）或通用 RAG 写入路径的前置过滤器，只需标定一个阈值即可跳过
  16–18% 的冗余 LLM 调用，且质量损失可忽略，适合在现有 Agent 架构中快速部署。

  - **利用嵌入几何替代语义判断**：在检索/推荐场景中，类似的思想可用于候选物品的新颖性检测（如是否已存在于某集合中），用角相似度聚合取代单个最近邻比较，提高对密集区域的区分能力。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：智能体 LLM 在长期交互中需要不断将新事实写入记忆，现有系统（Mem0、A-Mem 等）将其全部委托给 LLM 进行路由决策，导致写入路径成本极高。作者认为，记忆演化本质上是一个新颖性检测问题——应当通过轻量计算分辨明显新事实、明显冗余事实，仅让不确定性案例触发昂贵的 LLM 合并。

**方法**：提出 SAGE（Spherical Adaptive Gate for memory Evolution）。对每个候选事实，基于当前记忆嵌入在单位超球面上的 von Mises-Fisher 核密度估计计算支持度，转换为新颖性得分。采用自适应阈值：以 PCA 投影后坐标范围乘积估计存储体积，结合记忆数量形成密度代理 ρ_t，阈值 τ_t = τ_min + τ_0 e^{-λρ_t} 随密度升高而下降，并做 EMA 平滑。根据阈值和边距 δ，将候选路由到三种动作：新颖得分高于 τ_t+δ 直接 ADD，低于 τ_t 直接 NOOP，落入区间则触发 LLM UPDATE。此外还提供可插入现有写入路径的二进制 NOOP 门，仅用固定阈值决定是否跳过写入。

**关键结果**：在 LoCoMo 长期对话记忆基准上，SAGE 对比 Mem0 在全部 7 个开源主干上取得平均 token-F1 最优；在 GPT-4o-mini 上添加阶段成本降低 3.4 倍，延迟降低 2.5 倍，且 judge 得分仅微弱下降（平均 -1.3 分）。作为 A-Mem 的预过滤器，固定阈值门在 5 个模型中跳过 16–18% 的 LLM 写调用，token-F1 变化 ≤ 0.5%。**核心一句话：将记忆演化重铸为新颖性检测，用几何门控替代大部分 LLM 决策，在几乎不损质量的前提下大幅降低写入开销。**
