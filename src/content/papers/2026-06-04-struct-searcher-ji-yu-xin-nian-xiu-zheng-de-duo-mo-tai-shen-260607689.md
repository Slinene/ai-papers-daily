---
title: 'Struct-Searcher: Agentic Structural Thinking Advances Multimodal Deep Information
  Seeking'
title_zh: Struct-Searcher：基于信念修正的多模态深度检索结构思维框架
authors:
- Fan Zhang
- Vireo Zhang
- Shengju Qian
- Haoxuan Li
- Zheng Lian
- Hao Wu
- Yuan Gao
- Xinyu Geng
- Xin Wang
- Pheng-Ann Heng
affiliations:
- CUHK
- LIGHTSPEED
- PKU
- Tongji University
- THU
arxiv_id: '2606.07689'
url: https://arxiv.org/abs/2606.07689
pdf_url: https://arxiv.org/pdf/2606.07689
published: '2026-06-04'
collected: '2026-06-10'
category: Agent
direction: 多模态深度检索 · 信念修正 · 结构化思维
tags:
- Multimodal
- Deep Research
- Belief Revision
- Structural Graph
- Agentic Workflow
one_liner: 提出结构思维范式，以多模态结构图显式管理冲突证据，实现跨模态冲突感知的深度信息检索，平均提升17.2%准确率。
practical_value: '- **冲突消解可借鉴结构图**：在电商多模态商品信息（如详情图与评价视频矛盾）中，可构建假设–证据图，用支持/反驳关系驱动信息筛选，避免线性证据累积导致的错误传播。

  - **可解释的校验链**：MSG 显式记录 Goal → Hypothesis → Evidence 的依赖与验证链路，便于追踪 Agent 推理过程，适合对答案质量要求高的搜索、客服等场景。

  - **即插即用与模型无关**：框架对 Backbone 不敏感，在 GPT-4o 到 GPT-5 等 5 种模型上均稳定提升，可直接嵌入现有 VLM 驱动的
  Agent 管线。

  - **并行探索与剪枝**：对歧义输入（如商品模糊图）可并行生成竞争假设并验证，通过冲突证据即时剪枝，减少级联错误，可迁移到需要多跳推理的推荐解释或生成式推荐流程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有深度信息检索 Agent 大多遵循证据累积范式（EAM），线性堆叠多模态证据，缺乏对跨模态冲突（如文本描述与图片内容不一致）的机制化处理，容易在歧义或矛盾信息上积累错误。多模态检索从文本向图文混合演进，冲突问题日益突出，需要一种从“证据累积”转向“信念修正”的范式革新。

**方法关键点**：
- 基于 AGM 信念修正理论，提出 **Struct-Searcher** 框架，维护一个显式的多模态结构图（MSG）。
- MSG 包含四种节点：Query、Goal、Hypothesis、Evidence，以及 decompose、generate、require、support、refute 等有向关系。
- 工作流程由四个图操作驱动：Construct（分解目标）、Populate（工具召回证据）、Verify（假设验证与信念修正）、Prune（剪枝冲突分支）。
- 信念状态更新遵循 AGM 扩张/ revision 公式：支持则扩张，反驳则修正（撤回旧假设并引入否定）。
- 最终答案从最大无冲突子图中线性化生成，确保全局逻辑一致性。
- 工具编排支持图像搜索、网页搜索、爬取、图像/文本分析等，并行执行独立目标。

**关键实验**：
- 数据集：MM-BrowseComp（224题）、HLE-VL（330题）、BrowseComp-VL（399题），均为多模态深度搜索基准。
- 对比基线：GPT-4o、GPT-5、o3、Gemini-2.5-Pro、多种开源 Agent（WebDancer、Flash-Searcher 等）。
- Struct-Searcher (GPT-5) 在三个数据集上均取得 SOTA：MM-BrowseComp 准确率 32.7%（相对第二提升 3.7%）、HLE-VL 17.3%（提升 1.5%）、BrowseComp-VL 48.6%（提升 0.7%）。
- 在 5 种 backbone 模型上平均性能增益 17.2%，验证了模型无关性；相比于线性 ReAct 和并行 Flash-Searcher，结构化工作流在所有基准上均领先。
