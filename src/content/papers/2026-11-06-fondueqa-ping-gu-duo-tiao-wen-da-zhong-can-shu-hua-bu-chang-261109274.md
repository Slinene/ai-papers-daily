---
title: 'FondueQA: A Benchmark for Evaluating Parametric Compensation in Multi-Hop
  QA'
title_zh: FondueQA：评估多跳问答中参数化补偿的基准
authors:
- Laurin Schmid
- Suman Navaratnarajah
- Koel Dutta Chowdhury
- Steffen Eger
- Josif Grabocka
- Christian Frey
affiliations:
- University of Technology Nuremberg
arxiv_id: '2611.09274'
url: https://arxiv.org/abs/2611.09274
pdf_url: https://arxiv.org/pdf/2611.09274
published: '2026-11-06'
collected: '2026-11-09'
category: RAG
direction: RAG 参数化知识评估
tags:
- RAG
- Multi-Hop QA
- Parametric Knowledge
- Evaluation
- LLM
one_liner: 提出 FondueQA 基准，通过文档级证据消融研究 LLM 在检索证据不全时的参数补偿机制
practical_value: '- 在 RAG 链路中，对热门实体/头部商品可适度降低召回冗余，依赖模型参数补偿；但对长尾 query/新品必须保证检索覆盖，因为参数补偿在冷门实体上显著变差。

  - 构建多跳问答/推荐理由时，桥接性证据（如类目、品牌、属性关系）可能比直接包含答案的文档更重要，应优先召回并保留这类“连接”信息。

  - 若上下文存在相似竞争实体（如同款商品、相似品牌），模型容易被干扰，建议在输入前做实体消歧或去重，避免混淆；可参考 FondueQA 证据消融方式，设计线上
  RAG 的压测与诊断。

  - 评估 RAG/生成式推荐时，建议加入“参数知识 vs 检索证据”消融测试，识别哪些 query 可少召回、哪些必须强依赖检索。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有多跳 QA 基准可能已被预训练语料污染，无法区分参数知识与基准记忆。为研究检索证据不完整时 LLM 如何调用内部知识补偿，需要可控的文档级证据消融。

**方法**：FondueQA 将每个多跳事实唯一绑定到指定证据文档，支持精确移除某类文档（如桥接文档、答案文档）来模拟检索缺失。基于该基准评估多个 LLM 的参数补偿行为。

**关键结果**：参数补偿与实体流行度强相关：流行实体的事实更易被补偿。桥接文档缺失时损失可能大于答案文档缺失——桥接证据有时比答案文档更重要。模型能孤立回忆某事实，但在部分证据+竞争实体上下文下，仍会用错该事实，Exact Match 最多下降 15 个百分点。
