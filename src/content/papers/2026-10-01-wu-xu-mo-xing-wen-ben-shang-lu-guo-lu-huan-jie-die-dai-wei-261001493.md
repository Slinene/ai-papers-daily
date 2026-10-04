---
title: 'No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning
  Collapse'
title_zh: 无需模型：文本熵率过滤缓解迭代微调崩溃
authors:
- Lewis Mitchell
affiliations:
- Adelaide Data Science Centre, University of Adelaide
- School of Mathematical Sciences, University of Adelaide
arxiv_id: '2610.01493'
url: https://arxiv.org/abs/2610.01493
pdf_url: https://arxiv.org/pdf/2610.01493
published: '2026-10-01'
collected: '2026-10-04'
category: Training
direction: 迭代微调多样性维护与数据过滤
tags:
- Model Collapse
- Entropy Rate
- Data Filtering
- Iterative Fine-Tuning
- QLoRA
- Diversity
one_liner: 提出基于 Kontoyiannis 熵率估计器的纯文本过滤器，在不访问模型的情况下有效提升迭代微调多样性
practical_value: '- **合成数据微调管道可直接引入熵率过滤**：在生成式商品描述、搜索 query 或广告文案的迭代训练中，用 Kontoyiannis
  熵率估计器对合成样本打分，过滤低多样性样本，避免模型输出重复化；无需调用模型 API 或持有 logprob，工程开销低，适合无模型推理权限的场景。

  - **多 Agent 系统多样性监控**：将文本熵率作为多智能体生成内容的实时监控指标，当熵率持续下降时触发干预（如提高采样温度或注入新提示），防止 Agent
  间输出趋同。

  - **替代传统 logprob-based 过滤**：论文显示 logprob 过滤在该任务上无显著收益，业务中若已使用 perplexity 等模型依赖的过滤，可尝试替换为纯文本熵率过滤，可能获得更好的多样性且更轻量。

  - **少样本验证结论**：熵率估计器跨域适用，可作为生成式推荐模型微调时的通用质量代理，用于快速评估数据集的多样性是否充足。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：迭代微调合成数据导致模型崩溃，输出多样性收窄、罕见模式丢失，最明显的迹象是短语级重复。现有缓解方法要么需要模型 log-probabilities、外部 oracle，要么持续访问真实人类数据。

**方法关键点**：采用非参数 Kontoyiannis 熵率估计器 $h_k$，完全基于原始文本的匹配长度统计计算，无需任何模型。在六代 Llama-3.1-8B QLoRA 崩溃实验中，将 $h_k$ 作为训练数据过滤器，与最成熟的 logprob-based 过滤基线对比。

**关键结果数字**：logprob 过滤在所有文本多样性指标上无显著收益（$p>0.23$）；而 $h_k$ 过滤带来 +42% 唯一 trigrams、+30% 词汇量、-19% 重复，均 $p<0.001$。跨 4 个领域、2 个温度、2 组生成器-评分器模型对、1520 篇生成文档验证：$h_k$ 是跨域熵代理（$\beta=0.924$，$R^2=0.746$）和崩溃检测器（$\rho=+0.454$，$p<0.0001$）。
