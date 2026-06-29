---
title: 'From Bootstrapping to Sequence Modeling: A Unified Generative Framework for
  Personalized Landing-Page Modeling'
title_zh: 从自举到序列建模：个性化着陆页统一生成式框架
authors:
- Fan Li
- Chang Meng
- Jiaqi Fu
- Shuchang Liu
- Tianke Zhang
- Xueliang Wang
- Xiaoqiang Feng
- Yongqi Liu
- Kaiqiao Zhan
affiliations:
- Duke University
- Kuaishou Technology
arxiv_id: '2606.27865'
url: https://arxiv.org/abs/2606.27865
pdf_url: https://arxiv.org/pdf/2606.27865
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: 个性化着陆页选择 · Decision Transformer
tags:
- Personalized Landing Page
- Decision Transformer
- Sequence Modeling
- Offline RL
- Hierarchical Reward
- L-RTG
one_liner: 提出基于Decision Transformer的GLAN框架，用日级回报引导与分层奖励模型解决信用分配，在线提升DAU+0.158%和LT+0.108%。
practical_value: '- 对于拥有多入口（首页、推荐页、关注页等）的平台，可将每日多次启动的推荐决策转化为序列建模问题，用Decision Transformer捕获跨会话依赖，替代传统MDP+Q-learning。

  - 日级RTG预测模块(L-RTG)结合周期性attention与序列动态建模，通过约束优化同时预测用户当天总使用时长和会话数，为日内所有页面分配提供全局目标信号，避免手动设定目标值的OOD问题。

  - 分层奖励模型(HRM)将会话总时长拆解为各页面类型时长并预测落地页快速退出风险，用focal loss处理样本不均衡，有效分辨“偏好匹配”与“下游补偿”的信用模糊，可作为多页面场景下动作评价的通用方案。

  - 推理时将RTG作为可消耗预算动态更新，实现闭环自适应策略；该模式可迁移到电商权益分配、消息推送节奏控制等需要日级长期价值最大化的场景。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
快手等平台采用多页面架构，用户每次进入APP时被分配到某个落地页（如精选、发现、关注页），这一导航决策直接影响后续参与度和留存。传统强化学习方法（如原方案KLAN基于CQL）存在两个根本缺陷：(1) 马尔可夫假设难以捕捉用户行为中的强非马尔可夫时序依赖；(2) TD学习在延迟奖励下累积误差和信用分配困难，尤其在用户每天多次进入APP的长周期场景中。为此，需要一种能够全局建模日内轨迹、精确评估单次会话价值的序列决策框架。

## 方法
GLAN基于Decision Transformer，从全局-局部统一视角优化个性化落地页分配，包含两个关键模块：
- **L-RTG（日级回报预测）**：预测用户当天的总使用时长，作为初始目标回报。由周期感知的注意力编码器（引入模-7偏置捕获周周期）和序列动态建模的Transformer编码器并行提取特征，通过自适应门控融合后预测使用时长和会话次数，采用约束优化同时保证预测精度和两个目标的经验一致性。
- **HRM（分层奖励模型）**：将会话级反馈分解为各页面类型消费时长和落地页快速退出风险，使用MMoE多任务学习，结合focal loss处理退出标签不均衡，最终输出风险校准后的会话价值作为即时奖励，为每次页面分配提供精细的局部监督。
推理时，每日初始调用L-RTG生成目标RTG，每次进入应用时DT以当前状态、剩余RTG和历史轨迹自回归生成落地页动作，会话结束后HRM计算奖励并更新RTG，形成闭环决策。

## 实验
在快手平台部署并进行56天在线A/B测试（14天AA + 42天AB），对比基线为原来的CQL方案KLAN。主要结果：
- DAU提升0.158%，LT提升0.108%。
- APP使用时长+0.369%，观看时长+0.394%，视频曝光+0.469%，页面退出率下降15.832%。
- 消融实验中，去掉L-RTG或HRM后各项指标明显下降，验证了全局引导和分层奖励的重要性。
- 页面分配分布更均衡，精选页分配比例下降，发现页和关注页上升，同时各页面有效进入频率均正向增长，说明模型挖掘了被忽视的多样化意图。
