---
title: 'UniDot: A Unified Network for Sequence Modeling and Feature Interaction in
  Large-scale Recommendation'
title_zh: UniDot：统一序列建模与特征交互的大规模推荐架构
authors:
- Rongcheng Lin
- Yan Sun
- Jamey Zhang
- Guanglei Xiong
- Ivan Ji
- Xianjie Chen
- Shujian Bu
affiliations:
- Meta
arxiv_id: '2608.16797'
url: https://arxiv.org/abs/2608.16797
pdf_url: https://arxiv.org/pdf/2608.16797
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 统一序列建模与特征交互架构
tags:
- UniDot
- Feature Interaction
- Sequence Modeling
- CTR-CVR
- Factorization Machine
- Multi-path Mutual Learning
one_liner: 以点积为统一原语，用双总线并行堆叠块融合序列与特征交互，获 KDD Cup 2026 工业赛道亚军
practical_value: '- **显式保留 FM 级点积交互**：在深层残差网络旁路增加一个 FM Highway，把每层 token 点积、Gram 矩阵、跨总线
  user-item 点积直接 concat 送进分类器，消融显示去掉后 AUC 掉 0.127%，成本极低。现有 DeepFM/DCN 等模型可以借鉴：不要把所有低阶信号都交给深层网络隐式学习，显式旁路对
  CTR/CVR 任务性价比很高。

  - **多路径互学习（DML）**：两条相同结构、共享稀疏 embedding 表的路径互相蒸馏，推理时可以只用单路径（1× 成本），但训练时多路径正则化能把单路径模型拉到更好最优解。论文中单路径就能拿亚军，适合需要严格控制线上推理成本的场景。

  - **序列编码一次、多处共享**：行为序列 embed 一次，同时供 cross-attention、池化等多个消费者使用，避免重复编码。多域行为按时间戳 merge
  成一条流，再与原始 domain 并行，能捕捉跨域时序模式。这个工程实现可显著降低推荐系统序列侧的推理延迟。

  - **冷重启 embedding 对抗时间漂移**：每个 epoch 后把高基数 embedding 表重新初始化，dense 参数保留，让 embedding
  每轮重新学习，适配广告推荐中训练/测试时间差小的场景。对于电商大促、广告新广告位等快速变化场景有参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐系统长期存在两套独立演进的模型家族：特征交互模型（Wide&Deep、DeepFM、DCN）处理多域静态特征，序列模型（DIN、DIEN、SIM）建模用户行为历史。生产系统通常只做松耦合，两者缺乏统一架构。TAAC×KDD Cup 2026 工业赛道明确提出“统一序列建模与特征交互”，要求一个统一的 tokenization 方案和同质堆叠骨干。UniDot 的出发点是把 FM 内积与注意力 query·key 点积视为同一原语，显式保留协同过滤的泛化能力，而不是让深层网络隐式学出交互。

## 方法关键点
- **统一 token 空间**：所有输入（用户/物品多域特征、行为序列）都被嵌入到同一个 d_model 维度。非序列字段通过 NCB 沿 token 轴压缩，行为序列按 fid 压缩到统一 per-position 宽度。
- **双总线并行宏块**：每层包含 token-mixing bus（默认 Wukong 块）和 sequence-retrieval bus（item token cross-attend 行为序列），两者并行运行，每层通过 MLP-Mixer 风格的 FuseFFN 交换状态。
- **FM Highway**：每层把 per-sequence dot product、聚合 Gram 矩阵、user-item cross-dot 等显式点积交互直接送入分类器，绕过融合路径，保留 FM 式二阶信号，消融显示最关键。
- **序列编码器**：多域行为按时间戳 merge 成一条流；depthwise Conv1d 捕捉局部 N-gram；DIN 风格条件 SwiGLU 为 gate 注入候选 context；因果 Transformer 建模长程依赖；序列只嵌入一次，所有消费者共享。
- **训练技巧**：双优化器（稀疏用 Adagrad，dense 矩阵用 Muon）；辅助转化延迟头；两路径互学习（共享稀疏 embedding 表，相互蒸馏，推理平均 logits）。

## 关键实验
- 数据集：腾讯广告日志，35M train / 12M test，label 为转化，指标 AUC。
- 最终结果：工业赛道亚军，测试 AUC 0.83217，与第一名差距仅 0.037%。即使只用单路径推理，AUC 0.83184 也能排第二。
- 消融：去掉 FM Highway 掉 0.127% AUC；去掉 token-mixing bus 掉 0.067%；去掉 sequence cross-attention 只掉 0.053%（多通道池化补偿）。
- 多路径互学习在 d=64 时带来 +0.135% AUC，超过整个宽度扫描（+0.050%）。
- 数据 scaling 呈 log-linear，说明 unified block 数据饥饿，尚未饱和。

## 最值得记住的一句话
FM 内积和注意力 query·key 是同一个点积原语，显式保留这个低阶交互可以对抗深层残差网络对二阶信号的稀释。
