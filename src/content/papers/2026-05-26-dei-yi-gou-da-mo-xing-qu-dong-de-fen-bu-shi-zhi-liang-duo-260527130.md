---
title: 'DEI: Diversity in Evolutionary Inference for Quality-Diversity Search'
title_zh: DEI：异构大模型驱动的分布式质量多样性进化搜索
authors:
- John Donaghy
- Shikhar Rastogi
affiliations:
- Gensyn
arxiv_id: '2605.27130'
url: https://arxiv.org/abs/2605.27130
pdf_url: https://arxiv.org/pdf/2605.27130
published: '2026-05-26'
collected: '2026-05-27'
category: MultiAgent
direction: 分布式进化搜索 · 异构LLM协作
tags:
- Quality-Diversity
- LLM
- Evolutionary Search
- Distributed
- Heterogeneous Ensembles
- Asynchronous Communication
one_liner: 通过异步通信将异构LLM作为变异算子协同进化，在同等算力下实现覆盖率+28%、QD得分+124%。
practical_value: '- **创意生成的多样性互补**：在生成式推荐或广告素材生产中，可部署多个异构LLM（如不同家族或规模的模型）作为变异算子，利用各自不同的生成先验覆盖更广的创意空间，提升推荐列表或商品描述的新颖性与覆盖率。

  - **异构节点的异步协同**：参考其无同步屏障的gossip通信设计，推荐系统可混合使用云端大模型和本地小模型进行候选生成，通过异步共享精英解，低延迟节点无需等待慢节点，提升整体吞吐和多样性。

  - **模型多样性的因果验证**：实验严格保持总LLM调用预算不变，证明了收益来自模型多样性而非额外算力。这提示在A/B测试或多臂老虎机中，可刻意引入不同模型家族的先验探索不同用户分群，再通过合并archive实现全局最优。

  - **多智能体对抗压力引入**：在对话推荐或谈判Agent场景中，可让不同LLM Agent扮演推荐者和挑战者，通过类似Red Queen的对抗压力持续提升策略鲁棒性，避免单一模型自博弈的退化。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现有LLM驱动的进化搜索（如FunSearch、Digital Red Queen）均使用单一模型作为变异算子，其固有的归纳偏置导致搜索多样性不足，在质量-多样性（QD）档案中留下永久盲区。为克服这一局限，本文提出DEI（Diversity in Evolutionary Inference），显式利用不同LLM之间的生成先验差异，通过分布式协同实现更广泛的探索。

**方法关键点**  
- **异构模型分配**：将多个不同家族的LLM（如GPT-5.4-mini、Claude Sonnet 4.6等）分别部署为独立搜索节点，每个节点运行本地MAP-Elites优化器，以其专属LLM作为变异算子。  
- **异步冠军共享**：各节点每轮结束时通过gossip协议广播其最优解（冠军），同时异步接收其他节点的冠军，无需同步屏障，允许不同延迟的硬件（如本地开源模型与云端大模型）共同参与。  
- **跨模型对抗压力**：接收到的外来冠军被加入本地对手池，形成跨模型的红皇后压力；同时被播种到本地档案的空缺行为单元格中，带来生态位新颖性。  
- **算力控制**：总LLM调用预算保持恒定（四节点×62次≈单节点250次/轮），确保性能提升归因于多样性而非额外算力。

**关键结果**  
在Core War编程对战环境中，以MAP-Elites的QD-Score、档案覆盖率以及泛化性为指标：  
- 异构集成（4种模型）的合并档案QD-Score达到45.90，比单节点基线（20.46）提升 **+124%**，覆盖率从63.0%提升至 **80.6%**（+28%）。  
- 在相同计算预算下，异构集成在泛化性上全面优于同质集成（四个节点同模型）和单节点，验证了模型多样性而非简单并行的驱动作用。  
- 异步通信设计使慢节点不会拖累整体进度，添加慢速本地模型仍能提升档案覆盖率。  

**核心断言**  
**“模型多样性，而非仅仅并行，应成为分布式LLM搜索的一阶设计原则。”**
