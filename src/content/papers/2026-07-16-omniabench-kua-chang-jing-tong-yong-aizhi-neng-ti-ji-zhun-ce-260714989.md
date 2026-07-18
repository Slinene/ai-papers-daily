---
title: 'OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios'
title_zh: OmniaBench：跨场景通用AI智能体基准测试
authors:
- Chengyu Shen
- Yujie Fu
- Gangtao Xin
- Yanheng Hou
- Wenlong Fei
- Guojie Zhu
- Jiawei Li
- Hongcheng Gao
- Runming He
- Zhen Hao Wong
affiliations:
- Huawei Cloud Post-Training Team
- PKU DCAI Team
arxiv_id: '2607.14989'
url: https://arxiv.org/abs/2607.14989
pdf_url: https://arxiv.org/pdf/2607.14989
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: 通用AI智能体多场景评测基准
tags:
- Benchmark
- Agent
- LLM Evaluation
- Multi-turn
- Tool Use
- Capability Taxonomy
one_liner: 构建覆盖ToC/ToB/ToE多领域、支持细粒度能力评估的通用智能体基准，前沿模型Pass@1仅约58%
practical_value: '- **多领域评测维度复用**：OmniaBench 从应用商店、产品文档等提炼的 90 个一级领域、354 个二级领域的层次化分类，可直接迁移到电商场景，构建覆盖商品搜索、客服对话、营销文案生成等不同业务子领域的
  Agent 评测框架，确保评估广度。

  - **能力诊断框架借鉴**：十维能力分类（如规划、工具调用、约束维持）和八种原子难度因子可用于拆解搜索推荐 Agent 的关键短板，例如诊断是意图理解不足还是工具选择错误，针对性优化模型训练或
  prompt 设计。

  - **任务合成方法迁移**：DAG/Solver/Program 等合成路线可辅助自动化生成电商多轮交互测试用例（如退货流程引导、多条件商品筛选），减少人工设计成本，特别适用于验证
  Agent 在长链路、约束复杂场景下的表现。

  - **工程化启示**：基准揭示前沿模型在自适应纠错、状态追踪上的普遍局限，提示在构建生产级推荐对话 Agent 时，需显式加入外部状态管理模块或校验步骤，而非单纯依赖模型自身能力。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有智能体基准多聚焦有限场景或单一交互范式，无法系统刻画模型在千差万别的真实应用中的能力边界。OmniaBench 旨在提供一个涵盖消费者（ToC）、企业（ToB）以及新兴领域（ToE）的宽覆盖、细粒度评估平台。

**方法关键点**：
- 从应用商店、产品文档、行业资源等源头摘取场景知识，构建层次化领域分类（90 个一级、354 个二级领域），并搭建可执行环境。
- 通过四种任务合成路线生成单轮/多轮任务：DAG（基于状态图）、DAG-S（带子目标的 DAG）、Solver（自动求解）和 Program（程序直接定义）。
- 定义十维能力分类（如规划、工具调用、约束维持）和八个组合原子难度因子（如状态空间大小、所需工具数），支持细粒度分析和可控难度设计。
- 数据集包含 1,431 个任务，另设 644 个任务的挑战性子集以降低评测成本并防止数据污染。

**关键结果**：当前最强模型 Claude-Sonnet-5 和 GPT-5.6-Sol 整体 Pass@1 仅 58.54 和 57.14，不同领域和能力维度表现差异明显，且在规划、约束维护和自适应纠错方面存在持续局限，模型仍有较大提升空间。
