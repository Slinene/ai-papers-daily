---
title: 'Statistically Valid Hyperparameter Selection: From Tuning to Guarantees'
title_zh: 统计有效的超参数选择：从调参到保证
authors:
- Amirmohammad Farzaneh
- Osvaldo Simeone
affiliations:
- Northeastern University London
arxiv_id: '2606.25601'
url: https://arxiv.org/abs/2606.25601
pdf_url: https://arxiv.org/pdf/2606.25601
published: '2026-06-24'
collected: '2026-06-28'
category: Other
direction: 统计学习与假设检验
tags:
- Hyperparameter Tuning
- LTT
- Multiple Hypothesis Testing
- Risk Control
- Statistical Guarantees
- E-values
one_liner: 提出 learn-then-test 框架，将超参数选择转化为多重假设检验，提供有限样本风险控制的形式化保证
practical_value: '- 可将推荐系统中 LLM 推理参数（温度、top-p）、检索环节 top-k、广告出价阈值等超参数选择问题，套入 LTT 框架，在有限验证集上获得可证明的风险上界

  - 当业务要求安全或可靠性约束（如推荐多样性最低容忍度、广告点击率下界），用假设检验方法筛选出满足要求的候选超参组合，替代纯经验调优

  - 引入 e-values 替代 p-values 作统计量，支持随时停止与在线校验，适合在线 A/B 测试中持续监控超参风险

  - 将模型升级、数据分布变化后的重新调参视为再检验，利用错误发现率控制（如 Benjamini-Hochberg 流程）避免选择出的超参存在过检验风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：现代 AI 系统部署中，超参数（推理参数、规则阈值、系统设置）的选择普遍依赖网格搜索或贝叶斯优化等启发式方法，缺乏统计意义上的可靠性保证，存在“选择后风险未知”的问题。

**方法关键点**：该专著系统呈现了一种名为 learn-then-test (LTT) 的统一统计框架。其核心是将超参数选择转化为**多重假设检验**：每一个候选超参数组合对应一个假设“该配置下风险达标”，利用 p-values 或 e-values 在有限样本下控制整体错误发现率 (FDR) 或族系错误率 (FWER)，从而输出一个可证满足风险约束的超参数子集。附录从第一性原理推导了 p-values、e-values、集中不等式等统计工具。

**关键结果**：在图像分类与无线调度等任务上，LTT 能选出符合平均风险或分位数风险要求的超参数，并给出有限样本保证（如错误选择概率控制）。相比于传统调优，LTT 提供了量化的可靠性边界。
