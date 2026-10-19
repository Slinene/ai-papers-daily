---
title: 'ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid
  Linear Attention Large Language Models'
title_zh: ReaDy：循环状态作为动态上下文加速混合线性注意力大模型投机解码
authors:
- Bohan Sun
- Zunhai Su
- Xialie Zhuang
- Jianjin Li
- Ngai Wong
- Chuan-Wei Kuo
affiliations:
- StartLux
- University of Chinese Academy of Sciences
- The University of Hong Kong
arxiv_id: '2610.20503'
url: https://arxiv.org/abs/2610.20503
pdf_url: https://arxiv.org/pdf/2610.20503
published: '2026-10-13'
collected: '2026-10-19'
category: LLM
direction: LLM 投机解码加速 · 循环状态
tags:
- Speculative Decoding
- Hybrid Linear Attention
- Recurrent States
- Qwen3.8-27B
- DSpark
- Decoding Acceleration
one_liner: 首个利用混合线性注意力循环状态做位置特定上下文检索的投机解码方法，平均3.16倍解码加速
practical_value: '- 如果业务里用 Hybrid Linear Attention 类模型（如 Qwen3、Gated DeltaNet 等）做对话式电商助手或
  Agent 长链路生成，可以把目标模型已计算过的 recurrent states 作为草稿模型的辅助上下文，而不是只用最后层 hidden states；这类状态累积历史
  token 关联，对预测后续位置更有帮助。

  - 工程实现上，参考 ReaDy 的低秩状态读取（low-rank state reads）和 fused operators：将额外上下文投影到低秩空间再融合进
  draft representation，避免草稿模型显存带宽和 I/O 显著增加，适合在线推理服务做低延迟 speculate。

  - 采用两阶段轻量适配：先冻结 backbone 只训练 query/reader，微调 sequential prediction head；这种改造方式可在已部署的生成模型上低成本引入投机解码，无需全量重训，利于快速线上验证。

  - 论文在单卡 B200 上对 Qwen3.8-27B 平均 3.16x 加速，吞吐比 DSpark 提高 7.97%。如果业务需要大量长文本生成（自动文案、Agent
  planning、多轮推荐解释），可以把 speculative decoding 作为默认推理优化方案之一。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：投机解码常用 feature-based drafter，但目标模型隐藏特征对后续多个草稿位置的上下文强调可能不匹配。混合线性注意力（HLA）模型维护紧凑的循环状态，累积历史关联，可以作为草稿模型补充上下文的高效来源。

**方法关键点**：ReaDy 为每个草稿位置学习一个 query，从目标模型已 committed 的循环状态中检索补充上下文；轻量 state reader 通过残差更新把这些上下文融入草稿表示。通过低秩状态读取和融合算子控制额外计算与 I/O 开销。整体建立在 DSpark 的并行骨干和顺序预测头之上，采用两阶段轻量适配：先训练 reader/query，再微调预测头。

**关键结果**：在数学、代码生成、对话等 7 个 benchmark 上，ReaDy 用 Qwen3.8-27B 在单张 NVIDIA B200 GPU 上平均取得 3.16x 自回归解码加速；每个 benchmark 都超过 DSpark，吞吐平均提升 7.97%，接受长度平均提升 8.50%。
