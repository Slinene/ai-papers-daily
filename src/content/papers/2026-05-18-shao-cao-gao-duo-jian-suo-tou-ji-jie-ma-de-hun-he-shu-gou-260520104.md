---
title: 'Draft Less, Retrieve More: Hybrid Tree Construction for Speculative Decoding'
title_zh: 少草稿，多检索：投机解码的混合树构建
authors:
- Yuhao Shen
- Tianyu Liu
- Xinyi Hu
- Quan Kong
- Baolin Zhang
- Jun Dai
- Jun Zhang
- Shuang Ge
- Lei Chen
- Yue Li
affiliations:
- Zhejiang University
- Qwen Applications Business Group of Alibaba
- University of Science and Technology of China
arxiv_id: '2605.20104'
url: https://arxiv.org/abs/2605.20104
pdf_url: https://arxiv.org/pdf/2605.20104
published: '2026-05-18'
collected: '2026-05-20'
category: LLM
direction: 投机解码 · 草稿树优化
tags:
- speculative decoding
- draft tree
- pruning
- retrieval
- inference acceleration
- hybrid tree
one_liner: 通过剪枝释放预算并用检索补偿，构建混合草稿树，打破稠密树与剪枝树的帕累托权衡
practical_value: '- **推理加速的预算重新分配**：将剪枝释放的 VRAM 与算力用于检索高预测性 token，适合电商搜索/推荐系统中低延迟生成场景的资源调度。

  - **无损、免训练的即插即用**：方法无需额外训练，可直接嵌入现有投机解码框架，对模型效果零损失，便于在 Agent 对话或推荐结果生成等在线服务中快速验证。

  - **检索与生成的深度融合**：通过拓扑嫁接将检索 token 无缝插入树结构，启发在生成式推荐中，利用外部知识库或高频序列库补充生成草稿，提升命中率。

  - **长上下文与大规模模型的稳定增益**：在 235B 大模型和 64K 长序列上表现突出，为电商大模型（如商品描述生成、多轮对话）的实时推理提供高效加速方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：投机解码（SD）通过草稿-验证范式加速 LLM 推理，但为提高接受率构建的稠密草稿树会带来严重的 VRAM 带宽和计算开销，实际加速受阻。动态深度剪枝能降低延迟，却丢弃了潜在有效分支，限制了接受率上限。关键在于：从稠密到剪枝的过渡释放了大量计算资源，存在补偿机会。

**方法**：提出 Graft 框架，将剪枝与检索耦合成互补操作。采用“先剪枝后嫁接”机制：首先剪除标准草稿树中的低概率分支，腾出计算预算；然后利用检索模型（如基于 BM25 或语义相似度）从上下文或语料中召回高预测性的 token，将其嫁接到剪枝留下的拓扑空洞中，形成混合树。整个过程训练-free 且无损，几乎无额外开销。

**结果**：在短上下文、长上下文及超大规模模型上均建立了新的帕累托前沿。短上下文场景最高加速 5.41×，在 Qwen3-235B 上比 EAGLE-3 平均加速比提升 21.8%；长上下文（64K）下 LLaMA3.1-8B 平均解码加速 3.22×，Qwen3-14B 上超越 EAGLE3-64K 达 16.6%。初步探索了块级草稿范式的扩展性。
