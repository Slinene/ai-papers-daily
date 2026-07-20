---
title: 'BayesPO: Bayesian Prompt Optimization via Parallel-Tempered Gradient-Guided
  Discrete MCMC'
title_zh: 贝叶斯提示优化：基于并行回火梯度引导离散MCMC的后验采样
authors:
- Junjie Zhou
- Zhijian Ou
affiliations:
- Speech Processing and Machine Intelligence (SPMI) Lab, Tsinghua University
arxiv_id: '2607.16001'
url: https://arxiv.org/abs/2607.16001
pdf_url: https://arxiv.org/pdf/2607.16001
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: LLM Prompt 优化
tags:
- Bayesian prompt optimization
- MCMC
- LLM
- Gradient-guided discrete sampling
- Parallel tempering
- Prompt optimization
one_liner: 将提示优化建模为离散提示令牌上的贝叶斯后验采样，用梯度引导MCMC与并行回火提升指令归纳准确率
practical_value: '- 提供一种原则性后优化工具：给定初始提示和少量示例，可通过后验采样自动微调提示，适合电商/推荐场景中优化查询改写、商品描述生成等LLM指令。

  - 贝叶斯框架可输出多个候选提示，支持集成或不确定性估计，提升生产环境鲁棒性。

  - 梯度引导的离散MCMC方法比纯启发式搜索更高效，可考虑在Agent工作流中嵌入，利用历史交互数据在线优化Agent的指令模板。

  - 需注意当前实现计算成本高，且容易在小样本优化集上过拟合，建议结合正则或交叉验证。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有自动提示优化多依赖启发式搜索，缺少原则性概率框架。本工作将提示优化重新定义为在离散提示令牌上的贝叶斯后验采样，通过结合任务似然（解释输入-输出对）与语言模型先验（保持提示流畅）构建后验分布。
**方法**：将问题转化为基于能量的后验采样，利用梯度信息引导离散MCMC（Gibbs-with-Langevin提案，Metropolis-Hastings校正）。引入并行回火机制在LLM崎岖的能量景观中全局探索，并通过concrete sampler解决非权重共享嵌入的实践约束。
**结果**：在诊断任务上发现语义有意义的提示；并行回火帮助诗歌补全任务逃离局部最优；在24个指令归纳子任务上对APE提示进行后优化，平均准确率从60.04%提升至63.23%。该方法揭示了能量最小化可能在小优化集上过拟合，且当前采样器计算开销较高，指向了概率提示优化的可行方向。
