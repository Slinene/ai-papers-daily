---
title: 'J-Comm: Jacobian-Guided Latent Communication between LLM Agents'
title_zh: J-Comm：基于雅可比引导的 LLM 智能体间潜在通信
authors:
- Xiangwei Wang
- Wei Wang
- Sachith Seneviratne
- Ken Chen
- Yu Xia
- Peng Wang
- Saman Halgamuge
affiliations:
- The University of Melbourne
- Shanghai Jiao Tong University
arxiv_id: '2610.32871'
url: https://arxiv.org/abs/2610.32871
pdf_url: https://arxiv.org/pdf/2610.32871
published: '2026-10-23'
collected: '2026-10-26'
category: MultiAgent
direction: 多智能体潜在通信与推理加速
tags:
- Latent Communication
- Multi-Agent
- Jacobian
- LLM
- Training-Free
one_liner: 用无需训练的 GEAR 潜在推理与 H+J 隐式/雅可比双通道接口，让不同宽度 LLM 智能体高效传递推理状态并大幅减少文本 token
practical_value: '- 可将 H+J 接口用于跨模型 Agent 协作：H 通道传递连续输入，J 通道注入雅可比中间状态，无需共享 KV cache
  或相同宽度，适合电商多模型（如召回/排序/文案 Agent）异构部署。

  - GEAR 属于训练免重排：在已有模型 embedding 上按几何共识单调优化 token 候选，可直接作为 LLM 推理后处理，低成本提升生成质量。

  - J-Comm 相对 TextMAS 减少 19.2–74.8% 文本 token，能在 Agent 密集交互（如商品文案生成、对话式推荐）中显著降低推理延迟和
  token 成本。

  - J 通道的 vocabulary-indexed Jacobian-lens 坐标提供中间计算的可观测视角，可用于模型诊断、蒸馏或跨模型知识迁移。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现有 LLM 多智能体多用文本交换推理过程，token 成本高且难以跨异构模型传递中间计算；潜在通信需要有效连续推理与可被外部模型利用的接口。

方法关键点：J-Comm 由两个核心组成——① GEAR，无需训练，在现有模型 embedding 上对 token 候选加权，每步单调优化候选 token 在嵌入空间中的几何共识；② H+J 通信接口，H 通道提供来自反馈分布的连续输入，J 通道以 vocabulary-indexed Jacobian-lens 坐标传递中间状态。Receiver 用自身词典重建这些线索并在 prefill 阶段注入中间层，无需共享 KV cache 或要求模型宽度一致。

关键结果：在 Qwen3-8B→Qwen3-4B 通信设置下，J-Comm 在七个基准上取得最高平均分，包括 MATH500 94.80%、GPQA-Diamond 54.55%、AIME2024+2025 73.33%、ALFWorld 62.93%；相较 TextMAS 提升 1.29–8.59 个百分点，同时生成文本 token 减少 19.2–74.8%。
