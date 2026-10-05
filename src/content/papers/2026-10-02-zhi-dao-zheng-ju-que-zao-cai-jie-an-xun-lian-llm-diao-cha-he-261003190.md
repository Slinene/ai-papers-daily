---
title: 'Not Until the Evidence Says So: Teaching LLM Investigators When to Close a
  Case'
title_zh: 直到证据确凿才结案：训练 LLM 调查员何时结案
authors:
- Tingzhu Bi
- Ping Wang
- Meng Ma
affiliations:
- Peking University
arxiv_id: '2610.03190'
url: https://arxiv.org/abs/2610.03190
pdf_url: https://arxiv.org/pdf/2610.03190
published: '2026-10-02'
collected: '2026-10-05'
category: Reasoning
direction: LLM 推理闭环与不确定性判断
tags:
- LLM
- reasoning
- evidence
- investigation
- SFT
- RLVR
one_liner: 构建 Nautil 事故调查数据集与三阶段结案评估，显著降低 LLM 过度自信并提升证据依赖结案准确率
practical_value: '- 在客服、工单诊断、风控等需要“证据不足不下结论”的场景，可借鉴「证据依赖测试」：人工删除关键证据，要求模型必须停止闭环或明确缺失项，避免模型仅靠少量线索强行给出推荐/诊断。

  - 用「仅来源规则」作为 baseline：在构建推荐或诊断数据集时，先检查 label 是否被来源/品类等浅层特征泄漏，若规则 baseline 已很高，需按来源分层评估，防止虚假高准确率。

  - SFT 阶段用 teacher trajectories 显式教导模型输出“缺失信息”而不只给结论，可有效降低 LLM 过度自信，适合迁移到对话式推荐/Agent
  的“不知道就反问”设计。

  - RLVR 只奖励闭环决策可大幅提升准确率，但会牺牲对证据变化的敏感性；实际部署时建议将 evidence dependence 作为关键 offline 指标，避免模型“学会猜标签”而非真正依赖证据。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在事故、缺陷和故障调查中常过度自信，即使证据不足也强行结案。评估结案能力较难，因为案例来源会泄漏标签，仅看来源就能在测试集上达到 83.0 balanced accuracy。

**方法关键点**：构建 Nautil 数据集，含 731 个审计案例，覆盖航空、铁路、海事、化工安全、车辆缺陷和生产服务器事故，配有 teacher trajectories、OOD 测试集和反事实证据版本。提出三项结案评估：closure accuracy（对照 source-only baseline 并按来源分层）、evidence dependence（移除结论依据后检查模型是否停止结案）、conclusion and gap quality（判定结论和缺失项质量）。在 9B 模型上先 SFT 再 RLVR：SFT 学习何时结案并命名缺失信息；RLVR 仅奖励结案决策。

**关键结果**：未训练 9B 模型 97% 答案过度陈述；前沿模型识别正确原因达 84% 但仍 91% 过度陈述，并关闭 17/41 个官方“原因未定”案例。SFT 后移除依据使结案率下降 26 点，过度陈述从 97% 降到 35%，正确且不过度陈述的结论从 3% 升至 43%。RLVR 将 balanced accuracy 从 69.2 提升到 83.3，与 teacher 相当；within-source accuracy 从 60.4 到 74.1，但证据依赖有代价。
