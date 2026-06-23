---
title: 'EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic
  Memory'
title_zh: EvoEmbedding：可进化的表示模型，解决长上下文检索与Agent记忆动态匹配
authors:
- Chang Nie
- Chaoyou Fu
- Junlan Feng
- Caifeng Shan
affiliations:
- Nanjing University
arxiv_id: '2606.21649'
url: https://arxiv.org/abs/2606.21649
pdf_url: https://arxiv.org/pdf/2606.21649
published: '2026-06-18'
collected: '2026-06-23'
category: RAG
direction: 可进化嵌入 · 长上下文检索与Agent记忆
tags:
- Evolvable Embeddings
- Latent Memory
- Long-Context Retrieval
- Agentic Memory
- LoRA
- RAG
one_liner: 通过FIFO潜在记忆队列实现可进化的上下文感知嵌入，在长上下文检索和Agent记忆任务上大幅超越静态大模型
practical_value: '- **用户行为序列的动态嵌入**：电商场景中，同一用户在不同时段对同一query的意图不同（如“耳机”先浏览后比价），EvoEmbedding的可进化表示可压缩历史上下文，使召回/排序阶段感知时序变化，避免检索过时信息。可直接用其FIFO潜在记忆队列增量更新用户状态，嵌入维度仅1024，开销低。

  - **多LoRA解耦训练与无损切换**：将记忆更新和表示生成拆分为两个LoRA适配器，基座LLM参数冻结，既避免了灾难性遗忘，又可在推理时按需激活。业务中可借鉴为同一个基座模型同时具备记忆压缩和检索嵌入能力，省去额外部署专用嵌入模型。

  - **长度加权对比损失**：对于电商长序列（如用户全生命周期行为），正负样本数量差异极大且长度悬殊。论文的`log(N+1)`自适应校准因子可稳定训练，避免模型偏向短序列，值得直接移植到用户长序列表示学习。

  - **Segment-Batching加速技巧**：将多个连续片段拼接后并行编码，训练提速3.8倍且性能小幅提升。在处理用户流水数据时，可按时间窗口并行化，平衡效率与效果。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有文本嵌入模型（如Qwen3-Embedding、KaLM-Embedding）对每个文本块独立编码，完全忽略块之间的时序与上下文关联。在长对话、用户记忆等高动态场景中，同一查询在不同时间点的正确答案不同，静态表示会导致检索到过时信息（如会议时间被修改后仍返回旧时间）。这严重制约了RAG在Agent长期记忆中的实用性。

**方法关键点**  
- **可进化嵌入**：维护一个FIFO潜在记忆队列（容量C=512 token），在处理连续文本段时，每段输出K=16个可学习记忆token，经投影后入队，形成动态上下文摘要。查询时联合当前记忆生成上下文感知的嵌入，使得相同query在不同历史阶段产生不同向量。  
- **多LoRA解耦**：记忆更新与向量生成分别用两个独立LoRA适配器，基座LLM参数冻结。既避免灾难性遗忘，又允许推理时灵活切换。训练时通过记忆生成损失（交叉熵，冻结LLM迫使记忆token兼容基座语义空间）和长度加权多正样本对比损失联合优化。  
- **EvoTrain-180K数据集**：三阶段流水线构建18.4万样本，混合长/短上下文、多领域文本（网页、对话、记忆），包含40+模板的语义匹配与复杂推理问答，最大训练长度12K token。  
- **工程优化**：动态Segment-Batching（并行处理k个连续段，总长不超阈值）加速训练3.8倍，长度加权`log(N+1)`平衡不同长度样本的梯度尺度。  

**关键实验**  
在8个长上下文检索基准和2个个性化生成基准上，EvoEmbedding-4B（嵌入维度仅1024）在Overall Recall@10上达80.5，比KaLM-12B高7.8%，比Qwen3-8B高11.1%。在LongMemEval上，只用Top-8片段的简单RAG达到77.6%准确率，超越LightMem（70.2%）等专用记忆系统。作为即插即用模块插入A-MEM等记忆框架时，带来+19.2%的绝对提升。Temporal分析显示模型能根据“firstly/lastly”等时间关键词准确检索到对话开头或结尾片段，t-SNE可视化表明其潜在空间按时间顺序清晰分离。
