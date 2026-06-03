---
title: 'Entropy Gate: Entropy Quenching for Near-Lossless Token Compression in LLM
  Pipelines'
title_zh: 熵门控：LLM管线中近乎无损的令牌压缩熵淬灭技术
authors:
- Justice Owusu Agyemang
- Jerry John Kponyo
- Kwame Opuni-Boachie Obour Agyekum
- Francisca Adoma Acheampong
- Kwame Agyeman-Prempeh Agyekum
- James Dzisi Gadze
affiliations:
- Kwame Nkrumah University of Science and Technology
arxiv_id: '2606.03739'
url: https://arxiv.org/abs/2606.03739
pdf_url: https://arxiv.org/pdf/2606.03739
published: '2026-06-02'
collected: '2026-06-03'
category: LLM
direction: LLM推理优化 · 提示令牌压缩
tags:
- entropy quenching
- token compression
- prompt compression
- fidelity gate
- agentic workflows
- energy-squared amplification
one_liner: 提出基于熵淬灭的多因子信息能量令牌压缩框架，结合保真门与能量平方放大，实现40-60%压缩且语义保持>0.80
practical_value: '- **令牌重要性建模**：多因子能量（统计+结构+位置）及自校准域能量可迁移至电商搜索/推荐场景，对商品描述、用户查询进行关键令牌保留，压缩冗余而不丢失实体词。

  - **能量平方放大技巧**：通过能量平方拉伸分布右尾，放大信噪比，使得高信息令牌更易被保留。可应用于任何基于分数排序的文本压缩或关键信息提取任务。

  - **复合压缩策略**：上下文去重结合外部记忆，实现88-96%的令牌削减。在Agent多轮对话或商品信息重复出现的场景中，可借鉴“记忆+淬灭”乘法组合，极大降低推理成本。

  - **输出侧淬灭**：利用模型回复信息密度低的特点，以更激进的压缩率减少回复长度。可在生成式推荐或对话式导购中压缩冗长回应，兼顾准确性与效率。

  - **保真门机制**：以能量加权相似度作为无模型推理的语义保留指标，为压缩提供数学保证。可引入任何压缩流程作为安全阀，确保任务关键信息不丢失。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM推理中的大量token消耗在重复上下文、冗余回复和样板文本上，现有压缩方法各管一段，缺乏统一的数学框架与保真保证，且多需额外训练。

**方法**：提出Entropy Gate，受统计力学熵淬灭启发，将令牌压缩建模为逐步冻结低能令牌的过程。
- 定义多因子信息能量 \(E(t) = w_1 E_{\text{stat}} + w_2 E_{\text{struct}} + w_3 E_{\text{pos}}\)，融合统计TF-IDF、结构角色权重与位置衰减，并加入自校准域能量（基于任务动词的邻近性）自动捕获域关键词。
- 淬灭调度 \(T(\tau) = T_0/(1+\alpha\tau)\)，令牌以玻尔兹曼概率 \(p_i = e^{-E_i/kT}\) 生存，通过能量平方放大（\(E \rightarrow E^2\)）拉伸分布右尾，提升信噪比。
- 能量加权相似度 \(S_E\) 作为保真门，当低于阈值 \(\theta\) 时停止压缩，保证语义保留 \(\ge \theta\)。
- 支持上下文块去重、输出侧淬灭、多轮结构压缩，可与外部记忆组合，理论压缩削减达88-96%。
- 实现为无状态HTTP代理，无需训练，模型无关。

**实验**：在代码审查、安全审计、文档生成、SQL生成、系统提示五类提示上，Phase 1确定性模式达到40-60%压缩率，\(S_E>0.80\)。消融显示能量平方放大单独贡献18.7个百分点。上下文去重带来50-70%额外节省。标准基准（MMLU、HumanEval、GSM8K）上，压缩后问题正确率在6/9项中保持，有效压缩率24%时LLM-jugde质量评分3.9/5。结合外部记忆的乘法效应经定理11.1证明，推估压缩比0.4-0.6且重复率70-90%时总削减88-96%。

**要点**：Entropy Gate将热力学淬灭与信息能量统一，为LLM令牌压缩提供了有保真保证、无需训练的数学框架，其能量组合与放大策略可直接迁移到任意文本重要性筛选场景。
