---
title: 'IntBMoE: Integrating Block-Level Conditioning into Expert Composition for
  Full-Participation Mixture-of-Experts'
title_zh: IntBMoE：块级条件专家组合的全参与 MoE
authors:
- Ran Cheng
- Longfei Xu
- Zheng Liu
- Kaikui Liu
- Xiangxiang Chu
affiliations:
- DreamX, Alibaba Group
arxiv_id: '2609.21346'
url: https://arxiv.org/abs/2609.21346
pdf_url: https://arxiv.org/pdf/2609.21346
published: '2026-09-17'
collected: '2026-09-22'
category: LLM
direction: MoE 架构 · 块级专家组合
tags:
- MoE
- expert composition
- block-level routing
- hypernetwork
- generative recommendation
- serving efficiency
one_liner: 用代码本+超网络预组合全量专家，解耦参与/执行/物化，AMap 线上 UVCTR +2.4%
practical_value: '- 面向 60ms 级延迟预算的生成式推荐/广告召回，可复用「输入无关代码本 + hypernetwork 预组合专家 + 缓存块参数」方案：训练时按
  batch 摊销组合成本，推理前一次性预计算 composed blocks，请求期只执行 Top-k 块，专家池大小 E 不再直接影响线上 FLOPs。

  - DPRG 是低成本增强专家交互的 trick：对同一组 expert bases 组合 value path 和 gate path，gate 用 RMSNorm+SiLU
  做乘法 residual 调制，不扩大专家数即可增加非线性；适合替换现有多专家融合中的简单加权或 convex combination。

  - block-conditioned feature filter 可将 token/用户表示与 block code 拼接，再生成 sigmoid 软掩码，给不同专家块提供不同输入视图；可借鉴到多兴趣召回、多场景建模中的软过滤门控。

  - 组合系数不做 softmax/sigmoid，保留负值并加 1/√E 缩放，是提升组合表达范围的实用做法；业务上做 expert fusion 时可尝试替代标准归一化系数。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：MoE 扩容量时，稀疏路由限制专家参与，dense output mixing 让执行成本随专家数增长，parameter merging 又让物化成本随 routing 单元增长。三者本应独立但现有方案互相耦合。

方法关键点：
- 用 K 个可学习块代码本定义块；共享 hypernetwork 从块编码生成 value/gate 组合系数，在每层融合 E 个 expert bases 成 K 个 L 层块。块与输入无关，可预计算缓存。
- token 级 router 对每个 token 选 Top-k 块；进入块前用 block-conditioned feature filter 生成 sigmoid 软掩码，输出按路由概率聚合。
- DPRG：对同一 expert pool 独立组合 value path 与 gate path，用 RMSNorm+SiLU 做乘法 residual 调制；保留恒激活 shared SwiGLU expert 建模公共通路。系数不做 softmax/sigmoid，加 1/√E 缩放。

关键结果：
- ImageNet-1K：Top-1 73.76%，超 SMEAR 1.98 个百分点；缓存块后 inference 3.457 GFLOPs，内存 104.33MB，E 从 1 到 128 请求期成本不变。
- MiniPile PPL 14.5878，比最强 µMoE(CP) 低 2.9%；IntTravel HR@1/5、NDCG@5 全面最优。
- 已部署 AMap 生成式推荐：平均 19ms、P99 38ms，一周 A/B UVCTR 相对 +2.4%。

最值得记住：MoE 的参与/执行/物化可解耦——输入无关代码本预组合全量专家，token 只路由到少量块，推理期缓存组合结果。
