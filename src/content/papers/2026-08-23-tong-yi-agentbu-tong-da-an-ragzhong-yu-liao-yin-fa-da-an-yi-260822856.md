---
title: 'Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer
  Churn in Retrieval-Augmented QA'
title_zh: 同一Agent不同答案：RAG中语料引发答案漂移的重复感知审计
authors:
- Jingjie Ning
- Xueqi Li
affiliations:
- Carnegie Mellon University
arxiv_id: '2608.22856'
url: https://arxiv.org/abs/2608.22856
pdf_url: https://arxiv.org/pdf/2608.22856
published: '2026-08-23'
collected: '2026-08-26'
category: Eval
direction: RAG 索引更新答案漂移审计
tags:
- RAG
- Answer Churn
- Retrieval-Augmented QA
- Backward Compatibility
- LLM Evaluation
- Index Updates
one_liner: 提出Snapshot Compatibility Audit，用同快照重复分歧校正跨快照差异，量化RAG索引更新导致的答案漂移
practical_value: '- **上线前做兼容性回归**：每次更新商品知识库、搜索语料或索引版本时，不要只看整体准确率/点击率，用同一批query做快照对比；在每个快照内对同一query重复采样多次，估计生成随机性基线；跨快照不一致减去同快照基线即为索引引起的真实漂移，可避免把LLM随机性误判为更新影响。

  - **关注repeat-stable semantic flips**：用LLM判断答案语义是否真变化，并筛出重复采样中稳定翻转的query；这些是索引更新真正伤害或改变用户体验的场景，应优先修复或设置告警。同义改写不应算作churn，语义判断能降低误报。

  - **聚合指标会掩盖局部恶化**：即使整体准确率基本不变甚至上升，仍可能有个别高频或长尾问题答案翻转；建立query/商品粒度的回归测试集，跟踪答案级兼容性指标如excess
  churn，而不是仅依赖平均指标。

  - **成本可控**：论文用400题即可统计显著检测到约6-10pp的漂移；在电商客服、商品问答、推荐理由生成等RAG场景中，可以构造几百条核心query做轻量上线前审计。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：检索增强QA在索引扩展后，即便固定模型标识、prompt、检索策略、证据深度等，返回答案仍可能改变；聚合准确率会因涨跌相抵而掩盖变化，单次比较又受生成随机性干扰。

**方法关键点**：提出Snapshot Compatibility Audit，通过同快照重复采样估计生成随机性基线，用跨快照不一致减去同快照重复不一致得到超额答案漂移（excess answer churn）。实例化时将冻结的FineWeb前缀从1个shard扩展到7个shard。

**关键结果**：在预注册的400题Natural Questions上，normalized-exact和盲评语义超额漂移分别为6.44pp和10.25pp，而精确匹配准确率仅变化-1.50pp；post-hoc发现40/400题存在重复稳定的语义翻转。另在200题TriviaQA上超额漂移方向一致但更小，准确率反向变化。100题DeepSeek复制中，语义超额漂移8.75pp，准确率却上升3pp。
