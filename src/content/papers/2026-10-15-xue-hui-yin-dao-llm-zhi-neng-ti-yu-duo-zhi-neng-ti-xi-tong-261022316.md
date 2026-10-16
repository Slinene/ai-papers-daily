---
title: Learning to Steer LLM Agents and Multi-Agent Systems
title_zh: 学会引导 LLM 智能体与多智能体系统
authors:
- Leyang Shen
- Yaxin Gong
- Yang Zhang
- Chenxiao Fan
- Jiakai Wang
- Dong Wang
- Yang Liu
- Fuli Feng
- Chun Kai Ling
- Tat-Seng Chua
affiliations:
- National University of Singapore
- University of Science and Technology of China
- Qwen Business Unit of Alibaba
arxiv_id: '2610.22316'
url: https://arxiv.org/abs/2610.22316
pdf_url: https://arxiv.org/pdf/2610.22316
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 外部监督与强化学习
tags:
- goal drift
- steering agent
- GRPO
- multi-agent systems
- fast-slow paths
- RL
one_liner: 提出外部 steering agent，用 fast/slow 双路径和 RL 联合训练，在长程执行中实时纠正 goal drift，提升单智能体和多智能体搜索任务表现
practical_value: '- 对商品搜索/导购等多步 Agent，可增加一个外部 steering policy：fast path 只需一次单 token
  判断“是否需要干预”，再触发 slow path 生成干预动作；阈值可在部署时调节干预频率，无需重新训练，直接控制成本与效果。

  - 训练时冻结执行器，只训 steering agent；用 pairwise ranking 学 fast path 的状态优先级，用 GRPO 学 slow
  path 的干预生成，并把“不干预基线”加入 group 归一化。这套目标适合作为业务 Agent 在线监督模块的训练模板。

  - 多智能体电商链路（query 规划→召回→验证→回答）可在 agent 交接点插入 steering，动作设为 note/retry，重点抑制 verifier
  过度拒绝导致的重复修订，减少无效 API 轮次。

  - 该 steering 能力可跨执行器迁移：用 Qwen executor 训练后可直接监督 Llama/Mistral/Phi 执行器，适合多模型后端共存的平台。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：LLM agent 和 MAS 在长程执行中容易发生 goal drift——局部子目标压过整体任务目标，如搜索 agent 在已获得关键信息后仍反复搜同一主题，或多智能体中 verifier 过度拒绝已合格答案。规划与事后验证无法及时止损，而实时外部监督能更早纠正。

方法关键点：
- 设计 steering agent，观察任务目标与执行上下文，动作空间为 `pass` 或具体干预（note/retry 等）。
- 采用 fast/slow 双路径：fast path 仅用单 token yes/no 的 log-odds 计算 steering priority，经 soft threshold 触发 slow path；slow path 生成 CoT 和干预动作。
- RL 训练：从无干预 rollout 建 state bank，采样状态并生成多条干预，通过多次 continuation 取平均 reward；fast path 用 pairwise ranking loss 学状态优先级，slow path 用 GRPO 学动作，且把无干预基线 b_s 放进 group 归一化；执行器冻结，只更新 steering agent。

关键实验：单智能体设定下，用 Qwen2.5-7B 执行搜索任务，steering agent 用 Qwen3-8B 训练。在 7 个 QA benchmark 上，zero-shot steering 仅提升 1.84 点；RL 训练后提升 6.66 点，且平均仅 0.93 次干预。相比 planning(+3.21) 和 verification(+2.17) 的 RL 版本更高。将干预频率调到最高，增益达 17.11 点。OOD 搜索 benchmark 上也有提升（Frames Avg@4 26.46→36.32，Pass@4 44.17→59.71）。跨执行器迁移：训练于 Qwen2.5-7B 的 steering agent 监督 Llama/Mistral/Phi 分别提升 15.78/12.01/5.92 点。多智能体五角色场景中，zero-shot 在 25% 干预频率下掉 1.04 点，RL 训练后转为 +3.90，至高干预频率为 +5.34。

最值得记住的一句话：把监督能力从执行器中解耦出来，用 fast path 学“何时干预”、slow path 学“如何干预”，并通过 RL 联合优化，是低侵入、可迁移地抑制 goal drift 的有效方案。
