---
title: 'Dense Contexts Are Hard Contexts: Lexical Density Limits Effective Context
  in LLMs'
title_zh: 密集上下文：词法密度限制LLM有效上下文容量
authors:
- Giovanni Dettori
- Matteo Boffa
- Danilo Giordano
- Idilio Drago
- Marco Mellia
affiliations:
- Politecnico di Torino
- University of Turin
arxiv_id: '2606.06203'
url: https://arxiv.org/abs/2606.06203
pdf_url: https://arxiv.org/pdf/2606.06203
published: '2026-06-04'
collected: '2026-06-07'
category: Eval
direction: 长上下文 · 信息密度 · find-the-needle评测
tags:
- lexical density
- long-context
- LLM evaluation
- needle-in-a-haystack
- information density
one_liner: 发现词法密度是长上下文性能衰减的第三大因素，高密度信息显著降低LLM检索准确率
practical_value: '- 在Agent、RAG等长上下文构建中，高密度信息（如密集拼接商品详描、用户行为序列）会直接导致LLM忽略关键事实，可尝试先做信息解耦或摘要，降低局部密度后再输入。

  - 评测LLM应用的上下文利用能力时，除长度和位置外，应监控信息密度指标，指导prompt压缩或分段策略。

  - 生成式推荐的item特征拼接若过于紧凑，可能退化生成质量，需控制信息密度，或采用结构化表示替代自由文本拼接。

  - 多智体协作中，多次传递的上下文若不经清洗，密度累积会加速遗忘，可设计密度感知的记忆管理机制。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
LLM长上下文性能衰减通常归因于输入长度和信息位置，但词法密度——上下文引入不同信息的速度——作为第三大因素被系统忽视。实际LLM系统常将高密度信息（如文档检索、Agent记忆）拼入上下文，此时模型可能突然失效。  
**方法**  
作者设计了三个find-the-needle基准，固定长度约12k tokens，控制needle位置，但逐步增加上下文的信息密度（低→中→高）。在9B到685B的开源LLM上，通过检索准确率衡量性能。为排除任务类型干扰，进一步在同一基准内异动密度进行验证。  
**结果**  
从稀疏到密集，模型性能急剧崩塌：高密度基准下检索得分降至60%以下，而稀疏上下文近乎满分。降低密度普遍恢复性能，尤其高密度区间提升显著。证实有效上下文容量是词法密度的函数，与长度、位置形成三方制约。
