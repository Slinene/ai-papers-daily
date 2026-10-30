---
title: Learning Calibrated Confidence for Multi-Agent Collaboration
title_zh: 多智能体协作中的校准置信度学习
authors:
- Chenxiao Fan
- Chongming Gao
- Gangyi Zhang
- Yaxin Gong
- Leyang Shen
- Jiakai Wang
- Dong Wang
- Yang Liu
- Haoyan Liu
- Xinting Hu
affiliations:
- University of Science and Technology of China
- Qwen Business Unit of Alibaba
- National University of Singapore
arxiv_id: '2610.39927'
url: https://arxiv.org/abs/2610.39927
pdf_url: https://arxiv.org/pdf/2610.39927
published: '2026-10-29'
collected: '2026-10-30'
category: MultiAgent
direction: 多智能体协作 · 置信度校准
tags:
- Multi-Agent Collaboration
- Confidence Calibration
- GRPO
- LLM Agents
- Calibration
- Agentic IR
one_liner: 让多智能体在 RL 中联合学习任务与校准置信度，并在交接与最终输出传递该信号，提升协作准确率与可靠性
practical_value: '- 在多级 Agent 检索/推理流水线中，每个 handoff 都附上 calibration 后的置信度，而不仅是最终答案；下游做
  query 分解、召回、重排或审核时，可以把上游置信度作为显式特征，决定是否追加检索、采信或改写中间结果。

  - 训练下游 Agent 时，上游模型冻结并用其真实报告做训练数据，避免离线报告与在线行为不一致；可用 confidence-aware weighting 的做法：把置信度
  mask 掉重打分，以 per-token log-prob 变化识别真正受置信度影响的位置，对这些位置加权 task advantage，能强化模型对置信度信号的利用。

  - 最终置信度可用于选择性回答和定向复查：高置信请求自动返回或进入低成本通道，低置信请求追加检索/二次审核/人工兜底，实现覆盖率和准确率的可控权衡；在电商搜索、广告文案生成、Agent
  客服等对可靠性敏感的场景尤其适用。

  - 小心未校准置信度：论文显示去掉 BCE calibration loss 后，融合场景准确率会低于完全不传置信度的 MAS；也就是说不可靠的置信度可能比没有信号更误导下游，上线前应做
  Brier/AUROC 校验。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：复杂信息获取需要多 Agent 分工，但上游给出中间答案时没有可靠性信号，下游只能靠文本证据决定信任或复核；口头或后验 confidence 不够可靠，未校准信号甚至比没有更差。MASCAL 把置信度作为 Agent 间可学习、可传递的信号，通过 RL 联合学习任务与校准置信度。

方法关键点：
- 每个 Agent 轨迹切为 task segment 与 confidence segment；confidence 从特殊 token H/L 的 logits 读出 c=sigmoid(z_H-z_L)，可端到端梯度校准，避免 verbalized 采样的方差。
- 训练信号有三类：task policy gradient 用 correctness/format reward；confidence policy gradient 用 1-(Y-c)^2 只作用于 confidence segment；BCE loss 直接对齐 c 与 correctness。
- 上游先训练后冻结，用其真实报告训练下游；confidence-aware weighting 将上游置信度 mask 掉重打分，用 per-token log-prob 变化 |Δ| 归一后加权 task advantage，强化真正受置信度影响的位置。

关键实验：基于 Qwen3-8B + GRPO，覆盖顺序交接、报告融合、答案审阅三种架构；数据集包括 MuSiQue/HotpotQA/2Wiki 多跳 QA、LogiQA2/ReClor/AR-LSAT 逻辑推理、DeepScaleR/MATH500/AMC&AIME 数学推理。MASCAL 在所有场景准确率最高：顺序交接平均 59.00（Task-RL MAS 47.49），融合 61.45（54.78），logic 76.59（73.85），math 78.69（72.91）。校准质量明显提升：MuSiQue 上游 Brier 0.0972 vs 0.1576，AUROC 0.8663；数学 Brier 0.0827 vs 0.2513。干预隐藏或随机化置信度会使准确率明显下降，验证下游确实依赖该信号。3-hop/4-hop 直接迁移仍最强，1.7B/4B/8B 均有效。消融显示 BCE 校准损失影响最大，去掉后融合准确率甚至低于无置信度 Task-RL MAS。

最值得记住：要让 confidence 在 Agent 间可用，必须同时学习校准和利用；把 confidence 做成可微分 readout，并按位置加权利用信号是关键。
