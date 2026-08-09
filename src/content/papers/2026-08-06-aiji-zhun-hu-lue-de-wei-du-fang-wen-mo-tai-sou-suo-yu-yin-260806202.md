---
title: 'What Current AI Benchmarks Leave Unmeasured: Modality, Search, Citations,
  and Implications (for Safety Evaluations)'
title_zh: AI基准忽略的维度：访问模态、搜索与引用稳定性
authors:
- Ro Encarnación
- Tina Behzad
- Emma Lurie
- Danaé Metaxa
affiliations:
- University of Pennsylvania
- Stony Brook University
arxiv_id: '2608.06202'
url: https://arxiv.org/abs/2608.06202
pdf_url: https://arxiv.org/pdf/2608.06202
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: LLM评估方法论与安全审计
tags:
- LLM evaluation
- safety
- modality
- web search
- consistency
- citation grounding
one_liner: 揭示LLM评估仅用API单次运行忽略搜索和模态差异，会掩盖高达21%的输出不一致与8%准确率下降
practical_value: '- 评估搜索推荐中LLM（如商品描述、推荐理由生成）时，不能只看单次API调用的准确率；应在不同访问界面（类似Chat UI vs
  API）和多次运行下衡量输出一致性，避免上线后行为漂移

  - 引入RAG或搜索增强的推荐系统，必须量化搜索条件对模型行为的影响：搜索可能降低准确率或改变回答风格，需针对性设置安全兜底策略

  - 关注模型的弃权行为（abstention）：在敏感推荐（如金融、医疗商品）中，明确定义模型何时应拒绝生成，避免错误推荐

  - 若LLM输出引用外部来源，评估引用准确性和稳定性，防止不实信息扩散到商品详情或推荐理由中，引发用户投诉'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM基准评估通常只通过API单次运行并报告准确率，忽略访问模态（如Chat UI）、搜索开关及多次运行一致性，可能隐藏实际部署中的行为变异，影响安全风险判断。

**方法**：审计ChatGPT的聊天UI与API两种模态，在开启/关闭搜索的条件下，从BBQ和SafetyBench安全基准分层抽样401个提示，每个提示重复运行3次，共收集4812个响应。分析维度包括准确性、响应一致性、文本相似度、引用来源及弃权行为。

**关键结果**：
- 搜索关闭时，UI响应准确率低于API；开启搜索后准确率最多下降8个百分点，甚至反转某基准的模态性能趋势
- 同一提示多次运行中最多21%产生不一致响应
- 两种模态的答案引用不同来源，弃权行为也不一致
- 简单准确率指标会掩盖与安全评估相关的重要行为变异
