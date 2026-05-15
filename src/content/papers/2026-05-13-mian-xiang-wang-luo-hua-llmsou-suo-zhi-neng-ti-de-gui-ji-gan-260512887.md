---
title: 'EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents'
title_zh: 面向网络化LLM搜索智能体的轨迹感知证据生态系统
authors:
- Hengwei Ye
- Jiasheng Mao
- Zhenhan Guan
- Zheng Tian
affiliations:
- ShanghaiTech University
arxiv_id: '2605.12887'
url: https://arxiv.org/abs/2605.12887
pdf_url: https://arxiv.org/pdf/2605.12887
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- Web Agents
- GEO
- RecSys
- Trajectory
- Evidence Ecosystem
one_liner: 提出生态系统生成引擎优化视角，通过导航入口与异构支持页面协同引导智能体浏览轨迹，提升目标产品推荐成功率
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

现有 Generative Engine Optimization (GEO) 研究主要关注单网页内容改写以提升在生成式引擎中的可见性。然而，面向 Web 的 LLM 搜索智能体（如 WebGPT、Search-R1）并非仅依据单一文档作答，而是通过多轮搜索、链接爬取、查询重构和跨源证据综合来生成最终答案。影响力既来自页面内容，也取决于页面如何被组织、链接，以及智能体在浏览轨迹中何时遭遇这些页面。因此，需要从生态系统层面重新定义 GEO，关注协调的证据环境如何塑造智能体的搜索与综合行为。

## 方法关键点

- **EcoGEO 视角**：将 GEO 从单页优化问题提升为环境级影响问题，研究证据生态系统的组织方式如何改变 LLM 智能体的信息获取轨迹。
- **TRACE 生态系统**：为每个目标产品构建一个协调证据图，包含：
  - 一个导航入口页面（评测导向的指南页），提供决策相关属性汇总和指向下游页面的结构化链接；
  - 六个角色化支持页面（官方、评测、专家、新闻、论坛、社交），通过共享术语、一致的产品属性与交叉引用维持证据一致性。
- **控制化暴露协议**：采用“9+1”搜索环境，将合成目标相关结果固定插入搜索结果列表第 5 位，确保初始曝光机会一致；后续搜索中，目标特定查询直接返回支持页面池，非目标查询则从 Google API 抽取干扰项并插页。
- **与页面级 GEO 对比**：单页面基线、C-SEO、E-GEO、AutoGEO 均只提供单页优化，而 TRACE 提供多页面协调环境。

## 关键实验与结果

- **基准 OPR-Bench**：从 SafeSearch、E-Commerce、E-GEO 中筛选出 3,124 个推荐意图查询，并配以虚构但合理的目标产品，实现安全、可控、可复现评估。
- **测试设置**：使用 GPT-5.1 作为搜索骨干，每实例最多 5 次搜索与 5 次爬取，通过 Google Search API 提供开放网络干扰项。
- **最终推荐率**：TRACE 在 SafeSearch、E-Commerce、E-GEO 上分别达到 67.2%、71.9%、73.9%，比最优页面级基线绝对提升 14.9–31.3 个百分点。
- **轨迹指标**：TRACE 显著提高初始目标结果爬取率（例如 E-Commerce 上 61.2% vs. 最高 43.8%）、目标特定二次搜索率（23.1% vs. 最高 18.2%）和内部链接爬取率（19.0%，其他方法为 0）。
- **消融实验**：强制首爬后，协调多页面比独立支持页面效果更好，而导航式入口进一步带来增益，内部链接爬取率从 0% 跳至 29.7%，表明导航设计会改变智能体的证据遍历行为。

## 总结

GEO 不应再只盯着单页排名，而要转向设计可导航的证据生态——通过入口页面和内部链接网络，主动引导 LLM 智能体的多步证据获取轨迹，这才是影响最终生成内容的关键。
