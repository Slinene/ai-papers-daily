---
title: 'Motif 3: Technical Report'
title_zh: Motif 3：分组差分潜注意力与细粒度 MoE 的高效 LLM
authors:
- Junghwan Lim
- Joon Son Chung
- Sungmin Lee
- Wai Ting Cheung
- Gihun Cho
- Minsu Ha
- Sangho Kang
- Beomgyu Kim
- Dongseok Kim
- Jangwoong Kim
affiliations:
- Motif Technologies
arxiv_id: '2608.09119'
url: https://arxiv.org/abs/2608.09119
pdf_url: https://arxiv.org/pdf/2608.09119
published: '2026-08-09'
collected: '2026-08-11'
category: LLM
direction: 大模型架构优化 · 稀疏 MoE
tags:
- MoE
- Grouped Differential Attention
- KV Cache Compression
- Long-Context Training
- Multi-teacher Distillation
- Low-precision Training
one_liner: 提出 GDLA 注意力及 384 选 8 稀疏 MoE，结合在线蒸馏实现高效 LLM 推理与多能力整合
practical_value: '- **KV 缓存压缩用于 Agent 长记忆**：GDLA 结合差分注意力与 MLA，将 KV 缓存降低至 16 个潜表示头，显著减少多轮
  Agent 交互的显存占用，可直接启发推荐系统中的大模型会话 bot 或长期用户建模。

  - **细粒度专家路由与负载均衡**：384 选 8 的稀疏 MoE 配合 sigmoid 路由、辅助损失退火等策略，确保专家充分利用且避免崩溃，可迁移到大规模推荐模型的混合专家路由设计。

  - **多教师在线蒸馏聚合能力**：用 6 个 RL 专精教师与 1 个 SFT 软件工程教师进行 MOPD 蒸馏，得到兼具推理、编码、工具使用能力的统一模型，方法可直接用于电商
  Agent 能力集成，将细分任务专家合并至单一服务模型。

  - **MXFP8 低精度训练与通信优化**：专家激活预量化、梯度同步 BF16、免 All-Gather 权重保留等技巧，降低显存和通信成本，对推荐系统中需要大规模
  GPU 集群稀疏训练的团队有实用价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：随着 LLM 向更大容量发展，MoE 架构能够在不增加计算成本的前提下扩展参数量，但面临训练不稳定、专家利用率不均以及推理 KV 缓存开销大等挑战。Motif 3 旨在设计一种兼顾表达力与效率的架构，并通过训练系统和后训练策略实现全面的能力增强。

**方法关键点**：
- **GDLA**：融合分组差分注意力(GDA)与多查询潜注意力(MLA)，采用 64 信号头与 16 噪声头的非对称设计，学习 token 级门控系数，共享 16 个压缩 KV 头，大幅降低缓存同时保留噪声抑制能力。
- **细粒度 MoE**：每层 384 个路由专家、Top-8 激活，配套 Expert-Specific PolyNorm 激活，让每个专家学习独立的多项式响应，提升专长分化。
- **训练稳定化**：sigmoid 路由、辅助损失自适应退火、路由器注入衰减噪声、mHC 后映射乘子从 2 退火至 1，防止残差流激活异常。
- **系统优化**：MXFP8 分组 GEMM、专家预量化、梯度同步 BF16、免权重 re-gather、Muon 优化器 + QK-Clip，支持 256K 长上下文训练，通过窗口感知上下文并行处理全注意与滑动窗口层。
- **后训练**：通用 SFT 后，训练 6 个 GRPO 专精教师 + 1 个 SFT 软件工程教师，用 Multi-teacher On-Policy Distillation (MOPD) 将能力蒸馏至统一学生模型。

**结果**：在 12.5T tokens 预训练后，Motif 3 在智能体、数学推理、科学知识、多轮指令遵循等基准上与领先开源模型相当；控制实验显示 GDLA 比 MLA 少用 9.2% tokens 达到同损失，PolyNorm 维持更高门控权重有效秩。
