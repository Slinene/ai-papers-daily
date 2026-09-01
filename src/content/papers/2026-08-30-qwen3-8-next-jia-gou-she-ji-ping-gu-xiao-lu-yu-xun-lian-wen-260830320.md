---
title: 'On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training
  Stability'
title_zh: Qwen3.8-Next 架构设计：评估、效率与训练稳定性
authors:
- Zihan Qiu
- Zekun Wang
- Xiao Li
- Yanpeng Li
- Yang Xu
- Yixuan Wang
- Huaqing Zhang
- Rui Men
- Bochao Mao
- Chengruidong Zhang
affiliations:
- Qwen Team
arxiv_id: '2608.30320'
url: https://arxiv.org/abs/2608.30320
pdf_url: https://arxiv.org/pdf/2608.30320
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: 大规模稀疏 MoE 架构与训练优化
tags:
- MoE
- Gated DeltaNet
- Sparse Attention
- N-gram Embedding
- Training Stability
- Muon
one_liner: 稀疏 MoE 联合优化效果、效率与训练稳定性，在约 1/9 训练 FLOPs 下追平前代旗舰
practical_value: '- 长序列用户行为建模/Agent 长期记忆：QSA 的压缩 lightweight indexer 在 micro-block
  粒度打分，压缩比 r=4，索引成本从 O(n^2) 降到 O(n^2/r)，1M context 下 prefill 7.6×、decode 4.9× 加速，且短序列指标不退化。对电商历史行为序列、会话日志、Agent
  记忆库读取等长上下文场景有直接借鉴价值。

  - 外部容量扩展：n-gram embedding 表托管在 host memory 并异步预取，51B 参数几乎不增加 per-token FLOPs。推荐系统可借鉴其思路，将大规模
  ID/属性交叉特征、低频但重要的记忆型特征放在 off-accelerator 表中，避免主模型算力膨胀；但要注意论文反复出现的结论——loss 单调下降不意味着下游指标同步提升，必须用业务指标单独验证。

  - 训练稳定性与优化器：Muon 只用于 2D 线性映射权重，embedding/head/router/GR 低秩投影保留 AdamW；用 4× 最优学习率压力测试验证稳定性，提前暴露
  spike 风险。大模型或大 embedding 模型训练时可复用该策略，减少对 qk-clip、SwiGLU-clip 等显式裁剪的依赖。

  - 残差门控设计：GR 四分支 + elementwise 门控读取替代 pre-norm，去掉分支间 mixing 后既提升表达能力又减少显存流量。该思想可迁移到序列建模的残差路径；但论文也警示仅看
  pre-training 指标会误判，sparse read 在后训练阶段退化就是反面案例。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：前代 397B-A17B 旗舰训练与推理成本极高，目标是在约 1/9 训练 FLOPs、1/3 激活参数、1/3 训练 token 下追平质量。架构改动同时影响下游能力、计算成本与训练稳定性，因此需要将三者作为一个联合设计问题。

**方法关键点**：
- **Token mixing**：层间混合 Gated DeltaNet(GDN) 与全局注意力，每 4 层保留 1 个 full-attention；继续预训练阶段将 full-attention 替换为 Qwen Sparse Attention(QSA)。QSA 用压缩 lightweight indexer 在 micro-block 粒度打分，压缩比 r=4，token budget K=2048，索引复杂度从 O(n²) 降到 O(n²/r)。
- **残差路径**：Gated Residual(GR) 将残差流加宽为 4 分支，用 elementwise sigmoid 门控读取，写入为 per-branch scalar gate，替代 pre-norm 并去掉分支间 mixing 算子 Hres，减少显存流量。
- **容量扩展**：单层 n-gram embedding 放在 Layer 2，表托管在 host memory 异步预取，51B 参数几乎不增加 per-token FLOPs。
- **优化器**：Muon 用于 2D 线性映射权重，NS 迭代 8 步；embedding、head、MoE router、GR 低秩投影保留 AdamW；重拟合 scaling law 得到更大学习率与 batch size，无需 batch warmup。

**关键实验**：在 14 个预训练基准上，125B 总参数 6B 激活的 Qwen3.8-Flash-Next 领先前代 397B-A17B 八项，其余差≤2.6 分，训练 FLOPs 约 1/9。QSA 在 1M context 下 prefill 7.6×、decode 4.9× 加速；RULER 512K+ 从 90.08 提升到 93.00，MRCR 512K 从 30.66 提升到 40.53。GR 相比 pre-norm 残差在 9 个基准平均提升约 3.75 分。n-gram vocab 增大时 loss 单调下降但下游指标饱和甚至波动，说明 loss 与下游并不总是一致。

**最值得记住的一句话**：Loss、benchmarks、效率与稳定性是一个整体设计问题，必须联合求解，任何只看单一指标的选择都可能在大规模训练或后训练阶段翻车。
