---
title: 'From Understanding to Action: Feedback-Grounded Policy Discovery for Generative
  Recommendation'
title_zh: 从理解到行动：基于反馈的策略发现用于生成式推荐
authors:
- Zhi Chen
- Minmao Wang
- Xingchen Liu
- Haoqiang Liang
- Huihuang Lin
- Likang Wu
- Hongke Zhao
- Yulong Wang
- Shijie Yi
- Fei Pan
affiliations:
- Huazhong Agricultural University
- Fudan University
- Kuaishou Technology
- Tianjin University
arxiv_id: '2607.27789'
url: https://arxiv.org/abs/2607.27789
pdf_url: https://arxiv.org/pdf/2607.27789
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · 策略发现与知识蒸馏
tags:
- Generative Recommendation
- Semantic ID
- LLM Agent
- Policy Discovery
- Relational Distillation
- Feedback-driven
one_liner: 识别理解-行动差距，提出反馈驱动的策略发现与关系蒸馏框架，将LLM决策知识迁移至轻量SID生成器，实现高效推荐
practical_value: '- **解耦意图与策略，用结果反馈筛选有效策略**：将推荐决策拆分为意图理解（用户要什么）和策略（怎么推荐），通过LLM生成多个候选策略，再用实际推荐结果的增量收益（相比仅意图）筛选并迭代优化策略，避免语言合理但推荐效果不佳的策略。可直接用于电商推荐中优化决策逻辑，提升收入。

  - **关系蒸馏替代直接匹配，将LLM知识迁移至轻量在线模型**：由于LLM的语义空间与行为推荐空间不一致，采用一阶与高阶关系蒸馏对齐用户间的相对结构，比直接匹配嵌入更稳定。可在广告/电商系统中离线用LLM生成意图与策略，蒸馏到轻量生成式模型，在线推理仅增加两个Token位置，延迟仅从0.023s增至0.032s，无需LLM在线调用，适合大规模部署。

  - **利用历史轨迹和群组反馈进行策略演化**：策略代理基于用户正历史子序列生成多个推荐方向与拒绝边界，执行器统一评估各策略的相对优势，反馈代理通过对比分析给出群体级优化信号，最多两轮演化即可得到稳定增益。该多候选-执行-反思的Agent协作模式可推广到其他需要决策优化的场景，如搜索重排或广告创意选择。

  - **意图与策略的粗-细分工设计**：实验表明，意图Token主要提升Semantic ID第一层（粗粒度类别）的召回，策略Token在更深层级（细粒度区分）贡献更大。可据此设计分层生成结构，由意图约束大类，策略处理细排，有效提升推荐精度。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于语义ID（Semantic ID）的生成式推荐通过序列生成直接预测下一物品，但现有方法主要依赖物品级行为监督，仅捕获共现和局部迁移，未显式分离用户需求理解与推荐决策。LLM虽能通过推理识别用户意图，但其语言合理性未必转化为有效推荐，即存在“理解-行动差距”。为此，本文区分意图知识（当前需求）和策略知识（在该需求下的推荐方向与拒绝边界），并提出反馈驱动的策略发现框架，通过推荐结果反馈筛选并优化策略，弥补这一差距。

### 方法关键点
- **任务导向意图诱导**：用LLM代理从用户历史及物品元数据中推断任务导向的文本意图，而非预测具体物品，为后续策略发现提供语义条件。
- **反馈驱动的策略发现**：
  - 策略代理基于用户历史子序列生成多个候选推荐策略（推荐方向与拒绝边界）。
  - 执行器对比仅意图基线和策略条件推荐的语义相似度，计算增量优势（Advantage）。
  - 反馈代理结合所有候选的执行结果与优势进行群组反思，识别有效模式与失败模式，驱策策略迭代演化（最多R轮），仅保留有正增益的策略。
- **双重空间关系蒸馏**：引入Intent Token和Policy Token到轻量SID生成器的解码序列，将LLM产生的意图和策略文本表示作为教师，通过一阶（直接相似度）和高阶（邻域结构）关系蒸馏对齐用户关系，而非直接匹配嵌入，消除在线LLM调用。
- **联合训练**：推荐损失（自回归生成目标SID）加上意图和策略的关系蒸馏损失，使模型直接从行为历史推断意图和策略Token状态。

### 关键结果
- 在Amazon Beauty/Toys/Sports三个数据集上，与TIGER、LETTER等基线相比，Recall@10和NDCG@10均有显著提升（如Beauty上TIGER+Ours: R@10 0.0739 vs. TIGER 0.0617）。
- 分析证实理解-行动差距：87.74%的训练用户至少一个策略有正优势；仅加Policy Token无蒸馏提升有限，完整模型最佳。意图主要提升第一层语义ID召回，策略提升更深层区分。
- 策略发现必需优势验证与迭代：去除演化或随机选择性能明显下降；目标物品描述直接作为策略效果差，说明收益来自于抽象决策原则。
- 线上A/B测试（13.25M用户，1.61M物品，7天）：相比生产基线，Revenue提升4.506%，广告主价值（ADVV）提升4.621%，在线推理延迟仅增加9ms。
- 关系蒸馏优于直接匹配，且高阶蒸馏提供互补结构信息。
