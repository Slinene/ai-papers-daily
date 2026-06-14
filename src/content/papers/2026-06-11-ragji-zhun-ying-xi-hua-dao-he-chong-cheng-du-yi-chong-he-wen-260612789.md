---
title: How Fine-Grained Should a RAG Benchmark Be? A Hierarchical Framework for Synthetic
  Question Generation
title_zh: RAG基准应细化到何种程度？一种合成问题生成的层次化框架
authors:
- Chase M. Fensore
- Kaustubh Dhole
- Jason Fan
- Eugene Agichtein
- Joyce C. Ho
affiliations:
- Emory University
arxiv_id: '2606.12789'
url: https://arxiv.org/abs/2606.12789
pdf_url: https://arxiv.org/pdf/2606.12789
published: '2026-06-11'
collected: '2026-06-14'
category: Eval
direction: RAG评估粒度优化
tags:
- RAG
- Benchmark
- Granularity
- Synthetic Data
- Hierarchical
one_liner: 提出HieraRAG层次化框架，通过判别力和一致性比率确定RAG评测的最佳粒度
practical_value: '- 构建内部RAG评估集时，可借鉴层次化粒度框架，在不同问题维度（如复杂度、答案类型）上计算判别力，选取最大化类别间生成质量标准差的粒度，避免过分细分或过粗。

  - 一致性比率（Coherence Ratio）可作为维度细分有效性的诊断指标，评估子类别是否继承父类特征，指导电商搜索或Agent问答基准的类别体系设计。

  - 合成QA对的生成流程可用于低资源场景，例如从商品说明或客服对话日志中自动生成评估样本，但需结合人工校验确保质量。

  - 整个框架可移植，可直接应用到电商RAG、多智体协作等场景，根据自身配置（检索器、生成器）重新测定最佳粒度，降低盲目套用通用基准的风险。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：评估RAG系统需要基准覆盖多样的问题特征，但实践中缺乏关于维度和粒度的实证指导，过度细分可能浪费标注资源，过于粗粒度又无法区分系统能力。

**方法**：提出HieraRAG层次化框架，将最佳粒度定义为最大化**判别力**（各类别间生成质量的标准差）的划分等级。在FineWeb-10BT数据集上，围绕问题复杂度、答案类型、语言变化三个维度，分别生成2、4、8三个粒度的合成QA对共5,872条。使用BM25+Falcon-3-10B管线评测，发现复杂度维度在细粒度（8类）判别力最高（0.053），而答案类型和语言变化在中粒度（4类）达到峰值。此外，引入**一致性比率**指标衡量细粒度划分是否干净地继承父类特征，复杂度维度仅0.40（继承性弱），答案类型达1.44（继承性强），揭示了不同维度的结构差异。人工评估110个分层样本确认合成质量。

**关键结果**：该框架验证了粒度选择应依维度而定，不可一刀切；一致性比率可提前预测细分有效性。尽管具体结论基于单一配置，但HieraRAG提供了一套可复用的流程和验证指标，供从业者嵌入自有RAG设置，经济地确定评估粒度。
