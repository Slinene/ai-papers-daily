---
title: Token-Level Credit Assignment Optimization for Generative Document Retrieval
title_zh: 生成式文档检索的 Token 级信用分配优化
authors:
- Xinpeng Zhao
- Yang Liu
- Ran Chen
- Xinyu Ma
- Daiting Shi
- Pengjie Ren
- Zhumin Chen
- Zhaochun Ren
- Xin Xin
affiliations:
- Shandong University
- Peking University
- Baidu Inc.
- Leiden University
arxiv_id: '2608.12049'
url: https://arxiv.org/abs/2608.12049
pdf_url: https://arxiv.org/pdf/2608.12049
published: '2026-08-12'
collected: '2026-08-13'
category: GenRec
direction: 生成式检索 · Token 级信用分配
tags:
- Generative Retrieval
- Token-Level Credit Assignment
- RL
- GRPO
- DocID
- Semantic ID
one_liner: 提出 TCA，用 gold hidden-state 轨迹对齐赋予每个 DocID token 细粒度奖励，并以 GRPO 位置归一化优化生成式检索。
practical_value: '- 若在做生成式 item 检索 / semantic ID 生成，不要把 RL reward 当 sequence-level
  标量广播到所有 token；可复用 TCA：冻结 SFT 参考模型，缓存 gold item ID 的 decoder hidden states，用当前生成
  hidden state 与 gold 的余弦相似度作为 token 级 reward，再加 exact-match bonus 与长度惩罚，轻量且直接对齐解码轨迹。

  - 用 GRPO 时，优势估计采用按解码位置在候选组内做标准化，而不是学习 value function；这在离散、trie 约束的 ID 空间中更稳定，尤其适合电商类目树或语义
  code 类结构化 ID。

  - 保留 constrained decoding / trie 约束；没有约束的 rollout 会生成大量非法或低质量 ID，token 奖励噪声大，NQ-PQ
  上 R@1 掉 4.84。业务中生成类目路径或 SKU ID 时，RL 采样和推理阶段都要做合法前缀/路径约束。

  - KL 正则强度按 ID 类型区分：lexical / title-URL 类 ID 用很小 KL(0.01) 防止语言模式漂移；semantic / PQ
  code 类 ID 敏感，KL=0 效果最好。电商场景若生成长尾商品标题或 ID，可按 ID 是否语义化调这个超参。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式检索将文档检索建模为自回归生成 DocID，但训练目标存在粒度错配：评价是文档级相关性，而训练是 token 级 MLE 或 sequence-level RL reward。后者把同一个文档级反馈赋给所有 token，难以识别哪个 token 决策真正导致成功或失败，因此需要 token 级信用分配。

**方法关键点**  
- 将 DocID 生成视为序列决策：state = query + 部分 DocID，action = next token，最终结果由完整 DocID 映射的文档相关性决定。
- 提出 TCA：用冻结的 SFT reference model 缓存 gold DocID 的 decoder hidden state 轨迹；对策略生成的候选，在相同解码位置计算当前 hidden state 与 gold hidden state 的余弦相似度作为 token 级 trajectory reward，并加 exact-match bonus 和长度惩罚。
- 奖励形式：`r = cosine(h_gen, h_gold) + length_penalty + exact_match_bonus`，不需要额外 reward model。
- TCA 与优化器无关：TCA-GRPO 将 token reward 按解码位置在候选组内标准化得到 advantage，不学 value function；TCA-PPO 用 learned value head + GAE。
- 训练两阶段：先 SFT 初始化，再 RL post-training；rollout 和推理均使用 trie-based constrained decoding 保证合法 DocID 空间。

**关键实验**  
在 MS MARCO document 和 NQ320k 上，使用 TU（Title+URL）和 PQ（Product Quantization）两种 DocID，对比 BM25、DPR、DSI、Ultron、GenRRL、DDRO 等。TCA-GRPO 在 MS TU 上 R@1 39.60 / MRR@10 51.10，超过 DDRO 38.24/50.33；在 NQ PQ 上 R@1 50.02 / MRR@10 56.10，超过 DDRO 48.10/54.32。与 sequence-level GRPO 相比，token 级奖励在 NQ PQ 上 R@1 再提升 1.22。TCA-PPO 有效但不如 GRPO 稳定。消融显示 constrained decoding 对 NQ-PQ R@1 提升 4.84，group size 4-8 足够，TU 适用 KL=0.01，PQ 适用 KL=0。

**最值得记住的一句话**  
把信用分配到与生成决策相同的 token 粒度，用 hidden-state 轨迹对齐 + 位置归一化的 GRPO 优势估计，能稳定提升生成式检索的 top 精度。
