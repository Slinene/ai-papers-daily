---
title: 'RECAP: Feedback-Driven Streaming Semantic User Profiles for Short-Video Recommendation'
title_zh: RECAP：反馈驱动的流式语义用户画像优化
authors:
- Ziyi Zhao
- Xiaoyou Zhou
- Xiao Lv
- Yangyang Li
- Chubo He
- Zhao Liu
- Jiayao Shen
- Yuqi Liu
- He Li
- Chengyi Zhang
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
- China Academy of Cyber
arxiv_id: '2607.15730'
url: https://arxiv.org/abs/2607.15730
pdf_url: https://arxiv.org/pdf/2607.15730
published: '2026-07-17'
collected: '2026-07-20'
category: RecSys
direction: 流式用户画像 · 闭环 GRPO 优化
tags:
- User Profiling
- Streaming
- LLM
- GRPO
- Short-Video Rec
- Feedback Cleaning
one_liner: 闭环框架通过清洗隐式反馈训练双塔评估器，用GRPO优化流式结构化用户画像生成，提升推荐对齐度
practical_value: '- 将用户画像维护为有界结构化状态：LLM 只产出语义差异（确认已有兴趣、新兴趣），确定性状态机管理生命周期、容量和强度衰减。电商/广告场景中用户兴趣同样流式变化，这种解耦保证了画像状态可追踪、可解释，避免
  LLM 输出不稳定元数据，工程落地性强。

  - 从隐式反馈构建高质量奖励：通过 LLM pairwise judge 过滤行为对，只保留高置信语义一致的正负样本，再训练双塔评估器作为奖励模型。这比直接使用排序分或原始播放/跳过标签更干净，适合业务中缺乏显式语义偏好的场景，可用于优化文案生成或推送消息筛选。

  - GRPO 优化 LLM 画像更新器：用冻结的双塔评估器计算逐块画像更新的奖励，配合格式惩罚和多样性惩罚（如证据重叠惩罚），在 SFT 基础上进一步对齐下游任务。该范式可迁移至对话策略或搜索词推荐的在线优化，利用离线日志安全训练。

  - 流式分块并行训练：长行为历史分块，SFT 预计算前缀画像，每块独立优化，大幅降低序列计算开销，适合大规模用户行为流的工业训练。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
工业短视频推荐中，用户兴趣不断演化，语言画像需要以流式方式增量更新，且必须维持有界结构化状态。但现有画像生成器多采用开环总结，缺乏从隐式反馈直接优化更新策略的闭环机制，导致画像可能与下游推荐任务脱节。  

**方法关键点**  
- **结构化用户记忆**：画像由最多 L 个兴趣条目组成，每个条目包含 topic、desc 及生命周期字段（span、recency、strength）。LLM 仅输出语义差异（确认已有兴趣、新兴趣），确定性状态机执行 Update/Add/Remove 操作，管理容量与衰退。  
- **高置信反馈构建**：利用 LLM pairwise judge 从观看/跳过隐式标签中筛选语义一致的正负行为对，得到清洗后的反馈数据，降低曝光位置、用户惯性等混淆影响。  
- **双塔语义评估器**：基于清洗数据训练双塔模型，用户塔编码渲染画像文本，视频塔编码视频描述，联合 BCE 损失和对比损失优化，提供画像-视频语义匹配得分作为奖励信号。  
- **GRPO 策略优化**：以 SFT 初始化的 Qwen3-4B 为基座，冻结双塔评估器，用组内相对优势 GRPO 优化策略，并加入格式惩罚和证据重叠多样性惩罚，防止冗余输出。并行分块训练降低序列开销。  

**关键结果**  
在快手海外短视频数据集上，RECAP 相比 Base 模型离线 uAUC 提升 0.0084，Recall@2000 提升约 4.9%；清洗反馈比原始反馈带来更稳定、更抽象的兴趣更新；线上 7 天 A/B 实验用户日均使用时长显著提升 0.139%。
