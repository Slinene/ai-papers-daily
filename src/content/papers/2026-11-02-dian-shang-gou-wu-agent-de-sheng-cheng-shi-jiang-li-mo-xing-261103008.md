---
title: 'E-GenRM: Generative Reward Modeling for Open-Ended E-Commerce Shopping Agents'
title_zh: 电商购物 Agent 的生成式奖励模型 E-GenRM
authors:
- Ying Sun
- Qiuyu Zhao
- Xiao Wang
- Xiyu Zhao
- Gege Shi
- Zenghui Sun
- Jinsong Lan
- Haihong Tang
- Bo Zheng
affiliations:
- Taobao & Tmall Group of Alibaba
- Technische Universität Wien
arxiv_id: '2611.03008'
url: https://arxiv.org/abs/2611.03008
pdf_url: https://arxiv.org/pdf/2611.03008
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: 生成式奖励模型 · 购物 Agent
tags:
- Generative Reward Model
- E-Commerce Agent
- RLVR
- GRPO
- Evaluation Chain
- Personalization
one_liner: 从真实购物行为回溯构造评价链，三阶段训练生成式奖励模型，在线提升淘宝购物 Agent 有效协助率与满意度
practical_value: '- 用真实行为回溯构造评估轨迹：从购买结局反向切分 shopping task，将 120+ 行为信号翻译为 Agent 交互历史与候选响应对，能绕过「能力-轨迹反馈环」，持续产出覆盖长尾行为的
  reward/eval 数据；适合电商 Agent 搭建数据飞轮。

  - 评价链 + 三阶段训练可迁移：SFT 学动态加权 rubric 和证据支撑的 criterion-level 判断；RL 用 outcome reward
  + factual reward 给每个 criterion 部分信用，提供更密集训练信号；再用 teacher disagreement 和 utility
  margin 筛 hard negatives 提升个性化偏好敏感度。

  - 主动证据检索：用 retrieval-need label 和 tool-use reward 对齐检索决策，只在上下文缺 decisive evidence
  时调用工具；调用率从 95.84% 降到 22.12%，精度反而略升，适合线上成本敏感场景。

  - 用 E-GenRM 后训练淘宝购物 Agent，14 天 A/B 有效协助率 +1.39pp、满意度 +2.33pp、P99 延迟 -17.88%，可直接作为生成式
  RM 替代或校准 expert judge 的业务参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
购物 Agent 从 query 匹配转向开放多轮任务，奖励信号需要从 pointwise relevance 升级为 trajectory-level 多需求权衡。但现有训练轨迹受限于 Agent 当前能力，粗粒度标量 reward 丢失 requirement-level 信用分配，尤其在候选都满足显式需求、只在隐含偏好上有差异时无法区分。

**方法关键点**
- 数据构建：从 120+ 真实用户行为中回溯购买结局，按意图聚合为 shopping task，平均 3.8 sessions / 162 行为事件；分解为 4.6 个决策步，把后续行为和购买结果作为偏好标签，构造单一维度扰动的候选对。
- 评价链：模型生成任务特定加权 rubric、每个 criterion 的分数、rationale、证据引用，加权分数决定偏好，而非单点标量分。
- 三阶段训练：Stage 1 SFT 学 teacher 评价链；Stage 2 用 GRPO，奖励 = 偏好正确 + criterion-level factual feedback（每个候选评估是否被可见证据支持）；Stage 3 用 teacher disagreement 和 utility margin 筛个性化 hard negatives 继续 RL。
- 主动证据检索：retrieval-need label 监督 tool use，只在上下文缺 decisive evidence 时调用，不改变核心判断流程。

**关键结果**
- E-GenRM-Bench 上，E-GenRM-27B 无检索 82.57%，加检索 87.40%，比最强 baseline 高 6.97pp；比同数据标量 Bradley-Terry RM 高 16.35pp。
- SRB 外部基准 rubric 生成 full/hard 上指标领先或接近最优，证明 criteria 归纳可迁移。
- 消融：移除 outcome reward 掉 19.03pp，去掉 hard-negative 掉 5.09pp。
- 在线 A/B：淘宝购物 Agent 后训练，有效协助率 +1.39pp，满意度 +2.33pp，P99 延迟 -17.88%。

**最值得记住的一句话**
购物任务评估标准应从真实行为的时间组织（序列、重复、关系）中归纳，而非仅从 Agent 当前反馈里学。
