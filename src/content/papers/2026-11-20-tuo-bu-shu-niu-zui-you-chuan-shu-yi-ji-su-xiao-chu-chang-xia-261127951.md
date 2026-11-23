---
title: 'Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash
  Speed'
title_zh: 拓扑枢纽最优传输：以极速消除长上下文稀释
authors:
- Dylan Forde
arxiv_id: '2611.27951'
url: https://arxiv.org/abs/2611.27951
pdf_url: https://arxiv.org/pdf/2611.27951
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 长上下文注意力 · 最优传输稀疏化
tags:
- Optimal Transport
- Long Context
- Sparse Attention
- Sinkhorn
- Triton Kernel
- Zero-shot Length Extrapolation
one_liner: 提出 THOT，用 hub-and-spoke 最优传输与容量门控替代 softmax 注意力，实现长上下文零样本高召回和高效 Triton
  内核
practical_value: '- **超长用户序列/商品描述的注意力稀释问题**：电商场景中用户行为历史或商品文本可能长达数十万 token，softmax
  注意力会将概率质量分散到无关 token，导致关键行为或属性被淹没。可借鉴 THOT 的容量门控（sparsemax 或 thresholded ReLU）强制将
  distractor 质量置零，提升对核心信息的 recall，适合应用于长序列用户建模或商品描述编码。

  - **推理效率与实时性**：论文的 Triton 内核在 L=4096 时比 cuDNN FlashAttention 快 3.3 倍，且在大长度下显存占用更小。对于需要在线实时推理的搜索/推荐系统，可考虑将类似
  hub-and-spoke OT 结构部署到 GPU 推理链路，降低长序列處理延迟。

  - **零样本长度外推**：短序列训练（L=128）直接泛化到 L=262K 并保持高召回，意味着线上遇到超长输入时不需要重新训练，工程上可减少序列截断带来的信息损失，尤其适合需要完整用户历史或长文档理解的场景。

  - **注意**：该工作是基础架构研究，需要将注意力模块替换为 THOT 并重新训练模型；迁移到推荐模型时需验证与现有 embedding/交互层的兼容性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长上下文模型面临双重瓶颈——二次计算成本和 softmax 归一化随长度分散概率质量，导致关键事实被大量 distractor 稀释，检索召回下降。

**方法**：提出 Topology Hub Optimal Transport (THOT)，用 hub-and-spoke 最优传输替代密集注意力矩阵，实现线性大小图。包含四个核心设计：(1) 有界支撑容量门控，通过 simplex sparsemax (O(L log L)) 或无排序 token-local thresholded ReLU (O(L)) 将多余 distractor 质量强制置零；(2) 三扫 1+2 退火行闭 Sinkhorn 调度，抑制二分残差；(3) 精确 rank-(D+2R+1) One-Reference-Tile adjoint 的 batched split-factor Triton 内核，使用 BF16 Tensor Cores 和 FP32 potentials；(4) chunked exclusive-prefix causal 变体，验证零未来泄漏。

**结果**：在 NVIDIA L4 上，sparsemax THOT 在 L=128 训练后，零样本在 L=262,144 下固定绑定召回达 97.40%（纯任务损失 α=0）和 98.83%（α=0.05），而 softmax-gated hub OT 仅 3.52%。内核微基准：H=8, D=64, L=262K 时 forward+VJP 共 100.1 ms，比 latent softmax 快 2.2 倍且编译器临时变量小 4 倍；L=4096 时比 cuDNN FlashAttention 快 3.3 倍。WikiText-103 多 needle 零样本检索 128/128 全中（100%），对比短训练 RoPE FlashAttention 仅 0.78%；4 层 WikiText-4K 模型有 modest causal 和 masked LM 提升。
