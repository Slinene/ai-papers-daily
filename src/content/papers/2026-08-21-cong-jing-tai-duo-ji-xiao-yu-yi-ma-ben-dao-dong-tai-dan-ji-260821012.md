---
title: From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level
  Large Semantic Codebook for Generative Recommendation
title_zh: 从静态多级小语义码本到动态单级大语义码本：生成式推荐
authors:
- Tianlu Xie
- Xin Ku
- Mingjie Sun
- Yunhao Sha
- Lixiang Wang
- Peng Wang
- Yiyu Wang
- Wenjin Wu
- Zhaojie Liu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2608.21012'
url: https://arxiv.org/abs/2608.21012
pdf_url: https://arxiv.org/pdf/2608.21012
published: '2026-08-21'
collected: '2026-08-24'
category: GenRec
direction: 生成式推荐 · Semantic ID码本优化
tags:
- Semantic ID
- Generative Recommendation
- Codebook Update
- Exposure-aware
- RQ-VAE
one_liner: 单层大语义码本替代多层残差量化结合曝光感知动态更新，缩短SID并提升生成式推荐效果与吞吐
practical_value: '- 若业务在用生成式推荐/Semantic ID，优先评估单层大 codebook + hash disambiguation
  结构：把 [256,256,256] 换成 [1024,512] 可减少一个自回归位置，paper 中 FLOPs 降约 48%，QPS 提升 28%–47%；务必保留稳定的
  hash-based disambiguation token 解决物品碰撞，且不参与语义重建。

  - 面对 item 新老更替与曝光漂移，不要只定期全量重训 codebook：维护 exposure 时间衰减权重 w(t)=γw(t-1)+(1-γ)a(t)，a=1+log10(pv)；用上一版
  partition 做 anchor，EMA 更新中心，并在重分配目标里加 λ·w·I(切换) 惩罚高曝光 item 的 SID 变化，可明显减少训练目标跳变。

  - 先做 codebook 离线筛，再跑下游模型：指标用 reconstruction cosine similarity、code utilization、cluster
  load P95/max/CV、full-SID collision、temporal change rate（item/PV weighted），能把每个候选
  codebook 的下游训练成本省下来。

  - 若要上线生成式推荐，需按 serving 架构（decoder / LazyAR / MTP）分别评估自回归解码成本；缩短 SID 是直接且稳定的吞吐优化路径，即使效果打平，也可作为工程优化单独上线。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机：生成式推荐通常用多级残差量化构造 Semantic ID，工业部署的典型三层结构包含两个语义层和一个协同消歧层。本文分析 1.5B 工业样本发现，第二语义层虽然全局利用率 93.31%，但在每个活跃第一层码下平均仅使用 2.48% 的码本，形成条件稀疏的大层级空间，额外增加一个自回归解码步，且静态码本随新 item 和曝光漂移而失效。

方法关键点：
- 用单层大语义码本替代两层残差语义量化，SID 从三层缩短到两层；语义容量集中在单个 token，保留独立的稳定 hash-based disambiguation token 降低碰撞。
- 初始码本采用 exposure-weighted k-means（权重 a=1+log10(pv+1)）和加权 k-means++。
- 在线动态更新：维护时间衰减曝光权重 w=γw_prev+(1-γ)a；以旧码本 assignment 为 anchor，EMA 更新中心；最终 assignment 加入曝光加权切换惩罚 λ w I(k≠s_ref)，抑制高曝光 item 的 SID 突变。
- 构建 codebook 级离线评估：重构 cosine 相似度、码本利用率、cluster load、full-SID collision、temporal stability。

结果：Amazon Beauty 与 KuaiRec 上，两层 SID 相对三层 SID 使 OneRec-V1 Recall@10 提升 5.0%–8.8%、NDCG@10 提升 4.1%–5.1%；OneRec-V2 分别提升 7.1%–8.7% 和 3.8%–8.5%。固定日期 KuaiRec 下动态更新额外提升 OneRec-V1/V2 Recall@10 1.4%/2.7%，NDCG@10 7.0%/2.7%。推理侧，SID 缩短使自回归解码 FLOPs 降低 47.93%–48.70%，单卡 QPS 提升 28.57%–47.0%。5 天在线 A/B 2.5% 流量，主消费指标 +0.792%。

最值得记住：单层大语义码本+稳定消歧 token 的结构，配合曝光感知动态更新，是当前生成式推荐中兼顾效果与推理成本的实用选择。
