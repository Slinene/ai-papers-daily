---
title: 'Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting'
title_zh: 让 LLM 在会议中拥有情境意识并替参与者发言
authors:
- Muneeb Khan
- Frederic Kirstein
- Terry Ruas
- Bela Gipp
affiliations:
- University of Göttingen, Germany
arxiv_id: '2609.03923'
url: https://arxiv.org/abs/2609.03923
pdf_url: https://arxiv.org/pdf/2609.03923
published: '2026-09-03'
collected: '2026-09-05'
category: Agent
direction: LLM Agent 在多方对话中的发言时机决策
tags:
- LLM Agent
- Situational Awareness
- Meeting Delegation
- State Tracking
- Online Decision
- Evaluation Protocol
one_liner: 提出 CAPA 架构，通过显式会议状态预测与校准，将缺席者发言沉默率从 51.4% 降至 2.5%
practical_value: '- 在需要 LLM 实时判断“是否介入”的场景（客服对话、直播场控、主动推荐弹窗）中，显式维护结构化状态（立场、覆盖、发言权）比只堆原始上下文更能消除漏判；可借鉴
  Perceiver 将历史对话压缩成可更新的状态表示。

  - 将决策链拆成 Predictor→Controller→Generator，先预测下一 turn，再决定是否说话、说什么、怎么说；这种解耦便于在业务中单独调优“时机判断”和“内容生成”，也便于归因定位残差。

  - 用真实下一 turn 对预测和动作做在线校准，形成 Recalibrator 闭环；在推荐或对话 Agent 中可引入类似机制，让系统根据后续用户反馈实时修正决策状态，而非静态离线训练。

  - 评估协议值得复用：围绕实际语义单元（idea units）从 whether/when/what 三维打分，并用 schema 约束的 LLM judge
  自动评估，Kappa=0.71 说明可替代部分人工标注；对生成式推荐/对话策略的离线评估尤其有用。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**
在线会议委托中，LLM 代理无法识别何时该发言。没有结构化方式跟踪立场、覆盖度和发言权，代理错过本应贡献的关键时刻。仅靠 prompt 的代理在 AMI 语料上对缺席者发言机会的沉默率达 51.4%。

**方法关键点**
CAPA 将在线发言决策分解为多模块闭环：Perceiver 从每轮观察更新会议状态；Predictor 预测对话将如何继续；Controller 决定是否发言以及引入哪个命题；Generator 按参与者风格生成发言。两个 Judge 分别对预测与动作对照真实下一轮打分，Recalibrator 根据裁判结果更新会议状态，用于后续决策。评估上，引入 episode 级协议，围绕参与者的实际 idea units 从 whether/when/what 三维评分，使用 schema 约束的 LLM judge，与人类标注一致性达 Cohen's kappa=0.71。

**关键结果**
在 137 个 AMI 会议上，CAPA 将沉默率从 51.4% 降至 2.5%，有效恢复得分从 26.1 提升到 52.2，幻觉仅 0.6%。失败模式从遗漏转向选择，残余近失可归因到特定模块。消融实验表明会议状态是缩小识别差距的关键，仅增加原始上下文规模无效。
