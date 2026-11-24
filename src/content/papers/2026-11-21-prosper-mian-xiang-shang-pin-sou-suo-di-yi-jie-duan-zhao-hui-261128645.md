---
title: 'PROSPER: LLMs as Sparse Retrievers for First-Stage Product Search'
title_zh: PROSPER：面向商品搜索第一阶段召回的 LLM 稀疏检索器
authors:
- Hongru Song
- Yu-An Liu
- Ruqing Zhang
- Jiafeng Guo
- Maarten de Rijke
- Sen Li
- Wenjun Peng
- Fuyu Lv
- Xueqi Cheng
affiliations:
- State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- University of Amsterdam
- Taobao & Tmall Group of Alibaba
arxiv_id: '2611.28645'
url: https://arxiv.org/abs/2611.28645
pdf_url: https://arxiv.org/pdf/2611.28645
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: LLM 稀疏检索 · 字面保真
tags:
- sparse retrieval
- LLM
- product search
- SPLADE
- lexical fidelity
- e-commerce
one_liner: 用 LRN 与 LFW 缓解 LLM 稀疏检索中字面扩展幻觉并加速稀疏化，显著提升商品搜索召回与线上 GMV
practical_value: '- **显式保护字面词**：在电商搜索的 learned sparse 场景，若直接换 LLM 骨干，扩展词会淹没品牌/型号 token。可借鉴
  LRN 的残差补偿：基础权重来自 LM head logits，再对原文 token 位置加由 last hidden state 投影得到的补偿项 W = w
  + I ⊙ (max(w) - w'')。训练时让检索损失决定每个字面 term 需要多少补偿，比直接加 w'' 或统一提升到 max(w) 更稳。

  - **训练早期用 top-k 窗口快速稀疏化**：LFW 在表示非零维度超过 k 时只保留 top-k（论文最优 k_q=256, k_d=512），能加速早期收敛并提升最终效果。对其他
  LLM 稀疏化任务可尝试同样粗到细策略，配合 FLOPS 正则。

  - **工程部署思路**：线上选 Qwen2.5-1.5B 而非更大模型；query 推理只保留 top-16 weighted terms；商品侧离线预计算稀疏向量并建倒排索引，用
  block-max MaxScore 加速。80M 商品索引 93GB，匹配延迟 ~20ms，满足生产要求，比同规模 dense 索引更省。

  - **相似度归一化**：query 侧 ℓ2 归一化、item 侧不归一化，能抑制通用词、保留商品属性覆盖，并促进稀疏化。值得在召回双塔或稀疏表示中试验。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商商品搜索的第一阶段召回决定召回上限，需要高 recall、可解释和低存储开销。稀疏检索适合部署，但面临词汇不匹配，尤其在短 query 和商品标题场景。LLM 语义能力强，但直接替换 SPLADE 的 BERT 骨干会导致两个问题：语义扩展幻觉使品牌/型号等字面词被低估；LLM 巨大词表造成训练不稳定、稀疏化困难。

**方法关键点**：
- **Literal Residual Network (LRN)**：基础表示 w 来自 LLM LM head logits 的 last-pooling，额外用 last hidden state 经 FC 层投影得到词表级补偿 w'，对原文 token 位置 I 做 W = w + I ⊙ (max(w) - w')。用输入相关的 max(w) 作为参考，让弱字面 token 获得必要补偿，保留扩展同时强化关键约束词。
- **Lexical Focusing Window (LFW)**：条件 top-k 窗口，仅当表示非零维度 > k 时保留 top-k，早期快速稀疏化，之后自然退出；配合 FLOPS 正则继续细化。固定 k_q=256, k_d=512 最优。
- **训练细节**：使用 InfoNCE 对比学习和 in-batch negatives；query 侧 ℓ2 归一化，item 侧不归一化；使用 last-pooling 聚合。

**关键结果**：Multi-CPR E-commerce 上 PROSPER 的 Hit@1000 为 93.9%，高于 BM25 83.7%、SPLADE-v2 89.6%、SPQwen-echoembedding 92.4%；Hit@10 为 50.7%。真实电商日志数据集 Hit@1000 达 94.08%。线上 1% 流量 A/B 测试，净 GMV +1.60%、净交易 +0.31%、净 UV +0.24%。工程上，80M 商品索引 93GB，匹配延迟约 20ms。

**最值得记住**：商品搜索中用 LLM 做 learned sparse retrieval，必须显式保护字面 token，并用 top-k 窗口做粗到细稀疏化，才能平衡语义扩展与硬约束。
