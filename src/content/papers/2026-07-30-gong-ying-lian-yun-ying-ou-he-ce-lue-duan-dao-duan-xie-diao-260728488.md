---
title: 'SCOPE: Supply-Chain Operations through Coupled Policies for End-to-End Coordination'
title_zh: 供应链运营耦合策略端到端协调框架
authors:
- Yunhao Liang
- Xianqi Cao
- Pujun Zhang
- Yuan Qu
- Yongzhi Qi
- Ningxuan Kang
- Max Z. J. Shen
affiliations:
- The University of Hong Kong
- OptiMax AI
- JD.com
arxiv_id: '2607.28488'
url: https://arxiv.org/abs/2607.28488
pdf_url: https://arxiv.org/pdf/2607.28488
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 端到端供应链决策协调
tags:
- supply chain optimization
- end-to-end decision
- policy coupling
- shared representation
- replenishment planning
one_liner: 将供应链多阶段决策实体化为token，通过共享表示和顺序解码实现端到端协调。
practical_value: '- 多阶段决策耦合：推荐系统召回、粗排、精排、重排各阶段目标常不一致，可借鉴 SCOPE 的共享操作表示和顺序决策范式，让后阶段以前阶段输出为条件，端到端优化整体业务指标（如
  GMV、成交率）。

  - 业务实体 Token 化：将用户、商品、场景等视为 token，用统一编码器在上下文内交互，替代各阶段独立的特征工程，实现跨阶段信息高效复用。

  - 策略网络替代启发式规则：供应链分阶段优化多基于固定规则，类似推荐中粗排的静态打分或重排的经验规则，可替换为可学习策略，与最终效用对齐，减少碎片化调优。

  - 共享系统级效用函数：设计能评估完整推荐列表最终价值的效用模型，指导各阶段决策生成，从局部优化转向全局最优，提升全链路一致性。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：补货计划涉及选品、货源分配、补货频率与路线规划四个耦合决策，但实际供应链中各部门独立优化，常导致缺货、库存积压和高物流成本。亟需一种端到端协调方法。

**方法**：提出 SCOPE，将供应链实体（地点、商品、车辆等）表示为 token，通过共享操作表示编码全局上下文，再按逻辑顺序依次生成各决策：先选品，基于选品结果分配货源，再决定补货频率，最后规划路径。每一步以已生成的部分计划为条件，完整计划由共享系统级效用函数（综合考虑成本和服务水平）评估。模型在城市生鲜零售场景实例化，并在叮咚买菜和京东的真实数据上验证。

**结果**：在两种不同补货层级上，SCOPE 均一致优于分阶段独立优化方法和业务常用基准，证明学习跨部门操作耦合能显著提升端到端供应链决策质量。
