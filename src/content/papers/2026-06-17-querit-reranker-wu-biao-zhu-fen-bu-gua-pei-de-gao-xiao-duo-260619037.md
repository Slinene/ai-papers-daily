---
title: 'Querit-Reranker: Training Compact Multilingual Rerankers via Efficient Label-Free
  Distribution Adaptation'
title_zh: Querit-Reranker：无标注分布适配的高效多语言重排序器训练
authors:
- Yunfei Zhong
- Jun Yang
- Wei Huang
- Yinqiong Cai
- Haosheng Qian
- Yixing Fan
- Ruqing Zhang
- Lixin Su
- Daiting Shi
- Jiafeng Guo
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Baidu Inc.
arxiv_id: '2606.19037'
url: https://arxiv.org/abs/2606.19037
pdf_url: https://arxiv.org/pdf/2606.19037
published: '2026-06-17'
collected: '2026-06-18'
category: RecSys
direction: 多语言重排序器训练与分布适配
tags:
- Reranker
- Multilingual
- Cross-Encoder
- Distribution Adaptation
- SLERP
- Synthetic Query
one_liner: 通过合成query mining与teacher软标签实现无标注目标适配，结合SLERP合并checkpoint，产出紧凑且强劲的多语言重排序模型
practical_value: '- **无标注分布适配**：用目标语料库中的文档通过LLM生成合成query，并由teacher模型（如Llama-Embed-Nemotron-8B）打分作为连续软标签，代替昂贵的人工标注，可迁移用于电商搜索中的新行业/小语种适配。

  - **SLERP单模型合并**：将多个针对不同任务/数据分布训练的checkpoint用球面线性插值融合为一个模型，避免多模型部署的推理开销，适合线上低延迟重排序。

  - **紧凑MoE架构**：Querit-Reranker-A0.4B使用0.4B激活参数的MoE骨干，在保证效果的同时大幅降低推理成本，适合搜索重排序等高性能要求场景。

  - **多阶段数据配比**：一阶段用大规模开源+业务数据构建通用相关性，二阶段用少量目标分布合成数据精调；可迁移到电商多国家站点/多品类的重排序模型训练。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
在检索增强生成、多语言搜索等场景，需将粗召回结果进行重排序，而强多语言骨干模型直接用于重排序效果有限。为目标分布收集大量相关性标注成本高昂，尤其在多语言场景下。同时，针对不同任务微调的模型若分别部署会增加延迟与资源消耗。因此，如何在有限人工标注下高效地让通用骨干模型适配目标排名分布并合并为一个高效模型是核心问题。

**方法**  
Querit-Reranker采用三阶段数据驱动训练流水线：  
1. **大容量排序数据预训练**：混合开源检索/重排序数据集（MS MARCO、MLDR、T2Ranking等）与脱敏的真实业务数据，用teacher模型（Llama-Embed-Nemotron-8B）为query召回top-100文档并打分，按分数分层采样构建排序对，训练pairwise hinge loss。  
2. **目标分布无标注适配**：针对四个不同的多语言重排序任务（法语、俄语、中文、日文），用DeepSeek-R1根据目标库文档生成合成查询，复用teacher模型打分作为连续软标签，实现无需额外人工评判的分布适配。  
3. **SLERP模型合并**：将不同数据混合或训练运行的checkpoint通过球面线性插值合并为一，消除多模型集成的推理开销。  
模型采用cross-encoder架构，将query和document拼接后经骨干网络输出相关性得分。提供了基于MoE的0.4B版本和基于Qwen3-Embedding的4B版本。

**关键结果**  
- 在MTEB-multilingual-v2的6个重排序任务上，Querit-Reranker-4B平均分71.08，达到公开模型SOTA；Querit-Reranker-A0.4B平均65.84，超越多款更大参数模型。  
- 在BEIR通用英文检索重排序上，A0.4B将Qwen3-Embedding-0.6B第一阶段的nDCG@10从54.11提升至59.28；4B版本进一步提升至62.29。  
- 在MIRACL多语言检索上，A0.4B将第一阶段nDCG@10从59.87提升至67.70；4B版本达到71.13，显著优于对比的8B重排序器。

一句值得记住的话：**“用合成query配合teacher打分作为软标签，无需任务标注即可适配新分布，再通过SLERP合并得到一个高效的单模型重排序器。”**
