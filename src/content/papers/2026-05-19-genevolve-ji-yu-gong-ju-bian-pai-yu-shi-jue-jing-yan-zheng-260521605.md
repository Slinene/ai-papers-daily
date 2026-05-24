---
title: 'GenEvolve: Self-Evolving Image Generation Agents via Tool-Orchestrated Visual
  Experience Distillation'
title_zh: 'GenEvolve: 基于工具编排与视觉经验蒸馏的自进化图像生成智能体'
authors:
- Sixiang Chen
- Zhaohu Xing
- Tian Ye
- Xinyu Geng
- Yunlong Lin
- Jianyu Lai
- Xuanhua He
- Fuxiang Zhai
- Jialin Gao
- Lei Zhu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Meitian
- The Hong Kong University of Science and Technology
- National University of Singapore
arxiv_id: '2605.21605'
url: https://arxiv.org/abs/2605.21605
pdf_url: https://arxiv.org/pdf/2605.21605
published: '2026-05-19'
collected: '2026-05-24'
category: Agent
direction: 自进化图像生成智能体 · 视觉经验蒸馏
tags:
- Image Generation Agent
- Self-Evolution
- Visual Experience Distillation
- Tool-Orchestrated
- On-Policy Distillation
one_liner: 通过对比多条生成轨迹提取结构化视觉经验，以 token 级蒸馏实现图像生成智能体的自进化
practical_value: '- **自进化训练范式可迁移到推荐/对话 Agent**：通过生成多条候选轨迹、对比优劣并蒸馏 token 级监督，可让推荐系统智能体（如对话式购物助手）从交互中自行学会更好的搜索策略、知识激活与工具调用。

  - **工具编排的密集监督替代稀疏奖励**：采用 privileged teacher 提供 token 级差异信号，比标量奖励更精细，可提升 Agent 在复杂工具选择（如商品搜索
  API、图像编辑工具）中的决策质量，适合电商场景中的多步操作。

  - **视觉经验的结构化表示**：将最佳/最差轨迹差异抽象为可学习的“经验”，可借鉴到多模态推荐中大模型对图片、商品的细粒度对比与知识激活。

  - **自建数据与基准的思路**：为业务中缺少训练数据的问题提供了参考：通过构造任务和自动采样轨迹来生成训练信号，可应用于自建垂直领域的 Agent 训练数据集。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：开放域图像生成需智能体主动整合内部知识与外部工具，但现有方法仅用图像级标量奖励，缺乏对搜索、参考选择、技能调用等中间决策的密集反馈。

**方法**：提出 GenEvolve 框架，将每次生成建模为一条工具编排轨迹（证据收集→参考选择→技能调用→prompt 构建）。核心创新为**视觉经验蒸馏**：对同一请求采样多条轨迹，对比最佳与最差，将差异抽象为结构化视觉经验，仅提供给特权教师分支；通过 on-policy 自蒸馏，教师向学生模型提供 token 级监督，使其内化更好的搜索、知识激活、参考选择和 prompt 构造能力，从而无需手工奖励设计即可自进化。同时构建了 GenEvolve-Data 和 GenEvolve-Bench。

**结果**：在多个公开基准及自建基准上显著超越强基线，取得当前图像生成框架的 SOTA。
