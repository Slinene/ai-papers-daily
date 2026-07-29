---
title: 'MARS: Multi-Agent Re-ranking for Repeat-Order Food Delivery Recommendation'
title_zh: MARS：面向外卖复购推荐的多智能体重排序框架
authors:
- Jiahao Tian
- Zhenkai Wang
affiliations:
- Georgia Institute of Technology
- The University of Texas at Austin
arxiv_id: '2607.25420'
url: https://arxiv.org/abs/2607.25420
pdf_url: https://arxiv.org/pdf/2607.25420
published: '2026-07-28'
collected: '2026-07-29'
category: MultiAgent
direction: 多智能体协作重排序
tags:
- Multi-Agent
- LLM Re-ranking
- Food Delivery
- Repeat-Order
- Coarse-to-Fine
- Collaborative Filtering
one_liner: 结合轻量级协同召回与 LLM 分阶段重排序，证明预训练 LLM 在复购推荐中可匹敌专用模型。
practical_value: '- 粗排-精排两阶段设计：先用 LightGCN 进行菜系（cuisine）级粗排，再结合 Swing 协同相似度和 LLM 进行商家（vendor）精排，有效降低候选集大小，适合电商中品类多、商家多的长尾场景。

  - 协同信号作为 LLM 输入：不抛弃成熟的协同过滤，而是将 LightGCN 的全局偏好与 Swing 的局部共现信息提炼成文本证据供 LLM 推理，简单且实用。

  - 多智能体框架提升可解释性：Manager 调度、Profiler 提取特征、Analyzer 预测菜系、Critic 排序商家，中间输出结构化，便于监控和调试，尤其适合需要业务可解释性的推荐系统。

  - 推理时计算（test-time compute）能带来额外收益：启用 LLM 的 thinking 模式让模型在输出前自我修正，显著提升重排序精度，成本允许时可在关键环节采用。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：外卖复购推荐需要同时融合长期口味、短期时间上下文、地理位置和用户习惯，传统深度模型端到端优化虽然有效，但缺乏灵活性且可解释性差。LLM 在推荐中展现潜力，但性能提升究竟来自预训练知识还是检索管道本身并不清楚。MARS 通过一个受控的混合框架，回答「强大预训练 LLM 结合轻量级协同召回在复购推荐中能走多远」。

**方法关键点**：
- **两阶段粗到细设计**：第一阶段 Analyzer 预测用户可能感兴趣的菜系，用 LightGCN 提供的菜系偏好作为先验，结合近期行为生成菜系候选；第二阶段 Critic 在菜系过滤后结合地理可用性，利用 Swing 相似度找到类似用户的历史，输出商家排序。
- **多智能体协作**：Manager 负责流程控制和异常回退，Profiler 收集用户历史、地理候选和协同信号，Analyzer 和 Critic 各自完成推理，避免单个大模型处理全量信息的困惑。
- **轻量级协同信号**：使用三层的 LightGCN（BPR 损失）提供全局菜系偏好，参数自由的 Swing 相似度提供近邻用户共现证据，两者作为结构化 prompt 输入 LLM，无需复杂训练。
- **推理时扩展**：允许 LLM 输出前进行多步推理（thinking 模式），通过自我修正提升排序质量。

**实验结果**：在两个真实外卖数据集 DHRD-SE（瑞典斯德哥尔摩）和 DHRD-SG（新加坡）上评估重复购买场景，与启发式、序列模型、图神经网络和专用外卖模型对比。Gemini-2.5-Pro 在 DHRD-SE 上 HR@3 达 0.756，比最优非 LLM 基线 SNPR 提升 4.4%；在 DHRD-SG 上 NDCG@3 达 0.601，比 DPVP 提升 7.3%。消融实验显示，加入 LLM 推理后菜系命中率从仅 LightGCN 的 0.65 提升到 0.85，两阶段管道进一步带来收益。此外，更强的模型和启用 thinking 模式都能稳定提升效果。
