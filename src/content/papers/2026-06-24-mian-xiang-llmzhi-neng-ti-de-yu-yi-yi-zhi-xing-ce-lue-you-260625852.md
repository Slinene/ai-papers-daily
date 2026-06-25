---
title: Semantic Consistency Policy Optimization for Reinforcement Learning of LLM
  Agents
title_zh: 面向LLM智能体的语义一致性策略优化
authors:
- Peng Xu
- Sijia Chen
- Junzhuo Li
- Xuming Hu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2606.25852'
url: https://arxiv.org/abs/2606.25852
pdf_url: https://arxiv.org/pdf/2606.25852
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: LLM Agent强化学习的信用分配优化
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- Group-based RL
- Reward Shaping
- Semantic Consistency
one_liner: 提出SCPO，利用成功兄弟轨迹的语义对齐为失败步骤赋予正向信用，缓解群组RL中的信用不一致
practical_value: '- 在多轮对话推荐Agent训练中，失败对话里的部分有效步骤（如正确追问偏好）可通过语义一致性奖励得到正反馈，提升样本效率。

  - 工程实现上，仅需添加一个轻量的句子嵌入模型计算步骤间语义相似度，无需训练价值网络，可无缝接入现有GRPO/DAPO等群组RL管线。

  - 对于搜索/推荐中需多步决策的长周期任务，可用SCPO对中间步骤进行更细粒度的信用分配，避免仅凭最终转化给奖励导致的训练不稳定。

  - 失败轨迹的语义相似度阈值与权重可作为超参调节，控制探索与利用的强度，适配不同稀疏程度的业务场景。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：群组RL（如GRPO）在训练LLM Agent时，将步骤级信用完全绑定于轨迹最终成功/失败。语义几乎相同的中间步骤会因所处轨迹的结局不同而收到相反的信用信号，导致梯度冲突，并浪费失败轨迹中已取得的正确进展。

**方法**：SCPO是一种无值奖励塑形技术。对于每个失败轨迹，寻找同组中语义相近的成功轨迹作为“兄弟”，计算失败步骤与兄弟步骤的嵌入余弦相似度。当相似度超过阈值时，为失败步骤添加正向信用，鼓励模型沿成功路径学到的进展方向探索。该方法不引入价值网络，仅在群组优势估计后修改奖励。

**结果**：在ALFWorld和WebShop上，SCPO以1.5B模型达到93.7%和74.8%成功率，显著优于RLOO、GRPO等强基线。增益集中在需要多步推理和纠偏的困难任务上，验证了语义一致性信用分配对长周期稀疏奖励任务的有效性。
