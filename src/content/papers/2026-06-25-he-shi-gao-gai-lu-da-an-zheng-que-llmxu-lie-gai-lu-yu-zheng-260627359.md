---
title: When are likely answers right? On Sequence Probability and Correctness in LLMs
title_zh: 何时高概率答案正确？LLM序列概率与正确性对齐研究
authors:
- Johannes Zenn
- Jonas Geiping
affiliations:
- Max Planck Institute for Intelligent Systems
- ELLIS Institute Tübingen
- AI Center Tübingen
- University of Tübingen
- IMPRS-IS
arxiv_id: '2606.27359'
url: https://arxiv.org/abs/2606.27359
pdf_url: https://arxiv.org/pdf/2606.27359
published: '2026-06-25'
collected: '2026-06-26'
category: LLM
direction: LLM解码概率与正确性对齐分析
tags:
- decoding methods
- sequence probability
- correctness alignment
- self-consistency
- best-of-N
- LLM evaluation
one_liner: 量化LLM解码中序列概率与正确性的对齐关系，发现仅在固定数据集内概率可预测正确性，调参或换方法无效
practical_value: '- 电商推荐中使用LLM生成商品描述或推荐理由时，不要依赖调整温度、top-k等解码超参数来提升事实准确性，提高序列概率不一定带来正确性提升

  - 构建基于LLM的推荐Agent时，若用生成概率作为置信度过滤候选动作，需注意只在固定解码配置下有效，改变采样策略会破坏概率与正确性的对齐

  - 在自我一致性（self-consistency）投票中，序列概率加权可能无效，建议等权投票或引入外部验证器

  - 对于同一提示的多次生成，概率不能可靠区分好坏，应避免用概率选择最佳回答，考虑其他校准方法'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机：** 许多LLM解码方法（如温度采样、top-k、Best-of-N）通过将概率质量移向高概率输出来提高质量，但序列概率与回答正确性是否一致尚未量化，这直接影响这类解码策略的有效性。

**方法：** 在四个层次系统分析对齐关系：(1) 跨不同解码方法（如贪心、采样、Best-of-N等）；(2) 跨同一方法的超参数变化（如温度、top-k值）；(3) 跨同一数据集的多个prompt-answer对；(4) 跨同一prompt的多次重复生成。

**关键结果：** 在固定数据集内，高序列概率通常与正确性正相关，但这一相关性不能外推到解码决策中：通过改变超参数或解码方法人为提高序列概率，并不可靠地提升准确率；对于同一prompt的多个响应，序列概率更无法有效指示对错。这些发现为解码策略、自我一致性和无验证器的自我改进提供了实用边界。
