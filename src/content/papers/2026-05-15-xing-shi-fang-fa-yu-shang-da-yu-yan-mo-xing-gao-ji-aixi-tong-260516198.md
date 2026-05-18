---
title: 'Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance
  of Advanced AI Systems'
title_zh: 形式方法遇上大语言模型：高级AI系统的合规审计、监控与干预
authors:
- Parand A. Alamdari
- Toryn Q. Klassen
- Sheila A. McIlraith
affiliations:
- University of Toronto
- Vector Institute
arxiv_id: '2605.16198'
url: https://arxiv.org/abs/2605.16198
pdf_url: https://arxiv.org/pdf/2605.16198
published: '2026-05-15'
collected: '2026-05-18'
category: Agent
direction: Agent 行为合规监控 · 形式方法
tags:
- LTL
- Monitoring
- Auditing
- LLM-as-a-Judge
- Temporal reasoning
- AI Governance
one_liner: 利用LTL进展将时序合规监控拆解为LLM标注+形式推理，效果远超LLM直接评判，并实现预测性干预
practical_value: '- **用 LTL 形式化业务规则，监控 Agent 行为**：电商场景中复杂的时序约束（如“必须先确认支付再发货，且发货前需人工审核大额订单”）可直接用
  LTL 表达，结合 TRAC 对客服机器人、推荐流程或供应链Agent进行实时合规检查。

  - **小模型标注 + 形式逻辑推理 > 大模型直接评判**：不要依赖 GPT-4 等巨额模型作为时序行为裁判，改用 7B 小模型做动作/状态的命题标注，再交由
  LTL 进展自动推理，成本低且 F1 大幅度领先，适合大规模日志审计。

  - **预测与干预机制降低违规率**：新增预测监控模块，对即将发生的违规进行采样估计，并通过重采样、约束注入提示或切换更安全的模型进行黑盒干预，在保持任务完成率的同时显著减少违规，可嵌入到对话Agent或推荐Agent的推理循环中。

  - **审计日志自动生成可解释证据**：TRAC 在监控过程中记录每次公式进展的 witness，为每一步合规/违规提供可追溯的解释，便于满足监管审计要求。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：AI 产品与服务需遵守产品、行业和地域特定的时序行为规范（如“收到有效发票最终必须付款”），这类约束存在时间弹性，LLM 直接作为裁判（LLM-as-a-Judge）难以识别时序模式违规，尤其是事件间隔大、约束数量多时性能急剧下降。

**方法关键点**：
- **TRAC 算法族**：将监控问题分解为 LLM 标注器（从 I/O 序列中提取原子命题）和基于线性时序逻辑（LTL）进展的监控器。LTL 进展逐步重写公式，保留符号结构，支持新增约束无需重编译、生成可读的残留公式以用于干预。TRAC 可灵活用于在线监控或离线日志审计。
- **TRACP+I**：加入预测监控（采样未来 k 步估计违规概率）与黑盒干预（重采样、约束注入提示、模型替换），在预计违规前主动修正输入或输出。
- **重置机制（TRAC R）**：检测到违规后重置，支持持续监控和“合理合规”评估。

**关键实验**：
- **环境**：IPC-Trucks、TextWorld、ScienceWorld，均为长视自序列决策环境，带有时序行为约束。
- **对比基准**：LLM-as-a-Judge（零样本/少样本/少样本+真值标签）、不同规模的 LLM（Qwen-7B 至 Gemini-2.5-Pro）。
- **主要结果**：TRAC + LLM 标注器的 F1 普遍提升 0.3–0.5 以上，7B 小模型作标注器即可超越前沿模型直接评判。受控合成实验证实：LLM 的时序推理准确率随事件间隔、约束数量和每步命题数量的增加而明显下降，复杂公式下前沿模型也快速退化。TRACP+I 的三种干预策略在不同模型和环境均降低违规率（例如从 0.6–0.8 降至 0.2–0.4），且任务奖励无明显损失。

**核心启示**：将时序合规监控解耦为 LLM 负责感知标记、形式方法负责时序推理，是当前最可靠的工程路线；LLM 不应单独承担时序推理任务。
