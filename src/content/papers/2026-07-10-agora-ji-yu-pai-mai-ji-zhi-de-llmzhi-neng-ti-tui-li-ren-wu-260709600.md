---
title: 'Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation'
title_zh: Agora：基于拍卖机制的LLM智能体推理任务分配框架
authors:
- Kaiji Zhou
- Ales Leonardis
- Yue Feng
affiliations:
- University of Birmingham
arxiv_id: '2607.09600'
url: https://arxiv.org/abs/2607.09600
pdf_url: https://arxiv.org/pdf/2607.09600
published: '2026-07-10'
collected: '2026-07-13'
category: MultiAgent
direction: 拍卖机制驱动的多智体任务分配优化
tags:
- Agent Orchestration
- Auction Mechanism
- Calibration
- Multi-Agent Reasoning
- LLM Routing
- Confidence Calibration
one_liner: 通过校准置信度的拍卖机制，将复杂推理任务动态分配给最合适的专家模型，实现成本-质量可控。
practical_value: '- 将推理流水线分解为子任务，以校准后的置信度作为出价基础，通过拍卖动态选择最优专家模型/工具，适合电商搜索、推荐系统中的多模型路由，有效降低推理成本并避免过度自信导致的错误分配。

  - 校准策略（分组缩放+直方图分箱+在线自适应）可直接复用：先用静态校准器在多样化数据上消除原始模型置信度的系统性偏差，再用在线更新适配业务特有分布，确保模型选择基于真实能力而非幻觉。

  - 成本敏感参数β提供直接的成本-质量调节旋钮，可在不同流量层级或业务优先级下灵活切换：Quality-First、Balanced、Cost-Efficient三种预设模式无需重新训练，适合成本敏感的线上服务。

  - 框架与规划器解耦，可作为可插拔的分配层加入现有Multi-Agent系统，不侵入内部模型，也能集成数据集提供的分解步骤或基于LLM生成的依赖图，对搜索、Agent系统的容错调度有借鉴意义。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有LLM多智能体系统通常基于粗粒度匹配或静态分配专家模型，忽略了候选模型间的性能差异和成本效率，而细粒度动态分配面临智能体过度自信的挑战——模型输出的原始置信度不可靠，容易导致关键子任务分配给‘高置信但低胜任’的智能体。

**方法关键点**：
- **规划与任务单元提取**：LLM规划器将查询分解为有向无环图，然后通过启发式合并紧密耦合的节点形成可执行的“任务单元”，确保投标粒度适中。
- **层次化置信度校准**：静态校准器S利用分组缩放和基于KD-Tree的直方图分箱，在多样化基准上训练，输出基础校准置信度；动态校准器S′使用在线梯度下降（基于反馈标签）进一步修正分布偏移，迫使智能体出价反映真实能力。
- **拍卖出价与选择**：每个智能体对任务单元的出价 = 校准置信度的幂律变换（γ压缩高置信区分度） − β × 归一化成本（结合金钱消耗与吞吐量）。成本敏感参数β控制全局偏向：β≈0优先准确性，β增大优先成本效率。
- **执行与闭环优化**：中标智能体执行子任务，可选地将正确性反馈用于更新S′，实现持续适应。

**关键结果**：在MuSiQue、MMLU-Pro、SciCode、SPIQA、MathVision五个基准上，Agora在匹配的候选池下对比单模型、随机路由、级联和学习路由器等基线。
- MuSiQue（多跳QA）：EM 43.0, F1 54.3，优于所有基线。
- MMLU-Pro（多领域知识）：准确率71.9%，比最强单体模型提升3.8%。
- SPIQA（多模态科学QA）：平均L3评分65.0%，严格指标（≥0.8）56.9%，比最佳单模型提升8.7个百分点，显示出组合互补专家（Grok检索+Qwen推理）的增益。
- 消融实验证实校准是经济必需：无校准时拍卖在某些基准上性能反降（如MathVision下降4.0%），校准则转为正向增益。
- 成本灵敏度分析显示β可平滑调节成本-质量权衡，MathVision上从21.5%升至78.5% Grok使用率，准确率仅从55.3%微降至51.1%。

**核心洞见**：拍卖结构本身不足以保证分配质量，可靠的置信度校准才是防止‘赢家诅咒’的胜负手。
