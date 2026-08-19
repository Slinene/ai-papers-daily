---
title: Conditional Evaluation of Language Models with Cheap Auxiliary Signals
title_zh: 使用廉价辅助信号的语言模型条件评估
authors:
- Zhi Zhang
- Lingfeng Lyu
- Yue Kang
- Doudou Zhou
affiliations:
- Department of Statistics and Data Science, University of California, Los Angeles
- Department of Statistics and Finance, School of Management, University of Science
  and Technology of China
- Microsoft
- Department of Statistics and Data Science, National University of Singapore
arxiv_id: '2608.16210'
url: https://arxiv.org/abs/2608.16210
pdf_url: https://arxiv.org/pdf/2608.16210
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: LLM 条件评估 · 半监督控制变量
tags:
- LLM evaluation
- control variates
- semi-supervised
- conditional performance
- variance reduction
- cheap signals
one_liner: 提出 LACE 半监督估计器，用便宜信号局部中心化控制变量估计 LLM 条件性能，实现无偏且高效。
practical_value: '- 用 LLM-judge、模型置信度、pairwise 偏好等廉价信号，对推荐/搜索/Agent 系统按流量切片（新客、低活跃、长尾
  query、分业务场景）做条件效果评估；LACE 的局部中心化确保即便信号有偏也不影响估计目标，减少对人工标注的依赖。

  - 借鉴局部岭控制变量：在少量人工标注子集上估计 gold label 残差均值，与全量 cheap score 均值结合，可有效降低条件指标估计方差；评估体系选型可先计算
  cheap signal 与 gold label 在目标子群的局部 R²，优先选高相关信号。

  - 对 A/B 实验和模型迭代，可用其模型对差距估计器和部署加权得分，分析模型在不同流量桶/商品类目/用户群体上的条件提升是否显著，避免只看整体均值。

  - 在 Agent/LLM 推荐链路中，可把 reward model 或 judge 输出当作廉价信号，监控线上分场景性能，低成本识别退化区域。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：聚合准确率掩盖模型在不同子群体（难度、学科、用户分群等）上的差异，但仅靠 gold label 估计条件性能成本过高；LLM-judge 分数、pairwise 比较、置信度等廉价信号可全量收集，却常存在偏差或校准问题。

方法：LACE 使用局部中心化，在目标 profile 区域内减去廉价信号的条件均值，使任何线性增广的期望贡献为零，因此增广系数只影响效率、不改变估计目标。局部岭控制变量将标注子集上的 gold-label 残差均值与全量 item pool 的廉价信号均值结合。理论证明免校准识别、分组无偏、中心化线性增广内的局部 oracle 最优，以及对估计系数的一阶自适应；效率增益由局部 R² 决定。还扩展了直接模型对差距和部署加权得分的估计器。

结果：在 MATH-500、ScienceQA、MMLU、WinoGrande、HellaSwag、TruthfulQA、GSM8K、ARC 上验证主估计器，展示条件性能评估的可行性与效率提升。
