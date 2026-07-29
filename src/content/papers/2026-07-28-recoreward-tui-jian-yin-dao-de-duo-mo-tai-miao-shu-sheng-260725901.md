---
title: 'RecoReward: Recommender-Guided Multimodal Description Generation for Recommendation'
title_zh: RecoReward：推荐引导的多模态描述生成
authors:
- Guohong Mu
- Yueyang Liu
- Jiangxia Cao
- Changxin Lao
- Zijie Zhuang
- Yuhui Zhang
- Jiaqi Feng
- Ruochen Yang
- Shuang Yang
- Zhaojie Liu
affiliations:
- 南开大学
- 快手科技
- 中国科学院信息工程研究所
- 中国科学院大学
arxiv_id: '2607.25901'
url: https://arxiv.org/abs/2607.25901
pdf_url: https://arxiv.org/pdf/2607.25901
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 训练-推理解耦
tags:
- MLLM
- RLHF
- GRPO
- Two-Tower
- Live-Stream
- Semantic Description
one_liner: 利用行为反馈训练内容生成，实现推荐感知的共享描述，推理时无用户成本
practical_value: '- 可复用思路：在电商或内容推荐中，用已部署的双塔模型输出作为奖励信号，微调MLLM来生成对下游召回更友好的 item 描述，训练时接入用户行为信号，推理时完全剥离，保持线上低延迟。

  - RAS 的减法设计值得借鉴：用非目标用户的平均亲和度作为背景项，从目标用户打分中减去，能提升描述的区分度，让生成的语义向量更有选择性，而非放大普适偏好。

  - 工程实现细节：RL 阶段使用 GRPO+DAPO 组合，格式奖励保证输出可解析，语义奖励驱动排序，这种混合奖励可以避险 reward hacking；在线上的直播推荐
  A/B 测试中，有效用户渗透率与分发宽度均有正向提升，说明方案具备线上可行性。

  - 对于冷启动或内容重复使用的场景，该方法提供了一种训练一次、反复使用的范式，避免了为每个用户重复生成描述的推理开销，可直接桥接至双塔召回架构。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多模态大模型（MLLM）可把直播画面、语音转写成结构化的文本描述，用作推荐系统的语义特征。但仅基于内容生成的描述不区分哪些语义对推荐更有用，而引入用户历史的生成方式又带来高昂的推理成本与个性化缓存难题。该工作希望只利用训练时的用户行为信号，教会 MLLM 在推理时仅看内容就生成一份对下游召回更有效的共享描述。

### 方法关键点
- **行为分析驱动奖励设计**：在冻结的双塔匹配空间中，历史目标用户的表征含有未来目标用户信息，但也混入了全局活跃用户的共性成分；减去非目标用户中心能提升用户区分度，受此启发设计对比奖励。
- **Recommender Affinity Score (RAS)**：对每条生成描述，计算其与历史目标用户平均表征的内积，减去与非目标用户平均内积的 λ 倍，得到选择性兼容度。
- **训练-推理解耦**：训练时，冻结的双塔推荐模型提供 RAS 奖励，MLLM 仅接收多模态内容（视频帧+语音文本）生成描述；推理时无需用户信息，直接输出 item 侧特征，供双塔召回使用。
- **强化学习优化**：采用 GRPO 框架，结合格式奖励（JSON 有效性）和语义奖励（RAS），对同一输入采样多条输出，组内归一化进行策略更新。

### 关键结果
- 离线评测：在快手的直播推荐数据集上，RecoReward-9B 在 HR@10/64/128、NDCG@10/64/128、MRR 七项指标全面优于 Qwen3.5-9B 基线，相对提升 31.7%~40.4%，且超过 GPT-5、Gemini-3.1-Pro 等商业模型。
- 消融实验：非目标减法系数 λ=2 最优；rollout 数量 G=12 平衡探索与过优化；奖励用户上限 M=25 时信号最尖锐。
- 线上 A/B 测试：关键页面有效用户渗透率提升 0.265%，扩散页曝光用户数提升 0.740%，证实实际业务增益。

> **最值得记的一句话**：通过行为双塔的差分奖励（目标−λ×非目标），可以在训练中让 MLLM 学会生成更有推荐区分度的内容描述，而推理时完全不需要用户信息，做到了用户信号仅通过奖励注入、生成保持纯内容驱动。
