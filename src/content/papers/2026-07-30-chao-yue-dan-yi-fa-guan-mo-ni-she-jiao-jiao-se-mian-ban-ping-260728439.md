---
title: 'Beyond a Single Judge: Simulating Social Persona Panels for Generative UI
  Evaluation'
title_zh: 超越单一法官：模拟社交角色面板评估生成式UI
authors:
- Zheng Wu
- Yibo Luo
- Pu Zhang
- Cheng Yang
- Zhuosheng Zhang
affiliations:
- Shanghai Jiao Tong University
- ByteDance Inc
arxiv_id: '2607.28439'
url: https://arxiv.org/abs/2607.28439
pdf_url: https://arxiv.org/pdf/2607.28439
published: '2026-07-30'
collected: '2026-08-02'
category: Eval
direction: 生成式UI评估 · 多角色社交加权
tags:
- Generative UI
- LLM-as-a-judge
- Persona Simulation
- Evidence-Grounded
- Delphi
- Evaluation
one_liner: 用多角色证据锚定与社交加权面板评价生成式UI，与人类评分的相关性从0.716升至0.922
practical_value: '- **多角色模拟用户多样性**：在电商推荐或广告落地页评估中，可借鉴 ESPP 方法，构建反映不同用户画像（价格敏感、品牌偏好、视觉导向等）的角色面板，更全面地捕捉界面或推荐列表的感知差异。

  - **证据锚定提升评判可靠性**：要求评估者（LLM）基于界面上具体元素给出评分理由，这种“证据落地”机制可迁移到任何 LLM-as-a-judge 场景，减少幻觉和主观臆断，适用于搜索广告文案或推荐理由的质量审核。

  - **社交加权与分歧分析**：在多角色评分聚合时，采用有界置信模型进行观点交换与德尔菲式加权，产出更稳定的整体评分，同时保留各子群体评分用于分歧诊断，帮助识别推荐系统对不同人群的公平性问题。

  - **离线评估成本优化**：用一组自动化的角色面板替代部分人工用户测试，快速筛选出有潜力的UI方案或推荐策略，在进入 A/B 测试前过滤掉明显低质变体，降低实验成本。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：生成式 UI 能根据自然语言指令直接合成可渲染界面，但其评价仍依赖昂贵且不稳定的人工评估，或单一的 LLM-as-a-judge。单一评判者只能反映隐含的单一视角，无法捕捉真实用户群体的多样化感知。

**方法**：提出 ESPP，一个三阶段评估框架。(1) 独立评级：用心理特质多样的角色面板，对 UI 截图给出带证据的评分。(2) 意见交换：基于特质相似度和语义门控的有界置信机制，让角色有条件地交流观点。(3) 社交加权聚合：借鉴德尔菲法，根据讨论后的置信分布加权形成最终评判。

**关键结果**：在 GenUI 基准上，ESPP 与人类评分的 Pearson r 从单次评判的 0.716 提升至 0.922；单纯提示集成只弥补了约 1/3 的差距，确认角色多样性和证据锚定是主要增益。此外，保留每个角色的个体评分可揭示子群体在总体排序一致的同时在各维度上显著分歧，这种结构性分歧会被单一评委抹平。
