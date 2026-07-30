---
title: 'Learning from the Future: Privileged Self-Distillation for Sequential Recommendation'
title_zh: 从未来学习：时序推荐的特权自蒸馏
authors:
- Jiakai Tang
- Yang Zhang
- See-Kiong Ng
- Xu Chen
- Wen Chen
- Jian Wu
- Han Zhu
affiliations:
- Renmin University of China
- National University of Singapore
- Alibaba Group
arxiv_id: '2607.27055'
url: https://arxiv.org/abs/2607.27055
pdf_url: https://arxiv.org/pdf/2607.27055
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 序列推荐 · 自蒸馏与特权信息利用
tags:
- Sequential Recommendation
- Self-Distillation
- Privileged Information
- Future Interactions
- Attention Mask
one_liner: 将未来交互作为训练特权信息，通过双视图自蒸馏提升序列推荐性能，不增加推理成本
practical_value: '- 在训练序列推荐模型时，可利用用户完整会话中的后置交互作为特权信息，构建双视图自蒸馏：一个掩码看到未来项（教师），另一个只看历史前缀（学生），共享同一
  backbone，蒸馏后不改变推理模型与成本，适合对延迟敏感的电商场景。

  - 动量平均教师（EMA）和优势可达门控是两个关键稳定性 tricks：EMA 教师参数随学生缓慢更新，避免噪声；可达门控根据历史前缀判断未来项是否可达，自适应加权蒸馏损失，能防止强制学习不可达的未来，可迁移到其他
  teacher-student 蒸馏任务。

  - 该方法可叠加到任意因果注意力序列模型（如 SASRec）上，无需单独预训练教师，端到端单阶段训练，工程实现成本低：仅需在数据加载时保留多步未来，并在 attention
  层插入一个额外的未来感知掩码，适合快速实验。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统序列推荐用下一项作为监督信号，训练时仅建模前缀条件概率，忽视了序列中未来交互蕴含的用户意图演变信息。这些未来交互在训练时可见但推理时不可用，可作为特权信息提供更丰富的相对偏好监督。

**方法**：提出特权自蒸馏（PSD），在同一个序列模型上施加两种注意力掩码：未来感知掩码（教师）能看到目标项之后的若干未来项，产生一个条件于过去和未来的特权分布；前缀掩码（学生）仅看历史前缀，产生用于部署的分布。通过 KL 散度让学生模仿教师的特权分布，将未来交互转化为训练监督而非推理输入。关键设计包括：① 共享 backbone 的自蒸馏，教师优势纯粹来自信息而非架构，无需预训练；② 动量平均教师稳定蒸馏目标；③ 优势可达门控，计算教师分布与仅由前缀可达分布的比值，自适应加权蒸馏损失，避免强制学习历史不支持的未来信号。整个框架单阶段端到端，推理时完全复用原始学生模型。

**结果**：在 Beauty、Sports、ML-1M 等公开数据集和 SASRec、BERT4Rec 等多种 backbone 上，PSD 均带来一致且显著的提升，例如 Beauty 上 HR@10 提升约 5%、NDCG@10 提升约 6%，平均提升 3–5%。消融实验验证了未来视界长度、门控与动量更新的有效性。
