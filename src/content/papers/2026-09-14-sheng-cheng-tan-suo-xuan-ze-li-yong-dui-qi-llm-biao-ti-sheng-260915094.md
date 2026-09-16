---
title: 'Generate to Explore, Select to Exploit: Aligning LLM-based Headline Generation
  with Personalized Recommendation'
title_zh: 生成探索、选择利用：对齐 LLM 标题生成与个性化推荐
authors:
- Yi Chen
- Rufeng Cheng
- Qiang Xie
- Tao Li
affiliations:
- Baidu Inc., Beijing, China
arxiv_id: '2609.15094'
url: https://arxiv.org/abs/2609.15094
pdf_url: https://arxiv.org/pdf/2609.15094
published: '2026-09-14'
collected: '2026-09-16'
category: GenRec
direction: 生成式推荐 · 个性化标题生成
tags:
- LLM
- Recommendation
- Headline Generation
- Diversity
- GSPO
- Explore-Exploit
one_liner: 用 GSPO 训练 LLM 一次生成多样标题候选，再由实时反馈选择器做个性化利用，CTR 提升 2.57%
practical_value: '- **把“生成”与“选择”解耦**：不要让 LLM 做最终排序，而是让它生成 5-10 条语义多样的候选标题/文案；再用轻量实时
  ranker 根据用户即时行为、兴趣标签、上下文选择最优。这种架构能有效对抗用户画像噪声与 LLM 模式坍塌，电商标题、广告文案、push 文案均可复用。

  - **用 GSPO 组内相对优势替代 DPO/PPO 的绝对奖励**：组内归一化迫使候选差异化，避免生成重复安全文案；同时可让 LLM 单次推理生成整个候选集，显著降低推理成本。若在业务中做生成式推荐，可优先考虑组内对比训练，而非简单
  SFT 或逐样本 RLHF。

  - **分层奖励设计**：把 CTR 预测、faithfulness（质量模型/NLI）、novelty（编辑距离）、set diversity（IoU）拆开加权。质量护栏防止
  reward hacking 生成 clickbait；电商内容信任度要求高，这点尤其关键，建议显式加入事实一致性与安全约束。

  - **在线冷启动用 Confidence-Aware Thompson Sampling + 统计终止**：给新候选 Beta 先验，只有在小样本或高置信时才继续探索，并设置
  τ_max 安全预算；成熟后切到深度 ranker 融合用户画像、实时兴趣标签和语义嵌入，兼顾探索效率与长期收益。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
在推荐 feed 的展示层，静态标题往往只能迎合平均偏好，难以覆盖用户多模态、长尾的潜在兴趣。传统做法把个性化生成当作点估计任务，用 SFT 或 DPO 训练 LLM 生成单一最优标题；但在画像噪声和真实兴趣多峰的条件下，这类方法容易回归均值、发生模式坍塌，产生通用但无差异的安全文案，最终伤害长期 engagement。

### 方法关键点
核心思路是**解耦生成探索与选择利用**：LLM 只负责生成多样候选集，轻量实时模型负责个体化选择。
- **生成侧**：基于 Qwen3-14B，先用 30k 样本做 SFT，训练模型**单次推理生成 K 个不同标题**，显著降低推理成本。随后用 CTR Reward Model 提供吸引力信号，该 RM 融合 Qwen-Embedding 语义编码与展示偏置特征（长度、标点密度），在 800 万交互对上用 Bradley-Terry 损失训练。最后用 **GSPO（Group Sequence Policy Optimization）** 对齐：对采样的一组候选计算相对优势，组内归一化迫使模型生成差异化标题，避免坍缩到单一高收益模式。
- **分层奖励**：单个标题的效用 = CTR 预测 + 长度正则 + 质量约束（NLI 事实性）+ 新颖性（编辑距离与原始标题差异）；集合级再惩罚字符集 IoU 冗余，显式促进语义覆盖。
- **在线选择侧**：冷启动用 **Confidence-Aware Thompson Sampling**，候选服从 Beta 分布，通过统计终止条件控制探索成本；标题积累足够曝光后切换为深度 ranker，融合用户画像、20 个实时兴趣标签、粗粒度兴趣和候选语义嵌入，预测点击概率并选最优标题。

### 关键实验
在 MSR-50k（50k 资源、40+ 垂类）做离线评估，在 1 亿 DAU 商业平台做在线 A/B。相比原始静态标题：SFT-Only -1.50% CTR；SFT & UCB +1.37%；GSPO & UCB +2.28%；完整 GESE **+2.57% CTR、+0.87% dwell time、+0.79% 有效曝光**。离线指标上，GESE 将 Self-BLEU 从 18.02 降到 9.93，Distinct-N 56.20，NLI 80.17，CTR Score 11.38，均优于 120B 级大模型。消融显示去掉质量约束会出现 reward hacking（CTR Score 12.79 但 NLI 暴跌至 47.32），去掉多样性奖励 Self-BLEU 翻倍。

> 最值得记住的一句话：**让生成模型负责多样假设空间，让选择模型负责个体精确匹配，是噪声环境下生成式推荐的有效范式。**
