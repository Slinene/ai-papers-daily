---
title: 'RecoGEM: A Serving System for Production-Scale Generative Recommendation'
title_zh: RecoGEM：面向生产级生成式推荐的高吞吐低延迟服务系统
authors:
- Xiangrui Yang
- Yunfeng Zhao
- Jiawei Yang
- Fangyu Zhang
- Enrui Zhao
- Liang Zeng
- Cheng Peng
- Minhui Xie
- Jiaqiang Liu
- Xiao Liang
affiliations:
- The University of Hong Kong
- Kuaishou Technology
- Peking University
- Renmin University of China
arxiv_id: '2611.12296'
url: https://arxiv.org/abs/2611.12296
pdf_url: https://arxiv.org/pdf/2611.12296
published: '2026-11-09'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · 推理服务系统
tags:
- Generative Recommendation
- Serving System
- Self-Attention
- Beam Search
- Top-K
- LLM Inference
one_liner: 为生成式推荐构建的推理服务系统，通过运行时-引擎解耦与步骤级算子优化，单实例实现1000+ QPS、P99低于35ms
practical_value: '- 若在电商/广告落地生成式推荐或Semantic ID推理，不要把beam search当作LLM token采样；应把每个SID步的prefix长度、beam
  width、候选宽度编译成固定profile，离线生成step-specialized engine，可显著降低前几步延迟。

  - 候选选择在beam大、vocab大的场景是瓶颈：采用两阶段Top-K，先按beam行做local top-K，保持beam matrix边界，再跨行合并全局top-K；配合flash
  radix路径对大K友好，比ATen快1.4–2.24×，比bitonic在K=1024时快20×以上。

  - 短前缀、大batch的decode attention用row-tiled self-attention，把batch/head行打包进tile做fused
  QK/softmax/PV，避免长序列kernel的padding与running softmax开销；在B=16384、H=64、D=64时比SDPA最高快154×。

  - 模型权重/SID vocab/selection policy需要热更新时，采用contract gate + pointer switch：新engine在旁路准备并校验，短暂停止接新请求，旧请求走完后原子切换指针，能避免线上P99毛刺；同时把TensorRT
  engine生成放到离线发布链路，可降低部署时间约40%。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐（GR）从对候选item打分转向自回归生成Semantic ID，但它的serving形态与LLM推理有本质差异。每个请求只做几个依赖解码步，每步语义和tensor shape不同：per-step vocab、beam扩展导致候选数膨胀，候选选择在关键路径上，且生产环境要求模型权重、SID vocab、selection policy频繁热更新。直接复用LLM serving栈会出现结构错配与性能空转，因此需要GR原生服务系统。

**方法关键点**：
- **运行时-引擎解耦**：runtime负责SID步间状态转移、候选状态管理、live artifact更新；engine只做张量计算。通过自动生成deployment contract绑定模型图与服务策略，保持接口稳定。
- **候选状态管理**：cross-KV在请求内静态复用；self-KV按候选行生命周期维护，beam search后用double-buffered compaction把存活的KV slice聚合成稠密prefix。
- **Row-tiled self-attention**：将batch×head展开成大量独立短行，按64行一个tile做fused QK/softmax/PV，跨tile流水加载，避免长序列attention kernel的高额固定开销。
- **Step-granular planning**：编译期dry run推导每个SID步的prefix长度、beam width、候选宽度，生成step-bounded engine，而不是给所有步一个宽泛动态shape profile。
- **Fast candidate selection**：两阶段Top-K：先对每个beam行做local top-K，再跨行合并全局top-K；对超大K使用flash radix，避免bitonic在大K下性能崩塌。

**关键结果**：在生产环境部署9个月，服务400M DAU，支撑10多个GR模型家族。OneModel 0.2B模型batch=32时P99 30.8 ms、1053 QPS，较GeneralGen的89.0 ms/366 QPS有2.88×吞吐提升；OneRec-v2 4B模型P99 61.5 ms、526 QPS。峰值集群60k QPS，MFU 55.3%。row-tiled attention在短前缀B=16384时最高比SDPA快154×；候选选择比ATen快1.4–2.24×。热更新路径消除在线更新期的P99毛刺。

**最值得记住的一句话**：GR serving的性能瓶颈已经转向dense decode和候选选择，SID步边界必须作为优化边界显式保留，而不是继续塞进同质化的token loop。
