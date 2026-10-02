---
title: 'When Users Change Their Minds: Measuring and Repairing Intent Drift in LLM
  Agents'
title_zh: 当用户改变主意：LLM Agent 的意图漂移测量与修复
authors:
- Yanjie Zhang
- Bowen Cao
- Zixin Chen
- Yushi Sun
affiliations:
- HKUST
- CUHK
- LIGHTSPEED
arxiv_id: '2609.32520'
url: https://arxiv.org/abs/2609.32520
pdf_url: https://arxiv.org/pdf/2609.32520
published: '2026-09-25'
collected: '2026-10-02'
category: Agent
direction: Agent 意图状态维护与多轮任务评测
tags:
- intent drift
- state folding
- LLM agents
- multi-turn
- benchmark
- distillation
one_liner: 构建可控意图漂移基准 INTENTFLUX，提出显式状态折叠 StateForge 显著修复多轮任务性能下降
practical_value: '- 多轮购物/搜索助手场景：用户会持续改条件（价格、品牌、词槽）或撤回约束，直接拼历史容易让已撤销的筛选条件污染推荐结果。可在生成前用一个轻量
  tracker 维护“当前有效意图状态”，对每个条件做 ADD/DELETE/REPLACE，且同时删除依赖该条件的推导结论（如“预算升高导致推荐高端品”），再输入生成模型。

  - 工程上不必用主力大模型做状态追踪：9B tracker 已与 122B 无统计差异；2B tracker 经 on-policy distillation
  能从 0.266 提到 0.445。在电商 Agent 架构中可以把意图状态维护拆成小参数模块，降低成本与延迟。

  - 评测/回归验证时，务必避免在收尾轮次重述最终意图，否则会掩盖 drift 缺陷；可借鉴 clean vs drift 配对、CAR/IDG 指标，以及长度匹配无漂移对照，逼出真实的多轮意图追踪能力。

  - 压缩/摘要式 history management（滚动摘要、两阶段压缩）对意图漂移不可靠；如果业务中有多轮查询改写/约束增删，应优先考虑显式状态折叠，而不是依赖通用
  long-context 或摘要。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM agent 在多轮交互中用户意图在最终执行前可能变化，被取代/撤回的旧意图仍影响最终答案或工具调用，即 intent drift。现有评测未能区分旧意图残留与其他多轮错误，需要可测量的失败模式与修复方法。

**方法关键点**：
- 构建 INTENTFLUX 基准：将可验证任务转换为受控多轮对话，保留原始 grader。通过 ADD/DELETE/REPLACE 编辑操作构造意图演化；用 variant（被替换的替代值）和 decoy（被撤回的约束）注入陈旧信息；仅保留遵守 decoy 会改变 grader 判定的情况，使陈旧意图使用可经任务成功度量。
- 难度分层 easy/medium/hard 对应 variant/decoy 预算 1/3/5，联合增加陈旧信息负载。
- 提出 StateForge：train-free 状态折叠 harness。每轮后 tracker 将意图编辑折叠为显式活跃状态；删除/替换不仅移除被取代项，还使其推导出的结论失效；生成前将活跃状态插入对话历史与当前输入之间，使生成器看到显式当前意图。
- 两种迁移路径：on-policy distillation 训练小 tracker；thinking distillation 将状态折叠行为内化到独立 agent。

**关键结果数字**：
- 627 任务校准池，mean score 从 easy 0.476 降到 hard 0.384（-19.3%）；8 个模型在 GENERAL-TEST 上 clean-drift 全配对 IDG 均为正，hard 条件 CAR 比 clean 低 0.344-0.448。
- 长度匹配无漂移对照 score 0.734，接近 clean 0.778，远高于 drift 0.469，说明单纯多轮长度不解释下降。
- StateForge 在 GENERAL-TEST 上 mean score 0.367→0.467；GT 最终状态注入达 0.549，仍低于 clean 0.778，说明状态估计误差只解释部分差距。
- 外部压缩 harness（Deep Agents 0.354 / OpenHarness 0.392）并未优于裸多轮 0.367。
- OPD 将 2B tracker 从 0.266 提升至 0.445；9B tracker 与 122B 无显著差异；thinking distillation 将 35B 独立 agent 从 0.296 提升至 0.461。

**最值得记住的一句话**：多轮 Agent 的失败不仅来自历史压缩不足，更来自“哪些旧意图仍然有效”的状态估计；显式维护活跃需求并在生成前注入，是比滚动摘要/压缩更有效的修复路径。
