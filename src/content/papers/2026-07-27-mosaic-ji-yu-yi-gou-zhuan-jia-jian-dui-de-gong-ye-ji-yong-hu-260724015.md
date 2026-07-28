---
title: 'Mosaic: A Fleet of User Embedding Specialists for Recommendation at Meta'
title_zh: Mosaic：基于异构专家舰队的工业级用户嵌入平台
authors:
- John Zhiyuan Zheng
- Xian Sun
- Xiangyang Mou
- Yujunrong Ma
- Christina You
- Michael Jiayuan He
- Hrishikesh Paranjape
- Aakarsha Agarwal
- Hong Li
affiliations:
- Meta
arxiv_id: '2607.24015'
url: https://arxiv.org/abs/2607.24015
pdf_url: https://arxiv.org/pdf/2607.24015
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 用户表征多专家舰队
tags:
- User Embedding
- Specialist Fleet
- Multi-Task Learning
- Redundancy Loss
- Evaluation
- Hybrid Serving
one_liner: 设计四种异构专家模型分别捕捉用户行为侧面，结合MRM与CRL消除冗余，离线NE与线上多面指标均提升
practical_value: '- **模型架构选择**：将用户信号拆分为稀疏ID、密集统计、行为序列和下游任务对齐四类，分别使用记忆型哈希表、DCN/MHTA等密集交互网络、HSTU序列模型和CoTrain端到端梯度对齐，避免单一模型在多目标上共享容量的折中。

  - **增量信息保障**：当已有多个嵌入在线上服务时，新嵌入训练可引入**MRM**（对相关任务做Spearman聚类，用笛卡尔积构建细粒度复合监督标签）与**CRL**（余弦冗余损失，鼓励新嵌入与已有嵌入正交，配合warm-up调度），有效对抗边际收益递减。

  - **评估提效**：**CoEval** 冻结用户塔并在下游排序器中就地计算ΔNE，跳过特征日志积累与回流重训，可将迭代周期缩短3~5倍；**User Tower
  Zero-Out** 则可快速衡量上游模型中用户塔的增量值，二者均值得在解耦用户建模流程中推广。

  - **混合在线/离线服务**：根据新鲜度需求选择CPU在线、GPU在线或GPU离线批量生产用户嵌入；GPU在线推理叠加AOTInductor编译、模型拆分与2小时TTL的memcache，累计可降低79%的GPU用量并微幅改善延迟。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
用户表征是推荐系统的基石，但现有工作多围绕单一用户模型或共享骨干+轻量适配，难以同时高效捕捉稀疏ID记忆、密集统计交互、行为序列动态和下游特定任务对齐这四类信号。Meta 发现，将用户建模拆解为异构专家舰队，每个专家专注一种归纳偏置，既能独立迭代、又能通过去冗余手段持续叠加增益，是一种未充分探索的范式。

**方法关键点**
1. **四类专家架构**：
   - *记忆驱动*：超大规模哈希表 + Table-Batched Embedding (TBE) + TorchRec 行分片训练 + 分布式推理，将人工特征浓缩为紧凑向量。
   - *密集交互*：以 DCN v2、MHTA、SEDot、Wukong 等网络对多窗口计数值进行非线性交叉，发射多个嵌入。
   - *序列建模*：在 HSTU 基础上引入上下文前缀token、UIH 交插行为内容与元数据、层次注意力，并用随机长度训练对齐服务端短序列分布。
   - *CoTrain 对齐*：将下游排序器副本接在共享用户塔上联合训练，产出与目标面直接对齐的嵌入。
2. **冗余消除**：
   - *MRM*：对多任务标签做 Spearman 相关聚类，对高度相关任务进行笛卡尔积构造复合标签（如“点赞+分享”四类），让嵌入学习细粒度用户意图。
   - *CRL*：新嵌入与已部署嵌入的余弦相似度作为惩罚项，通过 warm-up 调度逐步引入，强制学出正交增量信息。
3. **日志无关评估**：CoEval 冻结用户塔并就地喂入下游排序器测量 ΔNE；User Tower Zero-Out 直接在上游模型中将用户塔输出置零计算 NE 差距，省去数天的特征回积与重训。
4. **混合服务**：CPU 在线、GPU 在线与 GPU 离线三条路径按新觧度/成本分配；GPU 路径通过 AOTI 编译、模型拆分与 2 小时 TTL 的 look-aside 缓存，降低 79% 的 GPU 使用。

**关键结果**
- 离线 NE：在 6 个产品表面、数十个任务上取得一致负向（改善）ΔNE，表面 1 主任务可达 -0.21%~-0.37%。
- 专家贡献：密集型专家贡献最大（-0.22% NE），CoTrain 次之（-0.15%），序列专家 -0.12%，记忆专家 -0.09%。
- 线上 A/B：多面 topline 指标提升 +0.10%~+0.28%，统计显著。
- 序列缩放：将序列长度从 512 扩至 2048，NE 改善从 -0.21% 加深至 -0.45%（QPS 下降 33%）。
- 评估加速：CoEval 将端到端迭代周期压缩至一半以下。

**最值得记住的一句话**
“用一族异构专家分别捕捉用户行为的不同侧面，并通过 MRM 与 CRL 持续榨取增量信息，是比扩大单一模型更可持续的用户建模路径。”
