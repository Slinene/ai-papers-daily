---
title: 'DKCD: Domain Knowledge-Enhanced Causal Discovery from Unstructured Data'
title_zh: DKCD：领域知识增强的非结构化数据因果发现
authors:
- Xin Li
- Jin Li
- Shoujin Wang
- Kun Yu
- Fang Chen
affiliations:
- University of Technology Sydney
arxiv_id: '2607.09348'
url: https://arxiv.org/abs/2607.09348
pdf_url: https://arxiv.org/pdf/2607.09348
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 因果发现与领域知识增强
tags:
- Causal Discovery
- Domain Knowledge
- LLM
- Unstructured Data
- Latent Factors
one_liner: 引入领域知识强化LLM因果推理，解决潜在因素识别不全和标注不可靠问题
practical_value: '- 在电商用户评论或搜索日志分析中，可借鉴「知识挖掘 + 知识引导推理」流程，用领域知识图谱或业务规则补充 LLM 常识，更完整地识别影响用户决策的潜在因果因素（如隐藏的价格敏感度、社交偏好）。

  - 当从非结构化文本为推荐模型构建特征或样本时，可利用外部领域知识减少 LLM 的标注噪声，提升因子标注的可靠性，从而改善下游因果关系训练的准确性。

  - 在推荐系统可解释性或反事实推理场景下，该方法可帮助构建更可信的用户-物品因果图，用于生成有因果解释的推荐或策略模拟。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：在高专业领域（如医疗、金融）中，从非结构化文本直接进行因果发现面临两大挑战：纯靠 LLM 通用知识难以捕捉隐含在数据中的潜在因果因素（CH1），且因子标注缺乏领域根基导致不可靠（CH2），错误会累积至因果图。

方法：提出 DKCD 框架，包含三阶段——（1）知识挖掘：基于可观察因子从领域知识库检索相关知识；（2）知识引导的因果推理：利用检索知识引导 LLM 发现潜在因子并生成关键因果线索，以此修正因子标注；（3）因果结构发现：基于更完备的因子集和更准确的标注构造最终因果图。

结果：在两个领域特定数据集上，DKCD 显著提升了因果因子识别的召回率与精度，同时构造的因果图在标准评价指标（如 F1、SHD）上均优于仅用 LLM 常识的基线方法。
