---
title: Evolving Semantic Indexes for Generative Retrieval
title_zh: 进化语义索引用于生成式检索
authors:
- Jinming Nian
- Jyun-Yu Jiang
- Henry Tsai
- Yi Fang
- Zhirong Liang
affiliations:
- Santa Clara University
- Coupang
arxiv_id: '2610.28568'
url: https://arxiv.org/abs/2610.28568
pdf_url: https://arxiv.org/pdf/2610.28568
published: '2026-10-20'
collected: '2026-10-21'
category: GenRec
direction: 生成式推荐 · 语义索引进化
tags:
- Generative Retrieval
- Semantic ID
- Evolutionary Search
- Proxy Evaluation
- LLM Mutator
- RQ-VAE
one_liner: 用 LLM 进化搜索自动优化生成式检索的语义索引，以 1M 参数 proxy 加速评估，在多个数据集显著提升召回率
practical_value: '- **用小 proxy 模型做快速评估**：训练 1M 参数的 GPT-2 只需 20 分钟，替代 1B 目标生成器 5 小时，单次评估成本降低
  15×。在电商场景中，若目标生成器训练周期以周计，可以用小模型先过滤候选 SID/索引方案，大幅节省试错成本。

  - **联合优化 SID 构建与冲突处理**：联合进化比单独进化 SID 或冲突处理提升更显著（NQ R@100 +4.75 vs +1.58），提示在实际生成式推荐系统中，应把语义
  token 的分组方式和同组内 disambiguation token 作为整体设计，而不是固定一个再调另一个。

  - **使用可执行程序搜索自动发现索引规则**：让 LLM 直接突变 SID 构建代码（如残差量化的距离度量、codebook 大小、是否加入 query 对齐损失），可以自动发现非手工设计的有效策略，例如
  max-cosine 残差分配、doc+query 混合向量等，适合业务中探索 semantic ID 生成策略。

  - **注意 proxy 转移性的边界**：代理评估对语义索引有效，但对训练目标等跨尺度不稳健。在业务上，如果要用小模型代理大模型评估，需要先在小范围校准代理与目标的秩相关性，并区分“改输入/索引”还是“改优化器/损失”，后者要谨慎使用代理。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式检索（GR）将文档/商品检索视为自回归生成离散语义标识符（SID）。SID 设计（构建、冲突处理、训练目标、解码）高度影响检索质量，但这些离散且相互依赖的选择无法通过梯度端到端优化，通常依赖手工设计。LLM 驱动的进化程序搜索可以自动化探索这些组件，但每次评估候选 SID 都需要训练下游生成器，成本极高（1B 目标生成器单次 5 小时）。

## 方法关键点
- 用 AdaEvolve 进化搜索在可执行代码层面突变 SID 构建程序，使用本地部署的 gemma-4-31b-it 作为 mutator，不依赖商业 LLM API。
- 使用约 1M 非嵌入参数的 GPT-2 proxy decoder 替代 1B 目标生成器做快速反馈，单次评估从 5 小时降到 20 分钟，加速 15 倍。
- 搜索过程中，候选程序输入固定 document embeddings 和训练 qrels，输出每个文档的 SID；mutator 只接触训练数据，测试集不可见。
- 候选程序执行有 gatekeeping：碰撞率门限（SID 搜索 <50%，联合搜索 <5%）、执行超时 2 小时、最多 20 次内层修复。
- 进化搜索可针对不同范围：仅 SID 构建、联合 SID+冲突处理、仅碰撞处理、训练目标、全流程。

## 关键结果
- NQ320K 上联合进化 SID 构建和冲突处理，Recall@1 从 55.8% 提升到 59.3%，Recall@100 从 85.8% 提升到 90.6%。
- MSMARCO300K 上 Recall@100 从 79.70% 提升到 82.55%；多语言电商数据集上相对 BM25 的 Recall@100 增益从 +49.01 提升到 +50.66 个百分点。
- 在 21 个 NQ SID 程序上，proxy 与 1B 目标生成器的 Recall@100 Spearman 相关性 ρ=0.90，证明小 proxy 对语义索引评估可靠。
- 但 proxy 转移性取决于被优化组件：语义索引改进可靠迁移，进化训练目标时 proxy 提升但目标下降（目标 R@100 从 85.82% 降至 84.46% 或 76.12%）。

## 最值得记住的一句话
代理评估的有效性不是普遍的，必须针对被优化的组件进行校准：语义索引改动对 proxy 和目标都友好，但训练目标改动可能只对 proxy 有利。
