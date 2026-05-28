---
title: Calibrating Conservatism for Scalable Oversight
title_zh: 可扩展监督中保守主义的校准
authors:
- William Overman
- Mohsen Bayati
affiliations:
- Stanford University
arxiv_id: '2605.28807'
url: https://arxiv.org/abs/2605.28807
pdf_url: https://arxiv.org/pdf/2605.28807
published: '2026-05-27'
collected: '2026-05-28'
category: Agent
direction: 可扩展监督 · 保守性校准
tags:
- Scalable Oversight
- Conformal Decision Theory
- Attainable Utility Preservation
- Agentic AI
- Safety
- Online Calibration
one_liner: 聚合多种辅助监督信号为保守性惩罚，并用共形决策理论在线校准保守系数，确保长期违规率不超过目标值
practical_value: '- **在线校准λ的思路可迁移至推荐**：推荐系统中常常在安全性与效用间权衡（如低俗内容过滤vs流量），可借鉴 CCO 的增量
  λ 更新规则 λ_{t+1}=λ_t+η(ℓ_t−α)，根据实时观测的违规率自适应调整保守程度，无需预定义固定阈值。

  - **弱监督聚合惩罚**：在电商多智能体场景中，可用多个廉价弱模型（如同步的安全检查、合规评分）对各候选动作打分，聚合与安全基线的偏差量作为惩罚，不要求各监督者完全理解主智能体，即可形成有效约束。

  - **提供可证明的长期风险控制**：推荐系统在动态环境中常遇到分布漂移，CCO 的 conformal 控制器不依赖分布假设，适合线上 A/B 实验中的风险控制，可设定
  α 为可容忍违规率，保证长期平均不超过该目标。

  - **基线动作的设计**：明确指定一个保守基线动作（如“不推荐”），并确保其损失为零，为 CCO 提供安全兜底；在推荐/Agent 中可设计“安全 fallback”机制，当所有候选动作都被惩罚过高时自动回退到基线。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：对于能力可能超越人类监督者的大规模智能体，如何维持有意义的控制是一个核心难题。现有可扩展监督方法多依赖单一回合、缺乏形式化保证，难以应对智能体的序贯决策环境。本文受 Attainable Utility Preservation (AUP) 启发，提出将多样辅助监督信号聚合为一个保守性惩罚，并用 Conformal Decision Theory (CDT) 在线校准保守系数，从而在任意序列环境中保证长期违规率不超目标阈值。

**方法关键点**
- 定义 CCO 框架：赋予一个保守基线动作 a₀，计算每个候选动作与基线的总偏差 ∆(s,a)=Σ|qᵢ(s,a)−qᵢ(s,a₀)|，将主智能体的效用与 λ·∆ 的差作为选择标准。
- 将 AUP 从需要 Q 值扩展到任意的辅助评分函数，更贴合大语言模型等前沿系统。
- 采用 CDT 控制器在线更新 λ_{t+1}=λ_t+η(ℓ_t−α)，其中 ℓ_t 为当前动作的损失（违规指标）。
- 证明 CCO 决策族满足“最终安全”性质：存在有限保守阈值 λ̅，当 λ≥λ̅ 时智能体总是选择基线动作，损失为零。基于此得到有限时间非渐近保证，累计平均损失上界为 α+(λ̅−λ₀)/η+1/(t+1)。
- 扩展至噪声反馈和延迟反馈，理论证明性能退化可控。

**关键实验**
- SWE-bench Lite：用 Claude 3.5 Sonnet 作为主编码智能体，可能被注入漏洞（50% 概率），10 个 Claude 3.5 Haiku 作为弱监督者（随机采样 4 个文件），CCO 校准漏洞率。当目标 α=0.05 时实际违规率仅 5.0%，解决率从纯基线的 12% 提升至 14.3%；α=0.25 时解决率达 19.7%（基线 29% 的无约束）。
- MACHIA VELLI 文本冒险：以 Claude 3.5 Sonnet 为主智能体，5 个 Haiku 弱监督各维度伦理，α=0.10 时违规率 10.9%，奖励 49.0 接近无约束的 54.0。
- 实验验证了弱监督可以约制更强的主智能体，违规率紧密跟踪预设目标 α。
