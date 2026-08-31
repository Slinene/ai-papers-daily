---
title: 'PAWBench: How Far Are We from Probabilistically Aligned World Modeling?'
title_zh: PAWBench：视频世界模型概率对齐差距基准
authors:
- Yuandong Pu
- Le Zhuo
- Sayak Paul
- Gabriel Jorge Menezes
- Avram Đorđević
- Shiyang Li
- Yifan Zhou
- Bin Fu
- Wenlong Zhang
- Junjun He
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Krea AI
- Hugging Face
- Shanghai Innovation Institute
arxiv_id: '2608.27345'
url: https://arxiv.org/abs/2608.27345
pdf_url: https://arxiv.org/pdf/2608.27345
published: '2026-08-26'
collected: '2026-08-31'
category: Eval
direction: 世界模型评估 · 概率对齐
tags:
- World Model
- Video Generation
- Probabilistic Alignment
- Benchmark
- Evaluation
- Stochastic Sampling
one_liner: 构建50场景基准评估11个视频生成系统，发现无一能稳定复现物理行为的参考概率分布
practical_value: '- 在生成式推荐或用户行为模拟中，不能只看单次生成结果的 plausibility；应增加分布级评估：对同一 context 重复采样，比较生成结果的类别/行为分布与真实分布的校准误差，捕捉模式坍塌与多样性缺失。

  - PAWEval 的 outcome-level 思路可直接迁移：把高维生成内容映射到可判定的低维结果空间（如点击/转化/浏览路径类别），再做经验分布对比，避免像素级评估高成本且难判校准。

  - 论文测试了语言 prompt、初始噪声、模型训练对预测分布的干预，对推荐系统里用 prompt 工程、采样温度/噪声、RLHF/DPO 调整生成分布有参考价值：应衡量这些干预对分布形状的迁移，而不仅是
  top-1 指标变化。

  - 若电商团队在训练 LLM/视频生成式的用户轨迹或广告创意世界模型，要注意当前模型即使内容真实，也未必覆盖全部有效行为；需要加入分布正则或多样性约束，避免只学到高频、低风险的输出。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频生成模型越来越被视为世界模型，但许多物理过程在相同初始观测和动作下存在多种有效演化方式。因此，世界模型不仅要生成单条合理轨迹，还要复现可能行为分布。现有评估只检查单视频是否 plausible，未检验重复生成是否恢复正确分布。

**方法关键点**：将这种分布级要求形式化为 probabilistic alignment。构建 PAWBench，包含 50 个物理场景，用 PAWEval 协议把同一初始条件下的多次视频 rollout 转换为可能物理行为的经验分布，与参考概率分布比较。评估覆盖 11 个当前视频生成系统，并进一步检验语言提示、初始噪声采样、模型训练三种干预手段能否重塑模型预测分布。

**关键结果**：在 50 个场景、11 个系统中，没有模型能一致匹配参考概率，同时覆盖全部有效行为范围；也就是说，现有视频生成器在分布校准与多样性覆盖上仍有明显差距。三种干预中，初始噪声和训练对分布有一定重塑作用，但仍未达到概率对齐。
