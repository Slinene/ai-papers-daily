---
title: 'Cartridges at Scale: Training Modular KV Caches over Large Document Collections'
title_zh: 大规模文档集合的模块化KV缓存训练框架
authors:
- Momchil Hardalov
- Gonzalo Iglesias
- Adrià de Gispert
affiliations:
- Amazon AGI
arxiv_id: '2606.04557'
url: https://arxiv.org/abs/2606.04557
pdf_url: https://arxiv.org/pdf/2606.04557
published: '2026-06-03'
collected: '2026-06-06'
category: LLM
direction: 文档压缩·模块化KV缓存与检索增强生成
tags:
- KV cache
- context distillation
- retrieval-augmented generation
- modular training
- document compression
one_liner: 提出CAS框架，通过动态混合训练及GPU/存储交换，实现数百个per-document cartridge的联合训练，消除多缓存混合的性能塌陷，结合检索较文本RAG节省3-4倍token。
practical_value: '- **可组合的KV缓存训练范式**：在需要为大量静态文档（商品政策、FAQ、医典）构建可重用缓存的场景，直接采纳混合可见性训练（P<sub>iso</sub>=0.75，每样例以一定概率加入其他文档的cartridge作为干扰），可完全避免多缓存拼接时的性能暴跌（从26%回至78%），能直接复用到电商长文档问答的缓存构建中。

  - **GPU内存有限的规模化训练**：预算管理器将KV缓存池轮换（每R步交换φ比例）并优先训练次数少的文档，配合FP32优化器与BF16权重、优化器状态卸载至NVMe，可在单GPU上训练数百个cartridge。对需要为海量商品文描或搜索结果页生成压缩预填缓存的场景极为关键，省去反复prefill的成本。

  - **自学习数据合成的省钱技巧**：将问题生成与回答模型解耦（用更大的MQ生成多样问题），一次API调用生成20个问题，并将文档采样权重设为与该文档长度成正比，可提升合成数据对长文档事实的覆盖，同时降低约20倍合成成本。这对需要自建训练语料的推荐/Agent项目同样适用。

  - **混合RAG与压缩缓存的推理策略**：Cartridge RAG用检索选出相关文档的压缩缓存代替原始文本块，在LongHealth上以3.7倍更少prompt
  tokens达到同等精度。对于电商搜索结果总结或客服知识库问答，可大幅减少输入长度、加速生成，同时保持片段级检索的准确性。在信息高度密集的表格型内容上需谨慎控制激活的cartridge数量，否则性能下降，这一点对金融/库存类文档压缩有直接启示。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：大型语言模型可在长上下文中推理，但为静态文档集合（如企业知识库、病历、法律卷宗）反复执行全量prefill极不经济。Cartridges（Eyuboglu et al., 2025）将文档蒸馏为可重用的KV缓存，无需prefill，但原始方案只生成一个整体缓存，无法扩展到大规模多文档集合——独立训练的多个缓存混合时会发生灾难性干扰，准确率惨跌至随机水平。

**方法关键点**：
1. **混合可见性训练**：以概率P<sub>iso</sub>=0.75仅开放正确文档缓存，其他25%样例随机加入k个干扰缓存，促使模型学习选择性关注，训练时将KL损失适配至多缓存场景（公式1-2）。
2. **预算管理器与旋转策略**：维持GPU上固定数量B的缓存，其余N−B个卸载到CPU/磁盘；每R步轮换φ比例，优先调入训练步数最少的缓存，实现数百个文档缓存的联合训练。
3. **自学习数据合成改进**：按文档长度比例采样，一次生成20个问题（多问题生成），用更大模型（GPT-OSS 120B）生成问题，目标模型仅负责回答，降低合成成本约20倍并改善事实覆盖。
4. **每文档专用初始化**：用文档自身的前p个token的KV初始化对应cartridge，初始损失降低50%以上。
5. **检索式推理**：用稠密检索选出top-k个相关文档的cartridge拼接，替代原始文本块，实现高效的知识注入。

**关键结果**：在LongHealth、QASPER、QuALITY、FinQA、TechQA五个数据集上，单文档cartridge在Oracle设置下比No Context提升33-55点；混合训练后同时加载所有20个patient记录cartridge仍保持77.8%准确率（比孤立训练高51.8点）。在LongHealth上，Cartridge RAG在仅用566–2,673额外prompt tokens情况下达到75-77%准确率，而文本RAG需9,860 tokens。对表格密集的FinQA，单文档cartridge（2×压缩）即达62.7%执行准确率，远优于同一预算下的整体缓存（14.1%）。
