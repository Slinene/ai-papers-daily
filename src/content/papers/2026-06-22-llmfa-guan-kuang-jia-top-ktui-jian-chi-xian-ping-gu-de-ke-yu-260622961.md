---
title: LLM-as-a-Judge for Reliable and Explainable Offline Evaluation in Top-K Recommendation
title_zh: LLM法官框架：Top-K推荐离线评估的可靠性与可解释性
authors:
- Yue Que
- Junyi Zhou
- Xiaokun Zhang
- Haiming Jin
- Qiao Xiang
- Chen Ma
affiliations:
- City University of Hong Kong
- Shanghai Jiao Tong University
- Xiamen University
arxiv_id: '2606.22961'
url: https://arxiv.org/abs/2606.22961
pdf_url: https://arxiv.org/pdf/2606.22961
published: '2026-06-22'
collected: '2026-06-23'
category: Eval
direction: LLM语义匹配替代ID匹配的离线评估
tags:
- LLM-as-a-Judge
- Offline Evaluation
- Top-K Recommendation
- Semantic Proxy
- MNAR Bias
- Explainable Evaluation
one_liner: 用语义代理和推理-评分流程替代ID匹配，使LLM法官提供可靠且可解释的离线Top-K评估。
practical_value: '- **用LLM替代有偏的留出集评估**：当业务数据存在严重的曝光偏差（MNAR）时，直接利用LLM从用户历史文本中构建语义代理，评估推荐列表与用户偏好的语义匹配度，可大幅提升离线评估与线上效果的一致性，降低AB实验成本。

  - **可解释的评估报告**：采用 reasoning-then-scoring 模板，为每个推荐项输出0/1打分和一句话理由，方便算法团队快速诊断推荐质量，例如发现模型是否忽略了用户偏好中的某些维度（如颜色、品类）。

  - **低成本复用的提示工程**：提示模板中固化的“默认拒绝”策略和推理步骤是效果的核心，改写措辞几乎不影响结果，且从4B小模型即可工作，工程落地门槛低，适合迭代初期的快速验证。

  - **文本侧信息即可驱动**：仅需用户行为关联的标题、描述、标签等文本，无需复杂的profile构建，电商/内容场景可复用商品标题、详情关键词或用户搜索词作为输入，直接迁移该框架。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 总结
LLM法官通过语义代理和推理-评分，在不改变原有推荐模型的前提下，大幅提升了离线评估的可靠性与可解释性，且在多个模型规模和输入条件下表现鲁棒，是替代传统有偏离线评估的务实方案。
