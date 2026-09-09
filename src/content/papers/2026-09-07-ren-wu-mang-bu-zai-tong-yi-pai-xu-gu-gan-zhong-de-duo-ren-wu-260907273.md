---
title: 'Task-Blind No MORE: Multi-Task Information Flow in Unified Ranking Backbones'
title_zh: 任务盲不再：统一排序骨干中的多任务信息流
authors:
- Yuchen Wang
- Feng Niu
- Qing Tan
- Junting Lu
- Baoxin Wu
- Jun Gao
affiliations:
- Hello Group
- University of Science and Technology of China
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Beijing Information Science and Technology University
arxiv_id: '2609.07273'
url: https://arxiv.org/abs/2609.07273
pdf_url: https://arxiv.org/pdf/2609.07273
published: '2026-09-07'
collected: '2026-09-09'
category: RecSys
direction: 多任务学习 · 统一排序骨干
tags:
- Multi-Task Learning
- Unified Backbone
- Anchor Tokens
- Ranking Model
- Task-Aware
- Recommender Systems
one_liner: 提出 MORE，以 Shared/Private Anchor Tokens 将多任务信息流嵌入统一骨干，逐层共同演化，在线多指标提升且延迟降低约30%
practical_value: '- **任务感知 Anchor Tokens 可嵌入统一骨干**：在电商/广告多任务排序中，不要只在塔层做 MMoE/PLE 路由，可在骨干每层引入
  Shared/Private Anchor Tokens，使序列读取和特征交互直接感知任务差异，缓解共享瓶颈。

  - **显式任务边界掩码是关键 trick**：在 token mixing 或 attention 融合阶段，强制 Private Anchor 之间不可见，防止高频任务梯度主导混合权重、稀释长尾任务表示。这比单纯增加每任务容量更有效，可直接复用到多任务特征交互层。

  - **请求级共享计算降低在线延迟**：将同一请求的多个候选聚合为一个样本，用户侧序列编码只算一次并广播，候选侧差异通过 F 和 Anchor Tokens 表达。无需改变模型结构即可降低约30%
  P99 延迟，适合高并发推荐场景。

  - **多行为序列 Cartesian product encoding**：对行为类型组合编码为唯一 ID，而非仅 item 位置编码，可为下游任务感知序列读取提供更细粒度输入，减轻跨任务梯度冲突。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
工业推荐排序模型的骨干演进中，特征交互与序列建模分别缩放，最近统一骨干（HyFormer、MixFormer、OneTrans）将两者合并。但多任务学习在真实场景必不可少，现有统一架构仍将任务分化限制在骨干后的预测塔，骨干本身任务不可知。这带来三个结构性缺陷：序列读取和特征交互无法依据任务调整；所有任务共享一个骨干输出，在任务分化前就压缩了语义空间；扩大骨干规模主要增强共享表示，多任务收益增长缓慢。

## 方法关键点
MORE 将多任务信息流嵌入骨干内部，核心是 Anchor Tokens：Shared Anchors 编码跨任务共性，Private Anchors 每个任务一个，携带任务先验。
- **输入表示**：多行为序列采用 Cartesian product encoding，把行为类型组合编码为唯一 ID，区分不同行为组合；非序列特征组织为 token 矩阵 F。
- **Anchor Token Construction**：从序列均值池化和非序列特征拼接后经 MLP 投影拆分得到 Shared/Private Anchors，Private Anchors 加入可学习任务先验嵌入。
- **每个 MORE Block 包含三个子模块**：
  1. *Task-Aware Sequence Reading*：Anchor Tokens 用 cross-attention 读取序列，Shared Anchors 共享查询，Private Anchors 用每任务独立查询；引入跨层序列寄存器 𝜼，用每 anchor/task 独立 SwiGLU 门控融合。
  2. *Selective Semantic Mixing*：将 F、Shared Anchors、Private Anchors 拼接为 token 矩阵，做 MLP-Mixer 风格混合，但施加任务边界掩码：F 和 Shared Anchors 对所有 token 可见，每个 Private Anchor 仅对自身可见，严格隔离任务间信息流。
  3. *Task Enhancing*：对每个 Private Anchor，用每任务独立 MLP 从 F 生成 FiLM 风格 scale/shift 参数，做仿射调制，增强任务判别性。
- **请求级训练推理**：同一请求的多个候选聚合为一个样本，用户侧序列计算共享，候选差异体现在 F 和 Anchor Tokens，无需架构改动即降低在线延迟约30%。

## 关键实验
在 Momo Nearby Feed 场景，90 天训练、次日评估，13 个任务中汇报 7 个核心任务。对比两阶段基线（Transformer+RankMixer、HSTU+RankMixer、STCA 等）和统一骨干基线（MixFormer、HyFormer、OneTrans）。MORE 在所有 7 任务上 GAUC 相对提升最高（如 Greet +1.58%、Like +1.47%、Deep Chat +0.33%），且 FLOPs 仅 1.85G，低于多数基线。消融显示任务边界掩码贡献最大，移除后平均 GAUC 下降 0.21%，互动任务下降 0.34%。缩放分析从 0.1B 到 0.9B 参数，MORE 比任务无关统一骨干更高效地将参数和计算转化为多任务增益。在线 A/B 测试：使用时长 +3.0%、点击 +2.8%、点赞 +2.0%、评论 +3.6%、打招呼 +2.5%、深聊 +2.0%，P99 延迟降低约 30%。

最值得记住的一句话：显式任务边界隔离比单纯增加每任务容量更重要——在骨干内部阻止 Private Anchor 之间的信息泄漏，是提升多任务统一模型的关键。
