---
title: 'Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities'
title_zh: 智能体式工件创建：系统、评估、原则与机会
authors:
- Tianfu Wang
- Zhezheng Hao
- Xilin Xia
- Lixin Liu
- Mengkang Hu
- Hongzhang Liu
- Xi Chen
- Ziyan Liu
- Xiankun Lin
- Weijia Zhang
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Zhejiang University
- University of Science and Technology of China
- Tsinghua University
- The University of Hong Kong
arxiv_id: '2608.28122'
url: https://arxiv.org/abs/2608.28122
pdf_url: https://arxiv.org/pdf/2608.28122
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Agent 智能体工件创建综述
tags:
- Agentic Artifact Creation
- Survey
- Runtime Verification
- Construction Policy
- Evaluation
- Benchmarks
one_liner: 综述智能体式工件创建系统，提出有状态构建、运行时验证与反馈重定向的原则
practical_value: '- 在广告创意/商品文案生成中，把生成结果建模为可操作状态，引入运行时验证（如自动检查品牌合规、卖点覆盖）并针对失败局部修复，避免每次全量重生成

  - 任务分解需权衡局部复杂度和重组成本：对于强耦合的推荐解释或营销物料，分解过细反而增加协调开销，适合采用分层但保留共享上下文的 agent 架构

  - 评估 agent 生成质量时，不要只依赖 LLM 作为评判者，因其可能与生成器共享偏好盲区；应加入业务指标、用户行为或人工抽检等独立信号

  - 变更后要重新验证受影响状态，例如广告文案修改关键词后，需重新检查页面落地页一致性、合规性和转化预期'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：生成式模型能快速产出草稿和组件，但难以直接形成完整可靠的交付物；实际影响取决于如何将生成片段转化为可依赖的工件。

**方法关键点**：综述将 Agentic Artifact Creation 定义为有状态构建：AI 系统实质构建或修订交付物，中间观察结果会重定向后续工作。功能上连接工件的操作表示、构建策略和运行时验证，反馈可定向修改。覆盖 259 篇工作（230 个系统 + 29 个基准），比较六个工件家族，并分别分析应用设置和评估实践。核心发现：跨家族挑战不仅来自模态差异，更取决于决策耦合度和失败在可修复阶段的可见性；任务分解降低局部复杂度但增加协调与重组成本；学习型评判若与生成器共享偏好，独立证据价值有限。提出三条原则：显式管理承诺与责任、将反馈转化为定向修复、变更后重新验证受影响状态。

**关键结果数字**：综述 259 篇文献，涵盖 230 个 agentic artifact construction 系统与 29 个基准。
