---
title: Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval
title_zh: 生成式检索中范式、标识符与解码的解耦分析
authors:
- Hicham Randrianarivo
- Logan Renaud
- Alexia Allal
affiliations:
- Artefact Research Center
arxiv_id: '2610.08716'
url: https://arxiv.org/abs/2610.08716
pdf_url: https://arxiv.org/pdf/2610.08716
published: '2026-10-06'
collected: '2026-10-07'
category: GenRec
direction: 生成式检索 · Semantic ID · 扩散解码
tags:
- Generative Retrieval
- Diffusion Models
- Semantic ID
- Decoding
- Controlled Study
- Document Retrieval
one_liner: 控制 AR/扩散、docid 与解码，证明解码可改变扩散 Hit@1 6.6-13.7 点，one-pass scoring 近似最优
practical_value: '- one-pass scoring：用全 mask docid 一次前向得到 L×K 概率表，按每个候选 docid 的 code
  概率求和打分，免迭代去噪，可直接作为扩散生成式推荐/检索的 top-K 召回或粗排；在本文 11/12 设置中打平或超过 generate-and-match，工程上非常适合低延迟场景。

  - 训练 recipe 必须按范式独立调：AR 的高 weight decay、线性衰减直接用于扩散会使模型输出常数；扩散需要更低 weight decay、常数学习率、warmup
  等。落地时不要复用 AR 训练配置。

  - random ID 在训练查询覆盖充分时保留 RQ 的 83-90% Hit@1，说明语义层级结构并非核心收益来源；若业务训练曝光已足够，可先用简单 ID
  或轻量语义 ID，把资源投入解码与训练稳定性。

  - PQ/独立 code 在生成 miss 后 gold 更容易留在候选里（恢复率约为 RQ 的 2.3 倍），且更适合并行解码；若采用 block diffusion
  或 MDLM，可优先考虑 PQ-like 或维度独立的 semantic ID，并搭配 one-pass/chain-rule 解码。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

动机
生成式检索中，DiffuGR、MaskGR 等用扩散替代 AR，但同时改变 identifier、训练 recipe 和 decoding，导致 Hit@1 差异无法归因到生成范式本身。现有结论混杂，缺少公平受控比较。

方法关键点
- 在 NQ320K 和 MS300K 上固定 docid 长度 16、codebook 大小 512、训练预算 16M examples，交叉训练 AR（T5 1.1 base, 260M）、MDLM、BD4、BD8（共享 DiT 架构, 182M）。
- Identifiers 包括 RQ（残差量化）、PQ（乘积量化）、随机 ID、RQ level 重排；query 作为 clean prefix 条件化扩散模型。
- 解码数种：AR 用 trie beam；扩散 ladder 包含 one sample、argmax+code matching+rerank（generate-and-match）、best-of-8、one-pass scoring，以及 chain-rule rescoring top20。

关键结果
- 仅改解码，扩散 Hit@1 从 one sample 到最佳解码上升 6.6-13.7 点；raw generation 精确命中仅 14-21%，code matching 贡献大部分命中。
- one-pass scoring 在 11/12 设置中打平或超过 generate-and-match；NQ320K 上 MDLM one-pass 的 Hit@100 超过 AR beam 5.2 点，说明其覆盖面更深。
- AR 仍 Hit@1 领先，但 NQ320K 上领先来自模型而非 beam：greedy AR 与 beam 差距不足 1 点。
- random ID 在 NQ320K 保留 RQ 的 83-90% Hit@1，表明模型主要记忆 query-docid 映射；MS300K 上随机码不收敛，内容码学习更快。
- 最佳解码下 AR 与扩散的 PQ-RQ 差仅 1.5 点，低于 ±2 阈值，不支持并行解码天然偏好 PQ；但 PQ 在 miss 后 gold 仍在候选的恢复率约 2.3 倍于 RQ。

值得记住：解码策略是扩散生成式检索最大的可调杠杆，公平比较生成范式必须固定在每个范式自己的训练配方和最佳解码上。
