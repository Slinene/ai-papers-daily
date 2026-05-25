---
title: '"I didn''t Make the Micro Decisions": Measuring, Inducing, and Exposing Goal-Level
  AI Contributions in Collaboration'
title_zh: 目标级AI贡献的测量、诱导与暴露：人机协作归属框架
authors:
- Eunsu Kim
- Jessica R. Mindel
- Kyungjin Kim
- Sherry Tongshuang Wu
affiliations:
- KAIST
- Carnegie Mellon University
- Seoul National University
arxiv_id: '2605.21363'
url: https://arxiv.org/abs/2605.21363
pdf_url: https://arxiv.org/pdf/2605.21363
published: '2026-05-19'
collected: '2026-05-25'
category: Agent
direction: 人机协作目标级贡献归属与 AI 主动性测量
tags:
- goal-level attribution
- indirect influence
- human-AI collaboration
- contribution measurement
- interaction design
- agent initiative
one_liner: 提出 COTRACE 框架，在目标与需求层面量化人类与 AI 的贡献，并揭示可控制的间接影响模式
practical_value: '- **目标分解为可验证需求**：可将电商对话中的复合意图拆分为一组独立、可检查的 `requirement`，用以量化 AI
  在需求创建、修改中的贡献，区分 AI 是简单执行还是主动塑造了用户目标。

  - **间接影响模式直接复用**：论文归纳的四种间接影响类型（under-specification, artifact-triggered elaboration,
  problem-triggered revision, interactional steering）可直接作为 prompt 模板或 agent 交互策略，在需要
  AI 更主动时故意模糊用户输入，或提供半成品以引导 AI 提出更细的需求，例如在生成式推荐中让 AI 先给一个粗方案，诱导用户补充细节。

  - **交互设计控制 AI 主动性**：强制 agent 每次行动前发送消息（Chat 模式 vs 直接工具调用的 Agentic 模式）使 AI 对目标塑造的贡献率从
  24.5% 提升至 42.9%。在 Agent 系统中，可以通过插入一条简单的“先表达计划再执行”规则，平衡自主性与可控性。

  - **贡献可视化提升用户校准**：将贡献分析图暴露给使用者后，其对自己执行贡献的评分平均下降 1.8 分（5 分量表），有效纠正对 AI 贡献的低估。在推荐解释或协作式购物助手中，可引入类似“决策影响回溯”视图，帮助用户理性评估
  AI 的建议。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有人类与 AI 协作的贡献归属方法几乎只关注最终产物（如文字、代码谁写的），忽略了协作过程中 AI 通过提出方向、细化约束、间接启发等方式对「目标」本身的塑造。这种进程级贡献的缺失使得用户难以校准自己对 AI 的依赖，评估者也无法判断 AI 辅助工作的原创性。论文认为，在用户表面领导全局、AI 仅执行指令的背后，AI 往往通过间接影响深度参与了目标的形成。

**方法关键点**  
- 提出 COTRACE 框架，将对话中的**目标（Goal）** 分解为一组细粒度、可独立验证的**需求（Requirement）**，并追踪每个需求的创建、修订、删除生命周期。  
- 引入**直接贡献**（显式创建或修改需求）和**间接影响**（通过提供上下文、提出问题等引导对方后续提出需求）两类度量，使用 LLM-as-judge 自动判行动–需求对的影响力。  
- 层次化聚合：从行动→需求→子目标→父目标，最终得到按说话人和角色（Shaper / Executor）划分的贡献矩阵。  
- 分析 638 段真实对话日志，归纳出 11 种间接影响子类型，归入四种模式：未充分指定意图、制品触发细化、问题触发修正、交互引导。  
- 在 CoGym 仿真环境中验证两种影响 AI 目标塑造的因素：用户提示的模糊性（under-specification）和交互模式（Chat 模式强制先消息后动作）。  
- 构建 COTRACE-viewer 并在 10 名被试中评估其对贡献感知的校正效果。

**关键实验与结果**  
- 真实日志：人类贡献 75–89% 的目标塑造（Shaper 质量），但在更具体需求层面上 AI 贡献比例升高；技术任务（编程、数据分析）中 AI 创造的需求随互动增多甚至反超人类。  
- 间接影响：用户创建的需求中有 60% 受到 AI 的制品触发细化影响；AI 创建的需求中有 46.7% 因用户未充分指定意图而产生。  
- 交互设计：Chat 模式下 AI 对需求的直接贡献率从 Agentic 模式的 24.5% 升至 42.9%。  
- 提示干预：用户模拟器采用 under-specification 策略时，AI 贡献率从 30.65% 跳升至 69.64%。  
- 用户研究：使用 COTRACE 分析后，被试对自己执行贡献的评分平均下降 1.8 分（‑1.8），并意识到 AI 在未明确指令下做出了大量微观决策。  

**核心结论一句话**：AI 在协作中经常以非显性方式塑造用户的微观目标，交互设计可以显著调控这种主动性，而暴露分析结果能有效纠正用户的感知偏差。
