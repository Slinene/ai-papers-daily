---
title: 'AgenticGen: Reward-Guided Agentic Video Generation for Advertising'
title_zh: 奖励引导的 Agentic 广告视频生成框架
authors:
- Xingyuan Bu
- Chengru Song
- Hao Zhou
- Tao Zhou
- Dong Li
- Wei Li
- Shilong Li
- Hao Shi
- Yongxin Guo
- Donghao Zhou
affiliations:
- ByteDance
- Tsinghua University
- The Chinese University of Hong Kong
arxiv_id: '2609.09187'
url: https://arxiv.org/abs/2609.09187
pdf_url: https://arxiv.org/pdf/2609.09187
published: '2026-08-30'
collected: '2026-09-10'
category: Agent
direction: Agentic 生成 · 在线反馈 RL
tags:
- Agentic Video Generation
- DPO
- GRPO
- Reward Modeling
- Advertising
- Online A-B
one_liner: 将广告视频生成拆成策略选择与草稿生成，用在线反馈训练性能与质量奖励并通过DPO+GRPO优化，在TikTok显著提升CTR/CVR/Advv
practical_value: '- **拆解生成管线，给业务反馈提供可优化抓手**：不要端到端直接出最终创意，而是拆成「策略选择 + 草稿生成」两个阶段，分别用
  process reward 和 outcome reward 监督。做电商广告文案/短视频生成时可借鉴：先让模型选择「改 BGM/加 hook/混剪」等策略，再生成具体脚本，使线上
  CTR/CVR 能分别指导中间决策和最终内容。

  - **用公平曝光管道收集偏好数据**：自然流量中创意的 CTR 混杂召回/排序偏置，AgenticGen 采用同一产品下 N=12 个候选随机曝光、绕过排序、至少
  1000 曝光才有效的 impression-balanced 管道。创意优选和生成式广告系统的 reward 建模都应优先采用此类剥离偏置的数据协议，再构造同产品上下文内的
  pairwise BT 偏好。

  - **性能 reward 与质量 rubric 必须互补**：单独用 CTR 学 reward 容易偏向 clickbait；引入专家 rubric 并用「三人一致才保留」的人工标注训练质量
  reward，GRPO 融合权重（文中 λ_draft=0.6 偏性能）可同时保住在线效果和创作质量。业务上可复制：在线指标 reward + 平台内容规范 reward
  一起进 RL。

  - **多模态特征工程与稳定训练 trick**：性能 reward 输入视频帧、音频/ASR、结构化故事线、广告特征；音频带来最大单点增益（+1.88%）。DPO
  加 NLL 正则（λ=0.2）防格式崩坏，GRPO 中多 reward min-max 归一化并用 group-relative advantage；这些都可直接迁移到广告创意生成和评估。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
广告视频生成不仅是合成任务，更是产品条件下的推理问题，成功由线上业务指标衡量。现有视频基础模型能生成真实片段，但不会优化「如何把产品变成有效广告」，也无法从线上反馈改进后续生成。因此需要可学习框架，将在线业务反馈闭环到生成决策。

### 方法关键点
- 将生成拆为两个可训练推理阶段：**策略选择**（从策略目录中选择资产编辑、参考引导生成、跨资产混剪等）+ **草稿生成**（将策略转为可执行草稿调用视频模型和渲染工具）。
- 用 Qwen3-VL-8B-Thinking 做推理 VLM，SFT 初始化后部署到流量平衡的曝光管道收集反馈；每组 N=12 个视频随机曝光，至少 1000 曝光才作为有效训练样本，减少召回/排序偏置。
- 训练两个互补 reward：**性能 reward** 基于同产品上下文内的 Bradley-Terry 成对比较，输入视频帧、音频/ASR、结构化故事线、广告特征；**rubric reward** 基于人工标注（三人一致才保留）对齐质量标准，捕捉 clickbait 和缺陷。
- 优化流程：先用 DPO 离线偏好数据预热两个阶段，加 NLL 正则稳定格式；再用 GRPO 做在线策略优化，策略选择用全局+局部 process reward，草稿生成用性能+rubric outcome reward，min-max 归一化后融合。

### 关键实验
- 性能 reward pairwise 在 impression-balanced 验证集准确率 60.85%，比 pointwise 高 7.93%；加入音频、storyline、广告特征逐步提升，音频增益最大 +1.88%。
- Rubric reward SFT 将人工标注准确率从 55.40% 提到 69.50%，对线上偏好也有正向迁移（49.20→53.30）。
- DPO 使策略选择偏好准确率 49.72→56.48，草稿生成 50.64→58.34。
- GRPO 融合 performance 与 rubric reward 获得 perf win rate 60.52%、rubric win rate 55.86%、平均 58.19%，优于单独使用任一 reward。
- TikTok 线上 A/B：SFT 相比 Pre-Agent 提升 CTR +3.48%、CVR +2.30%、Advv +9.83%；RL(DPO+GRPO) 相比 SFT 再提升 CTR +2.72%、CVR +2.63%、Advv +9.61%。

**最值得记住**：把生成任务拆成可被业务反馈监督的中间推理步骤，并用去偏曝光管道收集偏好数据，是在线广告创意 RL 能稳定起效的关键。
