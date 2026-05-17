---
title: 'VectorSmuggle: Steganographic Exfiltration in Embedding Stores and a Cryptographic
  Provenance Defense'
title_zh: 向量隐写：嵌入存储泄露与加密溯源防御
authors:
- Jascha Wanger
arxiv_id: '2605.13764'
url: https://arxiv.org/abs/2605.13764
pdf_url: https://arxiv.org/pdf/2605.13764
published: '2026-05-13'
collected: '2026-05-17'
category: RAG
direction: RAG 安全 · 嵌入完整性
tags:
- RAG Security
- Steganography
- Embedding Integrity
- Vector Database
- Provenance Defense
one_liner: 揭示通过嵌入后处理扰动隐藏数据的隐写攻击，并提出基于 Ed25519 签名的向量溯源协议 VectorPin。
practical_value: '- 在电商/Agent 的 RAG 检索管线中，应防止向量数据库写入权限被滥用，避免成为数据泄露通道。

  - 可引入类似 VectorPin 的嵌入签名机制，使用 Ed25519 对（text, model）签名，检索时验证完整性。

  - 简单的分布异常检测（如方差、均值偏移）无法识别正交旋转类攻击，需采用密码学手段。

  - 若使用托管向量存储（如 Pinecone、Weaviate），应评估原生是否支持嵌入完整性校验，若否，可在外围包装验证逻辑。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统将敏感文本转为高维嵌入后存入向量数据库，但绝大多数向量存储产品缺乏嵌入完整性控制、注入时异常检测或密码学溯源证明。攻击者可利用此缺口实施隐写泄露。

**方法**：攻击者在嵌入上施加微小后处理扰动（噪声注入、旋转、缩放、偏移、分片等），将任意载荷隐藏入向量中，同时几乎不影响检索质量（如 R@k、MRR）。文章在一系列模型（text-embedding-3-large 及 4 个开源模型）、语料（合成 PII、BEIR NFCorpus、Quora 子集，共超 26,000 块）、7 种向量库配置下评估，并引入自适应攻击者。发现分布偏移攻击易被简单异常检测器捕捉，但小角度正交旋转可绕过所有被测模型与语料的分布检测。文章给出基于不相交 Givens 旋转的容量上界 floor(d/2)·b 比特，但实际嵌入流形存在容量-可检测性权衡，检索保持的操作点远低于此上界。

**防御**：提出 VectorPin 协议，对每个嵌入计算其源文本与产生模型的 Ed25519 签名，绑定至向量，任何后嵌入修改均导致签名验证失败。实验表明嵌入级完整性是一种可部署、可标准化的防御，能彻底关闭该类攻击。
