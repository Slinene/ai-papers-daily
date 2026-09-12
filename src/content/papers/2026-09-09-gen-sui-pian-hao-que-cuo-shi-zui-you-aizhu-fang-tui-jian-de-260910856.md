---
title: 'Following the Preference, Missing the Optimum: Compliance Without Optimization
  in AI Housing Recommendation'
title_zh: 跟随偏好却错失最优：AI住房推荐的合规无优化审计
authors:
- Hsuan Lo
affiliations:
- Harvard University
- Independent Researcher
arxiv_id: '2609.10856'
url: https://arxiv.org/abs/2609.10856
pdf_url: https://arxiv.org/pdf/2609.10856
published: '2026-09-09'
collected: '2026-09-12'
category: RecSys
direction: LLM推荐系统审计与优化缺陷诊断
tags:
- LLM
- Recommendation
- Audit
- Compliance
- Optimization
- Ground Truth
one_liner: 大规模审计发现LLM在住房推荐中几乎完美遵守硬约束，但39%的推荐被同池中更优选项严格支配
practical_value: '- 在电商/推荐场景中，对LLM推荐不要只检查约束合规，应引入**支配性检测**：从候选池中计算被严格支配的比例，作为线上部署前的诊断指标，可提前暴露“只满足条件但非最优”的问题。

  - 将LLM作为推荐器时，需要显式的优化目标或后处理层：论文显示仅靠自然语言指令无法让模型自动寻找更便宜/更快的选项，可在LLM输出后用规则或排序模型在满足约束的候选中选择Pareto最优项。

  - 大规模候选集会放大优化差距（候选集越大，LLM推荐与最优的租金差距越大），因此在大规模召回的电商/广告场景中，应先用检索或粗排缩小候选集，再让LLM做精细推荐，避免直接让LLM面对海量候选。

  - 该审计成本极低（约57美元完成近万次调用），可在业务中构建自动化评估管道，用真实商品/广告库存定期审计LLM推荐质量，监测是否出现“合规但不优化”的漂移。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM正成为消费者搜索的第一入口，尤其在住房等高风险、法律明确的领域。已有审计发现模型会根据用户身份进行引导，但无法量化用户因推荐系统遗漏合适选项而遭受的损失，因为缺少可枚举的ground truth库存来对照遗漏。

**方法关键点**：构建150个纽约市合成租房场景，每个场景配120个真实房源（已知租金、卧室数、GTFS计算通勤时间），精确计算满足租客硬约束的集合，并推导其Pareto前沿。核心指标：若同池中存在一个更便宜、通勤更快且卧室数不更少的房源，则该推荐被“严格支配”。共进行9,945次模型调用（解析率96.5%），覆盖三家模型、两家供应商。

**关键结果**：约束合规近乎完美——违反硬约束的比例仅1.8%，而随机选择基线为66.6%；但优化表现差——39.0%的推荐被严格支配，支配房源中位租金便宜900美元/月、通勤快3.5分钟；在租金上模型甚至不如随机选择（+$498/月 vs +$261/月，相对oracle）。改变单句优先级说明模型能正确响应偏好，但推荐仍比屏幕上前五个合格房源中位租金高606美元/月；显式字典序指令在预定的50美元/月等价性边界下无改善。差距随候选集规模扩大而增大，且OpenAI与Anthropic模型间差异小于3美元。
