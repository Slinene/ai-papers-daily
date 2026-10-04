---
title: 'DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration'
title_zh: 声明式多智能体编排的数据视频生成系统
authors:
- Yupeng Xie
- Zhenyang Wang
- Liangwei Wang
- Jiayi Zhu
- Zhouan Shen
- Yuyu Luo
arxiv_id: '2609.33403'
url: https://arxiv.org/abs/2609.33403
pdf_url: https://arxiv.org/pdf/2609.33403
published: '2026-09-26'
collected: '2026-10-04'
category: MultiAgent
direction: 多智能体编排 · 声明式生成 · 数据视频
tags:
- Multi-Agent
- Declarative Specification
- Data Video
- Data Storytelling
- LLM Orchestration
one_liner: DataMagic 用 DVSpec 声明式规范统一图表、叙述与动画，通过生成后编排多智能体策略高效生成数据视频
practical_value: '- 声明式规范 DVSpec 用数据绑定引用和声明式同步统一表示多模态组件（图表、叙述、动画），保证数据溯源与自动对齐，可借鉴到电商推荐理由/商品文案生成：定义统一
  schema 绑定商品属性、卖点文案和展示节奏，避免 LLM 自由生成导致信息偏差。

  - “Generate-then-Orchestrate” 策略：并行生成多个候选场景，再全局编排优化叙事连贯性，可用于商品短视频脚本或详情页卖点生成：先并行生成多个卖点片段，再根据用户画像和上下文做全局排序与裁剪，提升生成效率与内容质量。

  - 多智能体共享状态（DVSpec）支持全自动与人工精细控制三种交互模式，适合 Agent 辅助的广告创意生产：LLM 生成初始草稿后，人类通过修改声明式规范局部调整，系统自动重新对齐其余部分，大幅降低人工修改成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：数据视频结合动态图表、旁白和动画，成为数据故事叙述的重要形式，但制作需跨领域专业知识；现有工具要么依赖预准备图表，要么端到端生成但无法保证数据准确性。端到端生成面临统一表示多模态组件与时间关系、高效搜索设计空间两大挑战。

**方法关键点**：提出 DataMagic 系统，核心是 DVSpec 声明式规范，统一图表、叙述和动画，包含数据绑定引用和声明式同步，确保数据溯源和自动音画对齐。采用“生成-再编排”多智能体策略：并行生成候选场景，再全局编排优化叙述连贯性。DVSpec 作为共享状态支持三种交互模式，融合全自动和精细人工控制。

**关键结果**：在 109 个真实样本上，最先进 LLM（如 GPT-5）质量仅 2.13/5，执行成功率 48.62%-86.24%；DataMagic 质量提升至 3.89（+83%），成功率高于 95%，动画和叙述维度增益最大。用户研究显示相比对话式 LLM 工作流，DataMagic 减少 79.7% 任务时间，降低认知负荷。
