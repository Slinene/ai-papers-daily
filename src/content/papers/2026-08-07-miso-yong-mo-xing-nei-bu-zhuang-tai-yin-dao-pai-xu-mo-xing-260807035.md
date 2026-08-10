---
title: 'MISO: Model-Internal-State-Guided Optimization for Ranking Models'
title_zh: MISO：用模型内部状态引导排序模型优化
authors:
- Yongzhe Zhang
- Xiaoyu Deng
- Yifan He
- Mengying Sun
- Sheng Luo
- Yijia Liu
- Hao Yan
- Zhuo Li
- Yi Meng
- Huiping Yao
affiliations:
- Meta
arxiv_id: '2608.07035'
url: https://arxiv.org/abs/2608.07035
pdf_url: https://arxiv.org/pdf/2608.07035
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 模型内部状态引导的排序模型局部优化
tags:
- Model Internal States
- Ranking Models
- Optimization
- AutoML
- Ads
one_liner: 利用模型参数、激活、梯度等内部状态聚合出可解释信号，将排序模型优化试错成本降低84–94%
practical_value: '- 将 MISO 的「ranking / alignment / comparison」三种聚合原语引入模型迭代流程，替代纯端到端指标判断，可以快速定位需要扩增容量、替换归一化模块或剪枝的位置，减少盲目试验。

  - 工程上可以直接在训练框架中挂载 MIS 提取器（参数、梯度、归一化统计），离线分析后给出一份优先级排序的候选动作列表，再用少量验证 run 确认；适合广告/推荐团队在模型版本频繁更新时做低成本诊断。

  - 对齐原语（Alignment）用于发现归一化层分布偏移，可提前干预不稳定特征流，避免线上指标漂移或训练崩坏；这一思路可直接用于电商搜索的 DNN 排序模型。

  - MISO 本身是一种闭环优化范式：提取信号→生成建议→验证→再提取。可以结合现有的 AutoML 或超参调优流程，用 MIS 信号做剪枝后的高效搜索，保留可解释性的同时大幅降低重训练消耗。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
排序模型（尤其是广告推荐）的迭代通常是在固定模型家族内做局部决策：扩展某个模块容量、替换归一化层、停用特征通路等。工程师依赖端到端指标反复试错，成本高且缺乏可重复性；黑盒 AutoML 又把模型当不透明对象，探索代价过大。模型内部状态（参数、激活、梯度、归一化统计等）大都没有被系统性地用作优化信号。MISO 正是要填补这个空缺。

## 方法关键点
- **三层架构**：提取层提供统一接口输出 MIS；分析聚合层用三类原语（排序、对齐、比较）将细粒度信号压缩成可决策摘要；优化决策层将摘要映射到候选编辑（扩缩、替换、剪枝等）并闭环验证。
- **排序原语**：计算神经元重要性，结合梯度-激活乘积与扰动后损失变化，定位高 ROI 容量区域。
- **对齐原语**：计算归一化前后分布与标准正态的 KL 散度，诊断层是否偏离理想统计量，识别需替换的模块。
- **比较原语**：对比不同模型或训练阶段的 MIS，定位变体间行为分叉点，辅助架构选择。
- **自适应闭环**：每次重训练后重新提取 MIS，使建议随数据分布和业务要求动态更新。

## 关键实验
在广告排序模型上做系统案例研究，对比黑盒扩展和专家手动调参，指标为 Normalized Entropy (NE) 和验证运行次数。
- **50x 参数规模**：MISO 相对专家调参的 NE 改进达 2 倍，所需训练试错次数从 50–92 次降到 3–12 次，最高减少 94%。
- 消融显示，排序、对齐、比较信号组合使用时 NE 增益最高（100%），同时能小幅优化参数量和延迟。

## 核心结论
> MISO 把模型内部状态变成了可解释的迭代优化语言，在重训练成本高昂的 ads ranking 现实里，用极低的探索预算就走通了‘该改哪里、为什么改’的决策闭环。
