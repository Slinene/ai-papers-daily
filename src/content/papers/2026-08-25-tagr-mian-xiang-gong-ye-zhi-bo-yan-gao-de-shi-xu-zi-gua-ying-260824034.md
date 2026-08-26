---
title: 'TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming
  Advertising'
title_zh: TAGR：面向工业直播广告的时序自适应生成式推荐
authors:
- Wencai Ye
- Guangyi Liu
- Chaoyi Wang
- Wenbin Luo
- Shengyu Wang
- Mingjie Sun
- Peng Wang
- Quanming Yao
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
- Tsinghua University
arxiv_id: '2608.24034'
url: https://arxiv.org/abs/2608.24034
pdf_url: https://arxiv.org/pdf/2608.24034
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 生成式推荐 · 动态Semantic ID与策略优化
tags:
- Generative Recommendation
- Live-Streaming Advertising
- Semantic ID
- Temporal Adaptation
- Preference Optimization
- Industrial RecSys
one_liner: 动态LSID、多尺度意图建模与间歇性在线策略偏好优化，使直播广告生成式推荐收入提升16.1%
practical_value: '- 动态 token 化：对直播间、闪购活动等时效性实体，周期性刷新 Semantic ID（如每分钟）并保持稳定词表，使用 RQ-KMeans
  量化 + streamer-aware hash 降低碰撞；实时更新双向索引即可支持新广告检索，无需重建全库。

  - 意图建模：将高密度浅层行为（进入直播间）做多时间尺度下采样（stride 1/2/10），深层行为（加购、下单）分开通道编码；用 post-request
  反馈深度（如加购/下单强于曝光）加权 NTP 损失，可迁移到用户序列建模。

  - 偏好对齐：在线 RL 采用间歇性 on-policy GRPO，穿插监督 NTP 维护，避免连续 RL 梯度干扰；BA-GRPO 用生成 ID 与真实下一
  ID 的 token 嵌入余弦相似度做行为锚，VA-GRPO 用 RM 融合 engagement 和 eCPM，组合可平衡行为相关与商业价值。

  - 工程部署：动态 token 更新 + 双向索引，支持 >2500 QPS/GPU、<100ms 延迟，为生成式检索的实时化提供参考。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
直播广告是短视频/电商平台的重要变现形式，但其内容、商品和用户反馈快速变化，对推荐新鲜度要求极高。现有生成式推荐主要面向相对静态物品域，静态 Semantic ID 无法表示动态直播广告，单尺度行为建模难以捕捉意图变化，偏好优化难以平衡新鲜策略反馈与训练稳定性。

**方法关键点**
- **LSID（Live Semantic-Collaborative ID）**：以直播场景和推广商品为两个动态对象，通过场景/商品/用户编码器与三种对比对齐（U2S/U2P/S2P）学习 embedding，RQ-KMeans 分层量化，最后加 streamer-aware hash 降低碰撞；活跃广告每分钟刷新 token 分配但词汇表保持不变，只更新索引即可检索新广告。
- **IAG（Intent-Aware Generation）**：首要意图序列是进入直播间行为，在多个时间粒度（stride 1/2/10）构建多尺度 entry tokens；辅助行为（点赞、加购、下单）分开编码，保留行为类型语义；请求时表示 M_u(t) 随新行为刷新。MF-NTP 用 post-request 反馈深度作为意图证据（w_feedback）加权，用户价值层级 w_user 和归一化 eCPM w_eCPM 作为商业价值权重，level-wise gamma 调整。
- **IOPO（Intermittent On-Policy Preference Optimization）**：warmup 后采用间歇性 on-policy GRPO：每隔 T 步采样当前策略候选组，进行短时 GRPO 更新，中间穿插 NTP 维护防止灾难性遗忘。BA-GRPO 用生成 LSID 与真实下一 LSID 的 token 嵌入余弦相似度作为奖励，VA-GRPO 用 RM 预测 post-exposure 进入直播间和 eCPM 作为奖励，二者组合平衡行为相关性和商业价值。

**关键结果数字**
在十亿级真实电商直播广告数据（5天训练/2天验证/2天测试）上，相比生产 DLRM 判别式基线，完整 TAGR 在线 A/B：live-room entry rate +8.5%，shopping-cart click rate +7.4%，revenue +16.1%；分段显示低价值用户收入 +28.8%，冷启动直播流 +18.4%。离线上 HR@128 LRE 0.7723, SCC 0.6965，均优于 OneRec v2。消融验证各组件贡献，LSID 压缩比降至 1.01，IOPO 相比 continuous RL 稳定性更高（NTP loss 1.53 vs 1.68）。

**最值得记住的一句话**
生成式推荐应对非平稳场景，应在 token、用户意图、偏好对齐三层同时做时序适应：动态刷新但稳定词表的 LSID，多尺度多行为意图编码 + 反馈深度加权，以及间歇性 on-policy GRPO 夹带 NTP 维护，是实用有效的系统级设计。
