---
title: 'UEmbed: Unified Sparse and Dense Multimodal Embeddings'
title_zh: UEmbed：统一稀疏与密集的多模态解码器嵌入模型
authors:
- Tingyu Song
- Mingxin Li
- Yanzhao Zhang
- Dingkun Long
- Pengjun Xie
- Zhijie Nie
- Yilun Zhao
- Shu Wu
affiliations:
- CASIA
- Alibaba Group
- University of Chinese Academy of Sciences
- Yale University
arxiv_id: '2608.02583'
url: https://arxiv.org/abs/2608.02583
pdf_url: https://arxiv.org/pdf/2608.02583
published: '2026-08-02'
collected: '2026-08-04'
category: RecSys
direction: 多模态嵌入 · 统一稀疏密集检索
tags:
- Sparse Retrieval
- Dense Retrieval
- Decoder-only
- Multimodal
- Unified Embedding
- MLLM
one_liner: 首次在纯因果解码器架构中同时产出稀疏词汇表示与密集语义向量，统一多模态检索。
practical_value: '- **稀疏-密集统一表示**：单一 MLLM 前向可同时获得稀疏词袋与密集向量，无需额外模型，可直接用于召回-排序联合优化，降低延迟。

  - **因果模型兼容 vLLM 等高效推理框架**：由于保持纯因果注意力，稀疏向量的生成可直接融入现有自回归服务栈，降低工程迁移成本。

  - **k-means 词汇划分与 FLOPS 正则**：该方法中的词表分割策略可迁移至电商商品标题或描述的关键词扩展，提升查询与商品的词汇匹配粒度；FLOPS
  正则保证稀疏激活可控，避免膨胀。

  - **Agent 搜索成本节约**：在 deep research 类场景中，稀疏表示让 Agent 用更少的搜索轮次达成相近召回，直接降低工具调用开销，可参考用于导购
  Agent 的关键词检索。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有 Learned Sparse Retrieval (LSR) 方法几乎都建立在双向编码器（如 BERT）之上，无法利用现代大语言模型（LLM）因果注意力架构的优势，而且多模态 LSR 需额外跨模态模块，扩展性差。同时，稀疏检索在可解释性、效率与倒排索引兼容性上仍优于密集检索，但一直缺乏与 MLLM 原生统一的可能性。因此，亟需一种在因果解码器中同时产出高质量稀疏与密集表示的方法。

**方法关键点**：
- **架构**：在 decoder-only 多模态大模型（Qwen3.5）输入末尾追加 N=16 个可学习的特殊 token，每个 token 负责词表的一个不相交子集；词表通过 k-means 语义聚类分割，使每个特殊 token 成为“topic specialist”。
- **稀疏头**：每个特殊 token 的隐藏状态通过线性投影生成各自子集内词汇的权重（log(1+ReLU)），拼接得到完整稀疏向量；密集向量由 EOS token 的隐状态获得。
- **训练**：联合 InfoNCE 损失（密集余弦相似度 / 稀疏内积）+ FLOPS 稀疏正则，引入硬负例挖掘与多模态数据混合训练；温度解耦（密集 τ=0.03，稀疏 τ_s=32）缓解内积尺度差异。
- **数据**：公开文本（Echo-Embedding、M3-Embedding 等）与多模态（MMEB、ColPali、VisRAG 等）混合，共 3.94M 样本。

**关键结果**：
- 在 MMEB-v2 多模态基准上，UEmbed-9B 密集 71.8、稀疏 71.0，均为公开数据训练最佳；稀疏仅比密集低 0.8 点，且显著超越同规模稠密基线（如 Ops-MM-Embed-7B）。
- 在 BEIR 文本检索 9 数据集上，密集 avg nDCG@10 56.3，稀疏 55.2，与专用稀疏模型 Echo-Mistral-SPLADE 持平，同时保持多模态与密集能力。
- 消融证实稀疏头分区（语义聚类优于随机）、温度参数（τ_s=32 最优）与特殊 token 数量（N=16 合适）的重要性；联合训练不损伤单模式性能。
- 在 BrowseComp-Plus agentic search 中，稀疏模式平均搜索轮次比密集减少 1.6-6.5 轮，校准误差更低。
