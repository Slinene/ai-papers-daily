---
title: 'SurvEval: Listwise Re-Ranking Evaluator via Survival-Based Exposure and Multi-Objective
  Value Modeling'
title_zh: SurvEval：基于生存曝光与多目标价值建模的列表重排评估器
authors:
- YaChen Yan
- Liubo Li
affiliations:
- Intuit Credit Karma
arxiv_id: '2611.15434'
url: https://arxiv.org/abs/2611.15434
pdf_url: https://arxiv.org/pdf/2611.15434
published: '2026-11-11'
collected: '2026-11-13'
category: Eval
direction: 列表级重排评估器 · 生存分析曝光
tags:
- Re-ranking
- Listwise Evaluation
- Survival Analysis
- Multi-Objective Learning
- Exposure Modeling
one_liner: 提出 SurvEval，用离散时间生存模型建模用户到达概率，并结合多目标不确定加权价值估计，提升列表效用评估
practical_value: '- 电商/广告重排可显式建模用户浏览深度：将列表效用拆为“到达概率 × 条件价值”，用离散时间生存模型估计每个位置的个性化到达概率，替代固定
  log discount 或位置偏置，更适合 feed 流、搜索结果页等顺序浏览场景。

  - 多目标价值解耦与自动加权：不要将点击、时长、转化等简单加权为一个标量；每个目标独立预测头，正样本按实际效用值做加权逻辑回归，再引入 Kendall 不确定加权自动平衡不同尺度和噪声，可稳定线上多目标融合。

  - 统一 transformer 结构可复用为 listwise 打分器：用户侧融合静态特征、多兴趣提取、最近 N 条短期交互，item 侧用 ID embedding
  + 边信息，位置嵌入后过自注意力/交叉注意力；可作为 multi-generator 框架中的评估器/选择器，无需直接生成最终排序。

  - 曝光建模的工程实现简单：从日志中按用户退出位置构造逐位置二元标签，右删失样本只贡献 survival 项，损失等价于 BCE；适合从真实浏览日志中学习曝光模型，无需手工定义折扣函数。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
重排序评估器需要同时回答两个问题：用户会浏览到列表多深，以及看到每个 item 后能产生多少价值。现有方法大多用固定位置折扣代替真实浏览深度，且将点击、观看时长、点赞等多目标信号加权成一个标量，忽略不同目标的尺度和噪声差异，导致列表效用估计失真。

**方法关键点**
SurvEval 将列表效用分解为每个位置的“到达概率 × 条件价值”。
- 曝光建模：把顺序浏览看作离散时间生存过程，设 M 为退出位置，条件风险 h_phi(t|u,L)=P(M=t|M≥t)，到达概率 p_phi(t|u,L)=连乘_{j=1}^{t-1}(1-h_phi(j|u,L))，p(1)=1，保证随位置单调下降。训练时用观测轨迹的负对数似然，等价于每个位置的二元交叉熵，支持右删失。
- 价值建模：每个目标（如点击、时长、点赞）使用独立预测头，采用加权逻辑回归，正样本权重=实际效用值，推断时取 exp(logit) 恢复期望效用；多任务损失通过可学习 log-uncertainty 自动加权，防止某目标主导。
- 统一 transformer backbone：用户 token 由静态特征线性投影、多兴趣提取层聚合长期交互、最近 N 条短期交互组成；item token 为 ID embedding+边信息；两者经过位置嵌入和 transformer 层后分别进入生存头和 K 个价值头。
- 列表效用 r_phi(u,L)=Σ_{t=1}^n p_phi(t|u,L)·Σ_k w_k·v_hat^{(k)}_phi(u,I_{l_t})。

**关键实验**
在 KuaiRand（随机曝光，4 个目标）和 Avito（搜索广告点击，1 个目标）上对比 DNN、PRM、PIER、CAVE。SurvEval 在 NDCG 和 uAUC 上均最优：KuaiRand NDCG 0.8523（CAVE 0.8450）、uAUC 0.7236（CAVE 0.7196）；Avito NDCG 0.7450（CAVE 0.7371）、uAUC 0.7326（CAVE 0.7258）。提升一致但幅度有限。

**最值得记住的一句话**
将用户浏览视为离散时间生存过程，把列表效用显式拆成“到达概率 × 条件价值”的乘积求和，是比固定折扣更贴近真实行为的列表评估方式。
