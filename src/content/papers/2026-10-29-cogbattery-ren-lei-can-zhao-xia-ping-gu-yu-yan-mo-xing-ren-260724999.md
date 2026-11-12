---
title: 'CogBattery: Human-Referenced Evaluation of Cognitive Task Behavior and Structure
  in Language Models'
title_zh: CogBattery：人类参照下评估语言模型认知任务行为与结构
authors:
- Dengzhe Hou
- Lingyu Jiang
- Fangzhou Lin
- Kazunori D Yamada
affiliations:
- Tohoku University
- Texas A&M University
- Worcester Polytechnic Institute
arxiv_id: '2607.24999'
url: https://arxiv.org/abs/2607.24999
pdf_url: https://arxiv.org/pdf/2607.24999
published: '2026-10-29'
collected: '2026-11-12'
category: Eval
direction: LLM 认知评估与人类参照
tags:
- cognitive evaluation
- LLM
- human alignment
- confidence calibration
- behavioral benchmark
one_liner: 用13个认知范式评估54个开放模型，发现效应方向一致但错误与置信度模式偏离人类
practical_value: '- 评估生成式推荐/query 推荐 LLM 时不能只看整体命中率或点击率是否与人类偏好方向一致；要按条件（不同 query 模板、用户意图、难度桶）拆分错误模式，尤其关注普通非目标上的误报/过度生成，避免总体指标掩盖缺陷。

  - 对 LLM Agent 或对话式推荐中的置信度输出做校准评估：业务场景下模型可能看似合理但区分正确/错误的能力弱于人类，且往往固定选择同一策略（如固定 top1
  或固定话术），需要在策略多样性上做显式约束或引入随机性。

  - 借鉴“人类参照数据”思路：为关键 query 或商品类目建立条件级人类行为基线（点击、改写、拒绝模式），模型上线前做逐条件对比，能更快发现模型复现了 bias
  方向但犯了不同类型的错误。

  - 注意模型家族共享缺陷：该文发现跨模型家族出现类似置信度/下注问题；在选型多个开源 LLM 做召回或排序时，不要假设不同家族模型错误独立，需做跨家族 error
  analysis，避免同源设计缺陷放大。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：已有研究用人类认知任务对比 LLM，但往往只看模型是否复现人类条件效应方向，这会掩盖具体错误与置信度报告的差异；现有工作覆盖范式或模型数量少，难以判断普遍性。

方法关键点：CogBattery 选取 13 个认知范式的文本改编版，在 54 个开放权重模型上测试，并与原研究的人类条件级数据逐一比较；除条件效应外，重点分析错误类型（如 n-back 诱饵响应与普通非目标误报）、置信度区分正确/错误的能力、下注选择；对跨任务分数做降维，检验预定义认知分组是否优于随机分组。

关键结果：模型在 n-back 诱饵上响应高于控制，与人类方向一致，但普通非目标误报远高于人类；多数模型置信度分离正确/错误的能力弱于人类，即使分类准确也不倾向调整下注；跨任务分数存在两个维度，第一个与规模相关，但更大模型并不一致地更接近人类；预定义认知分组不比随机分组有可靠优势。结论：匹配人类效应方向不等于人类式行为，需要条件级人类参照来评估错误与置信度。
