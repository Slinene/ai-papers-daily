---
title: 'OneBar: An End-to-End Content-Grounded Generative Query Recommendation Framework
  for E-Commerce Video Feeds'
title_zh: OneBar：电商视频流中内容驱动的端到端生成式查询推荐
authors:
- Yao Tang
- Ying Yang
- Ben Chen
- Yufei Ma
- Zihan Liang
- Chenyi Lei
- Wenwu Ou
- Jian Liu
affiliations:
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2606.15330'
url: https://arxiv.org/abs/2606.15330
pdf_url: https://arxiv.org/pdf/2606.15330
published: '2026-06-13'
collected: '2026-06-16'
category: QueryRec
direction: 生成式查询推荐 · 内容grounding与on-policy蒸馏
tags:
- Generative Query Recommendation
- Multimodal Grounding
- On-Policy Distillation
- PIOPD
- Short-Video
- Preference Internalization
one_liner: 端到端生成式框架，融合多模态意图grounding与偏好内化蒸馏，实时推荐搜索词，曝光+16.91%，GMV+21.67%
practical_value: '- 在延迟敏感的推荐场景，将多阶段级联压缩为单模型生成，并使用 [SEP] 分隔的紧凑 evidence 序列，离线缓存多模态与协同特征，可实现在
  20-30ms 内在线 serving。

  - 噪声内容 grounding：构造包含清理文本、多模态摘要、协同行为锚点和过滤后用户历史的 evidence schema，能有效对抗弱元数据下的意图漂移，对生成式推荐应对噪声输入有直接借鉴意义。

  - PIOPD 训练范式：用带后验点击 query 的教师模型对学生 on-policy 轨迹做 token 级双向 KL 蒸馏（FKL+RKL+熵正则），无需单独奖励模型，可避免
  reward hacking，并与 list-wise 偏好对齐组合使用，适合工业界偏好优化。

  - 内建安全拒绝：在 SFT 阶段加入 [REJECT] 训练样本，使模型学会对风险内容拒止生成，减少线上风控坏例，这种机制可推广到其他生成式推荐系统。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
短视频平台在播放画面下方展示可点击搜索词（底栏推荐），能引导用户从内容消费转向商品搜索，带来增量转化。传统方案采用检索 → 过滤 → 排序的级联架构，受限于 20-30 ms 延迟预算，主要依赖离线缓存，无法利用实时视频上下文，且多阶段优化目标割裂。现有生成式方法仍受限于内容侧噪声、候选空间受预定义 trie 约束，以及依赖独立奖励模型导致的偏好漂移与 reward hacking。

## 方法关键点
- **协同多模态意图 Grounding**：将每条视频抽象为结构化 evidence schema E = ⟨Tₓ, Mₓ, Aₓ, Hₓᵤ⟩，包括清洗后的文本、通过多模态大模型生成并每日更新的视频摘要、行为协同锚点（用 behavior‑aligned embedding 做 ANN 检索的相关 query 及 RAG 历史）和经视频相似度过滤的用户搜索历史。
- **低延迟统一生成器**：将所有 evidence 序列化为 [SEP] 分隔的紧凑 prompt，送入 BART encoder‑decoder，用一次生成取代多级级联，并支持输出 [REJECT] 表示拒绝对风险或弱证据内容推荐查询。
- **渐进式偏好内化训练**：
  1. 内容‑grounded SFT：从点击日志构造 trigger‑query 对，并对安全风险样本引入 [REJECT] 监督。
  2. List‑wise 反馈对齐：按 6 级行为（从当前用户点击后深入互动到仅召回未曝光）构造偏好排序，用 list‑wise Softmax DPO 将在线隐式反馈转为序列级偏好。
  3. 偏好内化 On‑Policy 蒸馏（PIOPD）：在学生自采样轨迹上，用带后验点击 query 的教师模型做 token 级双向 KL 蒸馏（FKL+RKL），辅以熵正则、R‑Drop 和 FGM 稳定训练；训练后丢弃教师和后验信号，部署模型仅需标准 context。

## 关键结果
- **离线评测**：在约 4000 万页面浏览的日志数据上，OneBar 全模型 Exact HR@8 达 0.3690，显著优于零样本 GPT‑5.5（0.0224）和 ANN 检索基线（0.1322）；消融证实各 evidence 字段及 PIOPD 组件的贡献。
- **在线 A/B 测试**：在快手主信息流，对比线上 MCA，Query Exposure +16.91%，Query Click +18.68%，CTR +0.19%，引导订单 +20.36%，引导 GMV +21.67%，人工评测整体查询质量 bad‑case 率绝对降低 9.00 pp。

最值得记住的一句话：**通过多模态证据融合与 on‑policy 偏好蒸馏，可在极低延迟下用单个生成模型取代工业级多阶段查询推荐系统，并直接带来搜索流量与 GMV 的显著增长。**
