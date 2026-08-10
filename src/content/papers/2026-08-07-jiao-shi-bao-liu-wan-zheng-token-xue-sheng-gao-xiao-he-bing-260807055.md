---
title: 'Teacher Retains Full Tokens, Student Merges Efficiently: TM20K for E-Commerce
  Sequence Modeling in Ad Recommendation'
title_zh: 教师保留完整Token，学生高效合并：面向广告推荐的电商序列建模TM20K
authors:
- Xinchun Li
- Duoru Zheng
- Wenlin Zhao
- Ziyi Zhou
- Jingxuan Tan
- Huizhi Yang
- Linlan Chen
- Dongjian Wang
- Dongyue Wang
- Xiaosong Li
affiliations:
- ByteDance
arxiv_id: '2608.07055'
url: https://arxiv.org/abs/2608.07055
pdf_url: https://arxiv.org/pdf/2608.07055
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 超长序列建模 · 知识蒸馏 · Token合并
tags:
- Ultra-long sequence
- Token merge
- Knowledge distillation
- Full attention
- Ad recommendation
- E-commerce
one_liner: 通过全注意力和两阶段蒸馏，用三种Token合并将电商序列扩展到20K，在线广告收入提升1.036%，延迟仅增5.6%
practical_value: '- **Token合并三策略可直接复用**：相同商品ID局部合并（LITM）可聚合短时间窗口重复行为，去噪并减少序列长度；位置自适应合并（PATM）对近期行为保留完整，对远期行为激进压缩，符合兴趣衰减现实；层间金字塔合并（LPTM）让底层用长序列提取细粒度，上层用短序列做高层抽象，这种分层压缩在Transformer中容易实现。

  - **两阶段蒸馏框架适合工业超长序列落地**：让昂贵的教师模型只训练一次，不参与在线推理，将计算开销剥离；学生模型用廉价Token合并压缩序列，通过蒸馏恢复大部分精度，突破了长序列的效率瓶颈。

  - **全注意力优于目标注意力**：实验证明在20K电商序列上全注意力AUC比目标注意力高约0.25%，且GPU利用率更高，说明序列内交互对预测很重要，不应只用目标-序列注意力。

  - **工程实现技巧**：LITM和PATM在CPU上合并原始特征而非嵌入，避免GPU-CPU带宽瓶颈；QK Norm可稳定超长序列训练；Stack Sequence重新排列变长序列的token以减少无效padding，节省显存约10GB。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业广告推荐中，超长电商行为序列（如20K）能提升CTR/CVR预测效果，但训练和推理效率急剧恶化：训练时间3.5倍，显存增加49GB，推理延迟6.3倍。现有方案或基于检索/聚类压缩丢失细粒度信息，或采用轻量注意力（如只做目标-序列交互）未能充分提取序列内依赖。本文目标是保留全注意力（FA）的有效性，同时让长序列可高效落地。

**方法**：设计TM20K框架，含一个仅训练一次的教师模型和多个用于在线推理的学生模型。教师使用全注意力处理完整20K序列Token，不进行任何压缩。学生模型则通过三种简单但动机明确的Token合并策略大幅压缩序列长度：
- **LITM**：将相同商品ID在短窗口内（如连续3次内）的Token连续求和合并，聚合重复行为；
- **PATM**：按位置分段，近期Token几乎不合并，远期Token用更大的合并因子，例如[1,1000]不合并，[10001,20000]每4个Token合一；
- **LPTM**：在Transformer层间逐步合并，每两层将序列Token数减半，底层处理较长序列，上层处理短序列。
合并后的学生序列从平均8.8K降至1.8K，训练吞吐量接近5K基线。学生通过教师logits进行知识蒸馏，额外添加蒸馏塔与主塔分离，蒸馏损失权重设为50以匹配CE损失尺度。

**关键结果**：在字节跳动电商广告真实数据上，学生模型TM20K-S单独使用合并策略，AUC较5K全注意力基线提升+0.15%，吞吐量仅下降5%；经过蒸馏后提升至+0.22%，接近教师模型的+0.26%。在线A/B测试中，广告主评分（ADSS）提升+1.036%，推理延迟仅增加5.6%。消融表明三种合并策略叠加导致的AUC损失仅0.11%，证明合并策略在保留关键信息上的有效性。

**核心结论**：在广告推荐中，通过“教师保留全Token训练，学生高效合并+蒸馏”的范式，可以接近无损地将行为序列从5K扩展至20K，在极低延迟代价下获得显著业务收益。
