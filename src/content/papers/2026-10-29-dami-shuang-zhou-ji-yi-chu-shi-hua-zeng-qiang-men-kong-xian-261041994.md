---
title: 'DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval
  in Gated Linear Attention'
title_zh: DAMI：双轴记忆初始化增强门控线性注意力长上下文检索
authors:
- Zhangchi Feng
- Harry Jiang
- Yangyifei Luo
- Ray Zhang
- Richong Zhang
affiliations:
- SpeedAI
- Beihang University
arxiv_id: '2610.41994'
url: https://arxiv.org/abs/2610.41994
pdf_url: https://arxiv.org/pdf/2610.41994
published: '2026-10-29'
collected: '2026-11-04'
category: Training
direction: 门控线性注意力 · 记忆初始化
tags:
- Gated Linear Attention
- Initialization
- Long-Context Retrieval
- Memory
- RULER
- Linear Recurrence
one_liner: 联合配置头时间尺度与层输入敏感度，在不增加参数的情况下提升五种线性注意力架构的长上下文检索准确率
practical_value: '- **用户长期行为序列建模**：若用 Mamba/GDN/RWKV 等线性注意力处理用户长 session，可将多个 head
  的衰减时间尺度几何分布（如 1~4096），让不同 head 分别捕捉近期点击与长期偏好；避免统一衰减导致远期信号被遗忘或近期噪声过拟合。

  - **分层表征初始化先验**：低-高-低输入敏感度可迁移到推荐/Ads 塔：浅层 embedding/low-level 层保持低敏感性求稳定，中间交叉层高敏感捕捉动态，深层汇总层再低敏感防止稀有关联消失；配合无梯度校准，只需少量业务激活即可完成初始化。

  - **工程可插拔且零推理成本**：DAMI 仅改变衰减侧初始化，不增加参数与推理开销；适合作为现有 SSM/线性注意力推荐模型的 baseline 增强，尤其当业务数据分布迁移或长上下文需求提升时，可低成本重校准。

  - **长上下文检索能力**：若模型需要从长会话/长文档中检索相关信息（例如客服历史、详情页关联），可参考 RULER 风格评估，并利用该初始化改善远距离依赖命中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
线性注意力/门控递归因 O(n) 计算与固定状态缓存，适合长序列部署，但存在有限状态记忆导致长上下文检索（如 NIAH）变弱。GDN 受控实验显示训练后记忆参数 A_log/dt_bias 与初值 Pearson 相关达 0.926/0.939，表明初始化结构被保留，仅靠后续训练难以修正。现有 PoST 只做频谱初始化，忽略 dt_bias 与激活的联合作用。

### 方法关键点
- 双轴目标：head 维度分配几何间隔时间尺度 τ_h ∈ {1,...,4096}，近似幂律依赖的指数混合；层维度采用低-高-低输入敏感度 S_ℓ。
- 无梯度联合校准：逐层用真实投影激活统计信息，先二分求解 dt_bias 匹配目标敏感度，再基于平均 Softplus 因子补偿求 A_log 匹配时间尺度，不增加可训练参数。
- 跨架构适配：KDA/GDN2 保留通道 bias；Mamba-2 用几何频谱 + 深度缩放传递低-高-低模式；RWKV-7 以 sigmoid 门控响应调度冻结缩放。

### 关键结果
在约 100M 参数、5B token 训练的 GDN/KDA/GDN2/Mamba-2/RWKV-7 上，RULER-style NIAH（11 个设置）平均准确率相对随机初始化提升 5.29–16.71 个百分点；相对 PoST 风格频谱提升 8.47–10.87。WikiText PPL 与常识推理基本持平。GDN 消融显示，随机化 A_log 或 dt_bias 之一会使 NIAH-2 从 42.75 掉至 2.40/16.90，证明联合配置必要。

### 最值得记住的一句话
初始化不是超参数而是行为设计：用真实激活校准记忆衰减双参数，可以以零额外推理成本获得长上下文检索的显著提升。
