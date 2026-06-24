---
title: 'DREAM: Dense Retrieval Embeddings via Autoregressive Modeling'
title_zh: 密集检索嵌入的自回归建模训练方法DREAM
authors:
- Yixuan Tang
- Yi Yang
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2606.24667'
url: https://arxiv.org/abs/2606.24667
pdf_url: https://arxiv.org/pdf/2606.24667
published: '2026-06-22'
collected: '2026-06-24'
category: Training
direction: 自回归监督的密集检索无对比训练
tags:
- Dense Retrieval
- Autoregressive Modeling
- Contrastive-Free
- LLM Supervision
- Embedding Training
one_liner: 利用冻结LLM的自回归损失作为监督信号，通过注意力注入相似度分数训练密集检索器，无需对比标注。
practical_value: '- **无标注训练检索器**：可利用海量用户行为数据（如点击、加购），通过 LLM 的生成任务（例如预测商品标题下一个 token）提供训练信号，免去构建正负样本对的人工成本。

  - **注意力注入梯度回传**：将检索相似度分数注入冻结 LLM 的注意力头，仅更新检索器即可从生成损失中学习，适合在推荐系统中快速迭代召回模型，无需微调大模型。

  - **端到端梯度通路设计**：可借鉴该架构，用用户行为序列预测任务替代语言建模，构建检索器与 LLM 之间的可微连接，实现联合优化而不破坏 LLM 已有知识。

  - **Agent 检索优化**：在 Agent 系统中，检索上下文直接影响后续动作；DREAM 可利用任务完成信号或环境反馈作为自回归目标，持续在线优化检索器，无需人工标注查询-文档相关度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：密集检索嵌入训练通常依赖对比学习，需大量标注正负文档对，成本高昂。本文探索利用 LLM 的自回归下一个 token 预测目标为密集检索提供监督。直觉：若文档与查询相关，以其为条件应使 LLM 更容易预测目标输出。

**方法**：提出 DREAM，将检索器生成的查询-文档相似度分数注入冻结 LLM 的选定注意力头。训练时，这些分数决定每个候选文档获得的注意力权重，LLM 预测目标输出的损失通过注意力机制反向传播梯度，仅更新检索器参数，LLM 保持冻结。整个过程无需显式正负标注，检索器直接从 LLM 的预测损失中学习语义匹配。

**结果**：在 BEIR 和 RTEB 基准上，使用 0.5B 至 3B 参数的嵌入骨干，DREAM 一致超越现有基线方法，验证了自回归建模替代对比学习训练密集检索器的有效性。
