---
title: 'InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost'
title_zh: InfluMatch：用4B模型级联实现媲美前沿LLM的泰语KOL搜索
authors:
- Krittanon Kaewtawee
- Petmongkon Pornpichitsuwan
- Natchaya Temyingyong
- Nutnicha Laplamoon
- Wachiravit Modecrua
- Krittin Pachtrachai
- Touchapon Kraisingkorn
affiliations:
- Amity AI Holdings Co., Ltd.
arxiv_id: '2607.05968'
url: https://arxiv.org/abs/2607.05968
pdf_url: https://arxiv.org/pdf/2607.05968
published: '2026-07-07'
collected: '2026-07-08'
category: RecSys
direction: 多阶段级联 · 偏好优化重排 · KOL匹配
tags:
- KOL matching
- multi-stage cascade
- SimPO
- LLM reranker
- pointwise scoring
- synthetic data
one_liner: 提出三阶段检索-重排-评分级联，用4B开源模型达到94.1% P@5，仅需前沿LLM 1/35的输出令牌
practical_value: '- **级联设计降低推理成本**：将昂贵的评分阶段仅作用于前10候选人类似于召回→粗排→精排，在商品推荐中可将LLM评估限制在小范围，大幅节省令牌与延迟。

  - **用偏好优化（SimPO）训练点式重排器**：仅利用人类成对偏好数据微调4B模型做单令牌“Yes”概率打分，比生成式A/B判断更经济且效果匹配前沿模型，适用于电商搜索的第二阶段精排。

  - **绝对标签未必比相对判断更有效**：基于绝对分数微调的评分器在离线指标上胜出但端到端下降，表明在电商场景中若标注存在主观性和噪声，更应收集成对优劣信号而非绝对评分。

  - **合成数据生成管道可复现**：通过 personas + 规则约束 + 网络搜索生成逼真的请求和标准，可为搜索/推荐系统的训练数据合成提供模板，降低真实业务数据不足的影响。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
泰语市场的KOL匹配面临自由格式、多维度营销要求的语义理解难题。传统关键词搜索无法捕捉语义契合度，而利用前沿LLM逐个评分虽准确但缓慢昂贵。需要一套低成本的级联方案，在有限资源下实现高精度匹配。

### 方法关键点
- **三阶段级联架构**：检索（向量召回50个候选）→重排（4B点式打分，保留10个）→评分（4B模型按标准进行0/1/2打分并给出泰语理由）。
- **重排器训练**：用SimPO直接优化“Yes”令牌的对数概率，仅靠人类成对优劣标签，无需参考模型，训练与推理目标一致。
- **评分器训练**：尝试用SFT+GRPO基于绝对分数微调，但在端到端测试中不如未微调基座模型。
- **数据合成**：通过 persona 采样、规则约束、网络搜索生成逼真泰语营销简报，再扩展为5个匹配标准，并收集点式、二值、成对多目标标注。

### 关键实验与结果
- **端到端P@5**：SimPO重排 +基座评分在11个全标注查询集上达到94.1%，比仅召回高近40点，与前沿模型Kimi-K2.6（91.8%）相当，但输出令牌少约35倍。
- **重排器离线EM**：SimPO微调的4B模型在成对测试上达到78.0%最佳选择准确率，与Kimi-K2.6持平，且显著扩大“最优-最劣”评分间隔。
- **评分器离在线反转**：SFT+GRPO微调评分器在支持加权F1上最高达59.0，但端到端P@5（85.9%）明显落后于基座（94.1%），根源在于绝对标签噪声大且与整体相关性目标不一致。
- **成本效率**：先重排后评分的级联比直接对全部50个候选人评分既便宜又准确（94.1% vs 80.0% P@5），令牌消耗减少近一半。

### 核心洞察
*在该领域中，可恢复的监督信号存在于相对判断中，而非绝对分数——因此基于偏好的重排器能迁移至端到端，而基于绝对分数的评分器不能。*
