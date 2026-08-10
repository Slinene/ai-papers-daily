---
title: 'CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing'
title_zh: CoBa：通过计算均衡路由实现具成本效益的测试时扩展
authors:
- Yan Zhou
- Yue Ouyang
- Kaiyang Zheng
- Suncheng Xiang
affiliations:
- School of Mathematics and Statistics, Changsha University of Science and Technology,
  Changsha, China
- School of Biomedical Engineering, Shanghai Jiao Tong University, Shanghai, China
arxiv_id: '2608.07424'
url: https://arxiv.org/abs/2608.07424
pdf_url: https://arxiv.org/pdf/2608.07424
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM 测试时计算优化
tags:
- test-time scaling
- compute routing
- verification
- LLM reasoning
- cost efficiency
one_liner: 提出计算均衡路由策略，动态分配生成与验证预算，以更少计算匹配多数投票准确率。
practical_value: '- **多候选验证的预算分配**：在生成式推荐或搜索中，当需要从多个候选 query/item 中投票选择时，可先使用廉价验证器（如轻量级打分模型）过滤大量候选，仅将高不确定性或高价值候选送入昂贵的大模型验证，大幅减少
  LLM 调用成本。

  - **Agent 循环中的动态路由**：在涉及规划-执行-评估的 Agent 系统中，可借鉴 CoBa 的“生成 vs 验证 vs 停止”决策框架，由路由模块实时判断下一步应生成更多方案、调用评估器，还是直接输出结果，避免无效计算。

  - **在线服务成本控制**：对于对延迟敏感的电商实时推荐，可基于 CoBa 的停止规则设定置信度阈值，当廉价验证结果一致性高时提前终止，节省的 token 可分配给更复杂的用户意图理解场景。

  - **粗-精验证管道设计**：构建类似于 CoBa 的两级验证结构，第一级用规则或小模型快速打分，第二级用大模型深挖，这在商品标题改写、用户评论情感分析等场景中可直接复用，提升吞吐量。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：测试时计算通常沿单一维度扩展（多采样、长思维链、强评估器），在固定推理预算下这些操作相互竞争，缺乏细粒度的动态分配策略。

**方法**：将测试时推理形式化为计算分配问题——在每一步决定将下一个计算单元用于生成新候选、执行廉价验证、调用强验证器，还是停止。提出 CoBa 路由策略：首先生成少量候选答案，用廉价验证器（如模型自评估）广泛评估；然后根据不确定度或候选价值，将部分候选路由到强验证器（如评分模型）做最终判断；最终通过加权投票等机制聚合结果。

**结果**：在 MATH-500、AIME 2024/2025、AMC 2023 等数学推理基准上，CoBa-Routed-Strong 宏平均准确率达到 85.13%，与自评估加权投票代理（85.20%）统计匹配，但使用的参数加权 token 减少了 49.1%；与 best-of-16 多数投票相比准确率仅差 0.01 个点，而 token 节省 58.9%。与单样本解码相比，提升显著。剩余与池 oracles 的差距表明路由策略仍有优化空间。
