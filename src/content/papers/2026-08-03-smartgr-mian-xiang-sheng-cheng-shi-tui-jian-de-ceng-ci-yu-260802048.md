---
title: 'SmartGR: Hierarchy and Beam-Aware Knowledge Distillation for Generative Recommendation'
title_zh: SmartGR：面向生成式推荐的层次与束搜索感知知识蒸馏
authors:
- Ziheng Zhang
- Yu Cui
- Bohao Wang
- Yong He
- Chao Yu
- Chuan Yuan
- Wujie Sun
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2608.02048'
url: https://arxiv.org/abs/2608.02048
pdf_url: https://arxiv.org/pdf/2608.02048
published: '2026-08-03'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 层次与束搜索感知蒸馏
tags:
- Generative Recommendation
- Knowledge Distillation
- Semantic ID
- Beam Search
- Prefix Pruning
- Hierarchy-Aware Distillation
one_liner: 提出层次感知SID蒸馏与束感知排序蒸馏，解决生成式推荐中蒸馏难度不均衡和束搜索前缀误剪枝问题。
practical_value: '- **层次感知蒸馏权重**：不要在所有SID层级上均匀施加蒸馏损失；引入可学习的单调递增权重（如tanh），根据教师在不同深度的增益自动调整蒸馏强度，解决层次间难度不均衡问题。

  - **束感知排序损失**：仅对齐每步条件分布无法防止前缀误剪枝；使用教师缓存的 beam 结果构造正负 beam 对，让学生直接模仿教师的累积前缀评分偏好，在训练中显式优化束搜索排序。

  - **离线缓存 + 最长前缀选择**：离线缓存教师 top-k token 分布与 beam 序列，蒸馏时选择与目标 SID 最长公共前缀的 beam 作为监督，避免不相关信号引入噪声；同时保留硬监督损失，维持基础生成能力。

  - **即插即用的蒸馏方案**：不修改学生模型结构，只增加 SID Loss 和 BEAM Loss 两个损失项，即可将 1.7B 模型性能提升 8.6%，推理速度比
  8B 教师模型快 2.39 倍，适合在广告/电商等实时推理要求高的场景直接落地。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式推荐（GR）通过 Semantic ID（SID）和自回归生成实现推荐，大模型虽性能更好但推理成本极高（8B 模型比 1.7B 慢约 60%–90%）。知识蒸馏可将大模型知识迁移到小模型，但现有方法未考虑 GR 特有的两大挑战：① SID 层次间蒸馏难度不均衡——教师模型在更细粒度的深层 SID 上优势更大，统一蒸馏会浪费教师能力；② 束搜索解码时前缀误剪枝——中间前缀得分低会导致最终高排名的 item 被意外丢弃，而单步条件分布对齐无法防范该问题。

**方法关键点**
- **层次感知 SID 蒸馏（Hierarchy-Aware SID Distillation）**：引入可学习的单调递增权重（归一化 tanh 函数），根据 SID 深度自适应调整每层蒸馏强度，深层次给予更高权重，且权重由数据学习。
- **束感知排序蒸馏（Beam-Aware Ranking Distillation）**：从教师缓存的 beam 结果中选择与目标 SID 最长公共前缀的 beam 作为正样本，其下一低分 beam 作为难负样本，计算两者累积前缀分数的 softmax 偏好分布，通过 KL 散度让学生模仿教师的排序偏好。
- **离线缓存与最长前缀选择**：提前缓存教师 beam 的 top-k token 分布和完整 beam 序列，仅对正样本 beam 与目标 SID 重叠的位置施加蒸馏，避免不良监督。
- **与硬监督结合**：总损失 = 自回归硬损失 + λ_SID * SID 损失 + λ_BEAM * BEAM 损失。

**关键结果**
在 Amazon Beauty/Toys、快手广告/视频四个数据集上，从 OneRec-8B 蒸馏到 OneRec-1.7B。SmartGR 在所有 16 项指标上平均提升 8.6%，超过 CD、DLLM2Rec、KD、MiniLLM、SeqKD、LOHRec 等 12 种基线；推理速度是 8B 教师的 2.39 倍。消融显示移除 SID 损失或 BEAM 损失均导致性能下降，且最长前缀选择和仅监督重叠位置的设计至关重要。案例研究表明 SID 损失有效缩小了各层次前缀保留能力的差距，BEAM 损失大幅降低了全局 Top-1 item 的前缀平均排名。

**核心思想**：生成式推荐蒸馏必须同时考虑 SID 层次结构的蒸馏难度差异和束搜索时的前缀排序偏好，仅靠 token 级或 item 级对齐会丢失教师的核心优势。
