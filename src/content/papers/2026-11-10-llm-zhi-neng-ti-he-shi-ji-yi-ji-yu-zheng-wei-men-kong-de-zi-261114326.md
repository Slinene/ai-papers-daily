---
title: When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents
title_zh: LLM 智能体何时记忆？基于证伪门控的自进化框架
authors:
- Runxuan Tang
- Haoyu Gao
- Yuyan Ding
- Junyi Yao
- Zihao Zheng
- Zecheng Sheng
- Liwei Hou
affiliations:
- Nanyang Technological University
- Georgia Institute of Technology
- University of Washington
- Washington University in St. Louis
- National University of Singapore
arxiv_id: '2611.14326'
url: https://arxiv.org/abs/2611.14326
pdf_url: https://arxiv.org/pdf/2611.14326
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: LLM Agent 自进化 · 记忆更新门控
tags:
- LLM Agent
- Self-Evolution
- Memory Update
- Falsification
- Verifier-Grounded
- Commit-Refine-Reject
one_liner: 将经验更新视为可证伪假设，通过转移、证伪、回归三组探针门控记忆提交，显著降低有害写入
practical_value: '- 将 Agent 每次执行后的经验改写成结构化假设：适用前提 precondition、行为变换 behavior、预期效应
  expected effect、可验证指标 verifier；不要直接写文本记忆。电商导购/售前 Agent 可把一次成功接待沉淀为「适用场景 + 动作 + 预期结果
  + 可验证信号」。

  - 新经验先在影子状态生效，跑 target / falsification / regression 三组探针，计算 gain、pfail、dreg 后再决定
  commit / refine / reject。这相当于策略上线前的 offline replay 或小流量验证，可避免局部成功策略污染线上。

  - 维护 regression archive：用历史上已成功任务持续回归，防止新技能破坏旧技能。推荐/搜索 Agent 每次更新记忆时，也可以把已解决的 query/用户场景加入回归集。

  - 运行时做 post-commit monitoring：记录 violation，超阈值自动移除或降权。这类似线上策略监控与自动回滚，能抑制长期漂移。

  - 尽量使用可执行/外部校验信号作为 verifier，避免 LLM-judge gate；论文中 LLM-judge gate 替代后效果下降 3-4 点，说明可靠验证器是关键。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent 在长周期、有 verifier 的环境里，现有自进化机制常把单次 episode 经验直接写入记忆。局部成功不等于可复用或安全知识，容易过泛化、遗忘旧技能、积累冲突。论文研究何时应把临时经验提升为持久状态。

### 方法关键点
- 将候选经验表示为结构化假设 h=(c_h,b_h,e_h,v_h)：适用前提、行为变换、预期效应、验证器。
- 仅在临时状态 Θ⊕h 下评估三组探针：T(h) target transfer、F(h) falsification、R(h) regression；探针必须满足 Verifiable(x,v_h)=1。
- 计算统计量 bG、bPfail、bDreg；当 bG≥η、bPfail≤δ、bDreg≤β 时 commit；否则对前提条件 refine 一次再重新评估，仍失败则 reject。
- 运行时按匹配前提激活，记录 post-commit violations，超阈值移除。

### 关键实验与结果
在 WebArena、AppWorld、τ-bench、AgentDojo、LongMemEval/LoCoMo 等基准上，FGSE 取得 WebArena SR 39.8、AppWorld Avg 78.8、τ-Retail Pass1 0.724、τ-Airline Pass1 0.487；同时将 falsification failures 降到 5.0%，regression damage 降到 1.3%，harmful committed updates 降到 3.6%。消融显示：去掉 falsification probes 使 bPfail 从 5.0% 升到 18.6%，harmful updates 从 3.6% 升到 10.6%；去掉 regression archive 使 bDreg 从 1.3% 升到 5.2%。

最值得记住的一句话：把每次经验更新当成可证伪假设，经目标转移、边界反例、历史回归三组 verifier 探针检验后才写入长期记忆。
