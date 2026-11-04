---
title: Multi-Agent Relay Thinking
title_zh: 多智能体接力思考框架
authors:
- Xu Liu
- Jungang Qiao
- Guikun Chen
- Xiaojuan Qi
- Wenguan Wang
affiliations:
- Zhejiang University
- Nanyang Technological University
- The University of Hong Kong
arxiv_id: '2610.35219'
url: https://arxiv.org/abs/2610.35219
pdf_url: https://arxiv.org/pdf/2610.35219
published: '2026-10-26'
collected: '2026-11-04'
category: MultiAgent
direction: 多智能体接力协作优化
tags:
- Multi-Agent
- Relay Thinking
- Confidence-guided
- LLM Reasoning
- Token Efficiency
- MACR
one_liner: 提出置信度引导的多智能体接力协作框架 MACR，动态转移推理权，在保持精度下大幅降低 token 开销
practical_value: '- 在电商 Agent 工作流中，可以将多步推理任务（如商品卖点提炼、广告文案生成、query 意图改写）从“多 Agent 并行讨论再聚合”改为“接力式串行
  refinement”，每个节点基于置信度决定是否继续、由哪个专职 Agent 接手，能显著降低 token 消耗，适合高并发在线服务。

  - 借鉴 MACR 的 bidding 机制：为不同能力 Agent 设置轻量置信度打分器，在推理阶段动态选择下一步执行者，而不是固定 pipeline，这能提升异构模型组合的鲁棒性。

  - 置信度引导的 relay triggering 可用于推荐解释生成或搜索排序后文案生成：当当前生成结果置信度低于阈值时再触发下一轮精炼，避免无意义重写，节省
  LLM 调用成本。

  - 主要学术贡献在于多智能体拓扑结构与协作效率，业务迁移时需注意：置信度估计本身可能引入额外开销，建议在关键高价值链路（如广告创意生成）而非全链路铺开。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
现有多智能体协作多采用“群体思考”拓扑：多个 Agent 独立生成答案，再聚合或讨论。这种方式虽能利用互补能力，但 token 开销大，且难以形成逐步深化的推理轨迹。本文提出“接力思考”拓扑：推理所有权随阶段动态转移，后续 Agent 继承并精炼已有推理链。  

**方法关键点**  
提出 Multi-Agent Confidence-guided Relay（MACR）框架，核心解决两个问题：何时接力、由谁接力。通过置信度引导的 relay triggering，当当前 Agent 对中间结果置信度不足时触发一次接力；再通过 bidding 机制，各候选 Agent 给出置信度报价，选择置信度最高的 Agent 继续推理。整个过程动态构建异构 Agent 间的串行精炼链路。  

**关键结果数字**  
在四个基准上，MACR 精度超过最强单模型策略：MathVista +3.3%、MMStar +3.9%；与多智能体策略精度相当，但在 HallusionBench 和 MMStar 上 token 开销减少 6.0×。分析显示接力协作能让异构 Agent 在不同推理阶段逐步整合互补见解。
