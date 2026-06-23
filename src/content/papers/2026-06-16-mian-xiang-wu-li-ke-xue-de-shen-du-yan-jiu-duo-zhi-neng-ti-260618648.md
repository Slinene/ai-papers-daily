---
title: 'Deep Research in Physical Sciences: A Multi-Agent Framework and Comprehensive
  Benchmark'
title_zh: 面向物理科学的深度研究：多智能体框架与综合基准
authors:
- Yigeng Jiang
- Tengchao Yang
- Taoyong Cui
- Jiaxing Wan
- Yuan Wang
- Weida Wang
- Zhiyu Liu
- Chuyi Peng
- Binzhao Luo
- Maoli Gao
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Xiamen University
- Chinese Academy of Sciences
- University College London
- Wuhan University
arxiv_id: '2606.18648'
url: https://arxiv.org/abs/2606.18648
pdf_url: https://arxiv.org/pdf/2606.18648
published: '2026-06-16'
collected: '2026-06-23'
category: MultiAgent
direction: 多智能体科学推理加速
tags:
- Multi-Agent
- Scientific Reasoning
- Benchmark
- LLM
- Self-Verification
- Cost Reduction
one_liner: 提出物理科学深度研究基准PhySciBench，并设计多智能体框架DelveAgent，通过自适应规划、双粒度记忆和分层反思显著提升准确率并降低成本
practical_value: '- **模块化多智能体设计可迁移至搜索推荐多步推理**：DelveAgent 的自适应规划循环（Adaptive Planning
  Loop）可直接用于电商搜索中的复杂查询分解与动态规划，比如商品对比、多方约束推荐等需要多步推理的场景。

  - **双粒度记忆（Dual-granularity Memory）提升长对话一致性**：短期记忆存交互轨迹，长期记忆存领域知识，可借鉴到用户对话系统中，跨 session
  保留用户偏好与领域事实，避免重复询问。

  - **分层反思（Hierarchical Reflection）实现业务规则自检**：物理基础反思机制强制模型验证结果是否符合物理定律，对应电商场景可设计“利润约束反思”“库存约束反思”等模块，降低幻觉，提升推荐合理性。

  - **成本降低至 1/3 的工程启发**：DelveAgent 在提升准确率的同时大幅降低推理成本，其架构中的知识检索、记忆复用等降本手段，可复用于线上 Agent
  的调用优化，减少 LLM 重复推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：深度研究代理在物理科学中具有加速研究的潜力，但缺乏全面评估其能力的基准。现有系统在长程推理、知识迁移和自验证上存在明显短板。

**方法**：
1. 提出 **PhySciBench**——包含 200 个由专家策划的物理、化学问题，覆盖 6 类真实科研任务。
2. 基于失败分析，设计 **DelveAgent** 多智能体框架：
   - **自适应规划循环**：动态调整子任务分解与执行顺序；
   - **双粒度记忆**：短期记忆存当前推理轨迹，长期记忆存领域知识；
   - **分层物理基础反思**：要求代理在每一步用物理定律自验证，错误时触发重规划。

**结果**：
- 在 PhySciBench 上，最强基线 Gemini Deep Research 仅 33.5% 准确率；DelveAgent 提升最高 7.5 个百分点。
- 推理成本降至最强基线的约三分之一。
- 在另外三个科学基准上也表现出跨域泛化能力。
