---
title: Conditionally Identifiable Latent-Environment Modeling for Out-of-Distribution
  Recommendation
title_zh: 面向分布外推荐的条件可识别潜在环境建模
authors:
- Qianqian Wang
- Wenwu Gong
- Yunshan Li
- Zhenqing Wu
- Ruili Wang
- Lili Yang
affiliations:
- Southern University of Science and Technology
- Massey University
arxiv_id: '2608.03647'
url: https://arxiv.org/abs/2608.03647
pdf_url: https://arxiv.org/pdf/2608.03647
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 分布外推荐 · 潜在环境识别
tags:
- OOD Recommendation
- Latent Environment
- Identifiable Representation
- Variational Inference
- Causal Representation
one_liner: 提出可识别潜在环境的推荐框架，利用条件指数族和特征索引多项式建模偏好偏移，并通过边际化预测提升OOD鲁棒性
practical_value: '- 在推荐模型中引入用户条件化的隐环境变量，用变分推断估计环境分布，然后对物品预测做边际化，可提升对季节、地域、营销活动等偏移的鲁棒性，直接用于精排或召回阶段

  - 训练时使用风险上界（excess deployment log-risk）作为优化目标，可参考其推导出的一种稳健损失，结合环境推断误差联合优化，比单纯对抗训练或不变性约束更易落地

  - 特征索引多项式作为解码器，能够精细刻画环境如何改变偏好，适合建模多维度偏移（如时间+地域），可迁移到电商跨域推荐或广告跨场景预估

  - 可识别性理论保证在充足变化和正确模型设定下，所学表征有清晰语义，便于后续分析环境成因（如大促期间品类偏好变化），增强模型可解释性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：推荐系统在部署时常面临由隐环境（如时段、地域、活动）引起的偏好偏移，现有环境感知方法对隐环境的统计定义模糊，难以可靠捕获并利用环境信息。  
方法：将任务形式化为**条件可识别的风险感知推荐（CI-RR）**，并提出 CILER 框架。CILER 用**用户条件指数族分布**建模隐环境，通过**特征索引多项式**指定环境如何调制物品偏好。训练时采用变分推断估计环境后验，预测时在推断的环境分布上边际化物品概率。理论表明，在充足变化、正确设定和解码器正则条件下，环境敏感表征可识别到等价类；同时用环境推断误差界定了部署对数风险的上界。  
结果：在三个真实数据集上，覆盖特征偏移、时间偏移和地理偏移三种 OOD 场景，CILER 在全部 12 个 OOD 排序指标（如 NDCG、Recall）上取得提升，仅考虑训练和测试共享的相同支持集。控制实验验证了充足变化和模型设定对可识别性的必要性。
