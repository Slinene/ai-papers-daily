---
title: Dynamic Short Convolutions Improve Transformers
title_zh: 动态短卷积：用输入依赖的局部混合增强 Transformer
authors:
- Oliver Sieberling
- Bharat Runwal
- Rameswar Panda
- Yoon Kim
affiliations:
- Massachusetts Institute of Technology
- MIT-IBM Watson AI Lab
arxiv_id: '2606.03825'
url: https://arxiv.org/abs/2606.03825
pdf_url: https://arxiv.org/pdf/2606.03825
published: '2026-06-02'
collected: '2026-06-03'
category: LLM
direction: 动态短卷积增强 Transformer 架构
tags:
- dynamic convolution
- transformer
- language modeling
- architecture
- scaling laws
- triton kernel
one_liner: 提出输入依赖的短卷积替代静态卷积，在 QKV 或全部线性层上带来 1.33–1.60× 计算优势，并保持低训练开销。
practical_value: '- 在推荐、Agent 序列建模中，可将动态短卷积作为一种局部上下文交互层，放置在 QKV 或所有线性层后，增强模型对内容依赖的局部组合能力。

  - 参数效率方面，使用低秩分解（rank R）或 head‑wise 共享动态卷积分量，在参数量仅小幅增加的前提下获得明显性能提升，适合资源敏感的业务场景。

  - 工程实现上，可借鉴 Triton 内核融合（将动态权重生成与卷积操作熔合，避免中间张量写回 HBM）以减少内存带宽压力，使训练吞吐仅下降约 8%，适合实际部署。

  - 动态卷积可与现有序列混合器（如 Attention、Mamba、DeltaNet）组合使用，替换其中的静态卷积，无需改动整体架构设计即能获得额外收益。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：静态短卷积对每个位置使用相同的局部聚合方式，难以处理随内容变化的局部组合函数（例如“the old can opener”与“the old can swim”的解析差异）。动态卷积通过让每个 token 根据自身表征生成专属的局部卷积核，既保留了局部归纳偏置，又增强了表达能力，有望成为 Transformer 架构中可扩展的新基元。

**方法**：
- 动态短卷积核心公式：\( y_t = \sum_{k=0}^{W-1} w^{(t)}_k \odot x_{t-k} \)，其中 \( w^{(t)} \) 由当前隐藏状态经线性投影（低秩或 head‑wise）生成。
- 为控制参数量，采用两种参数化：低秩分解（投影到 rank R，再恢复到 W·D）和 head‑wise 共享（将维度分头，每个 head 共享一组权重）。
- 放置位置：主要应用于 Q、K、V 向量（在 RoPE 前），并以残差形式叠加；也可扩展至所有线性层。
- 高效实现：自定义 Triton 核，将动态权重生成与卷积操作在芯片上熔合，避免中间张量搬运，输入/输出仅各读写一次 HBM；head‑size≥16 时延迟低于 CUDA 优化的静态卷积。

**关键实验**：
- 合成任务：在 variable‑key MQAR（键长度可变）和 MAD 基准上，动态卷积显著优于静态卷积与无卷积 Transformer，尤其在 Fuzzy Recall 上提升明显（0.298 → 0.726）。
- 语言建模：在 150M–2B 密集模型上训练，缩放定律拟合表明动态卷积在 QKV 上提供 1.33× 计算优势，在所有线性层上达到 1.60×；2B 参数上，QKV 变体验证 PPL 从 11.71 降至 11.24，全线性变体进一步降至 10.95。
- 效率：Head‑wise 动态卷积（H=16）的 Triton 核比 torch.compile 实现快 1.8–3.9×；端到端训练吞吐，QKV 变体仅比普通 Transformer 慢约 8%，全线性变体慢约 22%。
- 泛化：在 7B MoE、Gated DeltaNet 和 Mamba‑2 上替换/添加动态卷积均带来一致提升。

**核心结论**：动态短卷积是一种可扩展、硬件高效的局部内容依赖层，能以极小开销显著提升 Transformer 系列架构的性能。
