---
title: 'The Verification Horizon: No Silver Bullet for Coding Agent Rewards'
title_zh: 验证的边界：编码智能体奖励没有万能解
authors:
- Binghai Wang
- Chenlong Zhang
- Dayiheng Liu
- Jiajun Zhang
- Jiawei Chen
- Mouxiang Chen
- Rongyao Fang
- Siyuan Zhang
- Xuwu Wang
- Yuheng Jing
affiliations:
- Qwen Team
arxiv_id: '2606.26300'
url: https://arxiv.org/abs/2606.26300
pdf_url: https://arxiv.org/pdf/2606.26300
published: '2026-06-23'
collected: '2026-06-26'
category: Agent
direction: Agent奖励设计 · 验证信号共同演化
tags:
- Verification
- Reward Hacking
- Coding Agent
- RLHF
- Scalability
- Robustness
one_liner: 论证验证信号需兼具可扩展性、忠实性与鲁棒性，四种奖励构建实验指出验证必须与生成器协同演化
practical_value: '- 在推荐/广告排序模型优化中，离线代理指标（如CTR预估）常偏离真实业务目标，可借鉴可扩展–忠实–鲁棒三维框架，定期用用户直接反馈（类似论文“用户作为验证器”）校准奖励，防止过拟合代理指标。

  - 生成式推荐（如Semantic ID生成）场景，生成器与验证器应联合迭代更新，防止固定验证标准导致的奖励黑客；可引入自动渐进验证器，随生成能力提升动态调整评估维度。

  - 多智能体协作推荐中，对开放意图的用户Query，可采用类“rubric verifier”思路，将模糊需求分解为多个可自动检查的子指标（如多样性、时效性、相关性），提升验证信号鲁棒性。

  - 长周期购物助手Agent任务中，可设计自动化验证Agent监控并分段评估推荐链路的中间步骤，降低人工评估成本，同时保持信号忠实性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统观念认为验证比生成容易，但在现代编码智能体中，随着基础模型推理能力增强，生成复杂候选方案已不难，可靠验证反而成为瓶颈。每一个验证器都是人类意图的代理，本身存在意图不明确和优化漂移的双重困难——意图天然难以精准刻画，且在模型训练中代理与真实意图的差距会被放大，引发奖励黑客或信号饱和。

**方法**：论文提出从可扩展性、忠实性、鲁棒性三个维度评价验证信号质量，并系统研究了四种奖励构建：通用编码任务的测试验证器、前端任务的rubric验证器、真实场景的用户作为验证器、长周期任务的自动化agent验证器。针对不同任务类型和策略能力层次，深入分析奖励设计的核心挑战与利用方式。

**结果**：定向验证设计能有效抑制奖励黑客，提升任务完成质量，在多个内部与公开基准上取得显著提升。核心发现是：没有一种固定奖励函数能随策略能力持续保持有效，验证必须与生成器共同演化。
