---
title: 'Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search'
title_zh: 大型发现模型：基于实证的模型驱动开放式搜索
authors:
- Zhongwei Yu
- Yan Song
- Xue Yan
- Anjie Liu
- Xingyu Lu
- Yihang Chen
- Huichi Zhou
- Siyuan Guo
- Luoyang Sun
- Sihan Chen
affiliations:
- University College London
- The Hong Kong University of Science and Technology (GZ)
- Institute of Automation, CAS
- Jilin University
- AI Lab, The Yangtze River Delta
arxiv_id: '2608.15669'
url: https://arxiv.org/abs/2608.15669
pdf_url: https://arxiv.org/pdf/2608.15669
published: '2026-08-15'
collected: '2026-08-19'
category: Other
direction: LLM + 贝叶斯代理模型开放式搜索
tags:
- LLM
- Bayesian Optimization
- Open-ended Search
- Surrogate Model
- Uncertainty
- Scientific Discovery
one_liner: 耦合 LLM 生成与贝叶斯非参代理模型，用不确定性值引导候选生成与筛选，实现开放式搜索性能大幅提升
practical_value: '- 借鉴「LLM 生成 + 非参代理模型」的架构：在电商搜索/推荐里，可让 LLM 生成候选商品描述、广告创意、Query 改写等，同时训练一个轻量
  Bayesian surrogate（如 GP/随机森林）预测效果并输出不确定性，不依赖 LLM 自评/概率作为可靠打分。

  - 用 uncertainty-aware value 做候选筛选：例如生成多个广告文案或推荐理由时，按 surrogate 预测的 CTR/CVR 减去不确定性惩罚选择，可平衡探索与利用，降低对冷启动或分布外候选的误判。

  - 持续更新 discovery memory 与 surrogate：每个线上实验反馈（点击、转化）实时更新代理模型和记忆池，使候选生成越来越符合业务目标；类似在线贝叶斯优化，适合迭代优化推荐策略或创意素材。

  - 注意资源：LLM 生成多个候选成本可控，但每次实验反馈更新 surrogate 需要在线训练或增量更新方案；可参考论文中非参模型的选择，探索轻量实现。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学发现中，优化目标昂贵且空间开放（分子、蛋白、程序），LLM 提供强先验但 likelihood 和自评不可靠，对分布外候选尤其缺乏校准的认知不确定性。

**方法关键点**：LDM 是循环架构，生成模型提议并细化候选设计；贝叶斯非参 reward surrogate 预测性能并量化不确定性；不确定性感知价值指导候选生成、细化、选择；发现记忆和 surrogate 随每次实验观察持续更新。

**结果**：在神经网络训练、抗体设计、分子优化三个场景，相比 LLM-only reflection 或传统统计搜索，LDM 使验证 BPB 降低幅度达 2.4 倍，结合能相对降低 18.2%，分子多目标性能相对提升超过 60%。
