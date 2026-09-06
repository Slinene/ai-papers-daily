---
title: 'Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance
  When Ground Truth Is Unavailable'
title_zh: LLM推荐的认识论保证：在无真值条件下刻画依赖依据
authors:
- Shai Vardi
- João Sedoc
affiliations:
- University of South Florida, Muma College of Business
- New York University
arxiv_id: '2609.04127'
url: https://arxiv.org/abs/2609.04127
pdf_url: https://arxiv.org/pdf/2609.04127
published: '2026-09-03'
collected: '2026-09-06'
category: Eval
direction: 决策级LLM推荐可靠性评估
tags:
- epistemic warrant
- LLM evaluation
- decision-making
- reliability
- pairwise recommendation
- uncertainty
one_liner: 提出可操作的决策级认识论保证框架，将LLM两两推荐分为四层依赖证书并验证其有效性
practical_value: '- 在电商/推荐Agent中，对LLM生成的排序或推荐理由进行多轮采样与prompt扰动，统计候选偏好是否稳定；将跨上下文一致的推荐标记为broadly
  supported，低warrant的推荐降级或仅作参考。

  - 不要依赖模型的verbalized confidence（如“我很有信心”），论文表明epistemic warrant提供不同信息；在线决策中需单独计算决策级稳定性指标，而不是只取输出token概率。

  - 对context-dependent的推荐可触发额外验证，如A/B测试、人工审核或规则兜底；在冷启动或长尾等无ground truth场景，可为每个推荐附上reliance
  certificate，帮助下游Agent决定是否执行。

  - 在审计面板或管理工具中输出四层warrant标签，便于业务方按风险等级使用LLM推荐，而非依赖全局阈值。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM越来越多用于组织决策，但用户缺乏评估某个具体推荐是否可信的准则。现有方法要么评估整体模型属性（可靠性、不确定性、鲁棒性），要么关注用户信任，未刻画单个推荐背后的依据。

**方法关键点**：借鉴认识论，提出epistemic warrant这一决策级构造，刻画模型偏好的稳定性（stability）及偏好成立的适用范围（scope）。对pairwise推荐操作化为四层reliance certificate：unstable、context-dependent、locally supported、broadly supported。通过在不同prompt变体或上下文扰动下多次采样，判断偏好是否保持一致。

**关键结果**：采用known-groups tests验证，框架成功恢复专家预设的warrant排序；更强的warrant与独立众包共识系统对齐；epistemic warrant提供的信息不同于模型言语化置信度，也不被决策难度简单解释。
