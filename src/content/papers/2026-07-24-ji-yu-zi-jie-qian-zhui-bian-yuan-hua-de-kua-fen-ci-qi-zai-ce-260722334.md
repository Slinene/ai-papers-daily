---
title: Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization
title_zh: 基于字节前缀边缘化的跨分词器在线策略蒸馏
authors:
- Hao Wang
- Kun Yuan
- Wenlin Zhong
- Minglei Zhang
- Han Xiao
- Ming Sun
- Honggang Qi
affiliations:
- University of Chinese Academy of Sciences
- KwaiKAT Team
- Zhejiang University
- The Chinese University of Hong Kong
arxiv_id: '2607.22334'
url: https://arxiv.org/abs/2607.22334
pdf_url: https://arxiv.org/pdf/2607.22334
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 跨 tokenizer 蒸馏训练
tags:
- Knowledge Distillation
- Cross-Tokenizer
- On-Policy Distillation
- Byte-Prefix Marginalization
- Language Models
one_liner: 在共享字节空间将教师分布边缘化到学生词汇，无损对齐概率质量，大幅提升跨分词器蒸馏性能
practical_value: '- 若业务中需融合多个使用**不同 tokenizer 的文本模型**（如商品标题/描述编码器、多语言模型），可借鉴 BPM 将教师分布无损映射到学生词汇，避免丢弃概率或语义错配。

  - 字节前缀映射表可离线构建，蒸馏时仅需查表聚合，工程可行；残差类别处理未匹配质量，保证分布完整，可直接移植到自定义蒸馏 loss。

  - 对于**多模态推荐模型**（图文混合 tokenizer 不同），BPM 提供了一种统一概率空间的思路，有助于跨模态知识迁移。

  - 在 Agent 工具调用或搜索链路的 LLM 蒸馏中，若教师和学生分词器不一致，BPM 能保留关键 token 的分布结构，减少性能损失。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：不同词表结构的开源大模型能力互补，通过在线策略蒸馏（OPD）将其合并到小模型可以提升性能，但全词表 OPD 通常要求师生共享 tokenizer。现有跨 tokenizer 方法或丢弃部分教师概率质量，或将其分配给语义无关的学生 token，导致信息损失。

**方法**：提出 **Byte-Prefix Marginalization (BPM)**，在字节空间统一表达教师的下个 token 分布。对每个教师 token，找到其字节表示的最长前缀所对应的学生 token，将概率赋给该学生 token；若多个教师 token 映射到同一学生 token，则概率累加；无法匹配的剩余概率放入显式残差类别。该过程保证了目标分布的词汇完整性、字节对齐性，并严格保持总概率质量。当相关字节前缀不跨多个教师 token 时（覆盖 >99% 训练位置），BPM 恰好恢复教师诱导的字节前缀边缘分布；否则使用质量保持的链式分解下界。

**结果**：以 Qwen3-32B、GLM-Z1-9B-0414、MiniMax-M2.7 为教师，学生为 Qwen3.5-2B（base）。在 AIME 2026、HMMT 2026、MATH-500、HumanEval+、LiveCodeBench、TACO 六个数学与编程基准上，BPM 一致优于现有跨 tokenizer 方法，平均 avg@8 提升 3.7-6.6 点，相对最强基线显著缩小了师生性能差距。
