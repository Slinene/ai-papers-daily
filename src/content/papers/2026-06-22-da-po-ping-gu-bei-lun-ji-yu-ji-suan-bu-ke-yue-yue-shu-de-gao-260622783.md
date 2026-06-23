---
title: 'Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally
  Irreducible Constraints'
title_zh: 打破评估悖论：基于计算不可约约束的高熵搜索评估
authors:
- Juntao Wu
- Wei Wen
- Xianting Huang
- Shuai Pang
- Ruizhi Qiao
- Xing Sun
- Ke Wang
affiliations:
- Jinan University
- Tencent Youtu Lab
- The Chinese University of Hong Kong
arxiv_id: '2606.22783'
url: https://arxiv.org/abs/2606.22783
pdf_url: https://arxiv.org/pdf/2606.22783
published: '2026-06-22'
collected: '2026-06-23'
category: Eval
direction: 搜索评估 · 计算不可约约束
tags:
- evaluation
- search
- agent
- hash-constraint
- exhaustive-enumeration
- benchmark
one_liner: 提出 VERITAS 框架，利用计算不可约约束生成可验证的穷举搜索任务，解决高熵搜索无法完整评估的难题
practical_value: '- **电商搜索 Agent 评估新范式**：当前电商搜索 Agent 常需穷举品类、属性组合等，但缺乏完整 ground truth。可借鉴
  VERITAS 生成可控难度、可自动验证的测试任务，例如定义“检索所有满足复杂哈希条件的商品 ID”，成本极低且无需人工标注。

  - **防止 Agent 走捷径**：在推荐或广告物料生成场景中，若用 LLM 评判完整性容易导致循环论证。引入计算不可约约束（如不可优化的哈希条件），能确保
  Agent 必须真正遍历商品库或知识图谱，而不是靠记忆或模式猜测，适合评估真实系统的探索能力。

  - **生成式推荐的训练数据增强**：VERITAS 能无限生成多样化的高熵查询-答案对，可作为强化学习或 SFT 的训练数据，提升模型穷举不在单一召回通路内物品的能力，特别适合需要覆盖长尾商品的生成式推荐。

  - **线上评估轻量化**：边际成本仅为哈希计算，可将 VERITAS 任务嵌入日常回归测试，持续监控 Agent 在开放式搜索任务上的能力退化，对搜索事业部的工程实现非常友好。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：评估 LLM 在高熵搜索（如列举所有满足条件的实体）上的穷举能力面临严重悖论——验证完整性需要完整的 ground truth，但高熵任务使得人类无法全部标注。现有评估依赖部分标注、LLM 裁决或单答案问题，回避了真正的穷举搜索场景，导致模型可能超越标注者却因缺失答案而被扣分。

**方法**：提出 VERITAS 框架，核心是引入 **计算不可约约束**。通过构造新型、不可优化的约束（例如哈希函数满足特定性质的搜索条件），生成稀疏但可完美验证的搜索任务。这些任务的特点是：答案容易验证（检查是否满足约束），但 LLM 和搜索引擎无法通过捷径找到答案，必须真的遍历整个搜索空间。框架能自动生成近乎无限数量的测试用例，难度精确可控，每个实例的边际成本以哈希计算为主。

**关键结果**：VERITAS 提供了独立于人类标注的基准，能可靠评估 Agent 在不确定环境下的系统性探索能力；同时可作为生成训练数据的可扩展方法，用于提升模型目前尚不发达的穷举搜索能力。
