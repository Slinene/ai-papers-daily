---
title: Planning over Matrix-Factorization MDPs for Candidate Generation
title_zh: 基于矩阵分解MDP的候选列表规划
authors:
- Mikhail Trapeznikov
- Maksim Utushkin
affiliations:
- AI VK
- Lomonosov Moscow State University
arxiv_id: '2607.02115'
url: https://arxiv.org/abs/2607.02115
pdf_url: https://arxiv.org/pdf/2607.02115
published: '2026-07-02'
collected: '2026-07-04'
category: RecSys
direction: 动态感知的MF候选生成规划
tags:
- matrix factorization
- MDP
- planning
- candidate generation
- reinforcement learning
- MCTS
one_liner: 在固定MF嵌入上增加闭式秩一更新的前瞻规划，使检索列表感知用户状态变化
practical_value: '- 对现有MF检索管线几乎零改动：仅需缓存后验矩阵 \(A^{-1}\)、复用已有item embedding，用闭式 Sherman‑Morrison
  更新完成单步前瞻（Plan‑1），计算成本 \(O(d^2)\)，可快速集成到粗排或召回后重排。

  - 必须用余弦相似度替代内积：内积与物品流行度高度纠缠，导致规划偏向热门 item，余弦相似度是让规划生效的前提，业务上务必做相似度形式的消融验证。

  - 在全局时间切分（GTS）下规划增益不一定成立，因为物品流行度、用户行为分布会随时间段漂移，乐观的“推荐即接受”假设失效；实际部署前必须用未来时段数据验证，只在验证显示序列结构时启用
  Plan‑K。

  - MCTS 可采用 ANN 索引限制每个节点的候选动作数（Wolpertinger 风格），配合余弦先验的 UCT 探索项保持对数遗憾界，控制树搜索开销。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
标准矩阵分解（iALS）检索用单个用户向量静态取 top‑K item，忽略了推荐序列会改变用户后验状态，导致列表缺乏序列依赖性。本工作在固定 MF 嵌入基础上探究添加一个轻量决策层的收益，对比静态检索、单步前瞻（Plan‑1）与 MCTS 多步规划（Plan‑K），分离表示学习和规划的效果。

### 方法关键点
- **状态与动作**：将 iALS 后验对 \( (A^{-1}, u) \) 作为 MDP 状态，item 作为动作，跃迁为乐观假设“推荐即接受”下的闭式秩一更新（Sherman‑Morrison）。
- **闭式更新**：给定当前矩阵 \(P = A^{-1}\) 和候选物品向量 \(v\)，更新后 \(P^+ = P - \frac{z z^\top}{1+\ell}\)，\(u^+ = u + \frac{z(1-u^\top v)}{1+\ell}\)，复杂度 \(O(d^2)\)。
- **轨迹奖励**：\(r(s,a) = \text{sim}(u, v_a) + \eta \frac{1}{1+|\Delta s(a)|}\)，第二项为后验对齐项，衡量 item 加入后对其自身得分的改变程度。
- **规划深度**：Static 无前瞻；Plan‑1 对每个候选施加一次 fold‑in 后按下个状态的奖励重排；Plan‑K 用 MCTS 搜索长度为 K 的轨迹，并用 ANN 限制展开宽度，UCT 探索项引入余弦先验。

### 关键结果
- 在 5 个数据集（MovieLens‑1M、KuaiRec、VK‑LSVD 工业切片、YAMBDA）上进行 leave‑last‑n (LLN) 和全局时间切分 (GTS) 两类协议评估，固定使用相同 item embeddings。
- **LLN**：Plan‑1 在所有数据集上 Recall@10 均优于 Static，VK‑IP 从 0.0201→0.0294，VK‑UP 从 0.0161→0.0260；Plan‑K 在 KuaiRec 等部分数据集上进一步小幅提升。
- **GTS**：增益在 MovieLens‑1M 和两个 VK 切片上保留，但在 KuaiRec、YAMBDA 上消失，甚至负收益，说明时间漂移会使规划失效。
- **相似度消融**：将余弦替换为内积后，Plan‑1 全面大幅落后余弦方案，甚至不如 Static，表明余弦是规划起作用的必要条件。

### 一句话结论
在固定的协同过滤 embeddings 上，用闭式秩一更新做单步前瞻规划即可稳健提升 LLN 设定下的 recall，但时间漂移会削弱甚至逆转这一收益，部署前必须按全局时间切分验证。
