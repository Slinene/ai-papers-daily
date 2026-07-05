---
title: Will Scaling Improve Social Simulation with LLMs?
title_zh: 扩展会改善基于LLM的社会模拟吗？
authors:
- Caleb Ziems
- William Held
- Su Doga Karaca
- David Grusky
- Tatsunori Hashimoto
- Diyi Yang
affiliations:
- Stanford University
- Open Athena
arxiv_id: '2607.02464'
url: https://arxiv.org/abs/2607.02464
pdf_url: https://arxiv.org/pdf/2607.02464
published: '2026-07-02'
collected: '2026-07-05'
category: Eval
direction: 社会模拟扩展定律评估
tags:
- Scaling Laws
- Social Simulation
- LLMs
- Behavioral Modeling
- Opinion Modeling
- Calibration
one_liner: 发现LLM社会模拟在多数任务上随规模改善，但行为偏差校准等任务不随扩展改善
practical_value: '1. 当用LLM模拟用户行为（如点击、购买）做离线评估时，扩大模型可提升主流用户群的模拟准确度，但小众群体或风险偏好等认知偏差校准不会随规模改善，需额外校准或引入心理学模型。

  2. 纵向用户兴趣预测扩展缓慢，若用于推荐系统中的长期用户建模，应结合真实行为序列，不宜单纯依赖大模型模拟。

  3. 可利用本文的分层评估思路：对多数群体用大模型模拟生成训练数据，对少数群体做针对性数据增强或微调。

  4. 行为模拟中的认知偏差问题提示：大模型未必自然具备人类的非理性决策（如从相关任务学习奖励），在强化学习环境或Agent模拟中需显式设计偏差机制。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM社会模拟是研究社会现象的有效方法，但其保真度尚不足以广泛采用。亟需探明：当前语言模型的扩展范式能否缩小这一差距，还是模拟保真度与通用能力正交，需独立研究。

### 方法
基于扩展定律，系统考察计算规模、通用能力基准与社会模拟保真度之间的关系。选取三个代表性子领域：意见建模、行为模拟、纵向预测。使用85个Qwen3架构的Transformer模型，在DCLM网络文本语料上预训练，计算预算从10^18至10^20 FLOPs固定；并评估35个更大规模的开放权重模型（最高70B）。从预训练损失预测下游任务准确率。

### 结果
1. 意见建模和行为模拟任务随规模显著改善，尤其是英语网络语料中代表性好的人群。
2. 纵向预测和代表性不足的意见扩展更慢，这些任务与MMLU等通用知识推理基准相关性较低。
3. 行为模拟中，模型校准与人类认知偏差（如风险厌恶）以及基于相关任务学习奖励的启发式不随规模改善；即使微调，从0.5B到8B性能提升极微。
4. 结论：规模能在多数场景提升社会模拟，但存在异常值，低资源领域改善不可靠。
