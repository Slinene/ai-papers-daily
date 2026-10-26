---
title: Knowledge Distillation across Item and Code Spaces for Parallel Generative
  Recommendation
title_zh: 跨 item 与 code 空间的并行生成式推荐知识蒸馏
authors:
- Yixuan Xu
- Hailin Liu
- Linxiang Peng
- Can Yang
affiliations:
- The Hong Kong University of Science and Technology
- University of Science and Technology of China
arxiv_id: '2610.32943'
url: https://arxiv.org/abs/2610.32943
pdf_url: https://arxiv.org/pdf/2610.32943
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · 知识蒸馏跨 item/code 空间
tags:
- Knowledge Distillation
- Semantic ID
- Generative Recommendation
- Parallel Decoding
- Sequential Recommendation
- Cross-space Distillation
one_liner: 用 item 空间分布匹配和 code 边际匹配两个蒸馏目标，把序列模型的软分布迁移到并行语义 ID 推荐器
practical_value: '- 已有并行 SID 生成式召回/排序模型（如 RPG、AsymRec）只吃 hard label，可以低成本引入预训练 SASRec
  之类的 item 级 teacher 做软标签蒸馏，线上推理不增加 teacher，只换训练目标。IDM 提 Recall，CMM 提 NDCG，可按业务指标侧重选择。

  - 跨 space 投影实现简单：用固定 item-to-code 分配矩阵 M_h，正向 M_h 聚合 student 各 head logits 成 item
  分数，反向 M_h^T 聚合 teacher item probs 成每个 code position 的 marginal，代码量小、可复用。

  - 训练时注意 loss 尺度：hard label 和蒸馏 loss 梯度范数差异大，先用若干 batch 计算两者梯度 L2 范数比的中位数做系数校准，再加线性
  ramp 逐步引入蒸馏，能避免训练初期的破坏性梯度。

  - 若要同时拿召回和排序收益，建议分别训练 IDM 和 CMM 两个学生，线上做 score-level fusion（如 0.5/0.5），比 joint training
  更稳；teacher temperature 用原始分布即可，不要提前做温度平滑或锐化。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
并行 SID 生成式推荐模型（如 RPG、AsymRec）只对 observed next item 的 code 序列做 hard label 训练，每个 head 只看到 one-hot，缺少对 alternative items 的分布信息。与此对应，传统序列推荐模型（SASRec）能给出 history-conditioned 的 item 级概率，但 teacher 在 item 空间、student 在并行 code 空间，如何跨空间迁移软分布是一个未被解决的问题。

**方法关键点**  
- 用固定 item-to-code 分配矩阵 M_h 连接两个空间：student 的并行 code logits 可聚合为 catalogue 级 item 分数，teacher 的 item 概率可投影为每个 code position 的 marginal。
- **IDM**：将 student 的 code 概率按 item 的 SID 做 geometric mean，再过 catalogue softmax 得到 item distribution，用 soft cross-entropy 匹配 teacher；梯度由 catalogue-induced marginal 驱动，倾向召回。
- **CMM**：用 M_h^T 把 teacher item 分布投影成每个 head 的 code marginal，用 head-wise KL 对齐；直接监督每个并行 head，倾向排序。
- 理论分析：两者共享 teacher 诱导的 code marginal，差异在于 student-side normalization——IDM 在 N 个 item 上归一化，CMM 在每个 head 的 K 类上独立归一化。
- 训练目标为 hard label + λ_m w(t) L_m，w(t) 线性 ramp，λ_m 通过 hard/soft 梯度 L2 范数比中位数校准。

**关键结果数字**  
在 Amazon Beauty、Toys、Sports 三个数据集上，IDM 平均提升 R@10 +15.39%，CMM 平均提升 NDCG@10 +8.28%，均显著优于 hard-label AsymRec 及所有基线。消融显示非均匀 soft distribution 优于 top-1 和均匀平滑；48 个 head 全覆盖优于只监督 16/32 个残差 level。teacher 训练数据越多越好，temperature 不缩放最好，所有正蒸馏强度都能提升 Recall，但 NDCG 对强度敏感。IDM 与 CMM 的 score-level fusion 能进一步提升 NDCG，优于联合训练。

最值得记住的一句话：固定 item-to-code 映射提供了天然的跨空间蒸馏桥梁，IDM 用 item 空间重建分布提召回，CMM 用 code-marginal 空间对齐提排序，加上梯度校准和 ramp 是实现稳定迁移的关键。
