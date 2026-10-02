---
title: 'Beyond Memory: Harnessing Long-Horizon Agents with Explicit Belief States'
title_zh: 超越记忆：用显式信念状态驾驭长程智能体
authors:
- Yu Luo
- Jiamin Jiang
- Yimin Zuo
- Xidao Wen
- Rongchen Gao
- Yongqian Sun
- Shenglin Zhang
- Guiyang Liu
- Cheng Zhang
- Fang Situ
affiliations:
- Nankai University
- Alibaba Group
- Tsinghua University
arxiv_id: '2610.01415'
url: https://arxiv.org/abs/2610.01415
pdf_url: https://arxiv.org/pdf/2610.01415
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: 长程 Agent 信念状态维护与恢复
tags:
- LLM Agents
- Belief State
- Long-Horizon
- POMDP
- Context Management
- Recovery
one_liner: 提出 PoS 框架，通过显式信念状态、一致性验证与卡住感知恢复提升长程 LLM Agent 表现
practical_value: '- 在电商/搜索/推荐场景的 Agent 中，用 Entity-State-Relation 结构化信念替代原始轨迹摘要，把“仍需知道什么”（epistemic
  gaps）和“仍需完成什么”（achievement gaps）分开显式维护，作为每步 action selection 的上下文，避免长会话中状态混淆。

  - 引入独立 Belief Sentinel 校验模块（可用同一 LLM 角色分离），在每次信念更新后检查内部一致性（如冲突的实体状态）和外部一致性（与新 observation
  是否矛盾），显著降低错误状态污染后续决策的风险。

  - 对多轮交互 Agent（商品导购、售后诊断、搜索会话）增加“卡住检测”：监控窗口内 gap persistence、progress stagnation、belief
  recurrence 三个信号，一旦检测到 Belief Trapping，按动态模式（static/cycle/drift）和 gap 类型注入恢复约束，如抑制无效动作、强制获取判别证据或制造目标状态变化。

  - 注意成本均衡：信念维护会增加总体 token 成本，但能降低 Task Agent 的无效 token 消耗和提升成功率；实际业务可先用轻量校验器、缓存信念或降低更新频率，在关键长程任务中开启完整机制。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM Agent 的能力边界正在从短任务推进到长程交互，但现有方法大多把交互历史作为记忆进行保留、压缩或重组。这种方式难以从混合了旧信息与中间判断的上下文中识别哪些事实仍然成立、哪些推理仍然可靠、哪些需求尚未解决。当任务状态隐含在越来越长的轨迹中时，过时或矛盾的信息会持续影响后续决策，导致 Agent 反复无效动作、消耗预算但未向目标推进。因此，下一阶段的瓶颈不是“记住更多历史”，而是维护一个可验证、可更新的当前世界状态。

**方法关键点**
- 将 POMDP 信念状态显式化为结构化表示 B_t = (W_t, G, Δ^E_t, Δ^A_t)，其中 W_t 为 Entity–State–Relation 世界状态，G 为目标，Δ^E_t 与 Δ^A_t 分别表示仍未解决的信息缺口与成就缺口。
- 每步从当前信念与一个 active gap 出发选择动作；候选信念更新需经过 Belief Sentinel 审计，检查内部一致性（如实体被同时标记为 open 和 closed）与外部一致性（是否与最新观察矛盾），修订后才提交。
- 基于窗口内三个信号——gap persistence、progress stagnation、belief recurrence——计算信念健康分，低于阈值判定为 Belief Trapping（卡住）。
- 检测到卡住后进行因子化诊断：按动态分为 Static、Cycle、Drift，按阻塞缺口类型分为 Epistemic 或 Achievement，并组合恢复约束（如抑制无效动作、切断循环边、重新锚定 active gap、要求获取判别证据或引发目标相关状态变化）。

**关键结果**
在 ALFWorld、LOCA-Bench（执行）和 RCA-100、ClinDiag（诊断）四个 benchmark 上，PoS 在 Qwen3.7-Plus、Kimi-K3、GLM-5.3 三个 backbone 下均取得最高总体性能，相对最强 baseline 的领先幅度最高达 ALFWorld 22.68%、RCA-100 37.89%、LOCA-Bench 7.53%、ClinDiag 11.31%。上下文从 96K 扩展到 256K 时，PoS 基本保持稳定，在 256K 下超过最强 baseline 10.67–16.00 分；代价是总 token 增加约 5 倍，但 Task Agent 自身 token 消耗下降 20.9%。消融表明，单独移除一致性验证或卡住检测恢复都会带来明显性能损失。

**最值得记住的一句话**
长程 LLM Agent 的可靠性不只来自更长的上下文或更好的压缩，更来自显式构造并持续维护一个可验证、可恢复的当前世界信念。
