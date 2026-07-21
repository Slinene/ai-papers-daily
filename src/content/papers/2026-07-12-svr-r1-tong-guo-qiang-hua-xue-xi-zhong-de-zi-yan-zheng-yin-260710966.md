---
title: 'SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement
  Learning'
title_zh: SVR-R1：通过强化学习中的自验证引导多模态推理
authors:
- Mingyuan Wu
- Jingcheng Yang
- Shengyi Qian
- Xudong Wang
- Jize Jiang
- Qifan Wang
- Aashu Singh
- Khoi Pham
- Fei Liu
- Zhaolun Su
affiliations:
- University of Illinois Urbana-Champaign
- Meta
arxiv_id: '2607.10966'
url: https://arxiv.org/abs/2607.10966
pdf_url: https://arxiv.org/pdf/2607.10966
published: '2026-07-12'
collected: '2026-07-21'
category: Reasoning
direction: 多模态推理 · 自验证强化学习
tags:
- multimodal reasoning
- reinforcement learning
- self-verification
- GRPO
- VLM
one_liner: 在RL rollout中嵌入多轮自验证循环，让VLM自我纠正并提升推理准确率，无需外部监督
practical_value: '- 在对话式推荐Agent中，可引入类似的自验证-重试机制：模型生成推荐后自评置信度（Yes/No），低置信时触发二次推理，用RL优化整个过程，提升推荐准确性和用户信任度。

  - 异步多轮rollout框架可借鉴至大规模推荐策略的在线RL训练，支持高效采样和动态停止，降低推理成本。

  - 不依赖外部验证器的二值自验证信号设计，可作为强化学习奖励的辅助项，用于训练推荐Agent的自我纠错能力，在无真实反馈的冷启动场景中尤为有用。

  - 训练过程中模型验证轮次自然减少的现象表明，可将推理阶段的自我验证作为一种正则化机制，最终模型可在部署时跳过验证步骤，加速线上服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前视觉语言模型（VLM）的推理能力可通过强化学习（RL）在特定任务奖励上微调得到提升，但标准RL只奖励最终答案的正确性，未显式利用模型自我验证和修正的潜能。受人类“二次思考”行为启发，提出SVR-R1，旨在将自我验证融入RL训练循环，让模型学会自我纠正。

**方法关键点**：基于GRPO，每个查询模型使用相同权重首先生成答案，并输出一个二值自验证判定（Yes/No）。若判定为“No”，则触发第二次思考重新生成答案；若为“Yes”或达到轮次上限，则最终答案用于计算结果奖励。整个多轮交互过程以异步rollout方式实现，无需外部监督或辅助critic。

**关键结果**：在多个视觉语言推理基准上，SVR-R1相比标准GRPO基线大幅提升准确率。训练动态显示，随着策略优化，模型所需的验证轮次逐渐减少，但测试准确率持续提高，表明模型内化了自我纠正能力，缩小了验证与生成之间的差距。
