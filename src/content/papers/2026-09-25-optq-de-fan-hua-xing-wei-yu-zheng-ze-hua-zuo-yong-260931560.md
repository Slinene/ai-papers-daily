---
title: Generalization behavior of OPTQ and the role of regularization
title_zh: OPTQ 的泛化行为与正则化作用
authors:
- Erin George
- Rayan Saab
affiliations:
- University of California, San Diego
arxiv_id: '2609.31560'
url: https://arxiv.org/abs/2609.31560
pdf_url: https://arxiv.org/pdf/2609.31560
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 模型量化泛化理论
tags:
- OPTQ
- quantization
- generalization
- regularization
- stochastic OPTQ
one_liner: 为 OPTQ 及其随机变体建立泛化误差上界，并提出更优的正则化参数选择
practical_value: '- 在做 LLM 部署量化（如推荐系统的排序大模型、Agent 规划模型做 INT4/INT8 量化）时，OPTQ 校准集的正则项
  λ 不要沿用默认值，可参考文中理论选择方式，可能显著降低线上量化误差。

  - 若业务场景数据分布随时间漂移（电商大促、季节性变化），可考虑 stochastic OPTQ 这类随机化量化，其泛化误差界不依赖特定校准集，对分布鲁棒性更强。

  - 论文提供量化误差与校准集大小、分布匹配的理论关系，可用于指导校准集构建：尽量保证校准集与线上分布同源、样本量足够，避免离线效果好但线上掉点。

  - 总体学术性较强，除上述适用点外，大部分理论结果难以直接落地；业务团队可关注其 λ 选择建议或对量化工具的超参数默认值做调整实验。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：大型神经网络存储和推理成本高，量化是重要压缩手段。OPTQ 是渐进量化算法，在给定校准数据集上最小化平方量化误差，但校准集误差与测试分布泛化误差之间关系缺乏理论分析，正则化项 λ 的选择也常靠经验。

**方法关键点**：研究 OPTQ 及随机变体 stochastic OPTQ 的泛化行为，在测试点来自固定分布的设定下推导期望平方误差上界。第一个结果将泛化误差与校准数据集（同分布独立样本）误差关联；第二个结果对任意足够好的分布约束 stochastic OPTQ 的泛化误差，且不依赖具体校准集。两个结果中正则项 λ 起关键作用，基于理论洞察提出新的 λ 选择推荐。

**关键结果**：新的 λ 选择在实验中优于文献中先前推荐，验证了理论指导的有效性。
