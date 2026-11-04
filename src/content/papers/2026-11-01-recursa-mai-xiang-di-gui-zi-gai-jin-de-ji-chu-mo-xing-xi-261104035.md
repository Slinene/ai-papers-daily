---
title: 'Recursa: Toward Recursively Self-Improving Foundation Model Systems'
title_zh: Recursa：迈向递归自改进的基础模型系统
authors:
- Erkang Zhu
- Yin Lin
- Xiaorong Shi
- Xuanrui Lin
- Jingren Zhou
affiliations:
- Alibaba Research
arxiv_id: '2611.04035'
url: https://arxiv.org/abs/2611.04035
pdf_url: https://arxiv.org/pdf/2611.04035
published: '2026-11-01'
collected: '2026-11-04'
category: MultiAgent
direction: Agent 多智体递归自改进
tags:
- Recursive Self-Improvement
- Multi-Agent
- Knowledge Repository
- Harness
- Domain Adaptation
- Long-Horizon Agents
one_liner: 构建知识仓库引导的多智能体递归自改进系统，无更强模型下将法律领域任务全对率最高提升至 55.0%
practical_value: '- **可复用 harness 设计**：给搜索/推荐/广告 Agent 使用 persistent Python REPL +
  append-only event log。召回、排序、筛选等中间结果留在 Python 变量，只把最终证据回传模型，长链路追踪不必全量进 context；故障诊断时按地址检索历史轨迹，避免上下文爆窗。

  - **把领域知识沉淀为可加载 skills**：电商新类目冷启动可以先构建类似导航结构，把类目规则、商家文档、商品属性约束浓缩为可加载技能包；每次任务后反思失败案例，将“该找什么证据”和“怎么判断证据是否充分”写成可叠加的
  memory/skill，而不是每次从头探索。

  - **多 learner 按失败模式拆分优化**：不要用一个全局 prompt 大修。按类目、意图、失败原因或技能子集拆分任务，并行做局部改进后合并验证；合并后必须抽样回归已通过任务，避免新编辑造成退化。单
  learner 很容易过拟合训练集，生产上推荐拆分+合并+回归。

  - **利用无权重更新做快速迭代**：在无法频繁微调推荐/搜索模型时，先通过文本化知识仓库快速迭代领域规则与策略，积累到一定程度再作为后续模型训练数据，这与生成式推荐里先沉淀
  Semantic ID 或知识卡片再训练模型的路径一致。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：基础模型进入新领域时，会同时遇到知识缺口（缺事实、术语、材料位置）和行为缺口（有信息但用错）。新领域往往没有大规模专家标注和可靠监督信号，而系统能力不只来自模型权重，还来自指令、技能、记忆和执行框架。因此需要一种不依赖更强模型或人类专家的系统级自改进方法。

**方法关键点**：
- 学习对象是知识仓库：instructions、skills、memory 三类文本组件，可即时生效、可检查、可合并；本文固定模型和 harness，只学习知识仓库。
- harness 设计：持久化 Python REPL + append-only event log。Agent 用代码组合工具，中间结果留在变量里，只回传精选内容；长轨迹按地址检索，避免上下文爆窗。
- 两阶段学习：先基于领域语料做 bootstrap，构建导航结构或探索笔记，并生成自练习任务；再基于训练任务与反馈做递归自改进，循环 solve → diagnose → edit → validate。
- 多 learner 拆分：父 learner 按话题/失败模式/技能/工具把训练任务分成子集，子 learner 并行改进，再由父 learner 合并去重、消解冲突、反思学习轨迹并指导下一轮。

**关键实验**：在 Harvey LAB Firm Knowledge 基准上，250 个法律长文任务（150 train / 100 test）。harness 本身已很强：Qwen3.8-27B 的 criteria pass 达 78.9%，all-pass 35.2%，超过已发布基准的最高 study 配置（31.0% all-pass）。bootstrap 主要降低约 20%–25% 的交互轮数和输入 token，all-pass 只是略增。多 learner 自改进后，DeepSeek-V4.1-Flash 的测试 all-pass 从 33.0% 升至 55.0%，Qwen3.8-Flash 从 34.0% 升至 46.0%；而单 learner 方案明显更差，Qwen 甚至低于 bootstrap 基线。

**最值得记住的一句话**：把系统知识表示为可合并、可验证的文本组件，并按照失败模式拆分并行学习，比一个大循环直接改 prompt 更稳。
