---
title: 'MVR-cache: Optimizing Semantic Caching via Multi-Vector Retrieval and Learned
  Prompt Segmentation'
title_zh: 利用多向量检索与可学习提示分割优化语义缓存
authors:
- Ali Noshad
- Zishan Zheng
- Yinjun Wu
affiliations:
- Peking University
- Renmin University of China
arxiv_id: '2605.24914'
url: https://arxiv.org/abs/2605.24914
pdf_url: https://arxiv.org/pdf/2605.24914
published: '2026-05-24'
collected: '2026-05-26'
category: LLM
direction: 语义缓存 · 多向量检索与分割学习
tags:
- Semantic Caching
- Multi-Vector Retrieval
- Prompt Segmentation
- Reinforcement Learning
- Cache Hit Rate
- MaxSim
one_liner: 通过轻量可学习分割模型与多向量检索（MaxSim）提升语义缓存命中率最高37%，并保持理论正确性保证。
practical_value: '- **提高在线LLM服务的缓存命中率**：在对话式电商推荐、Agent辅助客服等场景，采用MVR-cache的分割策略可将语义缓存命中率提升37%，大幅减少重复推理调用，降低延迟与成本。

  - **轻量级分割模型可在线部署**：提出的分割模型仅500–600MB，远小于生产LLM，可作为独立微服务实时分割提示，无显著额外开销，适合电商高并发推理场景。

  - **多向量相似度替代单向量余弦**：借鉴论文的对称MaxSim度量，在缓存或召回系统中用多向量精细匹配，能更好区分表层相似但语义相反的文本，如正/负评论、语义相近但意图不同的Agent指令。

  - **有理论保障的缓存策略学习方法**：论文证明了优化BCE损失即可最大化命中率并控制错误率，并给出RL训练框架，可直接用于需保证安全边界的推荐/客服缓存系统，实现可证明的正确性约束。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有语义缓存大多依赖提示整体向量的余弦相似度来判定是否返回缓存响应。这种粗糙的相似度无法捕捉提示内部的细粒度语义差异，导致语义相悖的文本被误匹配（例如同一主题但褒贬相反），缓存命中率受限且可能返回错误答案。  

**方法关键点**  
- **可学习切分模型**：设计了一个轻量的指针网络（BERT编码器＋MLP投影＋LSTM解码器＋注意力层），将提示按标点等候选位置自适应切分为多个片段，为每个片段生成嵌入，得到多向量表示。  
- **对称MaxSim相似度**：对两个提示的片段集合，先计算单边MaxSim再取双向均值，得到`SMaxSim`，作为更准确的语义相似度量。  
- **理论指导的训练目标**：基于正态假设，证明最小化BCE损失（使相似度与响应一致性标签对齐）等价于在用户指定的错误率约束下最大化缓存命中率。  
- **RL训练解决离散优化**：切分点是离散组合，不可微；将切分模型视为策略网络，用REINFORCE以BCE损失的负值为奖励进行训练，联合更新vCache的阈值参数。  
- **训练数据仅需3K示例**：每个任务只需少量带标签的提示对（由GPT-4o-mini生成答案后字符串匹配获得标签），且切分模型可跨数据集泛化。  

**关键实验与结果**  
- **数据集**：SemCacheClassification（电商文本分类45K）、SemCacheSearchQueries（搜索150K）、PromptBench（问答38K）、QNLI（问答29K）。  
- **基线**：vCache（带正确性保证的动态阈值）、ColBERT（token级多向量）、POQD（用LLM切分查询）。  
- **主要结果**（错误率δ=0.01）：在标准cache-on-miss协议下，MVR-cache的缓存命中率在所有数据集上均优，最高相对提升约25%（PromptBench场景）；在always-cache协议下提升高达37%（SearchQueries）；端到端推理延迟降低最多6%。  
- **泛化**：在PromptBench上训练的切分模型直接用于QNLI，命中率仍超过所有基线。  
- **效率**：切分模型仅500MB，算法额外耗时中位数约10ms/请求，远小于LLM调用。  

**核心贡献总结**  
“MVR-cache通过将提示自适应分裂为多片段、用双向MaxSim度量相似度，并基于RL在正确性保证下优化命中率，首次在语义缓存中实现了细粒度匹配与可证明增益的统一。”
