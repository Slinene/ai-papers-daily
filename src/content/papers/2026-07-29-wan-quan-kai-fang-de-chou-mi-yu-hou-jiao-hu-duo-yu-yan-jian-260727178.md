---
title: 'DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for
  Multilingual, Long-Context, and Code Search'
title_zh: 完全开放的稠密与后交互多语言检索模型：翻译训练的泛化差异
authors:
- Raphaël Sourty
- Antoine Chaffin
- Paulo Roberto Moura Junior
- Amélie Chatelain
affiliations:
- LightOn
arxiv_id: '2607.27178'
url: https://arxiv.org/abs/2607.27178
pdf_url: https://arxiv.org/pdf/2607.27178
published: '2026-07-29'
collected: '2026-08-01'
category: RecSys
direction: 开放检索模型训练与多语言泛化对比
tags:
- dense-retrieval
- late-interaction
- multilingual
- translate-train
- open-data
- hard-negative-mining
one_liner: 开放训练数据与 recipe 下，翻译训练使 late-interaction 比 dense 模型对未见语言泛化更好
practical_value: '- 可借鉴其非破坏性过滤流水线：对原始语料追加结构质量、语言置信度、交叉编码器分数等元信息，训练时按需过滤，便于定制，适合从电商商品/搜索日志构建召回训练集。

  - 多语言场景下，若只有英文标注数据，用翻译训练（translate-train）扩展到目标语言是可行方案；但稠密双塔泛化弱，推荐在后交互模型（如 ColBERT）上做，尤其当业务需支持未翻译语言时。

  - 微调阶段采用 mined hard negatives + 交叉编码器蒸馏可稳定提升召回精度，该 trick 可直接复用到精排或召回模型微调。

  - 长文本描述（商品详情、广告文案等）召回中，后交互的 token 级匹配更有效，可考虑将单向量替换为多向量方案。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：前沿检索模型越来越依赖闭源数据，复现困难。多语言、长文档、代码等场景又缺乏一套完全开放的训练配方。本工作尝试用公开数据重建检索前沿，并研究英文监督经翻译训练向多语言迁移的泛化行为。

**方法关键点**
- 数据重建：从 34 个开源来源收集 14 亿 query-document 对，通过非破坏性过滤（结构质量、语言置信度、cross-encoder 打分等元信息保留）最终得到 6.65 亿对英文预训练数据；并用 mined hard negatives 构建 188 万对微调数据。
- 英文模型：基于 ModernBERT-base（149M），训练稠密模型 DENSEON 和后交互模型 LATEON，对比学习 + KL 蒸馏 mxbai-rerank-large-v2。
- 翻译训练：将英文种子翻译到 8 种目标语言，加入跨语言对，构建 28 亿对多语言预训练语料；微调数据加入 MIRACL、MLDR、LateOn-Code 等有机数据，得到 1630 万样本。
- 多语言模型：在 mmBERT-base（307M）上训练 MDENSEON 和 MLATEON，保持骨干、数据、目标一致，仅检索范式不同。

**关键结果**
- 英文 BEIR：DENSEON 56.20 nDCG@10，LATEON 57.22，在 149M 级别均达到 SOTA；去污实验证明性能来自泛化而非基准泄露。
- 多语言 MIRACL：MLATEON 全语言平均 67.04，显著超过 MDENSEON（58.02），且对未见语言和陌生文字（如俄语、日语、泰语等）仍保持较高水平，而稠密模型在未见语言上急剧退化。
- 长文档 MLDR：MLATEON 全语言 77.92，比 MDENSEON（51.59）高出 20+ 点；代码检索也优于稠密版本（73.48 vs 71.53）。

核心启示：翻译训练用于检索时，后交互模型可将有监督信号泛化到训练中未出现的语言，而稠密双塔则停留在已翻译语言内。
