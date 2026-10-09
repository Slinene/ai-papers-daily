---
title: 'Agent Plasticity: Measuring Self-Improvement Through Experience'
title_zh: 智能体可塑性：度量基于经验的自我改进效率
authors:
- Harman Singh
- Anton Bakhtin
- Rulin Shao
- Gabriel Synnaeve
- Ilia Kulikov
- Rob Fergus
- Sanjeev Arora
- Kurt Keutzer
- Jason Weston
- Anuj Mahajan
affiliations:
- UC Berkeley
- Meta Superintelligence Labs
- University of Washington
- Princeton University
arxiv_id: '2610.08902'
url: https://arxiv.org/abs/2610.08902
pdf_url: https://arxiv.org/pdf/2610.08902
published: '2026-10-05'
collected: '2026-10-09'
category: Agent
direction: Agent 自改进评估 · plasticity
tags:
- agent plasticity
- self-improvement
- evaluation
- persistent artifacts
- held-out generalization
- learning efficiency
one_liner: 提出 agent plasticity 指标，度量智能体将经验转化为留出性能增益的效率，并诊断改进瓶颈
practical_value: '- 自改进 Agent 或线上学习链路不要只看最终指标；用「留出收益 / 累计学习成本」画 plasticity 曲线，能区分起点高但不会学和起点低但学习效率高的模型/策略。电商
  Agent 迭代 prompt、tool、memory 时可按此评估 ROI。

  - 把改进过程拆成持久化 artifact：tools / skills / memory，每个新 session 从 fresh context 开始并继承
  artifact。这样可以隔离「记忆/工具沉淀」的贡献，适合做 A/B 或消融；对应搜索推荐 Agent 的 query 改写工具、规则库、用户画像缓存。

  - 失败诊断用 F_absent / F_missed / F_used 分类：低复用率提示检索/部署问题，高复用但仍失败提示 artifact 质量/泛化/应用问题。上线前可对
  Agent 失败 case 打标，选择不同干预，例如 RAG 召回优化 vs skill 重写。

  - 评估 OOD 转移：除同分布 held-out 外，加入更难或更极端的流量层，如更强对手、长尾 query、大促场景，观测自我改进是否真正泛化，避免只在训练样本上打转。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 Agent 评测大多只测固定时点能力，忽略「在经验中自我改进」的效率。两个当前能力相近的 Agent，在相似学习机会后可能走向截然不同的轨迹；因此需要回答三件事：未来表现是否提升并泛化到交互之外、新能力多高效获得、改进过程在哪里断掉。

**方法关键点**
- 固定权重 Agent lineage：模型权重冻结，持久化 artifact inventory 包含可执行 Python 工具、自然语言策略/技能和文本记忆；每个 acting episode 从 fresh context 开始，未来实例继承这些 artifact。
- 三种评估 split：training interactions、held-out ID、held-out OOD；held-out 轨迹和分数不暴露给 reflection，报告完整 checkpoint 曲线而非只看终点。
- 学习成本包括环境交互和 reflection 调用 token，折算为美元；提出 agent plasticity，P = held-out 性能增益 / 累计学习成本。头条指标 Psat 用 Hill 曲线拟合到 90% 饱和，按每 $1,000 学习成本计算 held-out ID 增益。
- 失败诊断：对每个决策失败分类为 F_absent（无覆盖 artifact）、F_missed（有 artifact 未用）、F_used（用了仍失败），同时统计决策级 reuse 率。

**关键实验与结果**
- 环境：Chess（Easy/Hard）、5x5 Go、6x6 Hex、NetHack；模型覆盖 Claude Fable 5、Claude Opus 5、GPT-5.6 Sol、GPT-5.5、Gemini 3.1 Pro 等。
- Chess Hard 中 Claude Fable 5 held-out ID 从 37.5% 升至 73.3%（checkpoint 16–20 均值），Opus 5 从 25.0% 升至 66.4%，GPT-5.6 Sol 从接近 0% 升至 36.9%；另有模型保持近初始或退化。
- 三棋平均 Psat：GPT-5.6 Sol 298 pp/$1,000，Claude Opus 5 233，Claude Fable 5 57，Claude Opus 4.8 14，GPT-5.6 Luna 为 0。终点能力与获取效率明显分离。
- NetHack 中 Claude Opus 5.5 平均分约 2k 升至约 6k，Psat=61.75；其他模型大多无可靠提升。
- 失败分析显示：低 artifact 复用与弱提升相关；强改进者复用率 94–98%，但 83–99% 的剩余失败仍发生在使用 artifact 时，指向 artifact 质量、泛化或应用瓶颈。

**最值得记住的一句话**：评估长期 Agent 不仅要看它能做什么，还要看它如何高效地通过经验变得更强——artifact reuse 只是必要条件，不等于能力。
