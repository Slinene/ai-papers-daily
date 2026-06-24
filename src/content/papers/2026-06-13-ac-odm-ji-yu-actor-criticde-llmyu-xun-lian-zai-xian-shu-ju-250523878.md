---
title: 'AC-ODM: Actor--Critic Online Data Mixing for Sample-Efficient LLM Pretraining'
title_zh: AC-ODM：基于Actor-Critic的LLM预训练在线数据混合
authors:
- Jing Ma
- Chenhao Dang
- Mingjie Liao
affiliations:
- BRAIN, Renmin University of China
- Shanghai Jiaotong University
- Shanghai Artificial Intelligence Laboratory
- China Electronics Technology Group Corporation 15th Research Institute
- LiblibAI
arxiv_id: '2505.23878'
url: https://arxiv.org/abs/2505.23878
pdf_url: https://arxiv.org/pdf/2505.23878
published: '2026-06-13'
collected: '2026-06-24'
category: Training
direction: RL指导预训练数据混合 · Actor-Critic
tags:
- Data Mixing
- Actor-Critic
- Reinforcement Learning
- Pretraining Efficiency
- LLM
one_liner: 提出轻量Actor-Critic在线调控领域采样权重，最大化梯度建设性干涉，大幅加速预训练并提升下游表现
practical_value: '- **动态数据采样策略可迁移至推荐模型训练**：在多任务/多领域推荐场景中，常需平衡样本配比，AC-ODM的在线Actor-Critic框架可以低开销地学习每步采样权重，替换静态或启发式配比，提升训练效率。

  - **Proxy模式节省大规模训练成本**：先在小规模模型上训练数据混合策略，再外推到大模型，适用于电商搜索推荐中从蒸馏模型到全量模型的迭代过程，避免直接在大模型上试错。

  - **极低工程开销**：每步仅增加0.4%计算和2%显存，几乎不影响吞吐，可直接嵌入现有分布式训练管线，适合对训练延迟敏感的业务。

  - **最大化梯度建设性干涉的思想可泛化**：该文理论证明策略等价于线性代理优化梯度干扰，这一思想可借鉴到多任务推荐中的损失加权或正负样本均衡，减少有害梯度冲突。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM预训练数据配比直接影响泛化能力，现有动态混合方法要么计算开销大，要么无法灵活适应多样训练流程，且难以在样本效率与结构灵活性间平衡。本文从强化学习视角重新定义数据混合，将其建模为智能体动态调整领域采样权重的决策问题。

**方法**：提出AC-ODM，包含一个参数化的Actor策略（线性投影层）和Critic价值评估，以每步训练状态（如损失、梯度）为状态，输出下一批次的领域采样概率。理论证明该策略等价于最大化梯度建设性干涉的线性代理。支持两种模式：
- **Proxy模式**：在小型模型上学得策略，冻结后迁移至大模型，适合固定语料库。
- **Non-proxy模式**：从头端到端训练，策略与LLM同步更新。
框架极轻量：策略网络仅需少量参数，每步额外耗时0.4%、显存增2%。

**结果**：在Pythia-1B上，AC-ODM用少66%的步数达到最优验证困惑度，MMLU准确率相对提升27.5%，HumanEval pass@1达2.23倍。在多个架构和规模上一致优于静态混合及竞争性动态基线，且对超参数鲁棒。
