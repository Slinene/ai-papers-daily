---
title: Selective Synergistic Learning for Video Object-Centric Learning
title_zh: 视频对象中心学习的选择性协同方法
authors:
- WonJun Moon
- Jae-Pil Heo
affiliations:
- KAIST
- Sungkyunkwan University
arxiv_id: '2606.15527'
url: https://arxiv.org/abs/2606.15527
pdf_url: https://arxiv.org/pdf/2606.15527
published: '2026-06-13'
collected: '2026-06-22'
category: Training
direction: 视频对象中心学习·选择性对齐
tags:
- Video Object-Centric Learning
- Slot Attention
- Selective Alignment
- Pseudo-labeling
- Linear Complexity
- Object Discovery
one_liner: 提出SSync，通过选择性对齐编码器边界与解码器内部信息，避免错误传播并实现线性复杂度视频对象发现
practical_value: '- 当推荐系统中需要融合互补模块的输出（例如多模态产品表征对齐）时，可借鉴「选择性蒸馏」思想：只从边界清晰的模块传递结构信息、从内部稳定的模块传递语义，避免互相污染。

  - 「传递式伪标签合并」通过时空激活一致性合并重叠槽位，可用于推荐模型中的Embedding冗余压缩，例如将过度相似的物品向量合并，减少线上存储与计算。

  - 线性复杂度的伪标签策略避免了大规模匹配时的平方复杂度，对召回层中相似度计算或聚类算法有直接的效率优化启发。

  - 整体即插即用思路可用于快速实验新的训练激励信号，无需改动原有模型架构即可注入先验知识。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频对象中心学习（VOCL）常用槽（slot）框架，依赖编码器注意力图与解码器对象图两种空间映射。两者特性互补（编码器噪声多但边界清晰、解码器平滑但轮廓模糊），以往密集对齐（全图对比学习）粗暴一致化反而传播缺陷，且时空逐块比对计算复杂度为二次方，难以扩展。

**方法**：提出选择性协同学习（SSync），放弃全量逐块对齐，转为**仅提炼最可靠线索**——用编码器严格提炼边界，用解码器去除内部噪声。具体通过一种**线性复杂度的伪标签机制**实现：基于激活值分布生成可靠边界/内部伪标签，避免平方级的空间比较。同时引入**传递式伪标签合并**，依据时空激活一致性自动合并重叠冗余的槽位，防止架构偏置（如槽重复）被强化。整个模块即插即用，无需改变基础VOCL模型。

**结果**：大量实验表明SSync显著提升对象分解质量，对槽数量配置具有极高鲁棒性，可作为通用增强模块插入多种VOCL方法。
