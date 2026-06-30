---
title: Grounding LLM Reasoning under Incomplete Graph Evidence
title_zh: 不完整图谱证据下的LLM推理接地理论
authors:
- Jiaqi Li
- Fanghui Song
affiliations:
- Tianjin Normal University
- Harbin Institute of Technology
arxiv_id: '2606.30247'
url: https://arxiv.org/abs/2606.30247
pdf_url: https://arxiv.org/pdf/2606.30247
published: '2026-06-29'
collected: '2026-06-30'
category: Reasoning
direction: LLM推理接地 · 不完整图谱证据
tags:
- Knowledge Graphs
- LLM Reasoning
- Grounding
- Incomplete Evidence
- KL Regularization
- GraphRAG
one_liner: 证明不完整图谱下硬约束无法同时保证拒假和保真，提出KL正则化软接地框架并给出稳定性边界
practical_value: '- **电商知识图谱的软接地**：商品关系图谱常不完备，应避免硬性剪枝。采用KL正则化软约束，保留未被观察但非矛盾的推理路径，防止丢弃正确的长尾关联。

  - **GraphRAG检索策略**：在检索增强生成中，不必强制LLM完全忠实于检索到的子图。允许有限松弛可提高对缺失边的鲁棒性，避免因召回不足而拒真。

  - **Agent多跳推理的稳定性设计**：当Agent基于动态图证据进行多步推理时，可利用稳定性边界评估证据扰动的影响，指导高频更新下的容错机制。

  - **区分事实与声明**：将图谱相容性视为“声明支持”而非事实真理，在广告文案生成或推荐解释中，可避免因信源不完整而误判正确输出。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：知识图谱（KG）常被用来指导LLM推理，但系统实际可见的图是检索、链接、时间约束下的不完整证据快照，而非完整事实。答案正确可能掩盖脆弱的证据路径——模型可能漂移到错误实体、颠倒关系、或编造无支撑的桥接，而正确路径因缺失边而被排除。

**方法**：论文将LLM推理轨迹接地于不完整图证据，定义实体锚点、关系残差、路径能量与支持区域。核心证明：在开放世界不完整性下，不存在仅基于观察状态的硬规则能同时拒绝所有假的无支撑轨迹并保留所有真的但未观察轨迹。进而提出软接地框架，将LLM先验变形为KL正则化后验：有限松弛允许未被观察但非矛盾的轨迹保留支撑，而硬约束视为无限惩罚极限。框架还导出证据扰动下的稳定性界限，并明确适用于GraphRAG、KGQA、图Agent、约束解码等不同约束机制。

**结果**：给出了硬规则的不可能定理，建立了软接地为KL正则化的形式化对应，提供了稳定性量化边界，将KG相容性重新定义为声明性支持而非事实性真值。
