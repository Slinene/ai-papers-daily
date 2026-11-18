---
title: Multi-Branch Transformer
title_zh: 多分支 Transformer：并行分支结构与 Joint-KV 缓存
authors:
- Gaotang Li
- Lingjie Chen
- Chunyuan Deng
- Zhiwei Xu
- Hongzheng Chen
- Christopher De Sa
- Jingrui He
- Yingheng Wang
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- Rice University
- University of Michigan
- Cornell University
arxiv_id: '2611.19800'
url: https://arxiv.org/abs/2611.19800
pdf_url: https://arxiv.org/pdf/2611.19800
published: '2026-11-14'
collected: '2026-11-18'
category: LLM
direction: LLM 架构 · 多分支并行与 KV cache
tags:
- Multi-Branch Transformer
- MoE
- KV cache
- LLM scaling
- Inference Efficiency
one_liner: 并行组合完整 Transformer block 并在分支间共享 KV cache，同等训练预算下优于标准顺序模型，推理吞吐提升 51.4%
practical_value: '- 推荐/搜索的 LLM backbone 想提升质量又受推理延迟约束时，可尝试「共享前缀层 → 并行 Transformer
  分支 → 融合 → 共享后缀层」的 MBT 结构；在匹配总参数和训练 FLOPs 下，验证损失低于顺序 Transformer，尤其适合 MoE 骨干。

  - 长用户行为序列、长文档或多路候选打分场景，迁移 Joint-KV 思路：在每层对分支的 KV 做共享融合而不是保留各分支完整 cache，实测全模型 KV
  cache 最多降 34%，H200 单卡解码吞吐最高提升 51.4%。

  - 结构搜索时优先在中间层做分支，消融显示 middle layers 收益最大；融合函数比较鲁棒，业务上可先上 concat/简单加权，降低工程复杂度。

  - 资源受限下，2 分支 Balanced MBT 是实用起点：同等训练 compute 下相当于标准 Transformer 最高 1.26 倍 training
  body compute 的效果，可直接换成主干模型。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

Transformer 语言模型通常靠加宽 block 或加深层数来扩展。该工作探索第三条路径：分支，即在模型中间并行组合多个完整 Transformer block。目标是在参数和训练计算匹配的前提下，同时改善建模质量与推理效率。

**方法关键点**

Multi-Branch Transformer 先经过共享初始层，再进入多个独立参数化的分支，每个分支由若干 sequential block 组成，分支并行执行后融合输出，最后经过共享末层。作者对比三种分支配置：Wide-Shallow 保持 block 宽度、Narrow-Deep 保持顺序深度、Balanced 在两者间插值。实验中在 0.8B–2.1B 总参数的 MoE 规模做受控预训练。针对长上下文推理，提出 Joint-KV：在每层从分支表示构造共享 KV cache，减少完整模型 KV cache 存储，并配合利用分支分组和共享缓存的推理引擎。消融覆盖分支收益、融合函数、分支位置等。

**关键结果**

在匹配参数和训练 compute 预算下，2 分支 Wide-Shallow MBT 持续优于顺序 Transformer；Balanced MBT 进一步提升，且分支数从 2 增到 3/4 时质量基本不降。最终 Balanced + Joint-KV 方案下，标准 Transformer 需要最多 1.26× 的训练体 compute 才能达到相同验证损失；KV cache 存储最多减少 34%，单 H200 GPU 解码吞吐最高提升 51.4%。消融表明分支收益不能仅用宽度和深度变化解释，Joint-KV 有效，分支在中间层效果最佳。
