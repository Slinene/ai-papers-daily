---
title: 'MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression'
title_zh: MILO：基于块级低秩压缩的高效多示例上下文学习
authors:
- Youpeng Zhao
- Tian Tan
- Liqian Peng
- Jun Wang
- Alec Go
affiliations:
- Google
- University of Central Florida
arxiv_id: '2609.29913'
url: https://arxiv.org/abs/2609.29913
pdf_url: https://arxiv.org/pdf/2609.29913
published: '2026-09-24'
collected: '2026-09-25'
category: LLM
direction: LLM 推理 · KV cache 低秩压缩
tags:
- In-Context Learning
- KV Cache Compression
- Low-Rank Compression
- Many-shot ICL
- LLM Inference
one_liner: 利用块级低秩压缩和基于信息熵的动态秩分配，将多示例ICL的KV缓存降低50%、吞吐提升1.8倍
practical_value: '- 在电商推荐/Agent场景中，常需将用户历史行为、商品描述或工具调用日志构造成超长上下文做 many-shot ICL，KV
  cache 内存是线上服务瓶颈；可借鉴 MILO 的块级低秩压缩，对 KV cache 分块进行 SVD 低秩近似，减少显存占用并提升吞吐。

  - 动态秩分配策略：根据信息熵（或实际可用的 attention score 分布）评估每个块的重要性，对高信息密度块保留更多秩，对冗余块大幅压缩；这一思想可迁移到推荐系统的长序列用户建模或
  Agent 对话历史压缩，避免均匀压缩导致关键信息丢失。

  - 工程实现上，MILO 在 Qwen2.5 上达到 50% KV cache 内存降低和 1.8× 吞吐提升，且分类/推理基准性能几乎无损，说明低秩压缩可作为
  LLM 在线推理的默认优化手段，尤其适合广告/推荐场景中的大模型 serving。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
多示例上下文学习（many-shot ICL）通过注入上千条示例显著提升 LLM 在复杂任务上的表现，但 KV cache 随示例数量线性增长，成为在线服务和端侧部署的主要瓶颈。  

**方法关键点**  
MILO 利用 many-shot 上下文中的低秩冗余，提出块级低秩压缩：将 KV cache 按块划分，每块包含多个示例，对各块进行低秩近似。考虑到不同块的信息密度不同，MILO 基于信息熵动态分配秩预算，对关键块保留更高保真度，对冗余块进行更激进压缩。  

**关键结果数字**  
在 Qwen2.5 模型上，MILO 实现最多 50% 的 KV cache 内存降低和 1.8× 的推理吞吐提升，在分类和推理基准上性能几乎无下降，显著优于已有压缩基线。
