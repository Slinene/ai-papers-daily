---
title: 'Learning When to Think: Utility-Guided Adaptive Reasoning for Efficient Text
  Retrieval'
title_zh: 学习何时思考：效用引导的自适应推理用于高效文本检索
authors:
- Yingtao Luo
- Kangyi Zhao
- Shiyi Du
- Yubo Li
affiliations:
- Carnegie Mellon University
- University of Pittsburgh
arxiv_id: '2610.21030'
url: https://arxiv.org/abs/2610.21030
pdf_url: https://arxiv.org/pdf/2610.21030
published: '2026-10-15'
collected: '2026-10-16'
category: Reasoning
direction: 推理增强检索 · 自适应深度
tags:
- Dense Retrieval
- Adaptive Reasoning
- Utility Estimation
- Embedding
- Efficiency
- LLM
one_liner: 提出 AURA，用检索特异性监督中间推理状态并训练效用估计器，在推理时自适应停止，以更少步骤取得最优检索
practical_value: '- 电商搜索/推荐中，对 query 改写、LLM 生成式召回、Agent 推理链路不要无限展开。用线上日志构造“正样本 + 曝光未点击/难负样本”，在每个推理/改写中间态计算
  specificity margin 作为 utility label 监督，可抑制过度改写和语义漂移；论文证明该信号与 corpus nDCG 相关达 0.97。

  - 部署时训练一个轻量 MLP（10M）预测当前上下文 embedding 的检索/推荐效用，线上连续 p 步不提升就停止生成。论文中延迟从 4.6s 降到 0.76s，指标反升；这比
  full trajectory 或按 token entropy 停止都更可靠。

  - 多任务联合优化生成+对比检索/推荐时，建议对 embedding 损失做 gradient isolation：不回传到前缀 token，避免生成能力被对比损失干扰。论文消融中去除后
  nDCG 从 34.7 掉到 29.8。

  - 推理时用 greedy expansion 比 best-of-k 更划算：每步生成多个候选，用 utility estimator 选最优继续，而不是采样完整轨迹；对
  query 改写、Agent 多步检索、搜索词生成都可复用。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：稠密检索引入推理（query rewriting / reasoning-conditioned embedding）虽能提升复杂 query 的语义匹配，但现有方法默认“更多推理=更好”，且仅用最终检索结果监督，中间 refinement 无直接信号。论文观察到推理收益高度异质：BRIGHT 上不同 query 的最优推理深度差异大，到第 10 步已有超 50% query 越过自身最优步，继续推理会造成语义漂移、降低检索特异性。

**方法关键点**：
- 统一 LLM 骨干同时做自回归推理和 embedding 提取，在句子边界取 prefix-conditioned embedding z_t。
- 定义检索特异性分数 S(z_t)=sim(z_t,d+) − mean_{top-k} sim(z_t,d−)，衡量状态区分正负样本能力。
- 训练：InfoNCE 作用于所有中间状态，权重 w_t ∝ exp(max(0, stopgrad(ΔS_t)))，强调带来特异性增益的步骤，抑制饱和/有害步骤；并用 gradient isolation 阻止对比损失回传到前缀，缓解生成/检索优化冲突。
- 训练轻量 MLP utility estimator Vφ，用 pairwise ranking loss 学状态排序；推理时连续 p 步不提升则停止，选预测效用最高的状态检索。
- 数据：基于 ReasonIR 样本，DeepSeek-R1 采样 8 条轨迹/query，句子切分后保留 67.5% 轨迹，约 545K 训练样本。

**关键结果**：在 BRIGHT 12 个推理密集域，AURA-4B 平均 nDCG@10 达到 34.7，超过 GPT-4 query expansion + DIVER-Retriever-4B 的 32.1；不依赖外部推理模型。自适应停止将平均生成从 9.5 步/332 tokens 降到 2.8 步/96 tokens，延迟从 4.6s 降到 0.76s（约 6×），同时 nDCG 提升 1.7。消融显示 utility 加权优于均匀中间监督（34.7 vs 33.6）和 final-state-only（31.2），去掉 gradient isolation 掉到 29.8；utility estimator 与 oracle 选择差距仅 0.3。MS MARCO 上与 RaDeR-7B 相当，无明显域内退化。

**最值得记住的一句话**：检索推理的停止应依据“文档区分度”而非文本细节或生成置信度；用 utility estimator 在线估计中间状态价值并自适应分配推理，能以更少计算获得更好检索质量。
