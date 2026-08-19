---
title: 'VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?'
title_zh: VibeWorlding：多模态智能体能端到端构建3D开放世界吗？
authors:
- Yansong Ning
- Jingwen Ye
- Zhongkai Wu
- Yang Sun
- Yiqin Zhu
- Xingyi Li
- Weidong Zhang
- Hao Liu
affiliations:
- AI Thrust, HKUST(GZ)
- TEG AIPD, Tencent
arxiv_id: '2608.15265'
url: https://arxiv.org/abs/2608.15265
pdf_url: https://arxiv.org/pdf/2608.15265
published: '2026-08-14'
collected: '2026-08-19'
category: Agent
direction: 多模态 Agent 3D 世界构建
tags:
- Multimodal Agents
- 3D World Building
- RL Post-training
- Benchmark
- MCP Tools
- MLLM
one_liner: 提出 VibeWorlding 基准与训练框架，用多模态 RL 让开源 MLLM 在 3D 开放世界构建任务上超越闭源前沿模型。
practical_value: '- **rubric-based verifier 可迁移到 agent 闭环评估**：把奖励分解为“可行性”和“意图满足”两类维度，用规则检测器（如碰撞检测）和
  LLM 评分结合，能低成本扩展为 RL reward service，适合需要自动化评估长轨迹 agent 的场景。

  - **MCP 工具化沙箱**：将检索、编辑、渲染等异构工具统一为 MCP 接口，方便 agent 调用并与 RL 训练环境解耦；可直接复用到商品图片生成、页面布局、活动落地页等
  agent 工作流。

  - **反向合成数据降低标注成本**：人工构建少量种子世界，再反向生成大量多样化用户查询，可迁移到电商场景生成“意图→页面/推荐”训练对，减少人工标注。

  - **RL post-training 可针对性突破能力瓶颈**：当闭环评估显示模型在特定环节（如编辑）弱，针对性 RL 训练能让开源模型超越闭源前沿，提示针对业务闭环的
  agent RL 值得投入。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 3D 开放世界构建多在理想化简单查询上评估，难以系统分析多模态 agent 如何理解用户意图、使用 3D 工具、推理文本与视觉信息；缺少开源框架也阻碍训练方法研究。

**方法关键点**：构建 VWE-Bench，含 2,616 个高质量 3D 资产、323 个人工标注种子 3D 世界、6,828 个反向合成的多模态用户查询，分为有 GT 的 verified 与带 rubrics 的 unverified。开发 VibeWorlding-Gym：将资产检索、编辑、图像渲染统一为 MCP tools 的 sandbox 环境；rubric-based verifier 结合物理可行性（碰撞检测）和意图满足验证，支撑公平评估与可扩展 RL reward 服务。

**关键结果**：前沿 MLLM 成功率均低于 60%，瓶颈在精确 3D 世界编辑；RL 后训练可缓解此弱点，开源 VibeWorlder-8B 与前沿闭源模型相当，旗舰 VibeWorlder-30B-A3B 取得所有模型最佳 Pass@1。
