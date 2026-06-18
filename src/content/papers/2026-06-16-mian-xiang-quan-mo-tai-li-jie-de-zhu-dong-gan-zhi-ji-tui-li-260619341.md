---
title: Native Active Perception as Reasoning for Omni-Modal Understanding
title_zh: 面向全模态理解的主动感知即推理
authors:
- Zhenghao Xing
- Ruiyang Xu
- Yuxuan Wang
- Jinzheng He
- Ziyang Ma
- Qize Yang
- Yunfei Chu
- Jin Xu
- Junyang Lin
- Chi-Wing Fu
affiliations:
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
- Qwen Team, Alibaba Group
- Nanyang Technological University
arxiv_id: '2606.19341'
url: https://arxiv.org/abs/2606.19341
pdf_url: https://arxiv.org/pdf/2606.19341
published: '2026-06-16'
collected: '2026-06-18'
category: Agent
direction: Agent 主动感知与推理优化
tags:
- Active Perception
- Omni-Modal Agent
- POMDP
- Agentic RL
- Test-time Scaling
one_liner: '提出OmniAgent: 首个将长视频理解建模为POMDP迭代循环的原生全模态代理，通过按需主动感知与Agentic RL实现推理-时长解耦和测试时正拓展'
practical_value: '- **按需多模态信息抽取**：电商直播、商品讲解长视频中，可借鉴“观察-思考-行动”循环设计代理，仅针对用户咨询动态提取关键音视频片段，大幅降低首响延迟与计算开销，同时保持全量信息的可访问性。

  - **Agentic RL 功劳分配**：TAURA 利用回合级熵值将奖励集中于关键发现回合，适合多轮对话推荐、用户意图探索等序列决策场景，有效抑制无意义探索噪声，提升在线学习效率。

  - **持久文本记忆解耦**：将视觉、听觉等多模态原始数据实时蒸馏为可压缩、可检索的文本记忆，在用户意图漂移或长会话推荐中维持轻量、可扩展的状态跟踪，避免上下文窗口堆砌。

  - **测试时正拓展策略**：通过动态增加推理轮数提升复杂 query 的推荐/回答质量，可移植到交互式推荐系统的自适应深度推理，实现“思考越久，推荐越准”的效果。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
传统长视频理解采用“全部观看”范式，计算成本随视频时长线性增长；现有交互式框架仍需全局预扫描，上下文代价未解耦。针对此，将视频理解重新定义为部分可观测马尔可夫决策过程（POMDP），让代理按需主动提取信息，而不是被动接收全量数据。

**方法关键点**
- **OmniAgent 框架**：原生多模态代理，支持音频、视频、文本，通过“观察（从视频按需采样）→ 思考（规划下一步）→ 行动（执行检索/裁剪等）”循环，将视听线索逐步蒸馏为持久文本记忆，推理复杂度与原始时长彻底解耦。
- **Agentic SFT**：通过best-of-N轨迹合成与双阶段质量控制（过滤无效动作、校准思维链），引导基础模型获得主动感知的初始行为。
- **Agentic RL + TAURA**：引入回合级熵值对优势函数进行不确定性重标度（Turn-aware Adaptive Uncertainty Rescaled Advantage），使信用分配偏向“发现性”回合，提升多步推理中探索与利用的平衡。

**关键结果**
在10个长视频基准（VideoMME、LVBench等）上达到开源SOTA；LVBench上7B模型超越10倍规模的Qwen2.5-VL-72B（50.5% vs 47.3%）。推理回合数增加带来性能单调提升，验证主动感知的测试时正拓展定律。
