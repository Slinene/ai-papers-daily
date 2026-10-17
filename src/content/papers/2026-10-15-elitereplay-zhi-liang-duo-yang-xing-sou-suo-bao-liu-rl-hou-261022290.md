---
title: 'EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity
  Search'
title_zh: EliteReplay：质量多样性搜索保留 RL 后训练中的多样解
authors:
- Hanane Nour Moussa
- Doeun Lee
- Sachin Kumar
affiliations:
- The Ohio State University
arxiv_id: '2610.22290'
url: https://arxiv.org/abs/2610.22290
pdf_url: https://arxiv.org/pdf/2610.22290
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: LLM RL 后训练多样性保持
tags:
- RLVR
- GRPO
- Quality-Diversity
- Text-to-SQL
- Post-training
- Diversity Preservation
one_liner: 用质量多样性搜索构建精英解档案并与 GRPO 结合回放，提升准确率同时保留 LLM 解多样性
practical_value: '- 在 RL 微调用于搜索排序、query 改写或商品文案生成时，可引入**精英档案回放**：先用冻结模型采样多样正确解建立档案，训练中与策略梯度损失共同优化，避免模型只集中在少数高奖励行为，保持生成模式的多样性。

  - 将**质量多样性搜索**作为通用记忆库机制，在 RL 训练中周期性回放高质量多样样本，可缓解模式坍缩与灾难性遗忘，适用于需要多策略并存的推荐或 Agent
  协作场景。

  - 评测中除了准确率，加入 **pass@k 和 U@k（distinct correct strategies）** 两类指标，能更全面反映模型在多解场景下的能力；在搜索建议、歧义
  query 改写等业务中，覆盖多个正确意图比单一 top-1 更重要。

  - 对歧义 query（如 AmbiQT）的覆盖能力可以直接迁移到电商搜索/推荐：用多样性保持的后训练模型同时召回多个可能的商品意图或生成多个改写 query，提升用户体验与召回覆盖。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：RLVR（如 GRPO）已成为 LLM 推理任务的标准后训练手段，但会带来“行为锐化”效应，使模型只输出少数高概率解，丧失基座模型原有的解多样性。现有缓解方法往往优化不能反映正确解多样性的指标，难以真正保留多个优质解法。

**方法关键点**：提出 **EliteReplay**，将 GRPO 与基于质量多样性搜索构建的“精英档案”结合。训练前，用冻结的基座模型采样大量解，按语义或行为相似度分箱，保留每个箱内最高质量的解，形成覆盖不同解法的档案；训练时，除 GRPO 策略损失外，加入对档案中样本的回放损失，强制模型不遗忘并继续生成多样正确解。

**关键结果**：在多个 text-to-SQL 任务（BIRD 分布内、Spider 分布外等）上，EliteReplay 取得最高的 pass@128，相比最强基线多产生最多 77% 的不同正确策略；在策略保留率上显著优于现有方法，能保留大部分基座模型的正确策略；在 AmbiQT 歧义问答上，覆盖两种解释的频率接近最强基线的两倍，验证了多样性带来的实际收益。
