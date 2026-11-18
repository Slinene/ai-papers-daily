---
title: 'MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval
  with Multi-Category Solutions'
title_zh: MIPR：多模态意图到产品检索的推理密集基准
authors:
- Qiang Li
- Xuan Lu
- Jian Ruan
- Manxi Lin
- Jiacheng Chen
- Wen Shen
- Zhihua Wei
- Xiaoyu Shen
- Dan Ou
- Xiangheng Kong
affiliations:
- Tongji University
- Taobao & Tmall Group of Alibaba
- Eastern Institute of Technology, Ningbo
arxiv_id: '2611.22509'
url: https://arxiv.org/abs/2611.22509
pdf_url: https://arxiv.org/pdf/2611.22509
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 多模态意图到产品检索基准
tags:
- Multimodal Retrieval
- Benchmark
- E-commerce
- Reasoning-Intensive
- Fine-Grained Relevance
- Multi-Category Solutions
one_liner: 构建首个同时覆盖推理密集、多品类解决方案与细粒度相关性标签的电商多模态意图到产品检索基准，揭示现有模型显著差距
practical_value: '- 电商搜索/推荐中常遇到“需求意图不显式、多品类可满足”的 query，可借鉴 MIPR 的 5 级标注（L1 最优/L2 次优/N1
  约束违反/N2 相关非解/N3 无关）构建自己的细粒度相关性评估集，尤其区分“能用但次优”和“违反安全/兼容约束”。

  - 实验证明 reranker 对这类推理密集意图提升很大（nDCG@10 +10.88 点），而 embedding 检索器召回候选尚可但排序差；业务上可在召回后加专门训练的
  reranker，重点处理多品类覆盖和硬负样本排序。

  - 显式意图描述和产品词增强能让最佳 embedding 模型 nDCG@10 从 49.23 提升到 64.00，说明在实际系统中先用 LLM 抽取用户意图、生成候选产品词再检索，是低成本高收益的
  query augmentation 策略。

  - 指标设计上，SC-R@K（solution-category recall）比传统的 Hit@K 更能暴露“只召回一个最优品、但未覆盖多个解类”的问题，适合多解意图场景的离线监控。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：真实电商搜索中，用户常上传情境图片并提问（如“刀锈了怎么恢复如新”），并不指定目标商品，而一个意图可能由多个品类的产品满足。现有检索基准要么基于直接语义匹配，要么只针对单一目标品类且使用二元相关性标签，无法评估这种推理密集、多品类解决方案、细粒度相关性的检索场景。

方法关键点：
- 数据来自淘宝真实搜索日志，最终包含 3,522 个多模态 query（情境图+问题）、30,731 个共享产品、447,809 个标注对。
- 相关性采用 5 级标签：L1 最优解、L2 次优但可用、N1 违反约束（如食品级安全）、N2 相关非解、N3 无关。
- 候选发现：先用 LLM 从专用品/替代品/互补品/前置条件四个视角枚举产品词，并经反思补全；再通过 BM25、文本 embedding 融合、多模态 embedding 多路召回，合并形成共享候选池。
- 标注流程：粗筛排除明显无关 → 三个模型独立打 5 级标签 → 多数投票或裁定 → 用 10 个 embedding retriever 做 pooling 扩展未标注对。
- 指标：graded nDCG（L1=2, L2=1）、L1 recall、Hit L1、L1 solution-category recall (SC-R@K)，其中 SC-R 专门衡量多品类覆盖。

关键结果：最佳 embedding 模型 Qwen3-VL-Embedding-8B 仅 49.23% nDCG@10，Hit@1 不足一半；多品类查询的 SC-R@10 只有 55.86%。加入 reranker Qwen3-VL-Reranker-8B 后 nDCG@10 提升至 60.11%，SC-R@10 达 67.00%，但仍低于候选池 oracle（86.04/80.22）13-25 个点。模态消融显示多模态远好于单模态；显式意图和产品词增强可使最佳模型 nDCG@10 从 49.23 提升到 64.00。硬负样本 N2 命中率普遍 88-92%，排序误差大。

最值得记住的一句话：现有 embedding 检索器能召回相关候选，但排序与多品类覆盖严重不足，推理密集的多解意图检索仍远未解决。
