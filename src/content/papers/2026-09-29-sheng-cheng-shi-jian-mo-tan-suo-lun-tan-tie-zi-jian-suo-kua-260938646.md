---
title: Exploring Forum Post Retrieval with Generative Modeling
title_zh: 生成式建模探索论坛帖子检索：跨平台语义 ID 迁移
authors:
- Yang Li
- Yaguang Liu
- Heng Liu
- Shengbo Guo
- Samson Komo
- Jane Kou
- Yulian Zhou
- Gang Yang
- Shubhojeet Sarkar
- Gaurav Chakravorty
affiliations:
- William & Mary
- Meta
arxiv_id: '2609.38646'
url: https://arxiv.org/abs/2609.38646
pdf_url: https://arxiv.org/pdf/2609.38646
published: '2026-09-29'
collected: '2026-10-01'
category: GenRec
direction: 生成式推荐 · 跨平台语义 ID 迁移
tags:
- Generative Recommendation
- Semantic ID
- RQ-VAE
- Cold Start
- LLM4Rec
- GRPO
one_liner: 用 3B 指令模型生成跨平台语义 ID，系统验证 SID 深度、历史渲染与 RL 后训练对冷启动推荐的影响
practical_value: '- 冷启动新场景：直接复用已有大语料训练好的 RQ-VAE SID，不必为新 surface 训 tokenizer；用 prefix-based
  SID 跨平台迁移，能继承 item vocabulary，适合电商新频道/广告新位等冷启动。

  - SID 层数选择：层数决定命中难度和输出空间。3 层 SID 在 HR@10 上比 4 层高 2.2×，但碰撞率更高；如果下游有精排/ rerank 可解歧，优先选粗粒度
  SID 做召回，吞吐和命中联合更优。

  - 少样本 prompt 工程：在 history 里用 "liked <a_1><b_1><c_1>" 动词化，几乎零成本，比继续预训练对齐还划算；应优先做
  prompt 动词化，预算允许再做 text↔SID 对齐。

  - 模型容量不是瓶颈：3B 与 12B 效果几乎相同，算力应花在 SID grounding 和训练步数上。GRPO 在短序列生成式推荐中 reward 过于稀疏，约
  95% rollout 组无梯度；若要上 RL，需先按 prefix 重叠设计分级语义 reward，并把 non-zero advantage ratio 作为第一诊断指标。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Facebook Forum 是面向重度 Groups 用户的新独立应用，互动数据太少，无法从零训练生成式推荐模型。可行的路径是从更大的 Groups 互动语料迁移行为信号，并复用跨平台 Feed 数据训练好的 RQ-VAE 语义 ID，让新 surface 继承 item vocabulary。

### 方法关键点
- **编码**：用跨平台 RQ-VAE 把帖子 embedding 量化为 3/4 层、每层 2048 codes 的前缀式 SID；粗到细的 prefix 结构天然支持跨域迁移。
- **对齐**：利用生产环境免费的 text↔SID 对做双向继续预训练，让 SID embedding 与自然语言语义对齐；对全序列算 LM loss，不做 prompt mask。
- **SFT**：用 Llama-3.2-3B-Instruct 从用户 engagement history 生成下一正互动 SID；history 混入弱信号作上下文，仅强信号作目标；prompt 可选择带动作动词渲染。
- **RL 后训练**：从最佳 SFT checkpoint 出发跑 1000 步 GRPO，reward 分 accuracy 和 accuracy+ranking（beam）两种。

### 关键实验与数字
在 86,648 用户的 hold-out 集上评估 HR@3/5/10 和 NDCG@10：
- **SID 深度主导**：3 层 HR@10 为 0.0667，4 层为 0.0303，相差 2.2×；但 3 层碰撞率更高，需结合下游 ranking 理解 trade-off。
- **动词化 vs 对齐**：动词化 history 相对提升约 2%，继续预训练相对提升约 4%；两者互补，但无 CPT 的动词化 prompt 比有 CPT 的 raw SID 更好，说明先改 prompt 更划算。
- **历史长度**：固定 10 优于固定 50（HR@10 0.0667 vs 0.0544）和变长 5–25（0.0492）；更长历史在固定训练预算下反而降低精度。
- **模型容量无效**：12B Gemma 与 3B Llama 几乎无差别（HR@10 0.0661 vs 0.0667），4B Qwen 反而更低；瓶颈在 6144 token 的新词汇学习而非参数。
- **RL 失败**：GRPO 后训练未提升且 HR@10 略降；约 95% rollout 组没有命中，advantage 为零，说明 reward 过度稀疏，短序列生成式推荐不适合直接用当前 RLHF 方案。

### 最值得记住的一句话
跨平台复用 prefix-based SID、固定短历史、动词化 prompt、3B 模型已经够用；SID 深度是首要决策，RL 后训练在命中率低时应先 densify reward。
