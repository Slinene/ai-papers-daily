---
title: 'WatchLens: A Configurable Platform for Online Video Recommendation Experiments'
title_zh: WatchLens：可配置的在线视频推荐实验平台
authors:
- Deogyong Kim
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2608.04807'
url: https://arxiv.org/abs/2608.04807
pdf_url: https://arxiv.org/pdf/2608.04807
published: '2026-08-05'
collected: '2026-08-08'
category: RecSys
direction: 在线实验平台与日志规范
tags:
- open-source
- online experimentation
- video recommendation
- user behavior logging
- modular architecture
one_liner: 开源模块化平台，解耦 UI/内容/策略并绑定推荐上下文到行为日志，支持可控在线实验
practical_value: '- **模块化实验架构可复用到电商推荐 A/B 平台**：将 UI、内容池、推荐策略独立配置，策略可分别注入推荐流与商品详情页，适合首页猜你喜欢与详情页关联推荐的效果隔离实验。

  - **事件级推荐上下文绑定**：日志在记录时直接附上策略名与排序位置，避免后续离线拼接，对电商用户行为归因分析（点击、加购、转化是否由具体策略/坑位导致）有直接工程参考价值。

  - **单服务器可部署**：降低在线实验搭建成本，适合团队快速搭建可控的端到端推荐效果验证环境，用于孵化新策略的商业指标检验。

  - **会话级对比分析方法**：固定界面与内容池，仅变单一环节策略，可精确测量推荐变更对用户后续行为链的影响，可直接移植到直播电商的“直播间推荐卡”或详情页推荐槽位的效果评估。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有用户实验设施要么只提供播放行为数据，要么只提供推荐条件记录，无法在一个工作流中把用户观看行为与产生它的推荐策略、排序位置直接关联，导致推荐效果的因果分析困难。

**方法**：提出 WatchLens 开源平台，采用三层可配置架构：前端界面、内容来源、推荐策略均独立模块化。关键设计是推荐策略可单独配置到信息流（feed）和观看页（watch page），实现不同槽位的策略隔离。标准化的埋点层在每次事件记录时直接附加该事件对应的推荐策略 ID 及在推荐列表中的排序位置，无需事后拼接。

**结果**：通过短视频案例验证，固定界面、信息流策略和内容池，仅改变观看页推荐策略，平台能够捕获用户从 feed 进入观看页后的播放完成度、会话持续、页面间导航等行为变化，实现会话级策略效果对比，证明平台支持可复现、可解释的在线视频推荐实验。
