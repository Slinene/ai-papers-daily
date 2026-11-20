---
title: 'TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management
  and Layer-Wise Streaming'
title_zh: TideCache：混合LLM的高效服务系统，透明缓存管理与逐层流式传输
authors:
- Jinbin Luo
- Xiaozhe Yao
- Shang Yang
- Zhijian Liu
- Song Han
- Qinghao Hu
affiliations:
- Massachusetts Institute of Technology
- ETH Zurich
- University of California, San Diego
arxiv_id: '2611.26619'
url: https://arxiv.org/abs/2611.26619
pdf_url: https://arxiv.org/pdf/2611.26619
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理服务 · 混合架构缓存优化
tags:
- LLM Serving
- Hybrid LLM
- KV Cache
- Layer-wise Streaming
- SGLang
- CPU-GPU Superchip
one_liner: 针对混合LLM全局KV与有界状态缓存失衡，用透明缓存池加层间流式预取显著提升Agent吞吐并降低延迟
practical_value: '- 多轮推荐/电商Agent常积累长上下文（用户画像、商品浏览历史、工具输出），若部署混合架构LLM，历史前缀不必全部常驻HBM：把历史KV放host，decode时按层流式预取，可明显提升单卡可服务的并发会话数，尤其适合Grace
  Hopper/Blackwell superchip。

  - 静态给global-KV和bounded-state划内存会导致一个池阻塞而另一个闲置；可借鉴Transparent Cache Pool的思路：保留虚拟地址和backend接口不变，只在物理页层面做重映射，避免入侵注意力算子，工程落地阻力更小。

  - 准入控制可引入“resident vs streamed”两路决策：当resident区域容量受压力时，对长历史且已在host缓存的会话走streamed路径；队列压力用运行中请求的decode增长、等待请求需求与到达率预估，避免global-KV成为木桶短板。

  - 如果业务使用SGLang，可试用其unified memory pool或参考本文TCP设计；若只做上层算法，可吸收“不同缓存组件需求随workload漂移，需要动态在线调整资源配比”的结论，避免硬编码缓存预算。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
混合架构LLM中，全局注意力层缓存随上下文长度增长，有界状态层（滑窗/SSM/DeltaNet）缓存规模固定；实际服务负载会漂移，静态分区容易让一个缓存池阻塞请求、另一个池大量闲置。CPU-GPU superchip虽提供高带宽host内存，但decode阶段H2D带宽基本空闲，形成未利用的机会。

## 方法关键点
- **Transparent Cache Pool**：用CUDA虚拟内存API固定虚拟地址、动态重映射2MiB物理页，在不同缓存子池间共享HBM；每次只移动空闲或冷缓存行，不迁移活跃数据，保持原有注意力后端和索引不变。
- **Cache Streamer**：将全局注意力层的虚拟范围别名映射到两个物理slot，利用有界状态层的计算窗口，在decode过程中预取下一层历史KV；生成的新KV仍常驻。Graph-Compatible Handshake用固定图节点+运行时flag实现选择性传输，避免图分段和多余拷贝。
- **Request Scheduler**：根据队列压力、运行请求的decode增长和到达率，选择resident或streamed执行；容量不足时触发TCP增长。

## 关键结果
在GB300/GH200上覆盖Kimi K3、Ring-2.6、GLM-5.3-Flash、Qwen3.8、GPT-OSS共7个模型/平台配置。对比SGLang with HiCache，TideCache最高完成2.04× agent turns，整体P50 per-token latency降低20–59%，Agent P50 TTFT改善1.40–3.05×。动态TCP在无手工调优下达到最佳固定分区的96.3–113.6% turns/s；等batch下decode步开销最多+6.3%，但有效global-KV容量从148K提升到260K tokens。

最值得记住的一点：把全局注意力KV从“整段常驻”改为“按层流式预取”，用有界状态层计算隐藏host-to-device传输，可以在不改模型和注意力后端的情况下扩大全局KV容量并提升并发。
