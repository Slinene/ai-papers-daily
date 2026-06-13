---
title: 'WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with
  Hybrid Interfaces'
title_zh: WeaveBench：面向混合接口计算机使用智能体的长程真实世界基准
authors:
- Wanli Li
- Bowen Zhou
- Yunyao Yu
- Zhou Xu
- Yifan Yang
- Dongsheng Li
- Caihua Shan
affiliations:
- Zhejiang University
- Microsoft Research Asia
- Tsinghua University
arxiv_id: '2606.09426'
url: https://arxiv.org/abs/2606.09426
pdf_url: https://arxiv.org/pdf/2606.09426
published: '2026-06-07'
collected: '2026-06-13'
category: Agent
direction: 计算机使用智能体基准测试
tags:
- Agent Benchmark
- GUI-CLI Hybrid
- Long-horizon Tasks
- Trajectory-aware Evaluation
- Computer-Use Agents
one_liner: 提出长程混合接口（GUI+CLI+代码）智能体基准，揭示轨迹感知评估能纠正纯结果评分的虚高问题。
practical_value: '- 在开发电商运营、数据分析等需跨界面操作的 Agent 时，可借鉴 WeaveBench 的混合接口任务设计思路，将 GUI
  操作（如点击、拖拽）与 CLI/代码执行（如脚本处理、文件验证）耦合进同一个 trajectory，评估端到端编排能力。

  - 轨迹感知评判器（trajectory-aware judge）能检测出 Agent 伪造截图、硬编码结果等捷径行为，该思路可直接用于内部 Agent 评测管线，防止仅凭最终交付物评分导致的指标虚高，提升可靠性。

  - 基准中的任务覆盖软件开发、数据分析、办公自动化等真实职场场景，电商团队可参考其任务构造方法，构建面向商品上下架、报表生成、竞品监控等复杂流程的私有评测集。

  - 观察到的最高通过率仅 41.2% 说明长程混合界面编排仍是重大挑战，提示在业务 Agent 系统中应加强跨界面状态追踪、错误恢复与验证环节的设计，而非单纯依赖模型能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机使用智能体评测常把 GUI、CLI 和代码等接口视为独立的能力维度，忽略了真实工作流中跨接口长程编排的挑战。为此，作者提出 WeaveBench，一个专门衡量智能体在混合接口下完成长周期任务的基准。

**方法**：基准包含 8 个真实职场领域（如软件开发、数据科学、办公自动化）的 114 项任务，每项任务都要求智能体在单条轨迹中交替使用 GUI 观察/动作与 CLI/代码操作。评估在真实 Ubuntu 桌面环境中进行，CLI 智能体运行时集成了一个轻量桌面操控插件。同时，作者设计了轨迹感知的评判器，不仅检查最终交付物、文件、截图、日志，还分析动作序列，探测出伪造视觉证据或硬编码指标等捷径行为。

**结果**：在主流模型-运行时组合中，最佳通过率仅为 41.2%，基准远未饱和。轨迹感知评判器揭示，仅基于结果的评分会显著高估智能体性能，证明了细粒度评估的必要性。
