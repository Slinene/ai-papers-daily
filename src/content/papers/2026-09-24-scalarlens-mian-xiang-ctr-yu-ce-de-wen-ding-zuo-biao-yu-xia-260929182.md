---
title: 'ScalarLens: Numerical Embeddings with Stable Coordinates and Contextual Responses
  for CTR Prediction'
title_zh: ScalaRLens：面向 CTR 预测的稳定坐标与上下文响应数值嵌入
authors:
- Heng Yao
- Tianying Liu
- Yulou Shu
- Yong He
- Chuan Yuan
- Kaibin Qiu
- Guowei Chen
- Jiayu Zhao
- Siyun Hou
affiliations:
- Ant Group
- Independent Researcher
- Alibaba Inc.
- Henan Polytechnic University
arxiv_id: '2609.29182'
url: https://arxiv.org/abs/2609.29182
pdf_url: https://arxiv.org/pdf/2609.29182
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: 数值特征嵌入 · 坐标-响应解耦
tags:
- CTR Prediction
- Numerical Embeddings
- Contextual Response
- Low-Rank Dynamics
- Feature Representation
one_liner: 将数值 embedding 解耦为稳定坐标与上下文响应，在 27 个 CTR 设置中 25 个排名第一
practical_value: '- 可直接在现有 CTR 主线上以轻量模块替换数值 embedding 层，只输出 numerical token，不改 categorical
  token 和 backbone；坐标与响应分离后，上下文不会再重写数值的原始位置，适合需要审计数值特征不变量的业务场景。

  - 抛弃线上/离线 normalization 同步，直接用原始数值尺度训练和推理，把 fitted ranges 和 mesh 存进 checkpoint，减少特征
  pipeline 的存储、I/O 和一致性维护成本；在特征来源多、版本独立的电商/广告系统中尤其省事。

  - 共享低秩 UV 算子 + field-specific gate/drive + 固定步数有界更新，推理额外开销仅约 13%，训练优化后延迟低于 DEER；工程上容易控制算力预算。

  - 消融显示 categorical context 是可靠响应信号，numerical context 只是辅助；业务落地时可以优先只用类别特征做条件，降低复杂度，同时保留数值坐标的单调性和可解释性。

  - 稀有上下文收益更大（Criteo rare 组 margin 0.0012–0.0016 vs common 0.0007），对长尾用户/低频场景有参考价值。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统数值 embedding 把每个 scalar 映射为固定向量，同一数值在不同样本中的表示完全相同，忽略了上下文对数值含义的影响。论文在 Criteo 验证集上发现：同一个数值区间 (2,3] 在不同 categorical/numerical 上下文下，去除主效应后的残留 CTR 证据符号相反，说明“值在哪里”和“值对当前样本意味着什么”是两回事。此外，生产环境数值特征来自不同上游任务，external normalization 需要训练/在线同步，带来额外存储和一致性负担。

### 方法关键点
ScalaRLens 将数值 embedding 分成两部分：
- **稳定坐标**：由 focal scalar 单独决定，使用单调局部 mesh（类似 DEER）进行区间选择和线性插值，context 不参与。训练范围存入 checkpoint，推理直接接受原始尺度，仅做 clipping。
- **上下文响应**：所有 field tokens（数值局部坐标 + categorical embeddings）经 RMS normalization 后，field-specific heads 生成 drive δ 和 gate g；共享低秩 UV 算子进行 T=3 步有界更新，状态始终限制在 [-1,1]^M，无需迭代收敛。
- **数值 readout**：连接 focal coordinate、gate 和所有 transient states，经 SiLU head 输出最终数值 embedding；只替换 numerical embeddings，categorical tokens 和 backbone 保持不变。

### 关键结果数字
在 AutoML-A/E、Criteo 三个数据集上，覆盖 9 个 backbone、19 种表示、3 个种子，共 1539 次运行。原始数值尺度下，ScalaRLens 在 27 个设置中 25 个排名第一，2 个第二（AutoInt），平均 rank 1.074；平均 AUC 较最强 baseline 分别提升 +0.0070 / +0.0037 / +0.0012，Logloss 也最低。共享 z-score 标准化重跑后仍显著优于 DEER (+0.0031)、DAES (+0.0047)、NaryDis (+0.0103)，说明增益不完全是尺度容忍。消融证明 categorical context 可靠、numerical context 辅助，NoNorm/StopGrad/T=1 均带来损失，DEER+Norm 和 LocalMLP 无法复现。受控机制恢复实验显示 focal coordinate 位移恒为 0，而 DAES 在 categorical/numerical/mixed 交互 shift 上 AUC 分别为 0.8296/0.7463/0.7703，ScalaRLens 达到 0.8383/0.7969/0.7983。

最值得记住的一句话：**数值表示应该分离“值是什么”和“值在当前样本中意味着什么”——坐标属于值，响应属于值在上下文中的 pair。**
