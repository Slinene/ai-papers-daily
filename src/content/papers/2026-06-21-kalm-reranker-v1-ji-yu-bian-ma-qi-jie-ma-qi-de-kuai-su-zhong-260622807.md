---
title: 'KaLM-Reranker-V1: Fast but Not Late Interaction for Compressed Document Reranking'
title_zh: KaLM-Reranker-V1：基于编码器-解码器的快速重排序与可压缩文档表示
authors:
- Xinping Zhao
- Jiaxin Xu
- Ziqi Dai
- Xin Zhang
- Shouzheng Huang
- Danyu Tang
- Xinshuo Hu
- Meishan Zhang
- Baotian Hu
- Min Zhang
affiliations:
- Harbin Institute of Technology (Shenzhen)
- Shenzhen Loop Area Institute (SLAI)
arxiv_id: '2606.22807'
url: https://arxiv.org/abs/2606.22807
pdf_url: https://arxiv.org/pdf/2606.22807
published: '2026-06-21'
collected: '2026-06-23'
category: RecSys
direction: 高效重排序 · FBNL 范式
tags:
- reranking
- encoder-decoder
- Matryoshka embedding pooling
- efficiency
- cross-attention
- BEIR
one_liner: 用编码器-解码器解耦文档/查询计算 + 跨注意力 + 嵌套池化压缩，在保持强排序力的同时大幅降低在线计算量
practical_value: '- **离线编码 + 在线交叉注意力**：将文档编码器独立出来，文档表示可预计算并缓存；在线只需运行解码器进行查询‑文档交互，大幅降低重复计算。适合电商搜索/推荐中大量候选文档的场景，可显著节省
  GPU 成本。

  - **Matryoshka 嵌入池化**：沿序列维度压缩文档表示，通过均值池化得到紧凑的缓存向量，支持 2‑32 倍压缩比。工程上可按存储/延迟要求灵活选择压缩率，轻量模型（如
  0.27B）在 2‑4 倍压缩时性能几乎无损，能平衡存储成本与重排序效果。

  - **多阶段训练与知识蒸馏**：先做无指令通用重排，再加任务指令适配，最后用教师模型软标签蒸馏。可用于业务中冷启动或数据稀缺的垂类，提升正负样本区分度，尤其对困难负例更友好。

  - **FBNL 范式可嵌入现有 pipeline**：任何两阶段召回‑排序系统中，可将第二阶段的传统交叉编码器替换为 FBNL 结构，文档离线编码后即服务，重排时仅消耗轻量解码器。在推荐、广告、问答等场景均可尝试，建议优先用于长文档或多候选场景。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：现有重排序模型（编码器或解码器）通常将查询与文档拼接后联合编码，在线计算成本随候选数线性增长，且无法复用文档表示；晚交互方法（如 ColBERT）虽解耦编码但交互弱。亟需一种既能预计算文档表示、又能保持细粒度交互的高效重排序范式。

**方法关键点**：
- **FBNL 架构**：编码器-解码器分离。编码器（T5Gemma2 初始化）独立对文档编码，输出序列表示 Hp，可离线预计算并缓存；解码器接收系统指令、任务指令和查询，通过合并的自注意力与交叉注意力（查询 tokens 同时关注查询和缓存的文档 tokens）进行相关性建模，最后对比 “yes”/“no” token 概率得到排序分数。
- **Matryoshka 嵌入池化（MEP）**：对编码器输出沿 token 维度做均值池化，按比率 r 压缩文档表示长度，训练时多比率联合优化，使模型学会在压缩下仍保持排序能力，支持 2×‑32× 压缩，存储开销近线性减少。
- **三阶段训练**：① 无指令通用重排学习；② 加入任务指令进行适配；③ 用大模型（4B）软标签蒸馏小模型（1B/0.27B），提升细粒度区分能力。训练数据约 3.7M，包含中英文。

**关键结果**：
- 在 BEIR（13 个英文任务）上，KaLM-Reranker-V1-Large（4B）平均 nDCG@10 达 62.87，与 8B 的 Qwen3-Reranker-8B（65.11）相近，但在线计算量仅为其 1/8；Nano（0.27B）计算量仅为 gte-reranker-base 的 1/12，性能还略优（57.41 vs 56.77）。
- MIRACL 多语种重排上，即使未大规模训练多语数据，Large 模型仍以 70.07 nDCG@10 超越 bge-reranker-v2-gemma（69.82），效率提升近 2 倍。
- 压缩实验中，2‑4 倍压缩性能几乎无损（AUC 稳定），16 倍以上性能下降明显；更大模型对压缩更鲁棒。
- 在长时记忆检索 LMEB 上，0.27B Nano 模型可与 7‑12B 嵌入模型相抗衡。

**一句话**：FBNL 设计让重排序既能离线复用文档表示，又通过解码器交叉注意力保留强交互，配合嵌套池化实现灵活的存储‑性能折中。
