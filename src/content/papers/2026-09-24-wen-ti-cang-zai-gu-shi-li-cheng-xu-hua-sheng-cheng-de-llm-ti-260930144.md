---
title: 'EnigmaForge: The Question Is Hidden in the Story'
title_zh: 问题藏在故事里：程序化生成的 LLM 问题发现基准
authors:
- Daniel Eisner
arxiv_id: '2609.30144'
url: https://arxiv.org/abs/2609.30144
pdf_url: https://arxiv.org/pdf/2609.30144
published: '2026-09-24'
collected: '2026-09-26'
category: Eval
direction: LLM 评估 · 问题发现基准
tags:
- LLM
- benchmark
- problem discovery
- synthetic generation
- SAT solver
- intuition
one_liner: 用程序化生成的文档谜题测试 LLM 无明确问题时自主发现问题与求解，揭示直觉排序与事实恢复差异巨大
practical_value: '- **为 Agent 增加“无明确指令”评估轴**：现有 Agent 评测多给显式任务，但电商推荐/搜索中用户意图常隐晦（如浏览、收藏、负反馈）。可借鉴
  EnigmaForge 的 intuition vs guided 双指标，单独衡量模型在没有 question 时能否从行为日志或上下文文档中主动发现问题并产出可执行动作。

  - **用 SAT/约束求解生成唯一解且每条线索必要的合成样本**：在推荐规则引擎、策略配置、prompt 模板的单元测试中，可生成带消融证书的合成场景，保证每个条件都
  load-bearing，避免标注噪声和过拟合。

  - **区分安全拒答与能力失败，避免评估污染**：线上模型评估要单独记录 content filter 拦截率和 refusal 率，否则会把安全策略误判为能力差；尤其是电商
  Agent 面对用户生成内容时，需要把拒答路径从业务指标中剥离。

  - **程序化生成 + 种子控制，构建可无限扩展的回归集**：借鉴其从种子生成、永不重复、已发布题目不会成为测试泄漏的方式，为推荐/搜索模型搭建持续评测集，防止数据污染和
  leaderboard 作弊。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

动机：多数基准直接给出问题，测不出模型在真实场景中自主发现任务的能力。EnigmaForge 给出十份零散旧文档，不提供任何问题，文档中隐藏一个小逻辑谜题，要求模型察觉谜题、推导问题、求解并按规定行动。

做法：谜题由程序化生成器从种子生成，分五档难度；生成时用 SAT solver 证明解唯一，并输出消融证书，证明删除任一单条线索都会引入第二个解。指标分为 intuition（只给故事时的任务成功率）和 world reconstruction（事实重建）双轴，在 25 个前沿模型 + 4 个确定性基线、约 600 实例 / 17,400 条记录上，用三种匹配条件对照。

结果：intuition 排序与事实恢复排序差异极大，前沿模型分数从 4 到 80（22 倍差距），而事实恢复跨度仅 1.6 倍；事实恢复第二的模型在 intuition 上排第 14，事实榜前五之外的模型反而领先。告知问题对多数模型提升 9-37 分，但 Grok-4.6 无差异，GPT-6 Sol 在无问题条件下显著更好。部分模型在到达谜题前就被自身内容过滤器拦截，有模型拒绝全部 120 个正式符号表述但接受部分散文表述，说明将拒绝计为失败会混入过滤器行为。
