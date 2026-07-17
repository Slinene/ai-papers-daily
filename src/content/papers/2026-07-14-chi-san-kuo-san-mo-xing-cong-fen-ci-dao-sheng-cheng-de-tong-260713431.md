---
title: 'Discrete Diffusion Models: A Unified Framework from Tokenization to Generation'
title_zh: 离散扩散模型：从分词到生成的统一框架
authors:
- Ye Yuan
- Weien Li
- Rui Song
- Zeyu Li
- Haochen Liu
- Xiangyu Kong
- Zixuan Dong
- Linfeng Du
- Zipeng Sun
- Weixu Zhang
affiliations:
- McGill University
- Mila - Quebec AI Institute
- MBZUAI
- University of Cambridge
- Salesforce
arxiv_id: '2607.13431'
url: https://arxiv.org/abs/2607.13431
pdf_url: https://arxiv.org/pdf/2607.13431
published: '2026-07-14'
collected: '2026-07-17'
category: Other
direction: 离散扩散模型的设计空间统一化
tags:
- Discrete Diffusion
- Tokenization
- Unified Framework
- Generation
- Parallel Decoding
one_liner: 提出将离散扩散模型视为离散状态空间构建问题的统一框架，揭示设计权衡与未来方向
practical_value: '- 离散扩散模型的并行生成特性可大幅降低推荐列表的推理延迟，适合对实时性要求高的搜索/推荐场景。

  - 框架强调的状态空间设计（分词方案、词汇拓扑）直接影响生成质量：在生成式推荐中，物品ID的离散表示方式（如Semantic ID）可类比为“分词”，其设计应仔细考虑语义连续性与扩散过程中的噪声注入方式。

  - 统一视角提示了训练目标与推理算法的多种组合（如转移矩阵、掩码状态），从业者可以在物品生成任务中尝试不同配置，以平衡生成多样性与保真度。

  - 该框架对扩展性和系统优化的讨论，为大规模推荐系统下离散扩散模型的工程化提供了参考，如KV缓存、批处理策略等。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：自回归模型虽主导离散数据生成，但存在串行解码局限，无法利用并行计算。离散扩散模型（DDM）作为替代方案，能实现并行生成与迭代全局优化。然而，离散扩散模型的性能严重依赖离散状态空间的构建方式（分词方案、词汇表拓扑、领域特定结构），现有研究将这些设计视为孤立的实现细节，缺乏统一视角。

**方法关键点**：本工作提出一个统一概念框架，将离散扩散模型的核心归结为“如何构建离散状态空间”。在该框架下，转移矩阵、掩码/吸收态、基于分数/比率的方法等现有实例都成为公共设计空间中的不同选择。框架进一步梳理了训练目标、推理算法、扩展行为、系统工程与评估协议之间的设计权衡，并整合了系统加速策略，如缓存机制与批处理优化。

**关键结果与启示**：通过统一视角，论文明确了未来值得探索的方向，包括更高效的离散状态空间设计、训练与推理的协同优化，以及评估标准的确立。该框架为离散扩散模型的系统性改进提供了理论基础，尤其对希望在推荐系统中应用生成式模型的做法具有指导意义，提醒研究者关注分词阶段对最终生成效果的决定性影响。
