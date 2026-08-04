---
title: 'RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving
  Agent Memory via Reduced-Order Utility States'
title_zh: RoMeRL：降阶效用状态平衡 Agent 记忆反馈与记忆-奖励陷阱
authors:
- Yi Yang
- Zhennan Chen
- Yihong Zhuang
- Tiehan Fan
- Yinan Chen
- Jian Li
- Jian Yang
- Ying Tai
affiliations:
- Nanjing University
- Xiamen University
- Zhejiang University
arxiv_id: '2608.02508'
url: https://arxiv.org/abs/2608.02508
pdf_url: https://arxiv.org/pdf/2608.02508
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 记忆自进化 · 降阶效用状态
tags:
- Agent Memory
- Reduced-Order State
- Reinforcement Learning
- LLM Agents
- Memory-Reward Trap
- Utility Learning
one_liner: 用四个固定语义坐标替代轨迹级效用，将反馈密度提升6倍，记忆量减少84%并阻断噪声奖励
practical_value: '- 采用固定维度语义坐标管理 Agent 记忆，可按“正负极性×动态/巩固”划分槽位，避免记忆池持续膨胀导致的效用稀释，适合电商客服、对话推荐等需要持续学习的
  Agent 场景。

  - 检索时用 Q 值加权相似度（`(1-ω_Q)*similarity + ω_Q*Q`）既能利用任务反馈又可保留语义匹配，可在商品推荐或搜索的召回/排序中借鉴，让效用信号与相关性共同决策。

  - 设计“负向巩固坐标（NCC）”保留高 Q 值的失败案例，为后续决策提供纠错信号，类比推荐系统中保留高价值但未转化的交互，用于策略优化。

  - 降阶状态天然隔离错误奖励传播（MRT），类似控制曝光噪音，可在广告竞价或推荐策略评估中用有限坐标表示效用，避免无关 item 被误强化。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：
自进化 LLM Agent 的记忆系统面临两个耦合难题。第一，轨迹索引的效用值随交互增多而不断扩张，反馈信号被稀疏化，形成效用冷启动。第二，共享轨迹奖励会同时更新共检索的多条记忆，导致弱相关或负贡献的记忆被错误赋予正向奖励，陷入“记忆-奖励陷阱（MRT）”。更强的探索虽能提升反馈覆盖，却加剧了陷阱，形成探索‑污染困境。

**方法关键点**：
- 提出**降阶记忆强化学习（RoMeRL）**，将每个任务的增长型轨迹效用空间替换为固定维度的因子化状态。
- 状态按**结果极性（+/‑）** 与**记忆动态（凝聚型 C/自适应型 A）** 分解，得到四个语义坐标：
  - **PCC**（正凝聚）：保留全局最高效的成功轨迹。
  - **PAC**（正自适应）：记录从失败到成功的首次恢复路径。
  - **NCC**（负凝聚）：保留具有高下游回报的失败经验。
  - **NAC**（负自适应）：跟踪最近一次失败。
- 每个坐标只存一个代表记忆及其 Q 值，新体验通过继承、升级或替换更新坐标内容，不再新增效用变量。检索时以语义相似度和 Q 值的加权得分排序。
- 理论证明降阶状态能浓缩反馈（反馈密度提升至原 N_t/4 倍），且通过替换概率控制错误坐标的稳态占用。

**关键结果**：
- 在 ALFWorld 和 LifelongAgentBench 上，冻结 LLM 的 RoMeRL 取得最高综合成功率 0.862（基线 0.830）。
- Cold‑Q 比率降低 **80.0%**，反馈密度提升约 **6.0×**。
- 记忆池大小减少 **84.4%**（45K→7K），LLM 调用减少 **21.1%**（570K→450K）。
- MRT 压力测试中噪声正更新从 7.2 降至 2.4，最终噪声比仅 0.15%，显著优于 MemRL+UCB。
- 跨模型迁移实验表明冻结的记忆状态可跨 LLM 提升任务得分并减少步数。消融显示 NCC 和 PAC 分别支持高价值失败复用与恢复模式，缺一不可。

**核心一句话**：用四个语义坐标替代记忆效用空间，即可在更高反馈密度、更低存储与计算成本下，阻断错误奖励——远比扩张记忆池更高效。
