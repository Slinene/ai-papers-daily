---
title: 'HARP: Hierarchical Adaptive Ranking with Preference-Adaptive Fusion for Query-Based
  CVE Prioritization'
title_zh: HARP：面向查询的CVE优先级分层自适应排序与偏好融合框架
authors:
- Haochen Liu
- Zhengzhang Chen
- Haoyu Wang
- Yanchi Liu
- Jundong Li
- Haifeng Chen
affiliations:
- University of Virginia
- NEC Laboratories America
arxiv_id: '2608.19430'
url: https://arxiv.org/abs/2608.19430
pdf_url: https://arxiv.org/pdf/2608.19430
published: '2026-08-19'
collected: '2026-08-24'
category: RecSys
direction: 偏好自适应排序 · LLM 排序器
tags:
- CVE prioritization
- preference-adaptive fusion
- LLM ranking
- knowledge graph
- multi-view
- query-based ranking
one_liner: 利用历史标注样本隐式捕捉组织偏好，通过图证据与多视图LLM融合对CVE进行查询驱动排序
practical_value: '- **隐式偏好建模**：真实业务中用户/组织的偏好难以用文字 prompt 完整表达，但历史行为、已标注样本是现成的偏好信号。可借鉴
  HARP 的做法：用 support bank 做 few-shot 检索注入，而不是费力写偏好描述。

  - **多视图打分 + 可学习融合权重**：将排序信号拆成 global / segment / individual 等多视图，并在推理时用少量支撑样本动态拟合融合权重。这套机制可以直接迁移到电商搜索或推荐的多目标融合（GMV、CTR、转化率、多样性），避免固定加权带来的偏好漂移。

  - **图证据检索增强 LLM 排序**：对候选 item 先从知识图谱取关系、属性等结构化证据，再喂给 LLM，可显著提升可解释性和排序稳定性。在商品、内容、广告候选上可以构建
  domain KG（类目、品牌、用户行为关系）做类似增强。

  - **Query-conditioned ranking 框架**：用自然语言查询作为排序条件，结合候选特征进行 LLM 打分，适合搜索广告、个性化推送等场景，尤其当查询意图需要与历史交互偏好一起建模时。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：漏洞优先级排序天然依赖组织偏好，同一个 CVE 在不同偏好场景下应有不同排名。但传统评分系统（CVSS、EPSS、SSVC）假设固定标准，而实际组织的偏好往往隐含在历史已处理的工单中，难以写成显式 prompt。

**方法关键点**：HARP 针对“自然语言查询 + 当前偏好场景的历史标注样本”这一设定，构建图基础多视图排序框架。它从漏洞知识图谱中检索候选 CVE 的证据，用策略条件化（policy-conditioned）的 global、enterprise、user 三个视图分别打分，并从一个采样出的 support set 中学习视图融合权重，无需显式总结偏好场景。整个过程以 LLM 作为排序骨干，利用支持集中的案例进行 few-shot 偏好对齐。

**结果**：在三个不同偏好场景和多个骨干 LLM 上，HARP 均优于多个基线方法，验证了隐式偏好建模与自适应视图融合在 query-based CVE 排序上的有效性。
