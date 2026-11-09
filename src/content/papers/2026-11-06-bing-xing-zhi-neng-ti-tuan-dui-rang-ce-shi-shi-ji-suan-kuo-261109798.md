---
title: Test-Time Compute Scales Better with Parallel Agent Teams
title_zh: 并行智能体团队让测试时计算扩展更好
authors:
- Junlin Wang
- Haozhe Chen
- Ang Li
- Rahul Chalamala
- Zhuang Liu
affiliations:
- Duke University
- Modal Labs
- Princeton University
- New York University
arxiv_id: '2611.09798'
url: https://arxiv.org/abs/2611.09798
pdf_url: https://arxiv.org/pdf/2611.09798
published: '2026-11-06'
collected: '2026-11-09'
category: MultiAgent
direction: 多智能体并行采样 · 测试时扩展
tags:
- test-time compute
- multi-agent
- best-of-N
- parallel teams
- LLM agents
- verifier
one_liner: 将预算拆成多个小并行团队采样，兼顾均值提升与方差收益，优于 best-of-N 单 agent 和单一大团队
practical_value: '- 有 verifier/reward 的场景（搜索 query 生成、广告文案、商品标题、推荐理由），预算分配别只做 best-of-N
  单 agent 或上一个大团队；把预算拆成多个 8–10 agent 的独立 flat team，team 内共享 memory/log，最后用离线 verifier
  或线上 A/B 选最优团队结果。这比单纯多采单 agent 更能持续利用算力。

  - Agent 架构上避免 orchestrator/manager：直接用公共 forum 让 peer 分享尝试与分数，鼓励用 WIN/FAIL 等短标签做异步信息传播；这能提高团队均值，且不引入通信瓶颈。该设计简单、工程成本低。

  - 做预算规划前，先跑少量样本估计单 agent 和 team 的均值/方差，套用 E[best]≈μ+σ√(2 ln N) 判断是否值得花 10x 成本组队；任务越难（单
  agent 成功率越低）越值得组队，简单任务增益有限。

  - 如果用 frontier API 模型，其输出方差小，重复采样增益平；可以考虑用更便宜的开放模型+并行小团队来追平同等成本，尤其对长链路、可自动验证的优化任务。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：在可验证的长链路优化任务中，测试时扩展通常有两条路：best-of-N 独立 agent 采样（mean 低、饱和快）和单一大团队（mean 更高但只有一次观测，浪费方差收益，且团队变大不保证涨分）。需要一种能随预算持续获利的折中方案。

**方法关键点**：
- 提出 parallel agent teams：把预算 B 拆成 N=B/k 个大小为 k 的小团队并行独立运行，每个团队内部通过共享 forum 协作，最后 verifier 保留最好团队结果。
- 主实验用 Qwen3.8-27B，团队大小 k=10，在 12 个长链路任务（GPU kernel、形式化证明、漏洞利用、拓扑优化等）上运行约 100 个独立 agent 和 10 个团队。
- 统计模型：单样本分数 X~N(μ,σ²)，best-of-N 期望约为 μ+σ√(2 ln N)；parallel agents 方差收益最大但均值低，单一大团队只有一次观测、无方差收益，小团队并行在均值与方差收益之间平衡。
- 团队内采用 flat 结构，不设 manager/orchestrator；实验显示采用 manager 的团队反而更差。

**关键实验**：
- 在 100 agents 预算下，parallel teams of 10 在 12 个任务中 10 个超过 parallel agents；平均分数比 parallel agents 高 27%。
- 在运行过 single big team 的 4 个任务上，10 个 10-agent 团队全面超过 1 个 100-agent 团队，提升 8%–30%；大团队从 64 到 100 agents 时分数下降。
- 等成本下，27B 模型的小团队在 8 个任务中的 4 个上超过 GPT-5.6-sol 多次采样。
- 统计模型在 12 个任务中 9 个正确预测团队相对 parallel agents 的增益方向；非正态或截断任务会失效。

**最值得记住的一句话**：当预算大时，先把单个 sample/团队的质量（μ）提上去，比单纯增加 sample 数量更有效；小团队并行同时抓住均值提升和 best-of-N 的方差收益。
