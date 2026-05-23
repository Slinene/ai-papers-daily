---
title: Advancing Mathematics Research with AI-Driven Formal Proof Search
title_zh: AI 驱动的形式化证明搜索推进数学研究
authors:
- George Tsoukalas
- Anton Kovsharov
- Sergey Shirobokov
- Anja Surina
- Moritz Firsching
- Gergely Bérczi
- Francisco J. R. Ruiz
- Arun Suggala
- Adam Zsolt Wagner
- Eric Wieser
affiliations:
- Google DeepMind
- Aarhus University
- Google
arxiv_id: '2605.22763'
url: https://arxiv.org/abs/2605.22763
pdf_url: https://arxiv.org/pdf/2605.22763
published: '2026-05-21'
collected: '2026-05-23'
category: Agent
direction: 形式化数学证明搜索 · 多智能体系统
tags:
- Formal Proof
- Lean
- LLM
- Automated Theorem Proving
- Agent
- DeepMind
one_liner: 大规模评估 LLM 驱动的 Lean 形式化证明在开放数学问题上的自动求解，最高代理独立解决 9 个 Erdős 问题
practical_value: '- 对于需要严格逻辑保证的 Agent 任务，可借鉴 Lean 编译验证思路，用规则引擎或类型系统过滤 LLM 输出，控制幻觉影响

  - 基础代理采用「LLM 生成 + 外部工具反馈」的交替迭代模式，成本低且有效，可作为复杂 Agent 的基线设计

  - 多子代理独立搜索并集成最佳结果的策略，在提升成功率上有明显收益，适用于需要探索多条推理路径的推荐或决策系统

  - 部署时需权衡成本与成功率：对高难度问题使用更复杂的代理，普通问题用轻量版，可参考该研究中的阶梯式成本效益分析'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 在数学推理上表现亮眼，但自然语言证明易含隐蔽逻辑错误，阻碍其在严谨研究中的落地。形式化证明语言（如 Lean）可由编译器自动验证每一步逻辑，为 LLM 提供了可靠的输出校验手段。然而，过去该方法主要用于竞赛数学或人工辅助形式化，缺乏在大规模开放数学问题上的系统评估。

**方法**：该研究开发了 AlphaProofNexus 框架，并构建了两类代理。基础代理（basic agent）由多个子代理独立搜索证明，每个子代理交替执行 LLM 生成代码与 Lean 编译反馈，直至找到完整证明或超时。高级代理（most capable agent）在此基础上引入更复杂的搜索策略和成本优化。

**关键结果**：高级代理在 353 道 Erdős 开放问题中自主解决 9 道（每题成本约数百美元），在 OEIS 猜想集上证明 44/492 条，并已部署到组合优化、图论、量子光学等真实研究场景。基础代理虽能复制 Erdős 成功，但在最难问题上成本更高。实验首次展示 AI 辅助形式证明在开放问题上的规模化可行性，并揭示了代理设计对成功率和成本的影响。
