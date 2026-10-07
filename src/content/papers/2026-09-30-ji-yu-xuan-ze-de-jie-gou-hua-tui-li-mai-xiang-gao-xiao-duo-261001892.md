---
title: 'Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents'
title_zh: 基于选择的结构化推理：迈向高效多模态搜索智能体
authors:
- Feiyu Gavin Zhu
- Xiaoyu Zhu
- Jiqi Yang
- Rui Yang
- Arnab Kumar Mondal
- Yancheng Wang
- Xinke Deng
- Jean Oh
- Reid Simmons
- Joerg Liebelt
affiliations:
- Apple
- Carnegie Mellon University
arxiv_id: '2610.01892'
url: https://arxiv.org/abs/2610.01892
pdf_url: https://arxiv.org/pdf/2610.01892
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: Agent推理效率优化·选择式结构化推理
tags:
- Multimodal Agents
- Structured Reasoning
- Inference Efficiency
- Parallel Decoding
- RL
- KV Cache
one_liner: 将多模态搜索Agent的逐步推理从自由生成改为从候选库中并行选择，保持成功率且推理延迟降超90%
practical_value: '- 在电商导购/搜索 Agent 中，把每轮规划从自由生成改成路由选择：预先定义 5-10 条高频决策候选，如“澄清需求 / 生成搜索
  query / 比价 / 读图识别 / 基于证据作答”，让模型按上下文似然打分选择，再用选中候选引导 action 解码。这样能保留自然语言 guidance
  的效果，同时规避自回归推理的延迟不可控。

  - 工程上可直接复用“并行 prefill 打分”的做法：对候选文本做 teacher-forced logprob 计算，共享历史 KV cache，不需要额外分类头或
  SFT warm-up；用 SGLang 的 `logprob_start_len` + `max_new_tokens=0` 可实现。候选库可离线维护，p95
  延迟比自由生成稳定得多，适合在线流量。

  - 训练层面，若用 RL 训练 Agent，可把“规划/路由选择”当作 categorical action，动作 token 保持常规 importance
  ratio；用 GRPO 更稳，GSPO/SAPO 多步更新时 selector-gradient 近似会损失精度，业务上可采用更多 rollout 或一次更新。

  - 候选设计要注意两点：不要只打分 index，要打分完整自然语言文本的语义；库规模从 1 到 6 带来看得见的提升，所以可以先用日志聚类/高绩效轨迹总结出高频意图，再逐步扩展到
  6-10 条。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多模态搜索 Agent 通常在每步动作前自由生成一段 reasoning，但小模型容量有限，生成长文本经常对动作没有指导，而且自回归逐 token 生成带来严重延迟，不利于在线/端侧部署。但在多模态搜索中，高层决策模式经常重复：实体已知但属性缺失就做文本搜索，图像看不清就反向搜索等。因此可以把推理空间压缩到一组可复用候选，而不需要在完整自然语言空间里每步都思考。

**方法关键点**
- SSR：将每次动作前的“推理”从 open-ended generation 改成从预定义的 reasoning library 中选择。库由 6 条自然语言候选组成，覆盖反向搜索识别实体、文本查找事实、裁剪查看细节、基于证据作答、基于图像作答、通用知识作答。
- 并行推理解码：用语言模型自身打分，不添加分类头。对每个候选做 teacher-forced prefill，计算 length-normalized log-likelihood（α=1），softmax 后采样；所有 token 和候选共享 history KV cache 可并行计算，无需生成新 token。选出的候选作为自然语言 guidance 插入上下文，再生成该轮动作。
- 训练：SFT 用 categorical selection loss + action token loss；RL（GRPO/GSPO/SAPO）中 reasoning selection 只贡献一个 categorical importance ratio，动作 token 保持常规 ratio；可以直接 RL 训练无需 SFT warm-up，GSPO/SAPO 用 detached competitor scores 近似梯度。
- 工程实现上，可通过 SGLang 的 `logprob_start_len` 和 zero max_new_tokens 进行 prefill-only scoring。

**关键结果**
- 4B SSR GRPO 在 7 个测试集平均成功 61.37%，和同尺寸 SOTA TAPO+GSPO 的 61.25% 相当；2B SSR 51.26%。
- 相比 freeform reasoning，GRPO/GSPO/SAPO/SFT 下 per-turn 推理延迟降低 91.9-94.6%，每问题模型推理延迟降低 28.7-53.9%；有效推理吞吐从 ~70 tokens/s 提升到 2500-3300 tokens/s。
- 对比 Chain-of-Draft、Sketch-of-Thought、Efficiency-reward RL、Probe & Prefill，SSR 以最高成功率把推理时间再压缩约 7x，p95 推理延迟只有 0.071s，波动很小。
- 消融：index-only 选择平均成功率降 3.9 个点；库大小 1→6，成功率从 37.24% 提到 61.37%。

**最值得记住的一句话**
小模型搜索 Agent 不必每一步在完整语言空间中思考，把高频推理模式组织成一个紧凑可复用候选库并用模型似然做并行选择，是兼顾成功率与在线延迟的实用设计。
