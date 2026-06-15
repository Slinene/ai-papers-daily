---
title: 'CoRe: A Continuously Reward-Finetuned LLM Query Rewriter for Multi-Stage Context-Aware
  Relevance in Web-Scale Video Search'
title_zh: CoRe：面向短视频搜索的持续奖励微调 LLM 查询重写器
authors:
- Yilin Wen
- Rong Yang
- Xiaojia Chang
- Hong Sun
- Gefu Tang
- Chunhui Liu
- Jeffrey Chen
- Zeyu Ma
- Lisong Qiu
- Xiaochuan Fan
affiliations:
- ByteDance / TikTok
arxiv_id: '2606.14127'
url: https://arxiv.org/abs/2606.14127
pdf_url: https://arxiv.org/pdf/2606.14127
published: '2026-06-12'
collected: '2026-06-15'
category: QueryRec
direction: LLM 查询重写 · 持续偏好优化
tags:
- query rewriting
- preference optimization
- semi-online RL
- LLM
- production deployment
- reward alignment
one_liner: 以线上多模态相关性模型为奖励源、乘性奖励对齐排序融合，结合半在线 MPO 与稳定性门控实现每周持续重写
practical_value: '- **奖励设计对齐线上融合公式**：乘法形式的奖励 \(r_{\text{base}} = (S_{\text{pos}}^{1+\gamma}
  / S_{\text{neg}}) \cdot (S_{\text{pos}} / S_{\text{rand}})^{\alpha_R}\) 直接镜像了线上排序的融合代数，避免训练-线上信号不一致。在电商搜索中，可将精排模型的分数组合方式直接写进
  reward，让查询重写或生成式召回的训练梯度与线上排序目标保持一致。

  - **半在线 MPO 降低大模型迭代成本**：每阶段只采样一次并仅对 top-k vs bottom-k 偏好对计算梯度，将参数同步和 reward 调用批量化到阶段边界。对于需要高频迭代但推理成本高的多智能体或
  LLM 组件，这种梯度节约和调度解耦可直接复用。

  - **双族指标自动晋升门控**：用奖励类指标 (rmain, Spos, rrand) 和稳定性指标 (熵、perplexity、长度、截断率) 联合判断候选模型。在
  Agent 或多步推理的强化学习任务中，补充稳定性指标可提前捕捉模式坍塌或奖励黑客，已证明比纯奖励门控更可靠。

  - **增量并行路径消费，控制爆炸半径**：重写信号作为 recall、rawrank、finerank 各阶段的附加特征，失败时自动降级到原始链路。为在推荐/搜索系统里引入
  LLM 组件提供了安全落地模式——先叠加再逐步替代，避免一次性切换风险。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
短视频搜索“浏览后搜索”场景中，用户刚看过的视频（d_last）提供了窄上下文，随后的点击与跳过行为提供了稠密后验反馈。这为训练上下文感知的查询重写器提供了丰富信号。困难在于：重写器没有金标准，只能从后验行为和线上排序器的消费方式构建奖励，同时训练成本必须足够低以支持每周级持续更新。

**方法关键点**
- **生产对齐的奖励构造**：使用部署的多模态相关性模型作为奖励源，乘法形式 \(r_{\text{base}} = \text{clip}\left[ \frac{S_{\text{pos}}^{1+\gamma}}{S_{\text{neg}}} \cdot \left(\frac{S_{\text{pos}}}{S_{\text{rand}}}\right)^{\alpha_R} \right]\) 直接匹配线上排序融合代数（重写信号在精排阶段是以乘性因子介入），并对正向文档按严格点击率加权，负向文档按无操作率加权，额外加入长度/截断惩罚以抑制冗长黑客。
- **半在线混合偏好优化（MPO）**：每阶段仅采样一次 N 条候选，按 top-k/bottom-k 构建偏好对，梯度仅流过少量对，减少训练步数；阶段边界进行参数同步与 reward 批处理，解耦 inference 与训练时序。损失采用 DPO + BCO + SFT 的混合，BCO 纠正纯 DPO 下的联合概率坍塌，SFT 保分布多样性。
- **自动化晋升门控**：每周基于保留周数据评估 7 项指标（3 个奖励类：rmain, Spos, rrand；4 个稳定性类：top-10 熵、平均惊异度、平均长度、长度截断率），只有全部改善才部署新模型。这一门控成功拦截了冗长奖励黑客事件，5 个月内 20 次周迭代中 16 次晋升。
- **加性并行部署**：重写结果通过近线推理缓存在 KV 存储中，以并行信号注入召回、粗排、精排三阶段，缺失时自动回退至原链路，确保重写器故障不会中断服务。

**关键实验**
在大型短视频搜索平台上进行 4 阶段离线训练后，为期 5 个月的每周在线更新。离线阶段重写改善率从 50.5% 升至 58.9%，在线 A/B 测试显示：仅精排阶段部署（Config A）已显著降低改查率并提升全部相关性/参与度指标；进一步扩展至召回与粗排（Config B）后指标再次正向提升。消融实验证实乘性奖励的正指数、多模态奖励源、MPO 混合损失以及并行路径均对效果有实质贡献。
