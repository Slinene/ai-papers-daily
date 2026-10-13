---
title: Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer
  Selection
title_zh: 语言模型何时该弃权：策略学习与校准答案选择
authors:
- Juan Terven
- Diana-Margarita Córdova-Esparza
- Ruben Gomez
- Carlos Miranda Rocha
- Julio-Alejandro Romero-González
- Edgar Chavez-Urbiola
affiliations:
- CICATA Qro., Instituto Politécnico Nacional, México
- Facultad de Informática, Universidad Autónoma de Querétaro, México
arxiv_id: '2610.13821'
url: https://arxiv.org/abs/2610.13821
pdf_url: https://arxiv.org/pdf/2610.13821
published: '2026-10-09'
collected: '2026-10-13'
category: LLM
direction: LLM 弃权策略与答案选择校准
tags:
- abstention
- selective prediction
- calibration
- policy learning
- LLM
- uncertainty estimation
one_liner: 在 Qwen3-14B 事实问答上，独立答案选择器比模型置信度过滤显著提升效用，但跨数据集可靠弃权仍未解决
practical_value: '- 在业务中若想让 LLM 客服/导购助手“不确定时闭嘴”，可以优先训练一个独立的答案选择器（用模型置信度、问题难度等特征），而不是直接微调生成策略；论文显示选择器比直接对模型概率做阈值过滤更稳定。

  - 奖励设计要显式惩罚错误答案，避免只用正确率：若错误和弃权得分相同，模型会倾向乱猜；引入较大错误惩罚能改变弃权行为。

  - 上线前务必在目标分布上重新校准：论文中 TriviaQA 有效的方法在 NQ-Open 上仍低于“全部弃权”，说明弃权策略跨数据域泛化差，不能拿一个公开基准的阈值直接用于电商/广告流量。

  - 对推荐/生成式场景，可以为每个生成结果同时输出 confidence 或单独跑一个弃权打分器，只展示高于阈值的推荐理由、商品知识回答，降低事实错误带来的负面影响。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 在事实问答上即使不知道答案也常给出貌似合理的回答，因此需要学会何时回答、何时弃权。现有思路包括训练模型自身做出弃权决策，或训练独立组件审查答案；两种干预在特定模型和预算下孰优孰劣并不明确。

**方法关键点**：论文在 Qwen3-14B 上研究事实问答的弃权问题，定义效用函数：正确答案给正奖励、错误答案给惩罚、弃权为中性。比较两种路线：一是通过策略学习（含强化学习变体）改变模型自身的选择行为；二是保持生成模型固定，训练一个独立答案选择器，根据模型置信度等特征决定是否展示答案。实验使用 TriviaQA 和 NQ-Open，按 exact-match 评分，并采用三个训练种子和两个 held-out 置信度阈值评估稳健性。

**关键结果**：在 TriviaQA 上，学习到的答案选择器相比原始模型校准置信度过滤器显著提升 threshold-averaged utility：平均覆盖率从 20.2% 提升到 30.9%，被评分答案的整体错误率从 23.0% 下降到 14.5%。测试的强化学习改动没有带来一致增益。在 NQ-Open 上，选择器虽然优于置信度过滤器，但仍然低于“全部弃权”的效用，说明跨数据集可靠弃权尚未解决。部分人工复核保留了 TriviaQA 的结论。整体上，该设置支持学习答案选择器，但可靠弃权在不同数据集间仍存在挑战。
