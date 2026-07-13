---
title: 'WILDTRACE: Benchmarking Natural Evidence Trails in Long-Context Reasoning'
title_zh: WILDTRACE：长上下文自然证据链推理基准
authors:
- Zixin Chen
- Peng Liu
- Haobo Li
- Rui Sheng
- Jianhong Tu
- Xiaodong Deng
- Fei Huang
- Kashun Shum
- Dayiheng Liu
- Huamin Qu
affiliations:
- Hong Kong University of Science and Technology
- Alibaba Group
arxiv_id: '2607.09328'
url: https://arxiv.org/abs/2607.09328
pdf_url: https://arxiv.org/pdf/2607.09328
published: '2026-07-10'
collected: '2026-07-13'
category: Reasoning
direction: 长上下文推理 · 自然证据几何结构
tags:
- Long-Context Reasoning
- Benchmark
- Evidence Integration
- Causal Reasoning
- Multi-hop QA
one_liner: 从真实事故报告与小说中抽取文档内在的因果、时序证据链，构建多步推理基准，揭示长上下文模型的整合推理短板
practical_value: '- 在电商长文档分析（如商品详情聚合、售后纠纷报告）中，可借鉴其“源端优先”证据链抽取思路，利用文档目录、因果提示自动构建多跳推理样本，低成本生产高质量微调数据。

  - 对于搜索/推荐系统中的复杂用户意图理解，可设计类似的反事实分支（counterfactual branching）测试，评估模型在用户行为序列中识别因果归因的能力，而非仅靠相关性。

  - 若构建 RAG 或 Agent 工作流，需要在检索后增加“证据缝合”步骤，显式建模段落间的因果、时序关系，而不是简单拼接 Top-k 片段；可参考文中七种几何结构设计中间推理链。

  - 评估长上下文模型时，采用“证据隐藏”条件（withheld evidence）来检测模型是否真正理解文档内在逻辑，避免模型仅凭表层词匹配或位置线索蒙对答案，对业务中的可靠性测试有参考价值。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有长上下文基准多依赖人工植入事实（needle probe）或逆向工程链，与真实文档分布不一致，无法衡量模型对文档自身逻辑的整合推理。该工作旨在填补这一空白，构建完全源自文档内在因果、时序和叙事逻辑的推理任务。

**方法关键点**：从214篇自然长文档（事故报告与冷门文学叙事）中，利用Pearl因果层级及多跳推理分类，定义七种“证据几何结构”（如因果归因、反事实分支、时序汇聚等）；采用源端优先构造流程，先利用文档结构挖掘候选证据链，再撰写问题，并进行多阶段验证（线索必要性、答案扎根性、抗污染等），最终得到481个高质任务。

**关键结果**：18个前沿系统在证据隐藏条件下评估，最强模型仅达75.3%，在反事实分支、因果归因等推理密集的任务上表现尤弱；模型仍主要依赖信息检索而非深层证据融合，表明长上下文推理能力远未饱和。
