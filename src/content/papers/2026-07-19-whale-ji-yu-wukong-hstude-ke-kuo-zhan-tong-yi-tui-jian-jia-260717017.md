---
title: 'WHALE: A Scalable Unified Model for Recommendation with Wukong-HSTU Architecture'
title_zh: WHALE：基于Wukong-HSTU的可扩展统一推荐架构
authors:
- Renqin Cai
- Dawei Sun
- Yuanjun Yao
- Zhiyong Wang
- Velvin Fu
- Maggie Zhuang
- Yu Shi
- Zhongnan Fang
- Xuan Cao
- Jing Qian
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2607.17017'
url: https://arxiv.org/abs/2607.17017
pdf_url: https://arxiv.org/pdf/2607.17017
published: '2026-07-19'
collected: '2026-07-21'
category: RecSys
direction: 可扩展推荐架构 · 特征交互与序列建模统一
tags:
- Wukong
- HSTU
- Attention Fusion
- Scalable RecSys
- Industrial Deployment
- Triton Kernel
one_liner: 通过逐层注意力融合将Wukong特征交互与HSTU序列建模统一，实现可扩展的工业推荐模型
practical_value: '- **逐层注意力融合设计**：在排序模型中，不推荐简单的“先压缩序列再拼入浅层交互”方式，而是像WHALE那样，在每一层用特征交互的输出作为query去关注行为序列，让高阶交叉能反复检索细粒度历史证据，可移植到电商/短视频的候选感知历史建模。

  - **注意力实现与效率优化**：共享KV减少显存带宽；根据query长度与序列长度的不对称性动态选择query-parallel或KV-parallel的反向计算路径，提升吞吐；用shared-gate
  SwiGLU替换标准SwiGLU，FFN计算量降低33%。这些trick可直接用于自研注意力模块的加速。

  - **消除CPU-GPU同步**：在线推理中通过shape hint tensor避免动态形状导致的同步开销，单点可节省1~5ms延迟，适合对延迟敏感的大型排序模型。

  - **统一架构的缩放收益**：增加序列长度、模型深度和宽度均带来一致的离线收益，且在线主指标+0.113%仅付出5%吞吐下降，说明该架构在工业场景中具有成本有效的扩展性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现代推荐系统分别沿两个独立路径扩展模型容量：Wukong 类架构放大静态/上下文特征的高阶交互，HSTU 类架构放大长序列行为建模。然而，浅层混合（先压缩序列再输入交互模型）限制了候选感知的细粒度历史检索，无法实现两者在深层持续交互。工业界急需一种可扩展的统一方案。

**方法关键点**：
- **整体架构**：堆叠的 WHALE 层，每层包含 Wukong 模块、HSTU 模块和注意力融合模块，非序列与序列分支始终活跃，逐层交叉交换。
- **输入层**：非序列特征经 embedding + 数值 tokenizer 得 \(\mathbf{X}_{ns}\)；行为序列经 embedding + MLP 得 \(\mathbf{X}_{s}\)。
- **Wukong 模块**：对 \(\mathbf{X}_{ns}\) 应用 FMB+LCB 产生高阶交互表示 \(\mathbf{H}_{w}\)。
- **HSTU 模块**：对 \(\mathbf{X}_{s}\) 应用时序注意力产生序列感知表示 \(\mathbf{H}_{s}\)。
- **融合模块**：以 \(\mathbf{H}_{w}\) 为 query，\(\mathbf{H}_{s}\) 为 key/value 做交叉注意力，再经融合 MLP 与共享门控 SwiGLU FFN，输出序列感知的交互表示。非序列分支更新为融合结果，序列分支保持 HSTU 输出传递。
- **效率优化**：定制 Triton 核（共享 KV、按 shape 选择反向并行模式），shared-gate SwiGLU 减少 33% 矩阵乘法，训练用 BF16+编译优化，推理用 AOTInductor 算子融合与 shape hint 消除 GPU‑CPU 同步。

**关键实验**：
- 数据：80B 训练 + 4B 评估样本的短视频平台日志。
- 基线：Wukong‑only 和 HSTU‑only，对齐 FLOPs。
- 离线结果：同复杂度下 WHALE 一致优于两种单范式基线（8 GFLOPS 时 NE 增益 0.40%~1.39%）；序列长度从 3k→15k 持续收益，模型从 2 层→8 层、宽度 64→512 均稳定提升。
- 消融：浅层混合融合、平均池化代替注意力、移除融合 MLP 或 SwiGLU 均导致明显 NE 退化。
- 在线 A/B：主指标 +0.113%，两个辅助指标 +0.824% / +1.820%，推理 QPS 仅下降 5%。

**核心结论**：让特征交互在每一层通过注意力去查询行为序列，是统一非序列与序列建模的有效设计原则，能在工业约束下带来可观的推荐质量提升。
