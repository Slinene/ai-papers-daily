---
title: "Do Generative Recommenders Deepen the Information Cocoon? A Closed-Loop Simulation with LLM-powered User Simulators"
authors: Jiyuan Yang, Gengxin Sun, Mengqi Zhang, Xin Xin, Pengjie Ren, et al. (8 人)
affiliation: Shandong University × Renmin University of China
date: 2026-06
venue: arXiv (投 ACM TOIS)
topic: user-simulation
topic_name: User Simulation
topic_icon: 👥
idea: 用 LLM 当用户搭闭环仿真台 RecLoop（双记忆 + 周期反思 agent，推荐器每轮重训，跑 15 轮），系统量化生成式推荐 vs 传统 ID 序列推荐的信息茧房。结论：生成式更抗曝光层茧房（用户间 Jaccard 0.064 vs SASRec 0.223），但茧房转移进了 code 空间、集中在粗层（首 token 熵降 49.6%）；并首创 Code-Space 结构性茧房指标。
paperUrl: https://arxiv.org/abs/2606.17707
codeUrl: https://github.com/Dregen-Yor/RecLoop
tags:
- LLM User Simulator
- Closed-Loop Simulation
- Generative Recommendation
- Information Cocoon
- Code-Space Entropy
unverified: false
detail:
  contribution: |
    ① 提出 RecLoop 闭环仿真框架：LLM-powered user agent（动态画像 + 双记忆 + 周期反思）与推荐器每轮重训耦合，做长期（15 cycle）信息茧房分析，补上静态离线评测测不出反馈回路效应的空白；② 首创 Code-Space Structural Cocoon 指标（逐层 code 熵 + top-κ 集中度 + 相对熵降 δ_n），把茧房从 "用户看到什么" 重新定义为 "生成式模型内部 code 空间塌缩到哪"，这是传统 ID 系统根本不存在的视角；③ 系统对比 4 模型 2 范式，给出 tokenization 与 model scale 对茧房严重度的影响结论。
  background: |
    信息茧房是反馈回路（曝光→点击→重训）反复累积的长期现象，静态离线评测把用户偏好与曝光分布当固定的、根本测不出。传统 ID 序列推荐的茧房已研究透（用户表征与热门 item 越训越对齐导致同质化）；但生成式推荐把 "打分选 item" 换成 "自回归生成多层离散 code 序列"：共享 code 前缀既可能一次放大整片热门 item 区域、也可能把曝光扩散到共享 code 的多个 item，早层 code 决定晚层又可能让收窄向下传播——到底缓解、继承还是加深，是个先验无法判断的经验问题，必须搭闭环实测。
  method: |
    **RecLoop 闭环**：每轮推荐器输出 top-K=5 曝光，LLM user agent 按当前画像选 1 个 item + 给理由，选中项追加进历史与训练集，周期重训进入下一轮，跑 T=15 轮。**User agent**：base profile（离线从真实历史 prompt LLM 合成第一人称心理画像作偏好锚）+ stage-wise profile（每 Δ=5 轮经反思更新）；短期滑窗记忆（W=5 轮）+ 长期完整轨迹；action 用四层 prompt（画像 / 记忆 / 候选描述 / 约束层枚举合法 item ID 防幻觉），Qwen3-8B temp=0 确定性反馈。**被测模型**：SASRec / Mamba4Rec（传统 ID 打分）vs TIGER（RQ-VAE Semantic ID 自回归）/ OneRec（LLM-based，用 MiniOneRec 代码库，只 SFT 不 RL 以对齐 baseline 监督，含 0.5B/1.5B/3B）。**指标**：曝光层（品类熵 / 用户间 Jaccard / 覆盖 / Gini）+ code 层（逐层 code 熵 / top-κ 集中度 / δ_n 相对熵降）。
  experiments: |
    两 Amazon 数据集（Office 4.9K 用户/2.4K item，Toys 19.4K 用户/11.9K item，5K/20K agent，含 4 级品类树）。**RQ1 曝光层**：生成式更抗——Office 末轮用户间 Jaccard SASRec 0.223 > Mamba 0.138 > TIGER 0.108 > OneRec 0.064；但 Gini 对所有模型都涨（Office 0.966~0.993），头部 item 集中是范式无关的。**RQ2 code 空间**：结构性茧房集中在粗层——TIGER δ Layer0=53.6% / Layer1=40.4% / Layer2=13.4%；首 token 归一化熵 0.895→0.451（-49.6%），top-10 粗 code 累计概率 27%→86.6%。**RQ3 tokenization**：CID（协作信号）比 SID（语义）更易塌缩、削弱细层多样性缓冲（TIGER 明显），但 Toys 上出现反转，dataset-dependent。**RQ4 scale**：OneRec-3B 末轮各层熵 6.672/7.218/7.119 远高于 0.5B 的 5.303/5.238/4.873，最细层活跃 code 数 3B=233 vs 0.5B=70。
  pros: |
    ① 提出 "结构性茧房" 概念 + 配套 code 空间可量化指标，是生成式推荐特有、传统系统不存在的原创视角；② RecLoop（双记忆 + 反思 agent + 周期重训闭环）是可复用的长期仿真模板；③ 控制变量扎实——同用户集 / 同初始历史，OneRec 刻意只 SFT 不 RL 把差异干净归因到架构，RQ3/RQ4 是两组干净消融；④ 约束层防幻觉 + temp=0 确定性反馈保证可复现。
  cons: |
    ① 仿真效度是最大软肋——用户是 LLM 不是真人，且作者自承未对真实交互分布做任何校准，茧房绝对值不可解读为真实严重程度；② 每配置只跑一条轨迹、无多 seed、无置信区间，统计稳健性弱；③ 范围窄：仅 2 个 Amazon 数据集、每范式 2 模型、scale 仅到 3B，且无 diversity-aware / 去偏 baseline；④ 纯诊断、未提任何缓解方法（无 intervention）。
  inspiration: |
    ① OneRec 是字节自家生成式推荐，本文证明它抗同质化但有 code 空间结构茧房、且 3B 明显比 0.5B 更抗茧房——"逐层 code 熵 + 首 token top-κ 集中度" 可直接搬来当线上多样性监控指标，比品类熵更早预警塌缩；② tokenizer 选型多了茧房维度：CID 涨精度但把热度偏置带进 code 空间、削弱细层缓冲，做 Semantic ID 时别只用 next-item 精度调 tokenizer、要并行看 code 熵；③ RecLoop 的 "确定性反馈 + 约束层防幻觉 + 周期反思" 三件套可直接补强 push / 推荐 simulator 的长期演化能力。
  takeaway: |
    提出 "结构性茧房" 概念并给出 code 空间可量化诊断工具，证明生成式推荐是 "转移" 而非 "消除" 信息茧房——生成式推荐多样性 / 负责任方向上卡位清晰、工具有原创性、但尚停留在测量阶段的早期进展。
---
