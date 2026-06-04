---
title: Rethinking Sales Lead Scoring with LLM-based Hierarchical Preference Ranking
title_zh: 基于LLM的分层偏好排序重新思考销售线索评分
authors:
- Chenyu Zhang
- Yiwen Liu
- Yin Sun
- Xinyuan Zhang
- Yuji Cao
- Junming Jiao
- Juyi Qiao
affiliations:
- Li Auto Inc.
arxiv_id: '2606.04387'
url: https://arxiv.org/abs/2606.04387
pdf_url: https://arxiv.org/pdf/2606.04387
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: 销售漏斗转化预测 · 学习排序 · 偏好优化
tags:
- Sales Lead Scoring
- LLM
- Preference Optimization
- Learning to Rank
- Bradley-Terry
- LoRA
one_liner: 将稀疏转化标签转化为漏斗层级偏好对，结合LLM语义理解与边际感知Bradley-Terry目标，实现线索的精确排序与校准
practical_value: '- **漏斗层级偏好对构建**：借鉴将用户行为序列转化为偏好对（如加购>浏览>点击）的思路，在电商推荐中可利用用户行为深度构造软标签，配合边际参数表达业务知识（如高意向行为给予更大margin），缓解长周期转化中正负样本粗糙的问题。

  - **三头LLM判别式架构**：语义头（防止遗忘）、点估计头（校准）、排序头（相对序）的联合设计可迁移到Agent多任务场景：在LLM基础上挂接多个预测头，用不同的损失函数同时优化生成、校准和排序能力，配合差异化学习率避免过拟合。

  - **LLM+LoRA提取文本表示注入传统模型**：将LLM编码的对话嵌入注入Wide&Deep、DeepFM等CTR模型，可无痛提升传统模型对非结构化文本的理解，适合已有CTR基建的团队快速引入LLM语义能力，无需推翻原有架构。

  - **在线实验设计与评估**：分层抽样+按能力层级与历史转化指标分组的A/B测试方案，以及关注前0.1%线索精准度的业务导向指标（P@0.1%），对推荐系统线上评估中如何衡量头部排序质量有直接参考意义。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
汽车、房地产等长周期销售领域，客户决策链长达数周甚至数月，最终的锁单转化标签极度稀疏，且无法区分咨询、试驾等中间行为所隐含的意向差异。传统线索评分方法——规则打分、机器学习二分类以及深度CTR模型——都将未成交线索同等视作负样本，丢弃了销售漏斗中的过程信号，并且对CRM日志中非结构化对话的语义理解不足。通用LLM虽能理解对话语义，但输出文本而非可比分数，也不具备对齐漏斗优先级的排序机制。因此，需要一种既能利用LLM语义能力，又能将稀疏终端监督转化为密集漏斗感知信号的判别式框架。

**方法**
提出三层判別式架构asLLR（LLM-based Lead Ranking）：以Qwen作为语义骨干，通过LoRA高效微调；在最后隐藏层并联三个输出头——语义头（保留语言建模能力防遗忘）、点估计头（输出校准后的转化概率）、排序头（输出用于相对比较的分数）。核心创新HPRO（Hierarchical Preference Ranking Optimization）根据漏斗阶段（锁单 > 试驾 > 仅通话 > 战败）自动构造偏好对，并引入边际感知的Bradley-Terry目标进行优化：偏好概率P(x_w ≻ x_l) = σ(s_pair(x_w) - s_pair(x_l) - m)，其中m为不同配对层级（全局优势、关键动作、软信号）预设的边际值，显式注入业务先验。总损失=点估计BCE损失+HPRO损失+语义CE损失，并通过差异化学习率（头部5e-5，骨干2.5e-6）防止过拟合。

**实验**
在NEV品牌的两个数据集上验证：Benchmark数据集（340k样本）对比Wide&Deep、DeepFM、xDeepFM、DCN等CTR基线，asLLR+HPRO取得AUC 0.8161，较最优基线DeepFM（0.7917）提升2.3%，行外注入文本表示使传统模型平均AUC提升0.007；工业数据集（6.14M样本）上，前0.1%线索查准率P@0.1%从18.44%提升至25.76%，相对提升39.7%；132天省级A/B测试带来9.5%的销量提升（p<0.001）。

**关键洞察**
漏斗信息最适合作为结构化偏好监督注入排序目标，而非硬性排序规则；LLM的语义表示可泛化迁移至传统模型，而HPRO通过边际设计将业务知识平滑融入损失，在保证校准的同时显著强化顶部排序精度。
