---
title: 'StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with
  Diffusion-Based Stitching'
title_zh: StitchRAG：基于扩散拼接构建紧凑且保留证据的 RAG 上下文
authors:
- Minsang Kim
- Junpyo Lim
- Heeje Cho
- Seungjun Baek
affiliations:
- Korea University
- SK Telecom
arxiv_id: '2611.22766'
url: https://arxiv.org/abs/2611.22766
pdf_url: https://arxiv.org/pdf/2611.22766
published: '2026-11-17'
collected: '2026-11-18'
category: RAG
direction: RAG 上下文压缩与扩散式拼接
tags:
- RAG
- Context Compression
- Text Diffusion
- Dynamic Budgeting
- Anchor Selection
- Open-Domain QA
one_liner: 用效用最大化动态分配各检索段落保留比例，混合锚点选句后由扩散模型拼接证据，兼顾压缩率与事实保真
practical_value: '- 在电商 RAG 导购/商品问答里，检索回的详情页、用户问答、参数段质量参差，可以复刻动态预算：用 LLM 判断段落是否对回答有用，把
  yes/no logprob 归一化成相关性 R，再按 `R log(1+r) - βr²` 求每段保留比例；高相关段落多保留，低相关段落只留关键句，替代统一
  top-k 截断。

  - 锚点选句适合商品/广告文案压缩：混合 LLM 生成的答案候选 span（语义、属性）和 TF-IDF 稀有词（型号、价格、规格、活动词），优先保留含锚点句子，保证关键实体不丢，同时保持句子完整，比
  token 级删减更可读。

  - 多文档拼接建议用 diffusion infill 或双向注意力，不要用自回归 left-to-right 生成：只对句间/段间插入的 mask token
  去噪，证据 token 冻结，可避免事实漂移；工程上段内和段间要设不同 mask 预算（论文为 2 vs 7），并做成批量并行去噪。

  - 效果上，该方法在 Top-K 从 10 增到 30 时仍保持稳定，适合检索噪声较大的电商长尾 Query 场景；延迟约 10.6s，比 IRCoT/DRAG
  便宜，接近单轮 RAG。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：RAG 检索上下文通常较长且含噪声，增加推理成本并可能损害答案质量；现有压缩方法多采用固定比例或 token 级删减，容易破坏句子可读性和跨段落证据链。StitchRAG 将“每段保留多少”建模为成本感知的效用最大化，并在句子级保留证据后用扩散模型拼接，构建紧凑且忠实的上下文。

**方法关键点**：
- 对每个检索段落 x，定义保留比例 r，目标为 `max R(x,q)·log(1+r) - βr²`；R(x,q) 由 LLM 对“该段是否有助于回答问题”的 yes/no logits 归一化得到，β=0.25，闭式解为 `r*=min(½(√(1+2R/β)-1),1)`，相关性越高保留越多。
- 混合锚点抽取：`A = A_AR ∪ A_TFIDF`。A_AR 来自 LLM 以 query+段落生成答案候选中的关键 span；A_TFIDF 来自 query 与段落间高 TF-IDF 词项，保障罕见实体和词法线索。
- 预算内选句：在 r*|x| 的 token 预算下，优先保留含锚点句；不足时补充含 query 关键词或靠前句子，删除其余句，保持句子级完整。
- 扩散拼接：在相邻句之间插入 mask token，数量由 Jaccard 语义重叠决定，段内最大 2、段间最大 7；使用 text diffusion（LLaDA/Dream）仅对 stitching token 去噪，原证据 token 冻结，防止事实漂移。
- 工程优化基于 Fast-dLLM 的动态 remasking，批量 GPU 并行加速约 1.3×。

**关键实验**：在 HotpotQA、NQ、TriviaQA、PopQA、2Wiki 五个开放域 QA 上，StitchRAG 在 10 个指标中 6 个第一、其余第二；平均压缩到原始长度 72.29%，对比 RAG 在 HotpotQA 上 +2.4 EM/+2.3 F1，在 NQ 上 F1 +2.1，TriviaQA 上 EM +1.4/F1 +1.8。Top-K 从 10 增至 30 时，RAG 平均 F1 从 48.1 降至 45.1，而 StitchRAG 稳定在 51.2。消融显示动态预算、AR+TF-IDF 混合锚点、扩散拼接均带来稳定收益；自回归 stitching 明显退化，扩散拼接更适配受约束的文本编辑。延迟为 10.62s，低于 IRCoT/DRAG 的 24.66/27.39s。

最值得记住的一句话：RAG 压缩不应固定比例，而应把每段保留量建模为“相关性收益减预算成本”，在句子级保留关键锚点后，用只对 mask 位置去噪的扩散拼接重建连贯上下文，并冻结证据 token，才能同时获得紧凑性、可读性和事实保真。
