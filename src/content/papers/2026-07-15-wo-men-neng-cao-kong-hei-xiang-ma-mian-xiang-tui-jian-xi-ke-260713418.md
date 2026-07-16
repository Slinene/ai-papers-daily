---
title: Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender
  Systems with Collaborative Agents
title_zh: 我们能操控黑箱吗？面向推荐系统可控性的协同智能体评估框架
authors:
- Jiwen Zhou
- Xiang Liu
- Mingming Li
- Pengbo Mo
- Jiao Dai
- Honglei Lv
- Jizhong Han
- Songlin Hu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
arxiv_id: '2607.13418'
url: https://arxiv.org/abs/2607.13418
pdf_url: https://arxiv.org/pdf/2607.13418
published: '2026-07-15'
collected: '2026-07-16'
category: Eval
direction: 推荐系统可控性评估 · 多智体协同
tags:
- controllability
- evaluation
- multi-agent
- recommender systems
- black-box auditing
one_liner: 首个多智能体协同可控性评估框架CtrlBench-Rec，量化推荐系统在目标发现、画像塑造、偏见缓解上的可引导性，揭示长尾内容顽固抵抗
practical_value: '- 多智能体协作的评估范式可直接复用到电商推荐，用Agent模拟用户下达明确指令（如“推荐更多登山装备”），量化系统对显式意图的响应能力，构建内部可控性测试集。

  - 三大评估任务（目标内容发现、兴趣画像塑造、流行度偏差缓解）可作为新增CTR/AUC之外的离线评测维度，尤其适合检验推荐结果是否被热门头部绑架，与长尾新品冷启、ESG目标对齐。

  - 框架暴露长尾内容极难被引导，提示业务侧在召回层设计时必须引入显式引导通道（如query介入或主动探索模块），而不能仅靠隐式反馈。

  - 可将CtrlBench-Rec改造为审计工具，连续监测推荐系统在特定类目（如合规限制类目）上的可控性，为监管自查提供自动化手段。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

当前推荐系统评估几乎不衡量“可控性”——系统能否按用户或监管方的明确意图调整输出。本文提出CtrlBench-Rec，一个多智能体协同框架，系统评估推荐系统对显式引导的响应能力。框架定义了三个递进任务：① 目标内容发现，给定具体内容，检验系统是否能在Top-K中呈现；② 兴趣画像塑造，通过模拟用户自主标注兴趣标签，观察推荐分布变化；③ 流行度偏差缓解，引导系统提升长尾内容曝光，检验反偏差能力。实验覆盖多个真实数据集和经典/深度学习推荐模型，结果表明框架能有效量化各任务下的可控性得分，同时暴露出现有模型对长尾内容引导的高度抗性——即使强力干预，长尾内容排名提升仍十分有限。CtrlBench-Rec是首个推荐可控性标准化评估工具包，为算法审计、用户赋权和可控推荐研究提供了基础支撑。
