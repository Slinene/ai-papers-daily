---
title: 'MMDM: Measuring Massive Multitask Decision Making'
title_zh: MMDM：大规模多任务决策基准评测
authors:
- Junhao Shen
- Qing Zong
- Yue Guo
- Zhanqiu Zhang
- Yiwen Guo
- Hong Cheng
affiliations:
- The Chinese University of Hong Kong
- Hong Kong University of Science and Technology
- LIGHTSPEED
- Independent Researcher
arxiv_id: '2611.14309'
url: https://arxiv.org/abs/2611.14309
pdf_url: https://arxiv.org/pdf/2611.14309
published: '2026-11-09'
collected: '2026-11-11'
category: Eval
direction: 决策模型评测基准
tags:
- benchmark
- decision models
- evaluation
- multi-select
- long context
- agent state tracking
one_liner: 提出覆盖16类任务、5,448题的决策基准，揭露长上下文大选项空间下多选与约束规划的短板
practical_value: '- 可借鉴评测设计：构建长上下文、大选项空间、逻辑依赖的任务，电商/广告场景可设计类似“从大量候选商品或词中按约束选择”的评估，暴露模型真实决策能力。

  - 多选与软标签评估：真实推荐/广告常需多选标签或软概率，当前模型多选准确率极低，应重点优化多选恢复和概率校准。

  - 选项逻辑与约束规划：业务中互斥选项、预算约束等常见，模型在约束规划上表现差，可在 prompt 或训练中显式加入约束表示。

  - Agent 状态跟踪与工具选择：对电商导购 Agent，可参考该基准构建内部评测集，评估状态跟踪与工具调用能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有决策模型评测依赖已有基准，预训练数据污染导致泛化性难判断；真实决策任务常同时包含长上下文、大选项空间和复杂逻辑依赖，现有基准未同时覆盖。

**方法**：构建 MMDM 基准，包含 5,448 个高质量问题，覆盖 16 类任务，混合新构造任务与源数据改写，支持单选、多选和软标签三种决策形式；选项空间从 2 到 1,024，最长输入 64,817 tokens；任务类型包括 agent 状态跟踪、工具/技能选择、偏好判断、评分 rubric 等。

**结果**：评测 28 个决策模型，发现它们在常识知识上表现良好，但在选项逻辑、约束规划、多选恢复上显著下降。Perplexity Decider-V1.2 世界知识硬单选准确率 78.75%，选项逻辑仅 53.95%，约束规划 47.95%；所有模型最佳硬多选准确率仅 36.81%。工作突出联合推理、约束感知选择、完整多选恢复是决策模型发展的关键短板。
