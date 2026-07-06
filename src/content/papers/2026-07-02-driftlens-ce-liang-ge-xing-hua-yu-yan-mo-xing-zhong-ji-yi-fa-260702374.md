---
title: 'DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language
  Models'
title_zh: DRIFTLENS：测量个性化语言模型中记忆引发的推理漂移
authors:
- Xi Fang
- Weijie Xu
- Yingqiang Ge
- Yuhui Xu
- Stephanie Eckman
- Chandan K. Reddy
affiliations:
- Amazon
arxiv_id: '2607.02374'
url: https://arxiv.org/abs/2607.02374
pdf_url: https://arxiv.org/pdf/2607.02374
published: '2026-07-02'
collected: '2026-07-06'
category: Eval
direction: LLM 个性化推理漂移测量与缓解
tags:
- Personalization
- Reasoning Drift
- LLM Evaluation
- Memory Injection
- Value Category
one_liner: 提出无真值框架 DRIFTLENS，量化用户记忆注入对 LLM 推理路径的影响，并评估 GRPO/DPO 缓解策略
practical_value: '- 在电商推荐 Agent 中，使用用户属性（如年龄、职业、偏好）生成推荐理由时，可借鉴 DRIFTLENS 将解释步骤映射到价值维度（如性价比、品牌、售后服务），量化有/无记忆时的推理路径差异，监控伴随个性化带来的推理扭曲，确保解释一致性。

  - 对推荐式 LLM 做个性化微调（如 DPO/GRPO）时，可参考论文发现：降低漂移可能牺牲 helpfulness 等能力。需同时评估推荐准确性、用户满意度、解释合理性等多指标，避免单目标优化导致能力退化。

  - 工程实现上，DRIFTLENS 的无真值设计（零样本分类 + 分布散度）可直接复用到推荐解释的自动化评估，无需人工标注，通过预定义价值类别快速构建推理漂移监控管线。

  - 个性化记忆可能引入隐性偏见（如年龄导致保守/冒险推荐），可借此测量方法审计推荐系统全链条的公平性，作为个性化上线前的安全检查。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：个性化 LLM 通过注入用户记忆（年龄、职业、偏好等）来定制回答，但现有评测多关注回答内容的变化，忽略了推理轨迹的隐性偏移。这种“推理漂移”可能导致逻辑不一致或偏见，尤其在无标答的开放式问题上，如职业建议、冲突调解等。亟需一种无需真值框的测量方法。

**方法**：提出 DRIFTLENS 框架。首先将推理步骤通过零样本分类映射到预定义的价值类别（如“安全/伦理责任”、“情感连接”），形成推理轨迹；然后计算有记忆和无记忆条件下的轨迹差异（使用 JS 散度等指标）。引入“语用噪声”作为基底，区分随机扰动与实质性推理变化。实验覆盖 4 种 LLM、10 种用户属性，并对比 GRPO 与 DPO 两种后训练方法对漂移的缓解效果，同时监测下游能力、帮助性和指令遵循。

**关键结果**：用户属性记忆在所有模型上均引起显著高于噪声水平的推理漂移（效应量中到大），即便最终回答依然流畅、切题且看似合理。GRPO 与 DPO 均可降低漂移，但效果依赖具体模型和奖励设计，且存在与 helpfulness 等能力的 trade-off，没有一种方法完全占优。表明推理漂移是可测量的个性化失败模式，但现有缓解手段仍不充分。
