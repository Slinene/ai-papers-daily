---
title: 'PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design'
title_zh: PRISM：特权兄弟图引导的多智能体拓扑设计
authors:
- Phuong Tuan Dat
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.20628'
url: https://arxiv.org/abs/2610.20628
pdf_url: https://arxiv.org/pdf/2610.20628
published: '2026-09-28'
collected: '2026-10-19'
category: MultiAgent
direction: 多智能体拓扑设计 · 特权蒸馏
tags:
- Multi-Agent
- Topology Design
- On-policy Distillation
- Privileged Information
- LLM
one_liner: 利用同一 query 的其他成功拓扑作为特权输入，通过 on-policy 蒸馏改进多智能体拓扑生成器后训练
practical_value: '- 如果业务中已有 execution-verified 轨迹/方案语料，但只有成功与否、没有显式排序，不要直接继续 SFT 到高频解；可以借鉴
  PRISM，用同一请求/用户的其他成功解作为训练期特权输入，让学生模型在自己的采样轨迹上做 on-policy 蒸馏，保持多样性并提升 query-specific
  效果。

  - 推荐/搜索后训练常受 exposure bias 困扰：离线伪标签与线上自回归生成分布不一致。PRISM 的做法是学生按当前策略采样 M 条轨迹，教师在访问状态上给出决策级软标签，且用
  reverse KL 鼓励模式集中，这比 forward KL/JSD 在数学类任务上平均更高；适合有多个成功解、需要模型收敛到某个模式而非平均的场景。

  - 特权信息分支采用 zero-initialized FiLM + low-rank（rank=16）控制参数，训练后丢弃，部署结构不变、推理成本几乎不增；电商/广告中可将训练期才有的完整用户行为、后验转化信号、专家标注等作为特权输入，蒸馏进部署模型。

  - 做消融时建议同时跑 constant teacher 和 shuffled teacher 对照，分离“蒸馏过程收益”和“特权内容收益”；PRISM 显示
  shuffled 甚至会误导，constant 蒸馏只带来部分提升，真实 sibling 内容贡献额外 +1.66% 平均准确率，这种拆解对评估训练技巧很有用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：多智能体系统性能依赖协作拓扑，现有 query-conditioned 拓扑生成器从 execution-verified graph corpus 后训练，但 corpus 只记录成功图而不给排序，继续 SFT 使生成分布集中于高频拓扑，跨基准不稳定（AQuA 掉 12.6%）；teacher forcing 训练与自回归推理存在 exposure bias。需要从同一 corpus 中恢复 per-query 偏好信号，且不增加部署成本。

**方法关键点**：
- Stage 0: 基于 ARG-Designer 的 cold start，用 execution-verified graphs 训练生成器。
- Stage 1: 构造特权教师：克隆学生并加 zero-initialized low-rank FiLM 分支，输入 query + 同 query 的另一成功 sibling graph；教师最小化 SFT 目标。
- Stage 2: on-policy self-distillation：学生按当前策略采样 M 条轨迹，教师在这些访问状态上给出决策级软分布；用 reverse KL + anchor loss 训练；anchor 为固定参考图，λ=0.3。
- Stage 3: 部署学生，丢弃教师与特权分支；推理结构与 ARG-Designer 完全相同。

**关键实验**：
- 6 个 benchmark（GSM8K, MultiArith, SVAMP, AQuA, HumanEval, MMLU），Qwen2.5-7B-Instruct。
- PRISM 在每个 benchmark 上最优：GSM8K 88.02 vs ARG-Designer 79.98；AQuA 76.38 vs SFT 62.60 且比 ARG-Designer 75.20 高 1.18；平均 agent 调用仅从 3.00 增至 3.04（+1%）。
- 对照：shuffled teacher 无增益，constant teacher 平均 83.86，PRISM 平均 85.52，说明内容贡献；reverse KL 最优；rank 不敏感。
- 输出多样性：SFT 的 top-1 拓扑占比从 0.171 增至 0.346，PRISM 降至 0.157；查询条件互信息 excess 从 0.017 增至 0.160。

**最值得记住的一句话**：成功的 sibling graph 不直接作为标签，而是通过训练期特权教师 + on-policy 蒸馏，把“该 query 下哪种成功拓扑更值得跟随”的偏好压缩进学生，部署成本不变。
