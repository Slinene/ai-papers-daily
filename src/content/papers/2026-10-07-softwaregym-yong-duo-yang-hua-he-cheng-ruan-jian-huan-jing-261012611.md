---
title: 'SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized
  Software Environments'
title_zh: SoftwareGym：用多样化合成软件环境规模化训练计算机使用智能体
authors:
- Tian Jin
- Wenhao Wang
- Jing Kang
- Haoting Shi
- Rui Ye
- Yijun Lu
- Siheng Chen
affiliations:
- Shanghai Jiaotong University
- Zhejiang University
arxiv_id: '2610.12611'
url: https://arxiv.org/abs/2610.12611
pdf_url: https://arxiv.org/pdf/2610.12611
published: '2026-10-07'
collected: '2026-10-12'
category: Agent
direction: 计算机使用 Agent 环境合成与训练
tags:
- Computer-Use Agent
- Synthetic Environment
- GUI Benchmark
- Training Data
- Generalization
one_liner: 提出 SoftwareGym 自动化合成 GUI 软件环境及基准，训练 CUA 后在 OSWorld 上 Pass@3 提升 15.58 个百分点
practical_value: '- 对需要构建 Agent 操作业务系统（如电商后台、广告投放平台）的团队，可借鉴 SoftwareGym 的环境合成管线：自动生成多样化
  GUI + 迭代修复功能，低成本构造大规模仿真环境，避免每个内部系统手工集成。

  - 用合成环境收集轨迹做 SFT/RL 训练可显著提升 Agent 在未见过的真实系统上的泛化能力（OSWorld Pass@3 +15.58），适合跨平台/多工具
  Agent 的冷启动。

  - SoftwareGym-Bench 的 12 类 120 任务设计思路可迁移到电商工作流评测：覆盖不同操作类型、验证功能正确性而非仅界面匹配；GUI 任务通过率可作为应用可用性筛选指标。

  - 注意：合成应用与真实业务系统仍有差距，建议混合少量真实环境数据做适配；该方法更适合作为预训练/基础能力阶段，而非替代真实场景微调。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：训练计算机使用 Agent (CUA) 需要大规模、多样、可靠的软件交互环境；原生应用集成成本高且易过拟合，浏览器环境交互深度有限。

方法关键点：SoftwareGym 自动合成 GUI 软件环境，分三步——生成结构多样设计、实现为可运行应用、GUI 评估+迭代修复保证功能可靠。基于此合成 182 个应用（12 类），平均 GUI 任务通过率 91.5%；构建 120 任务基准 SoftwareGym-Bench；收集轨迹用于 CUA 训练。

关键结果：训练后模型在严格域外 OSWorld 上 Pass@3 从 41.39% 提升到 56.97%，在 SoftwareGym-Bench 上达 40.0%，证明合成环境可提供可扩展且可迁移的训练监督。
