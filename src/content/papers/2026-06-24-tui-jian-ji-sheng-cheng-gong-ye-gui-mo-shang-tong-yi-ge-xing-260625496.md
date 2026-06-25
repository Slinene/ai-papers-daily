---
title: 'Recommendation as Generation: Unifying Personalized Video Generation and Recommendation
  at Industrial Scale'
title_zh: 推荐即生成：工业规模上统一个性化视频生成与推荐
authors:
- Yanhua Cheng
- Bo Wang
- Haotian Zhang
- Xinyuan Gao
- Zhihui Yin
- Ben Xue
- Yongzhi Li
- Jieting Xue
- Ye Ma
- Minquan Wang
affiliations:
- Kuaishou Technology
- Beihang University
arxiv_id: '2606.25496'
url: https://arxiv.org/abs/2606.25496
pdf_url: https://arxiv.org/pdf/2606.25496
published: '2026-06-24'
collected: '2026-06-25'
category: GenRec
direction: 生成式推荐 · Semantic ID · 多智能体视频生成
tags:
- GenRec
- Semantic ID
- Video Generation Agents
- Reward Learning
- Industrial Scale
- Multi-Agent
one_liner: 提出 RaG 范式，以解耦语义 ID 连接生成式推荐与多智能体视频生成，在快手广告场景实现闭环优化并获得广告收入提升
practical_value: '- **解耦语义 ID 作为推荐与生成的统一接口**：将视频表征拆解为内容语义与创意风格两部分 ID，既用于用户兴趣建模，又直接驱动下游视频生成。电商推荐中，同样可以设计分离的语义码本，分别控制商品推荐逻辑与展示素材风格，实现从“选品”到“创品”的链路打通。

  - **多智能体分层视频生成架构**：用三个角色特化的 Agent（视觉规划、音频对齐、效果增强）顺序执行，共享一个 LLM 骨干并重用 KV-cache。在电商广告素材自动生成中，可借鉴
  Agent 协作流程和 append-only 状态序列化的 KV-cache 复用，降低大批量素材生成的推理延迟。

  - **带约束的多目标奖励优化（GDPO + PID Lagrangian）**：将用户反馈作为主目标，内容对齐与视频质量作为约束，通过组内奖励归一化和 PID
  控制的拉格朗日乘子更新，稳定优化三个异构奖励信号。适合多目标推荐场景，如在优化点击率时控制素材质量与相关性阈值。

  - **近线生成 + 缓存策略解耦实时推理**：视频生成延迟高，通过 SID 索引缓存已生成视频，在缓存命中时几乎零延迟返回，未命中时用最近邻视频占位并异步补全。对于个性化落地页、动态广告素材等非实时性要求稍低的场景，可采用“近线生成
  + 分层缓存”架构，平衡生成质量与响应时间。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统推荐受限于固定素材池，当用户兴趣长尾或动态变化时，只能“搜已有”，无法“造所需”。短视频平台这类问题尤其突出。近期视频生成能力爆发，但直接将大模型接入推荐系统面临两大鸿沟：一是推荐模型处理离散行为数据，而生成模型需要连续多模态信号，难以贯通；二是面向数亿用户的个性化生图、生视频成本极高，工业部署不现实。RaG 正是要解决这两个问题，将推荐范式从“检索已有”推向“生成所需”。

**方法关键点**  
- **解耦语义编码 (D‑SIDs)**：用多模态大模型编码视频，分离出内容语义（实体、话题）和创意风格（节奏、氛围），再经残差量化得到离散的 content SIDs 与 creative SIDs，形成推荐与生成共享的语义接口。  
- **生成式推荐 (GRM)**：基于用户画像与行为序列，自回归预测 future D‑SIDs，不再将 ID 用于检索，而是作为生成式兴趣表达直接进入内容生产。  
- **指令模型 (IM)**：将预测的 D‑SIDs 翻译成镜头级制作指令（场景、运镜、节奏等），用 Gemini 2.5 Pro 蒸馏的监督数据微调 Qwen3-8B，通过三阶段训练（投影对齐→全参微调→RL）提升指令质量。  
- **视频生成智能体 (VGAs)**：三个 Agent 共享一个 Qwen2.5-32B 骨干，通过不同角色 prompt 和注意力掩码区分功能，顺序执行视觉规划→音频对齐→艺术特效，并基于 append-only 状态实现 KV-cache 复用，将单次推理延迟大幅压缩；同时引入两轮反思迭代提升跨模态一致性。  
- **跨域协同奖励学习 (SCRL)**：以用户反馈（点击、转化）为主目标，内容对齐与视频质量作为约束，用 GDPO 做组内奖励解耦归一化，采用 PID 控制的拉格朗日乘子动态调节约束强度，避免多目标训练震荡。

**关键结果**  
- 在线 A/B 实验：在快手广告平台 4 亿+日活用户上，RaG 相比生产级 DLRM 基线广告收入提升 **+5.462%**，相比强 GRM 基线再提升 **+1.870%**，直接来自个性化视频生成。  
- D‑SIDs 的 R@1 比最强多模态基线 **+16.5%**，压缩误差 **-10.5%**，碰撞率 **15.6pp** 更低。  
- VGAs 对比手工作坊式工作流：自动评分均分提升 **+14.3%**，中位数提升 **+22.6%**，自动胜率 **+41.4pp**，用户研究胜率 **+18.5pp**。  
- 奖励消融：各质量子奖励独立提升胜率 18.6~24.0pp，联合优化提升 18.7pp；加兴趣对齐奖励后，对齐分数从 0.707 提升至 0.828。
