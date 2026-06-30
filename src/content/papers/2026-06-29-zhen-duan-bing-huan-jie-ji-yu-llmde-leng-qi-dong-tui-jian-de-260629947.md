---
title: Diagnosing and Mitigating Retrieval Bottlenecks in LLM-Based Cold-Start Recommendation
title_zh: 诊断并缓解基于LLM的冷启动推荐中的检索瓶颈
authors:
- Zhe Dong
- Fang Qin
- Manish Shah
- Yicheng Wang
affiliations:
- University of Maine at Presque Isle
- Stanford University
- Independent Researcher
arxiv_id: '2606.29947'
url: https://arxiv.org/abs/2606.29947
pdf_url: https://arxiv.org/pdf/2606.29947
published: '2026-06-29'
collected: '2026-06-30'
category: RecSys
direction: 检索瓶颈诊断与学习混合融合
tags:
- Cold-Start
- LLM Reranking
- Retrieval Coverage
- Learned Hybrid Fusion
- Retrieve-then-Rerank
- Recommender Systems
one_liner: 冷启动推荐性能瓶颈在检索覆盖而非LLM重排序能力，学习多路融合LHF部分缓解但仍需轻量排序器利用信号
practical_value: '- **冷启动瓶颈在召回不在精排**：即使LLM在候选池已有正确物品时有一定语义优势，真实场景下检索覆盖率仅4.6%–22.9%，因大量物品无交互记录。应优先投入多路召回、新物品索引与语义匹配，而非仅优化在线LLM重排序。

  - **学习型多路召回融合（LHF）即插即用**：利用多个检索器（文本/协同/图）的排名、分数、标志位，加上物品冷启标识、用户冷启标识等少量元特征，训练GBDT做候选池级融合，可提升覆盖率17–61%（内容域）。特征在服务时均可从训练快照或请求时计算，轻量易部署，适合电商冷物品曝光。

  - **LLM在线重排序性价比极低**：Qwen3-8B吞吐仅为LightGCN的1/937、显存占用9倍，但端到端Recall@10普遍下降或持平，在协同信号强的域甚至显著退化（Yelp降3.1pp）。建议将LLM仅用于离线生成语义特征或物品表示，而非在线重排序。

  - **评估协议要还原真实检索**：注入金标的“正控池”评估会高估LLM能力，且负采样方式（均匀/流行度加权）会反转CF与LLM的相对优势。搭建检索-真实池召回×条件Top-K的分解评估框架，才能正确诊断系统瓶颈。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM 重排序被寄望于解决冷启动推荐中的语义理解缺口，但重排序只能重排候选池内物品。实际检索阶段覆盖率可能成为瓶颈。该工作量化并隔离这一问题，指出真实管线中LLM的优势难以实现。

**方法关键点**  
- **三阶段评估协议**：正控池（注入金标，评估重排序能力）、检索-真实池（全量索引召回，评估Coverage@200）、端到端E2E@10 = Cov@200 × Cond@10。  
- **五域冷启动基准**：Amazon Arts、Video Games、MIND、MovieLens-20M、Yelp，按时序划分，突出**物品为新**（训练无交互）目标的占比（32–91%）。  
- **多路检索基线**：协同过滤、文本（TF-IDF、SBERT/BGE）、图模型等单路及启发式融合（RRF、CARA）。  
- **LHF（学习混合融合）**：对10个检索器返回的并集，利用排名、分数、出现标志、物品/用户冷启标签、物品流行度等元特征，训练GBDT分类器（验证集），重排并选Top-200作为下游候选池。特征在服务时可获取。  
- **LLM重排序**：Qwen3-8B为主，对比32B和Llama-70B，采用点式Yes/No对数概率。

**关键结果**  
- 检索-真实池下，最佳单路检索器Coverage@200仅4.6–22.9%，因为大量物品为**真正的全新物品**（无训练交互）。  
- LHF将覆盖率提升至6.1–24.3%，在内容富集域（MIND）恢复61%的并集上限空间，但协同强域（ML-20M、Yelp）仅恢复5–7%。  
- 端到端：将LHF池送入LLM，Recall@10普遍≤1.4%，且显著劣于同一池上的轻量LightGBM排序器（提升1.3–2.7pp）。LLM重排序在多数域引入负面效应（精确实验表明Yelp降3.1pp）。  
- Prompt级注入图/尾部信号（GraphPrompt+Tail）主要受益于尾部先验，图证据本身非正。

**核心教训**：冷启动的机会在检索和候选生成侧，而非在线LLM重排序。改善覆盖比增大LLM规模更紧迫。
