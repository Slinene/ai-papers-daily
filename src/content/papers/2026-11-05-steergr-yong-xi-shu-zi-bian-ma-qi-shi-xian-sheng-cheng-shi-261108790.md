---
title: 'SteerGR: Steering Generative Recommendation via Sparse Autoencoders for Controllable
  Game Discovery'
title_zh: SteerGR：用稀疏自编码器实现生成式推荐的可控游戏发现
authors:
- Sunkyung Lee
- Xiaokai Wei
- Da Long
- Hyunsik Jeon
- Jiajun Wu
- Rithwik Seth
- Jongwuk Lee
- Michelle Gong
- Gungor Polatkan
affiliations:
- Sungkyunkwan University
- Roblox Corporation
arxiv_id: '2611.08790'
url: https://arxiv.org/abs/2611.08790
pdf_url: https://arxiv.org/pdf/2611.08790
published: '2026-11-05'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · SAE 稀疏特征控制
tags:
- Sparse Autoencoder
- Generative Recommendation
- Controllability
- Feature Steering
- Interpretability
- Semantic ID
one_liner: 首次将 SAE 特征干预用于生成式推荐，实现文本定义游戏概念的可控推荐而无需重训模型
practical_value: '- 在已上线的生成式推荐模型上，可冻结参数并在中间层训练 Top-K SAE，将业务目标（如“低价好物”“应季新品”“高转化”）用文本嵌入与商品描述计算
  concept score，找到可干预稀疏特征。上线时仅对隐藏状态做加减增量，不涉及重训和索引更新。

  - 特征选择不要只看激活关联：候选可先用 Cohen''s d 或激活均值找，但最终必须在小流量验证集上实际放大/抑制，看目标商品 top-N 曝光份额变化（ΔE）来选择。论文显示
  Top-d 关联最强但控制效果只有 SteerGR 的 1/2.6–1/3。

  - 干预实现可用：放大时对 pre-activation 加 δ 后重新 Top-K；抑制时直接对 sparse code 做减法允许负值，再通过 decoder
  将增量写回原 hidden state，保留原重构误差。适合做在线控制旋钮。

  - 单概念单特征默认更稳，多特征会增加 off-target 变化；Semantic ID 比 Atomic ID 难控，若业务使用多级 RQ-VAE 做 item
  ID，需预留更强干预或 token-level 控制。干预强度 α 建议在 3/4 附近平衡目标满足与整体 recall/NDCG。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式推荐直接预测 item ID，但缺乏对推荐结果属性的显式控制。平台治理需要减少某类内容曝光，用户也有不体现在历史行为中的发现目标（如“找朋友合作”“恐怖体验”）。现有 LLM 的 SAE steering 已可解读并控制输出，但尚未连接到生成式推荐。SteerGR 的目标：用文本定义玩法概念，通过 SAE 稀疏特征干预，在不重训推荐模型的前提下控制目标概念曝光。

**方法关键点**
- 固定已训练的 GR 模型（Atomic ID / Semantic ID），在其第 3 个 Transformer block 输出训练 Top-K SAE，编码隐藏状态到 3072 维稀疏特征（k=32/64）。
- 概念定义与 grounding：LLM 生成 12 个跨 genre 的玩法概念（build, compete, traverse 等），用 text-embedding-3-large 嵌入概念定义与游戏描述，计算标准化 cosine similarity 得到游戏概念分；用户分取最近 20 次交互游戏平均。
- 特征发现与选择：按用户概念分 quartile 分高低组，对 SAE pre-activations 计算 Cohen's d 得到候选特征；再在验证集上实际放大每个候选，选使目标概念 top-10 份额增加最多的特征。
- 干预：放大时 pre-activation 加 ασ 后重新 TopK；抑制时直接对 sparse code 减去 ασ 允许负值，通过 decoder 将增量加回原隐藏状态。

**关键结果**
- 与最高 Cohen's d 的 Top-d、随机特征相比，基于干预效果选择的特征明显更可控。Atomic ID 放大使 target share 5.75%→7.95% (+38.4%)，抑制至 4.27% (-25.6%)；Semantic ID 放大 6.70%→7.46% (+11.5%)，抑制至 6.14% (-8.3%)。
- 12 个概念中，Atomic ID 放大平均提升 113.6%、抑制平均下降 42.5%；Semantic ID 分别为 +24.6%、-13.7%，表明 Semantic ID 可控性弱于 Atomic ID。
- 对 concept-matched 用户，放大使 R@10 提升 2.4%/2.3%，抑制使 R@10 下降 10.0%/1.9%；干预强度 α 过大（8）会使整体 NDCG 下降 7.3–42.9%，通常 α=3/4 概念匹配收益最好。

**最值得记住的一句话**
强概念关联不等于强控制效果，SteerGR 的核心经验是必须基于“干预后目标概念曝光变化”而不是激活差异来选择可控制特征。
