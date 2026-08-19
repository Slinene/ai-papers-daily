---
title: Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals
title_zh: MoE 块蕴含强幻觉检测信号
authors:
- Joao Fonseca
- Rodrigo Rodrigues
- Paolo Romano
affiliations:
- INESC-ID
- Instituto Superior Técnico
arxiv_id: '2608.17687'
url: https://arxiv.org/abs/2608.17687
pdf_url: https://arxiv.org/pdf/2608.17687
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: MoE 路由信号幻觉检测
tags:
- hallucination detection
- MoE
- router entropy
- token-level
- LLM-as-judge
one_liner: 利用 MoE 路由熵/专家不一致等内部信号提出 InnerExpert，实现 token 级幻觉检测并达 SOTA
practical_value: '- 若业务已使用 MoE 架构模型（如 Mixtral、DeepSeek），可直接采集路由熵、专家激活分布、专家不一致等特征，作为额外的“不确定性/事实性”信号，用于拒答、触发检索或降低生成置信度，成本几乎为零。

  - 借鉴 InnerExpert 的轻量分类器设计：将路由特征与隐藏状态拼接后训练一个小型检测头，只做一次前向即可输出 token 级幻觉概率，适合实时推荐/Agent
  场景。

  - 用 LLM-as-judge 自动生成 token 级真实标签，避免人工标注，支持线上数据回流持续更新检测器；对电商文案、推荐理由、Agent 回答可做细粒度事实核查和风险定位。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 幻觉检测通常停留在答案或句子粒度，无法定位具体错误 token，难以做细粒度干预；MoE 架构虽然被前沿开源模型广泛采用，其路由机制产生的内部信号（如路由熵、专家不一致、专家使用模式）此前未用于幻觉检测。

方法：InnerExpert 首次利用 MoE 特定信号做 token 级幻觉检测。它将每层的路由熵、专家选择分布、专家输出不一致等路由级特征与标准 transformer 隐藏状态结合，形成紧凑的逐 token 特征向量；然后用轻量分类器判别每个 token 是否幻觉。训练标签由 LLM-as-judge 自动标注，支持模型更新且无需人工。整个流程只需一次前向传播，不增加额外推理阶段。

结果：在 5 个数据集、2 种 MoE 架构上，InnerExpert 均优于现有方法，答案级 AUROC 最高达 0.91，token 级 AUROC 最高达 0.76，证明 MoE 内部路由信号对幻觉具有很强的指示能力。
