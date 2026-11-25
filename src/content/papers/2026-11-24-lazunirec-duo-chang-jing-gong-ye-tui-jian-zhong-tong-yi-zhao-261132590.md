---
title: 'LazUnirec: Unifying Retrieval and Ranking in Multi-scenario Industrial Recommendation'
title_zh: LazUnirec：多场景工业推荐中统一召回与排序
authors:
- Xiaodong Li
- Junfeng Zhang
- Shichao Nie
- Ziyue Guo
- Yiming Liu
- Xinxin Xu
- Xurong Li
- Jinyuan Dang
- Zhanming Ou
- Jianan Yan
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2611.32590'
url: https://arxiv.org/abs/2611.32590
pdf_url: https://arxiv.org/pdf/2611.32590
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: 统一召回与排序的多场景推荐
tags:
- Unified Retrieval & Ranking
- Gradient Conflict
- LoRA
- Sparse MoE
- Uncertainty Estimation
- Multi-scenario Recommendation
one_liner: 用LoRA注意力与稀疏MoE缓解召回-排序梯度冲突，线上GMV最高提升4.01%
practical_value: '- 若要把召回和排序合入一个 Transformer，别让两个任务反向传播到完全共享的 QKV/FFN；建议在 QKV 上挂 LoRA
  类低秩残差，FFN 用“每任务私有 expert + 共享 experts top-2 激活”，既能保留任务特异性又降低梯度冲突。

  - 召回/排序统一输入可借鉴其序列组织：用户历史 + trigger token + 多兴趣 retrieval tokens + 同 request 的多个
  ranking tokens，配合注意力掩码隔离不同候选；部署时用 KV cache 跨阶段复用用户序列编码，离线观察到约 20% QPS 增益。

  - 用 ranking 给 retrieval 蒸馏很值得迁移：对同一请求候选 list 的 CTR logits 做 softmax 作为 teacher，retrieval
  侧用多兴趣 max score 做 student，KL 蒸馏（T_rank 0.5, T_retrieval 0.01），多目标/多兴趣模型都可用，能显著提升召回命中。

  - 多任务/多场景联合训练时，周期性统计共享参数的梯度方向方差，给方向稳定的任务/场景更高 loss weight（如 0.8~1.2 clip），无需复杂优化器，能引导可靠更新方向。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐通常将召回和排序拆成两阶段，目标不一致、用户序列重复编码、算力浪费。已有工作尝试用一个 Transformer 同时建模两个任务，但共享 backbone 上存在严重梯度冲突：统计显示 Attention 与 FFN 中普通梯度冲突率分别约 45.85% 和 47.54%，鲁棒冲突率约 39.75% 和 38.40%。多场景下不同场景的交互模式和监督信号差异加剧了冲突。

### 方法关键点
- **统一序列 tokenization**：用户历史序列 + trigger token + K 个可学习 retrieval tokens + 同一 request 内所有 ranking target tokens，按要求设计 attention mask，使 retrieval/ranking tokens 只关注历史、trigger 和自身，避免候选间干扰。
- **LoRA-modulated attention**：QKV 共享投影权重，同时为 retrieval 和 ranking 各增一个低秩私有 adapter ΔW=BA；用户序列和 trigger 只用共享参数。
- **task-adaptive sparse MoE**：FFN 由一个共享专家池 + 每任务一个私有专家组成，router 条件包含 token、用户画像、场景和任务，激活 top-2 共享专家，输出为私有专家输出 + 加权共享专家输出。
- **不确定性估计**：周期性探测共享参数梯度方向，用 EMA 方差估计历史方向稳定性，对稳定方向的任务/场景 loss 赋予更高权重，权重经 stop-gradient，不参与梯度计算。
- **知识蒸馏**：ranking 侧 CTR logits 经 temperature softmax 作为 teacher，retrieval 侧多兴趣最高匹配分作为 student，通过 listwise KL 将 ranking 候选偏好分布迁移给 retrieval。

### 关键实验
在多场景电商日志上训练 25 天、次日测试，对比 Transformer、UniPinRec、UniR2、UniSGR、OneTrans-V2。离线结果：ranking 全面领先，CTR AUC +0.23%~0.31%，GAUC +0.23%~0.69%；CVR AUC +0.28%~0.36%，GAUC +0.43%~0.55%；retrieval 提升更显著，HR@100 最高 +8.19%。梯度冲突分析中，FFN 鲁棒冲突相对降低 37.76%。在线 A/B（10% 流量一周）trigger-free 场景 GMV +4.01%，trigger-based 场景 GMV +3.06%，IPV/Orders/Buyers 同步提升。

### 最值得记住的一句话
共享 Transformer backbone 下，不要只靠 stop-gradient 或纯共享参数解决召回/排序冲突；用低秩私有 adapter + task-private expert + 历史梯度方向不确定性加权，能在保留知识共享的同时显著降低梯度冲突。
