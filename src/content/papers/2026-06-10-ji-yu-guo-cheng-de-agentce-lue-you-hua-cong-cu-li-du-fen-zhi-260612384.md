---
title: 'APPO: Agentic Procedural Policy Optimization'
title_zh: 基于过程的Agent策略优化：从粗粒度分支到细粒度决策点
authors:
- Xucong Wang
- Ziyu Ma
- Yong Wang
- Yuxiang Ji
- Shidong Yang
- Guanhua Chen
- Pengkun Wang
- Xiangxiang Chu
affiliations:
- University of Science and Technology of China
- AMAP, Alibaba Group
- Southern University of Science and Technology
arxiv_id: '2606.12384'
url: https://arxiv.org/abs/2606.12384
pdf_url: https://arxiv.org/pdf/2606.12384
published: '2026-06-10'
collected: '2026-06-11'
category: Agent
direction: Agent强化学习 · 过程优化
tags:
- APPO
- Agentic RL
- Branching
- Credit Assignment
- Procedural Reasoning
one_liner: 通过细粒度决策点分支与未来感知信用分配，提升Agent强化学习的探索效率与最终性能
practical_value: '- **分支位置选择**：不要固定在工具调用或工作流边界，可以在整个思维序列中根据 Branching Score（token
  熵 + 未来似然增益）选取影响下游的高价值 token 进行分支，能更高效地发现关键推理转折点，适合多轮搜索 Agent 的训练。

  - **过滤虚假高熵**：组合未来 continuation 的 policy-induced likelihood gain 可过滤掉仅因词汇稀少导致的高熵
  token，只保留真正具有决策影响力的位置，避免在无关 token 上浪费分支预算。

  - **双组优势估计**：初始 rollout 与分支 rollout 由不同策略生成，混合计算优势会引入偏差；分别计算组内相对优势（dual-group advantage）能稳定训练，可借鉴到带在线采样的推荐链路优化中。

  - **未来感知的信用分配**：额外引入的未来感知优势项（基于 Ω 裁剪）对下游影响大的决策点赋予更高信用，鼓励对后果敏感的位置进行探索，可应用在长序列多步推荐的策略梯度中。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：现有 Agent 强化学习（Agentic RL）大多在粗粒度单位（工具调用边界、固定工作流）上进行分支与信用分配，难以捕捉推理过程中真正影响结果的细粒度决策点。初步分析显示，高影响力的决策点分布在整个思维序列中，而非集中在工具调用处，且 token 熵本身不能可靠反映其重要性。因此需要一种更细粒度的分支策略与信用分配机制。

**方法关键点**：
- **Branching Score (BS)**：结合 token 熵与未来 aware 的似然增益（Ω）。Ω 是累积的折扣重要性采样比，衡量当前 token 对后续 continuation 的当前策略相对于旧策略的似然提升，过滤虚假高熵位置，选出既不确定又对下游路径影响大的决策点。
- **过程级分支**：对每个初始 rollout 选取 top-B 个 BS 最高的 token 作为分支点，从这些位置重新采样 continuation 生成分支 rollout，构建树状结构；总分支预算通过 N（初始 rollout 数）和 B 的平衡分配获得最优探索。
- **双组优势估计**：将初始 rollout 和分支 rollout 分开计算组内相对优势（z‑score 标准化），避免不同策略分布混合带来的偏差。
- **未来感知优势项**：在最终优势中引入 ˆA_fut，它是 Ω 的裁剪版本，给予下游影响大的决策点额外的信用权重，鼓励过程级探索。

**关键结果**：在 13 个基准（数学推理：AIME24/25、MATH500、GSM8K；知识密集型推理：WebWalker、HotpotQA、2Wiki、Musique；深度搜索：GAIA、HLE 等）上，基于 Llama3.1‑8B 和 Qwen2.5‑7B 等 backbone，APPO 比强 baseline （GRPO、ARPO 等）平均提升约 3‑4 个百分点，Qwen2.5‑7B 上最高提升 8.9%；Pass@K 分析表明其改善了整体解空间的多样性；分支配置分析显示在初始多样性与过程深度间存在最优平衡；消融证明 BS、双组优势、ˆA_fut 均有稳定贡献。
