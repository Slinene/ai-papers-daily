---
title: 'ClawRec: A Claw-Native Recommender System'
title_zh: 'ClawRec: 一种Claw原生的推荐系统'
authors:
- Chenghao Wu
- Kesha Ou
- Xiaolei Wang
- Bowen Zheng
- Bingqian Li
- Enze Liu
- Wayne Xin Zhao
- Weitao Li
- Long Zhang
- Sheng Chen
affiliations:
- Renmin University of China
- Meituan
arxiv_id: '2607.23779'
url: https://arxiv.org/abs/2607.23779
pdf_url: https://arxiv.org/pdf/2607.23779
published: '2026-07-26'
collected: '2026-07-28'
category: RecSys
direction: Agent原生跨平台推荐 · 用户状态建模
tags:
- Claw-native recommendation
- cross-platform
- user state modeling
- task-aware
- marginal curation
- personal agent
one_liner: 提出Claw原生推荐范式，用证据关联的用户状态和边际策展实现跨平台互补推荐。
practical_value: '- **跨平台用户状态建模方法**：将不同端的行为标准化为统一事件，并维护证据关联的、带有时效状态（活跃/冷却/过期/抑制）的用户状态槽。可直接用于电商跨端（APP、小程序、网页）用户行为统一建模，避免将临时行为误判为长期偏好。

  - **基于功能角色的检索规划**：不依赖最近查询，而是从当前任务推断所需的信息支持类型（解释、指导、比较、官方验证等），再选择能提供对应功能的来源进行检索。这可以迁移到推荐feeds的版位规划，按任务需求分配不同功能的内容，提升整体的任务完成率。

  - **边际效用策展优化推荐列表**：选品时以增量价值为依据，覆盖未被服务的支持类型或互补功能，而非简单按相关性排序。可避免电商推荐中同类商品的重复展示，增强推荐列表的互补性和整体有用性。

  - **利用行为轨迹模拟评估跨平台推荐**：通过生活事件模拟和GUI代理生成跨平台行为序列，构造任务级推荐基准。可借鉴其方法构建更贴近用户真实跨端旅程的离线评估数据集。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
用户的一个任务往往跨越多个平台（搜索、内容浏览、比较、反馈），但推荐系统仍被限制在单个平台内，只能看到碎片化行为、只能推荐自家内容。近期出现的Claw式个人智能体可访问用户授权的跨平台上下文，使得推荐可以围绕用户当前任务组织，而不是局限于某个平台。ClawRec是第一个为这种环境设计的推荐系统，它需要解决三个挑战：跨平台行为时空混杂、来源功能角色差异大、推荐列表容易重复不互补。

**方法**  
ClawRec以**证据关联的用户状态**为核心，将异构行为转化为标准化事件，并通过用户状态推理维护任务槽、偏好槽和来源角色记录，每个记录都带有时间状态（活跃、冷却、过期、抑制）和证据引用。然后进行**角色感知规划**：由当前任务确定所需支持类型（如解释、指导、官方验证），再选择能提供对应功能的来源进行检索。最后通过**边际策展**，按候选内容对已选列表的增量价值进行贪心选择，确保推荐列表互补且覆盖多种支持功能，避免冗余。全流程保持来源链接，支持点击/跳过反馈来更新状态。

**关键结果**  
在基于生活事件和GUI代理生成的ClawRec-SimBench基准上，ClawRec的NDCG@20达到0.6134，比最强基线OpenClaw w/o ClawRec提高0.1126；Hit@20达到0.6944，提高0.0854。用户状态推断方面，当前任务识别得分4.57，时间对齐4.29，均显著优于其他有状态的方法。消融实验证实了统一事件构建、时间状态管理、来源扩展和边际策展各自的有效性。
