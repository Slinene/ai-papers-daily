---
title: Redesign Mixture-of-Experts Routers with Manifold Power Iteration
title_zh: 基于流形幂迭代重新设计 MoE 路由器
authors:
- Songhao Wu
- Ang Lv
- Ruobing Xie
- Yankai Lin
affiliations:
- Renmin University of China
- Tencent
arxiv_id: '2606.12397'
url: https://arxiv.org/abs/2606.12397
pdf_url: https://arxiv.org/pdf/2606.12397
published: '2026-06-09'
collected: '2026-06-11'
category: Training
direction: MoE 路由器设计 · 幂迭代对齐
tags:
- MoE
- Router
- Power Iteration
- SVD
- Load Balancing
- Optimization
one_liner: 让路由器行向量逼近对应专家权重的主奇异方向，以提升 MoE 路由质量
practical_value: '- **路由器显式编码专家特征**：在电商 Agent 多智能体或生成式推荐的 MoE 架构中，可直接替入 MPI，无需调整推理
  pipeline。每步仅需一次幂迭代与 L2 归一化，零额外推理开销，能与现有负载均衡损失、z-loss 等兼容。

  - **幂迭代替代正交化初始化**：若业务中专家矩阵动态更新，可借鉴 MPI 的“Power-then-Retract”模板，用廉价矩阵乘实时跟踪主奇异方向，代替昂贵的
  SVD 或静态正交初始化，使路由器持续对齐专家能力变化，尤其适合在线更新的场景。

  - **常数 C 的缩放准则**：论文给出的 C′ ≈ O(1/√N) 设计原则（C = C′/√N）可作为超参传递给不同专家数模型，在推荐系统扩容专家时降低调参成本，保障路由
  logits 尺度稳定。

  - **负载均衡意外收益**：MPI 天然降低负载均衡损失，省去一部分复杂的平衡策略，可用于电商多业务专家流量的自动均衡，减少“专家失活”问题。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
MoE 模型的路由器通常是一个线性矩阵，其每一行作为对应专家的“代理向量”，通过点积决定 token 分配给哪个专家。但现有设计缺乏约束，使得路由器行向量无法有效编码专家矩阵的内在特征，导致次优路由。作者提出，理想的路由器行应该与专家权重矩阵的主奇异方向对齐，因为主奇异方向是压缩表示矩阵信息的最优方向。  

**方法**  
- **核心思想**：让路由器行向量 R[i] 逼近专家权重 W_g 的主右奇异向量，即最大化投影 ∥R[i] W_g∥²。  
- **流形幂迭代 (MPI)**：每步训练对 R[i] 做一次幂迭代 (`R̂ = R W_g W_gᵀ`)，再通过 L2 投影回固定范数（`R' = C·R̂/∥R̂∥`），形成“Power-then-Retract”范式。此更新等价于在球面流形上做最速上升，自适应地将路由器推向主奇异方向。  
- **尺度规范**：指定 `C = C'/√N`，C′ 为全局常数，保证路由 logits 量级不受专家数 N 影响，防止数值发散。  
- **实现极简**：仅需在计算 gating weights 前插入几行矩阵乘和归一化，不改变 MoE 接口。  

**实验**  
在 1B、3B、11B 参数 MoE 模型上预训练，使用 FineWeb-Edu 等数据集，训练 tokens 达 350B。与标准路由器相比：  
- 1B 模型在四种优化器下，下游 25 项任务平均准确率提升 0.97~1.39 个百分点（如 AdamW 下从 42.26→43.56）。  
- 11B 模型预训练损失持续更低，验证集 PPL 从 0.764→0.754（3B），0.728→0.723（11B），下游挑战任务（MMLU、GSM8K 等）普遍提高。  
- 负载均衡指标 MaxVio 显著下降（如 3B 全局 MaxVio 从 0.964→0.711），且训练吞吐仅降低 0.2%。  

**核心启示**：通过极低成本的幂迭代使路由器主动“学习”专家参数的主成分，可以为 MoE 路由带来免费的性能与负载均衡增益。
