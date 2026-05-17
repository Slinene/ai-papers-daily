---
title: 'IdeaForge: A Knowledge Graph-Grounded Multi-Agent Framework for Cross-Methodology
  Innovation Analysis and Patent Claim Generation'
title_zh: IdeaForge：知识图谱驱动的多智能体创新分析与专利生成框架
authors:
- Joy Bose
affiliations:
- Independent Researcher, Bangalore, Karnataka, India
arxiv_id: '2605.13311'
url: https://arxiv.org/abs/2605.13311
pdf_url: https://arxiv.org/pdf/2605.13311
published: '2026-05-13'
collected: '2026-05-17'
category: MultiAgent
direction: 多智能体协作与知识图谱融合创新
tags:
- Knowledge Graph
- Multi-Agent
- Innovation Methodologies
- Convergence Detection
- Patent Generation
- FalkorDB
one_liner: 将创新方法论建模为共享知识图谱上的异构推理算子，通过跨方法论收敛检测提升创意置信度并实现结构化专利生成
practical_value: '- **多代理+知识图谱架构**：在电商推荐等场景中，可分别为用户意图、商品属性、营销策略等设计专用代理，各代理将分析结果写入图谱，通过语义相似度检测交叉收敛，筛选高置信度的推荐，增强可解释性与可追溯性。

  - **收敛检测作为集成信号**：借鉴跨方法论收敛思想，在Agent协作中让多个独立代理从不同角度推理同一问题，输出经向量相似度匹配，一致的方案自动获得更高权重，类似无监督的集成投票。

  - **结构化生成降低幻觉**：专利草案生成直接基于知识图谱子图，推荐结果的解释生成也可从结构化的用户-商品-上下文图提取路径，避免自由式LLM生成的不确定性。

  - **模型无关的设计**：框架使用1.1B小模型即可跑通，证明价值在于图结构化分析而非大模型能力，适合资源受限的工业环境，且可随时替换更大模型提升质量。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现有AI辅助创新系统通常只采用单一方法论（如TRIZ），通过顺序提示产生输出，中间推理状态未持久化，不同方法产生的洞察彼此割裂，无法系统性评估新颖性。IdeaForge针对这一问题，提出将多种创新方法论（TRIZ、设计思维、SCAMPER）作为异构推理算子，在共享知识图谱上协同工作，通过跨方法论收敛检测来增强创新候选的可信度，并实现可溯源的专利生成。

**方法关键点**
- **知识图谱模式**：定义Problem、Contradiction、Principle、Claim等8类节点及8种边关系，核心创新是引入了`CONVERGENT`边，用于连接不同方法论生成的语义相近的Claim。
- **方法论代理**：TRIZ代理识别技术矛盾并选用发明原理；设计思维代理生成用户画像与需求；SCAMPER代理应用七种变换生成创意；先验艺术代理检索arXiv并建立`CHALLENGES`边。所有代理均向同一个FalkorDB图谱写入结构化信息。
- **收敛检测**：嵌入合成代理用句子变换器（all-MiniLM-L6-v2）计算所有Claim对的余弦相似度，跨方法论且相似度≥阈值（默认0.65）则创建`CONVERGENT`边，实现结构三角化。
- **InnovationScore排序**：加权组合收敛边数量、方法论多样性、权利要求强度、先验艺术挑战数，筛选高信度专利候选。
- **专利生成**：专利代理从知识图谱中提取高排名Claim及其支持子图，以此为上下文生成结构化专利草案，而非无约束LLM生成。

**关键实验**
在“印地语语音法律助手”用例上测试，并扩展到医疗、教育、农业、无障碍等共五个领域，使用TinyLlama 1.1B作为底层模型。主要结果：
- 单用例生成16个节点、3个方法论专属Claim，三者之间余弦相似度高达0.817-0.837，全部超过0.65阈值，形成3对收敛。
- TRIZ声明获得最高InnovationScore (0.500)，因其收敛边最多、方法论多样性最高。
- 多领域测试中，4/5的用例达到完全收敛，医疗用例仅一对收敛，表明框架能识别不同方法论间的语义分歧，具备鉴别力。
- 与传统单一方法论基线相比，多方法融合产生的候选声明更丰富、可追溯性更强。

**一句话记忆**
“创新方法论可视为作用于共享知识图谱的异构推理算子；独立算子的收敛是高质量创新信号的原理，通过CONVERGENT边与InnovationScore公式得以量化。”
