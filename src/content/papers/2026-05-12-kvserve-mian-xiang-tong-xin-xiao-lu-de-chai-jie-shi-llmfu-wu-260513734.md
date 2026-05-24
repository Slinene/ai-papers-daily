---
title: 'KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated
  LLM Serving'
title_zh: KVServe：面向通信效率的拆解式LLM服务中服务感知KV缓存压缩
authors:
- Zedong Liu
- Xinyang Ma
- Dejun Luo
- Hairui Zhao
- Bing Lu
- Wenjing Huang
- Yida Gu
- Xingchen Liu
- Zheng Wei
- Jinyang Liu
affiliations:
- University of Chinese Academy of Sciences
- Institute of Computing Technology, Chinese Academy of Sciences
- Shanghai Jiao Tong University
arxiv_id: '2605.13734'
url: https://arxiv.org/abs/2605.13734
pdf_url: https://arxiv.org/pdf/2605.13734
published: '2026-05-12'
collected: '2026-05-24'
category: LLM
direction: LLM推理优化 · KV缓存压缩 · 拆解式服务
tags:
- KV cache compression
- disaggregated serving
- adaptive compression
- Bayesian optimization
- bandit control
- vLLM
one_liner: 首个服务感知的自适应KV缓存压缩框架，通过贝叶斯搜索与在线控制实现动态策略选择，显著降低拆解式推理的通信延迟。
practical_value: '- 电商/推荐系统若采用PD分离或KV拆解的LLM推理，可借鉴KVServe的“离线Pareto候选生成+在线bandit选择”模式，用轻量控制器动态匹配请求的时延/吞吐/质量约束，避免静态配置导致SLO违规。

  - 自适应压缩思想可迁移到生成式推荐中的Embedding或特征传输压缩：根据网带宽、查询复杂度和延迟预算等上下文，动态切换量化/稀疏化/选择策略，而非固定一种压缩方法。

  - 贝叶斯Profiling Engine通过全局探索+局部细搜+3D Pareto剪枝的方式大幅降低搜索开销（50×），在推荐系统的超参或策略组合爆炸场景中，可用于快速生成高质量候选配置集。

  - 在线控制中的“分析模型+bandit”机制可迁移到Agent多智体通信优化：为Agent间的消息大小、压缩等级建立延迟预测模型，结合多臂老虎机上探索，在满足延迟目标下最大化通信效率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：拆解式LLM服务（如PD分离、KV存储分离）将KV缓存推到网络传输中，成为端到端延迟的主要瓶颈。现有KV压缩方案多为静态配置，无法适应线上负载、带宽和SLO的动态变化，固定策略常导致次优甚至更差的效果。

**方法**：KVServe首先将KV压缩统一为模块化策略空间，允许跨方法重组（如量化+稀疏+选择）。离线阶段，通过**贝叶斯Profiling Engine**高效探索策略空间，利用贝叶斯优化和3D帕累托剪枝生成候选集，搜索开销降低50倍。在线阶段，**服务感知控制器**结合解析延迟模型与轻量级Bandit（多臂老虎机）选择策略，根据当前负载、带宽和SLO约束动态调整，并反馈校正离线模型偏差。

**结果**：集成于vLLM，在多数据集、模型、GPU和网络条件下评估，PD分离服务中JCT加速最高达9.13倍，KV拆解服务中TTFT降低最高达32.8倍，显著优于静态压缩和固定策略。
