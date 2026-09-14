---
title: 'Judging by the Cover: Cleaning LLM Truthfulness Benchmarks to Avoid Surface-Level
  Feature Leakage'
title_zh: 清洗 LLM 真实性基准：消除表面特征泄漏
authors:
- Foad Namjoo
- Remy Ogasawara
- Amirali Abdullah
- Cullen Anderson
- Narmeen Fatimah Oozeer
- Jeff M. Phillips
affiliations:
- University of Utah
- Thoughtworks
- University of Massachusetts Amherst
- Martian AI
arxiv_id: '2609.13003'
url: https://arxiv.org/abs/2609.13003
pdf_url: https://arxiv.org/pdf/2609.13003
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: LLM 评测基准清洗 · 表面特征泄漏
tags:
- benchmark leakage
- truthfulness
- surface features
- dataset cleaning
- LLM eval
- Audit-Prune
one_liner: 发现 TruthfulQA 等二选一基准存在表面特征泄漏，提出 Audit-Prune 机制清洗至接近随机水平
practical_value: '- 搭建二选一/成对评测集（如 LLM 排序、答案正确性、query 改写质量）时，先用简单逻辑回归对长度、否定词、标点、选项位置等
  surface features 做可判别性检查；若分类 AUC 显著高于 0.5，说明模型可能靠浅层 cue 刷分，评测目标无效。

  - 借鉴 Audit-Prune：迭代移除最能强化泄漏的 pair，直到表面特征分类器接近 chance；可用于业务中 LLM-as-judge 的偏好对、检索相关性标注、生成标题
  A/B 测试集的清洗。

  - 对内部排行榜或模型选型用的 benchmark，先跑特征泄漏审计再上线；否则模型可能学到“正确答案风格”而非真实能力，导致选型误判。

  - 在电商/Agent 场景做事实性、安全性评估或客服 bot 评测时，不要直接使用公开 TruthfulQA 原版作为唯一指标；可替换清洗版或对自有数据进行
  Audit-Prune。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：二选一事实性基准如 TruthfulQA 若正确/错误答案在表层语言特征上系统性不同，模型可以只学这些特征就超过随机，导致排行榜和模型能力评估失真。方法：作者用 6 个表面特征训练逻辑回归，能在 TruthfulQA 上以显著高于随机的准确率区分正确与错误答案；进一步发现其他基准也存在类似伪影。提出 Audit-Prune：先训练简单分类器检测可泄漏 pair，再迭代删除最能增强泄漏的样本，直到表面特征分类接近随机。结果：在 TruthfulQA 上明显减少表面特征泄漏，释放接近 chance 的清理版，并提供审计机制供新数据集发布前清理。
