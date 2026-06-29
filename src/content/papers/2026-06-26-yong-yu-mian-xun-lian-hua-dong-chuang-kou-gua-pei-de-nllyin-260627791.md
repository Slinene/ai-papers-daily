---
title: NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window
  Adaptation
title_zh: 用于免训练滑动窗口适配的NLL引导全注意力层选择
authors:
- Qiong Tang
- Xiangkun Hu
- Xiangyang Liu
- Yiran Chen
- Yunfan Shao
affiliations:
- Analemma
arxiv_id: '2606.27791'
url: https://arxiv.org/abs/2606.27791
pdf_url: https://arxiv.org/pdf/2606.27791
published: '2026-06-26'
collected: '2026-06-29'
category: LLM
direction: 长上下文推理效率优化
tags:
- Hybrid Attention
- Sliding Window
- Layer Selection
- Training-Free
- Long Context
- Negative Log-Likelihood
one_liner: 提出用答案标记的负对数似然下降来指导层选择，仅1/4全注意力层即接近1/2的精度
practical_value: '- 对于需要长上下文的电商对话Agent或多文档RAG，可部署混合注意力模型，用该方法离线校准选择保留全注意力的层，显著降低推理延迟和KV
  cache开销

  - 校准只需在目标数据集上计算每层用滑动窗口后的NLL下降，耗时约15分钟，无需训练，可快速适配新模型或新任务

  - 该方法不依赖特定模型架构，可广泛应用于各种Hybrid Attention模型，灵活调整计算预算

  - 在Agent设计中，若需要平衡长期记忆与推理效率，该层选择策略可作为推理成本的精细控制手段'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：混合全注意力与滑动窗口注意力的模型能高效处理长上下文，但如何选择哪些层保留全注意力一直缺乏有效方法。现有固定周期模式或基于注意力的启发式，都未直接衡量对下游任务的影响。

**方法**：提出NLL引导的层选择，无需训练。逐层将全注意力切换为滑动窗口，计算在答案标记上的负对数似然下降（degradation），以此量化该层对长距离依赖的重要性。选择degradation最大的若干层保留全注意力，其余用滑动窗口。

**结果**：在LongMemEval上，Qwen3-4B仅用1/4全注意力层达到64.6%准确率，与1/2全注意力层的65.0%相当，计算量减半。比周期性1/4-FA基线高10.4个百分点，比LightTransfer式基线高26.4个百分点。消因分析证实信号来自长距离注意力需求而非通用层敏感性。一次校准仅需约15分钟，大幅推进效率‑精度前沿。
