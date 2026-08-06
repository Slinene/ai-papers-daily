---
title: 'Skill-Use: Can LLMs Actually Use Skills in Agentic Harnesses?'
title_zh: 'Skill-Use: LLM 在 Agent 框架中真的能使用技能吗？'
authors:
- Jinyi Han
- Yuanjian Xu
- Ying Liao
- Xinyi Wang
- Zishang Jiang
- Zixiang Di
- Fanyang Lu
- Zhichao Hu
- Yanghua Xiao
affiliations:
- East China Normal University
- Hong Kong University of Science and Technology
- Fudan University
- Tencent Hunyuan
arxiv_id: '2608.04828'
url: https://arxiv.org/abs/2608.04828
pdf_url: https://arxiv.org/pdf/2608.04828
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 能力评估 · 渐进式技能使用
tags:
- skill use
- agent evaluation
- progressive disclosure
- benchmark
- LLM agent
one_liner: 提出 Skill-Use 基准，从触发、合规、边界三维度评估 LLM Agent 在渐进式披露下自主检索并遵循技能的能力，发现最高 SU 仅
  0.613，触发与合规是独立瓶颈，排名依赖框架。
practical_value: '- **技能触发是首要瓶颈，强化名称与描述的区分度**：在 Agent 技能库中，技能名和简短描述直接影响触发率。电商/推荐场景下设计技能时，应使用精确、无歧义的元数据，避免与通用话题重叠，降低“不触发”失败。

  - **预加载关键步骤可提升触发，但不宜直接暴露全过程**：实验表明预加载技能全文可大幅提高触发，但执行合规性改善有限。工程上可对高价值技能预先在 System
  Message 中隐式注入其执行约束或决策规则，而不必展示全部 SOP，平衡触发与技能保密性。

  - **技能库规模影响以“不调用”为主，而非错误调用**：增加技能库容量主要导致 Agent 完全放弃调用技能，而非选错技能。因此监控“技能未被触发”比检测“选错技能”更有价值，可设置兜底策略或主动提示。

  - **技能合规性与业务结果非线性相关，需设定最低 SU 阈值**：任务完成得分在 SU > 0.5 后才转为正向增益，半吊子遵循反而损害结果。实际部署中应设定内部合规门槛，低于此阈值的技能调用可关闭技能库或回退无技能基线。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

LLM Agent 越来越依赖技能（Skill），即规定何时行动、执行哪些步骤、允许使用哪些工具的结构化文档。现有评估大多关注技能本身的质量或对任务成功的贡献，却忽视了 Agent 能否在渐进式披露下自主识别并正确应用一项技能。作者因此构建 Skill-Use 基准，首次将技能使用分解为三重能力：**触发（是否检索到正确技能）、合规（是否按规程执行）与边界（是否避开禁止操作）**。

**方法**

- 从 10 万+ 社区技能中筛选出 79 个真实技能，对应 9 个领域，构造 177 个可执行任务，每个任务在 Docker 沙箱中运行并配有基于轨迹的评分量表。
- 每个任务要求 Agent 仅从技能名和简介判断相关性，主动打开技能文件后才能获得完整规程（渐进式披露）。
- 评分维度：触发为二值（是否读取技能文件）；合规为对各技能规定步骤的加权满足率；边界为对各禁止行为的遵守率；三者组合为 Skill-Use（SU）分（触发成功后才计入合规与边界，α=0.7）。
- 评估了 8 个前沿 LLM（Claude Opus 4.7/4.8、GPT-5.5、DeepSeek-V4 等）在 Claude Code 和 Codex 两种 Agent 框架下的表现。

**关键结果**

- 最强配置 GPT-5.5 + CC 的 SU 仅 0.613，远未达到可靠水平；合规性（最高 0.638）和触发率均构成独立瓶颈。
- 框架影响显著：CC 下触发率差异大，Codex 下合规差异更大；模型排名随框架变动，说明技能使用是模型-框架耦合能力。
- 预加载技能全文可大幅提升触发，但对已触发的任务执行质量改善甚微，揭示主要缺口在检索决策。
- 技能库大小的主要影响是使 Agent 放弃调用技能，而非选错技能。
- 技能遵循与任务完成的收益在 SU > 0.5 时才转为正向，部分执行可能比不用技能更差。

> **一句话**：Skill-Use 是 Agent 自助式技能使用的可靠试金石，分离了识别与执行，并揭示出“触发-合规”双重瓶颈与强烈的框架依赖，为技能驱动的 Agent 工作流设计提供了量化指南。
