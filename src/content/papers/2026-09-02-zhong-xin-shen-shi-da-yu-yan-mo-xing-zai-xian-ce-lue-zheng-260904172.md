---
title: 'Rethinking On-Policy Distillation of Large Language Models II: One Training
  Example'
title_zh: 重新审视大语言模型在线策略蒸馏：单训练样本
authors:
- Zixuan Fu
- Bingxiang He
- Yuxin Zuo
- Haohuan Huang
- Jinqian Zhang
- Ruhang Xiao
- Cheng Qian
- Qinyu Luo
- Huan-ang Gao
- Yudong Wang
affiliations:
- Tsinghua University
- University of Chinese Academy of Sciences
- Northeastern University
- University of Illinois Urbana-Champaign
- Johns Hopkins University
arxiv_id: '2609.04172'
url: https://arxiv.org/abs/2609.04172
pdf_url: https://arxiv.org/pdf/2609.04172
published: '2026-09-02'
collected: '2026-09-05'
category: Training
direction: On-Policy 蒸馏 · 数据效率
tags:
- On-Policy Distillation
- Data Efficiency
- State Coverage
- LLM Post-training
- Multi-Teacher OPD
one_liner: 一个 query 训练数百步即可恢复大部分 full-data OPD 增益，揭示 OPD 数据过剩、算法吸收是瓶颈
practical_value: '- 工业 OPD 数据筛选可转向 state coverage 视角：不是收集更多 prompt，而是选语义多样、能诱导互补状态的少量
  query（如 16 个/域即可匹配 full-data MOPD）。在电商 query 改写、生成式推荐、Agent 轨迹生成中，可先对 prompt/query
  做语义聚类，取代表点训练，大幅降低标注与训练成本。

  - 冷启动或无标注场景可借鉴 content-light 模板与离域日志：只要 teacher 能提供 token-level 监督，chat template
  + <think> 等空模板或历史对话也能驱动 OPD 接近真实 query 效果；可尝试用模板启动生成式推荐或 Agent 策略蒸馏。

  - OPD 训练瓶颈在吸收率而非数据量：固定 states 仍需数百步收敛，说明加大 batch 或数据量未必加速；应优先优化步效率，如 batch reuse、trust
  region、按 token teacher signal 加权，减少训练步数。

  - 多教师蒸馏可按域选少量语义代表 query，每域 16 条即可匹配全量，适合多业务线共享一个生成式推荐/Agent 模型时的数据配比与成本控制。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
OPD 在 Qwen3、MiMo、GLM-5、DeepSeek-V4 等前沿 LLM post-training 中广泛使用，但已有工作主要研究其算法动力学，训练数据的作用并不清楚。该工作用 one-shot OPD 这一极端设定将数据与算法解耦：只用一个 query 反复训练，观察学习曲线，追问为什么如此少的 prompt 能支撑数百步持续改进。

**方法关键点**
- **One-shot OPD**：每步从当前 student 采样 64 条 rollout，teacher 在每个 visited state 提供全 next-token 分布，采用 top-k advantage 或 sampled-token advantage 更新。
- **跨域与跨模型泛化验证**：覆盖数学、代码生成、指令跟随、Agentic tool use；学生-教师对包括 R1-Distill-Qwen-1.5B vs JustRL-1.5B、Llama-3B-It vs GT-Llama-3B-Math、OLMo-7B-It-DPO vs OLMo-7B-It 等。
- **State coverage 度量**：将 full-data OPD 访问的 states 用 teacher final hidden 表示，经 PCA + KMeans 分为 200 个 semantic clusters，统计某 query set rollout 到达的 cluster 比例。
- **Absorption rate 度量**：每个 update 吸收剩余 teacher–student gap 的比例，用于考察算法侧的步效率。

**关键结果**
- 数学推理 one-shot OPD 在 step 300 平均得分 68.5，full-data OPD 为 69.8，恢复 full-data gain 的 87%；到 step 1000 仍恢复 72%。
- 代码生成、指令跟随、Agentic tool use 单 query 分别恢复 teacher–student gap 的 73%、66%、64%，跨家族同样稳健。
- 状态覆盖：1 个 query 覆盖 full-data 状态空间的 71.5%，且大部分在前 100 步获得；16 个语义多样 query 覆盖 98.9% 并匹配 full-data OPD。
- 多教师 OPD 中，每域 16 个语义代表 query 匹配 full-data MOPD（52.9 vs 52.8）。
- 吸收率随训练下降，且与 query 数量无关；固定 states 的 off-policy 训练仍需数百步，说明长训练不是因新鲜 states 持续供给。
- Content-light 模板和 WildChat 离域 query 接近真实 query baseline；与 one-shot RLVR 相比，OPD 验证增益是其两倍以上。

**最值得记住的一句话**
OPD 是 data-overfed but algorithm-starved：数据设计的关键不是收集多少 query，而是选择能诱导哪些 states 的 teacher 监督；优化步效率比扩大数据更重要。
