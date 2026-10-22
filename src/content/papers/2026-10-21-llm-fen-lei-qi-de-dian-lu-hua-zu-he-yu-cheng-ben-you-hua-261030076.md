---
title: Circuits of LLM Classifiers
title_zh: LLM 分类器的电路化组合与成本优化
authors:
- Hadi Khalaf
- Sajani Vithana
- Kunal Talreja
- Haewon Jeong
- Viveck R. Cadambe
- Flavio Calmon
affiliations:
- Harvard School of Engineering and Applied Science
- Kempner Institute for the Study of Natural & Artificial Intelligence
- School of Electrical and Computer Engineering, Georgia Institute of Technology
- Department of Electrical and Computer Engineering, University of California, Santa
  Barbara
- Center for Computational Mathematics, Flatiron Institute
arxiv_id: '2610.30076'
url: https://arxiv.org/abs/2610.30076
pdf_url: https://arxiv.org/pdf/2610.30076
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM 多分类器自适应组合与成本优化
tags:
- LLM classifiers
- cost-accuracy tradeoff
- routing
- cascading
- inference optimization
- ensembling
one_liner: 将多个 LLM 分类器组织为自适应查询电路，以更低成本突破路由/级联的准确率前沿
practical_value: '- 在电商/广告/搜索中，LLM 常用于意图分类、商品属性打标、内容审核、相关性评分等；借鉴电路思想，将不同 prompt/模型/温度配置视为带成本的分类器，基于混淆矩阵动态调度，比固定级联更省调用成本。

  - 工程实现上，可把每个 LLM 分类器封装为统一 Query/Decision 节点，离线用验证集估计各节点的 per-class 错误率和成本，再用动态规划搜索给定预算下的最优执行路径；在线按查表决策，适合批量打标和实时流量。

  - 需要低成本高可靠性的 LLM 评审或 guardrail 场景，可先用便宜模型筛简单样本，对不确定性样本再追加强模型或 self-consistency，但要预先校准各分类器的条件错误率，避免误差传播。

  - 对 Agent 评估 / 自动评测 / 推荐理由质量把关等任务，论文结论支持在多个弱监督信号之间做电路化融合，不等同于简单投票或级联，能更高效利用算力预算。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 分类器通过 prompt 构建十分便捷，但预测非确定、且可靠性在不同样本间波动很大；如何组合多个分类器提升整体可靠性，同时控制平均查询成本？

方法：把每个 LLM 分类器视为对目标标签的噪声测量仪器；引入可组合的“电路”结构，将分类器组织成自适应查询与决策序列。与固定路由/级联不同，电路根据前序分类器的输出动态决定下一步调用哪个模型或直接给出标签。论文刻画了最优电路的形式，给出可达准确率的基本极限，并说明如何利用各分类器的条件错误概率与成本实现近似最优电路。

结果：在安全、健康、政治科学、人类偏好、agent 评估、决策、推理七类任务上，该方法均优于 routing 和 cascading baselines，改善了成本-准确率前沿。
