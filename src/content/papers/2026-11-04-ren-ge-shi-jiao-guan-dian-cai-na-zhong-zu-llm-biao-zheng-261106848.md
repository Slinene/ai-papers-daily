---
title: 'Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs'
title_zh: 人格视角：观点采纳重组 LLM 表征
authors:
- Austin C. Kozlowski
- Avital Mintz
- Madison Lee
affiliations:
- Knowledge Lab, University of Chicago
arxiv_id: '2611.06848'
url: https://arxiv.org/abs/2611.06848
pdf_url: https://arxiv.org/pdf/2611.06848
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM 人格化表征几何偏移
tags:
- LLM
- Representation Geometry
- Persona
- Linear Probes
- SAE
- Safety
one_liner: 发现 LLM 采纳政治人格会系统改变词向量投影与语义轴对齐，导致无 persona 训练的安全探针产生政治化偏差
practical_value: '- 在电商/推荐 Agent 中，若 LLM 被用户 prompt 诱导采用特定角色（如品牌客服、专家、极端用户），内部表征会偏移，导致基于
  linear probe/SAE 的内容安全、情感或真实性过滤器漂移；应在线上加入 persona 检测，并对安全特征做 persona 校准或动态适配。

  - 构建个性化文案或推荐理由生成时，不同品牌调性或用户 persona 下词向量几何变化会使固定的语义分类器（如意图、情绪）失效；建议为关键安全/合规特征设计
  persona-aware 表征或训练时加入 persona 条件。

  - 多 Agent 协作中，不同角色 Agent 对同一概念的几何编码不同，共享的监控 probe 可能不一致；可借鉴论文发现，为每个 Agent 角色单独校准安全探针或归一化跨角色表征。

  - 该工作主要针对政治人格与安全特征，业务场景可迁移为品牌声誉保护、广告合规与用户生成内容审核中的“角色漂移”风险检测。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 监控常用 linear probes / SAEs 假设特征跨上下文一致，但 LLM 可灵活采纳 persona 改变概念关系。
**方法**：令模型采取自由/保守政治人格，提取 9000+ 常见词在 33 个语义轴上的表征，与两个中性基线对比；测试 truthfulness 与 morality 两个安全特征。用无 persona 训练的 linear probe、SAE 分类器及手动选词分类器，评估政治争议句。
**关键结果**：persona 系统性地改变词在语义轴上的投影和轴间对齐，方向与指定意识形态一致；无 persona 训练的安全分类器在 persona 条件下分歧增大，给出带政治倾向的真实性/道德评分，削弱监控有效性。
