---
title: 'WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection'
title_zh: 自进化多智能体框架用于全 AI 生成视频取证检测
authors:
- Yipeng Du
- Yuxi Li
- Ying Zhang
- Chong Sun
- Chen Li
- Jing Lyu
- Ying Tai
affiliations:
- Nanjing University
- WeChat Vision, Tencent Inc.
arxiv_id: '2611.21373'
url: https://arxiv.org/abs/2611.21373
pdf_url: https://arxiv.org/pdf/2611.21373
published: '2026-11-15'
collected: '2026-11-21'
category: MultiAgent
direction: 多智能体自进化与双时间尺度RL
tags:
- Video Forensics
- Multi-Agent
- Reinforcement Learning
- Self-Evolving
- Policy Optimization
- AI-Generated Detection
one_liner: 自进化多智能体框架协调可进化检查器库，以双时间尺度RL在AI生成视频检测上达95.2%，超先前最强9个点
practical_value: '- 内容安全/电商场景：主控 Agent 动态选择检查伪影类型、时间窗和停止时机，比固定多智能体流程更灵活，可迁移到商品短视频、直播切片的深度伪造检测与审核。

  - DTPO 双时间尺度更新适合推荐 Agent 系统：策略主控快速在线 RL 调整决策，领域专家/工具子模型慢速迭代更新，避免频繁更新不稳定，同时持续增强专家能力。

  - ForenCue-30K 的标注思路（角色特定 artifact 标注 + 交互轨迹）可复用到多模态内容质量审核、虚假评论/拍摄素材取证数据集构建，同时监督单步检查和协调关系学习。

  - 将最终判断 grounding 到局部证据（如“0–8.0s 线缆弯折异常”）可作为推荐解释、审核理由生成的范式，提高可解释性和业务可操作性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频生成技术快速发展，但现有检测方法要么依赖单次 CoT 推理，容易忽略短时或局部伪影；要么采用预定义多智能体工作流，检查项选择灵活性不足；且仅优化调查策略无法直接提升固定检查器的取证能力。

**方法关键点**：WeVisForensics 采用主 investigator 协调自进化 inspector 子智能体库，覆盖视觉和音频线索。investigator 动态决定检查哪种伪影类型、在哪个时间窗检查、何时结束；两类智能体通过互动获得共享反馈。DTPO 双时间尺度策略优化中，快速强化学习更新 investigator，较慢速度精炼 inspectors，并利用标注 artifact intervals 让 inspectors 报告此前忽略的细微伪影。同时构建 ForenCue-30K 数据集，包含角色特定取证标注和交互轨迹，用于监督单次检查及协调行为。

**关键结果**：在 in-domain、out-of-domain 和 agentic benchmarks 上平均检测准确率 95.2%，比最强先前检测器高 9.0 个百分点，且判断依据明确落到局部证据。
