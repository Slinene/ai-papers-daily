---
title: 'AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System'
title_zh: AdCoEvo：协同进化的多智能体广告投放系统
authors:
- Tianzhu Hu
- Hang Yu
- Zeyuan Zhao
- Zeyu Pan
- Huan Luo
- Chun Gan
- Mingzhe Cao
- Liubin Wang
- Mingming Li
- Jiao Dai
affiliations:
- 中国科学院信息工程研究所
- 中国科学院大学网络空间安全学院
- 悉尼大学
- 京东
arxiv_id: '2610.19454'
url: https://arxiv.org/abs/2610.19454
pdf_url: https://arxiv.org/pdf/2610.19454
published: '2026-10-14'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体协同进化广告投放
tags:
- Multi-Agent
- Agentic RL
- Advertising Delivery
- Co-Evolution
- LoRA
- AuctionNet
one_liner: 角色分工+轮换更新的多智能体广告投放系统，相比规则基线 ADV 提升 14.02%、CPA 降低 7.07%
practical_value: '- **角色切分可复用**：把广告投放拆成账户级预算规划（Planner）、单元级 tCPA 调整（Optimizer）、周期末诊断（Inspector）三个独立
  LoRA 策略，按各自反馈结算周期更新。这比单 Agent 一条链路更稳定，且能分别积累运营经验。

  - **在线持续学习用异步轮换**：每周期只更新一个角色，其他参数冻结，用实际业务反馈（ADV/CPA）作为奖励；每个角色配一个轻量 PrefixValueModel
  做 baseline 降方差，适合延迟反馈场景。

  - **诊断 guidance 优于统计摘要**：让 Inspector 生成结构化诊断并作为下一周期 Planner/Optimizer 的输入，实验中比固定统计摘要
  ADV +1.61%、CPA −1.55%。

  - **小模型+领域训练更划算**：8B 模型+每角色 LoRA 的 API 成本远低于闭源大模型，且性能更好；广告投放任务组织与领域训练比模型规模更关键。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
广告投放自动化仍依赖人工协调，难以规模化；单个任务自动化（出价、预算分配）未解决整体协同，且市场动态变化使固定策略快速失效。需要一套能自动执行、持续从业务反馈中学习的多智能体系统。

**方法关键点**  
- **角色专业化**：Planner 负责账户预算分配（每 W 步一次），Optimizer 负责广告单元 tCPA 乘子调整（剩余每步），Inspector 周期末生成诊断 guidance 供下一周期使用。三者分别用独立 LoRA 策略。
- **奖励构造**：Planner/Optimizer 用代理回报 `Q(F,C,N)=F−η(C−ρN)s`，结合局部账户与全局回报；Inspector 奖励为相邻周期标准化反馈向量变化 `wᵀ(y_e−y_{e−1})`。
- **离线训练**：SFT 学动作语义和格式，GSPO 离线 RL 用 leave-one-out advantage（Planner/Optimizer）和与无诊断基线的差值（Inspector）做序列级策略优化。
- **在线协同进化**：每周期结算后轮换更新一个角色（P→O→I），其他参数冻结；每角色有独立 PrefixValueModel 做 baseline，Optimizer 用 GAE，Planner/Inspector 用 reward−V baseline；策略更新采用 token 级概率比 mask 与重要性裁剪。

**关键结果数字**  
在 AuctionNet Sparse 和 General 两个环境、5 个 50 周期市场序列上：相比规则基线 Rule，ADV +14.02%、CPA −7.07%；相比固定参数多智能体 AdCoEvo (Fixed)，ADV +3.96%、CPA −1.24%；相比最佳闭源模型 GPT-5.6-Terra，ADV +3.73%、CPA −3.23%；API 成本仅 0.235 CNY/周期，远低于大模型。消融证实角色分工、训练阶段、co-evolution 更新 Inspector、诊断 guidance 均有增益。

**最值得记住的一句话**：把跨时间尺度的广告运营决策拆成角色并异步轮换更新，能让多智能体系统用实际投放反馈持续协同进化，小模型即可超过大模型和固定策略。
