---
title: 'Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse
  Attention'
title_zh: 多层索引器：DeepSeek稀疏注意力中索引选择与注意力重叠
authors:
- Serdarcan Dilbaz
- Arjun Krishna
- Kiran Kamble
- Daniel M. Bikel
affiliations:
- Writer AI Research, Writer, Inc.
arxiv_id: '2611.03768'
url: https://arxiv.org/abs/2611.03768
pdf_url: https://arxiv.org/pdf/2611.03768
published: '2026-11-01'
collected: '2026-11-06'
category: LLM
direction: 长上下文稀疏注意力推理加速
tags:
- sparse attention
- KV cache
- long context
- inference optimization
- overlap
- IndexCache
one_liner: 复用相邻层索引选择，使 indexer 扫描与注意力并行，无需重训练加速长上下文推理
practical_value: '- 如果在线服务使用 DeepSeek-V3.2 或 GLM-5 做长上下文 Agent/RAG，可直接在 SGLang 上启用
  MLI+IndexCache 组合，128K 上下文下 decode 吞吐可达未优化模型的 1.32 倍，且无需重训练或改权重，部署风险低。

  - 对自研稀疏注意力或可学习索引器架构，可以借鉴“用上一层索引选择近似当前层”的做法，把索引扫描从关键路径移出，与 attention 计算 overlap，换取长上下文延迟的显著下降。

  - 默认实现不换 kernel、只改 decode graph 的编排方式，说明服务侧优化不一定需要侵入底层算子，可以更快在现网迭代。

  - 精度/吞吐折衷可参考 retention 1/4 的 MLI 在保持两倍新鲜索引选择下超过 IndexCache 1/8 的吞吐，提示通过复用频率与并行化的组合，能在成本敏感场景下获得更优边界。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：DeepSeek Sparse Attention (DSA) 在每层前用 lightning indexer 扫描整个 KV cache，选 top-k=2048 tokens 供该层注意。长上下文 decode 时，indexer 扫描成为瓶颈，且每层 attention 都必须等待本层 indexer 顺序完成。

方法关键点：相邻层选择的 token 高度重叠，因此可以让当前层直接使用上一层 indexer 的选择，消除串行依赖。Multi-layer Indexer (MLI) 使每个 indexer 与本层 attention 并行执行，无需重训练、无新权重。默认实现运行在 SGLang 生产 decode graph 中，不改 kernel；可选 fused decode kernel 在 DeepSeek-V3.2 上进一步加速。MLI 可与 IndexCache 组合：IndexCache 跳过部分层的 indexer，MLI 隐藏剩余层的扫描。

关键结果：在 DeepSeek-V3.2 和 GLM-5 上，retention 1/2～1/32、上下文 10K～195K 范围内，等 retention 下 MLI+IndexCache 比 IndexCache 更快：1/2 时 DeepSeek-V3.2 最高快 14.5%、GLM-5 快 9.8%；1/4 时分别快 7.9% 和 5.1%。在 128K 上下文、retention 1/4 时达到未修改模型 1.32 倍 decode 吞吐，高于 IndexCache 1/8 时的 1.28 倍。LongBench、RULER、LongBench v2 准确率与 IndexCache 相差几个百分点以内。
