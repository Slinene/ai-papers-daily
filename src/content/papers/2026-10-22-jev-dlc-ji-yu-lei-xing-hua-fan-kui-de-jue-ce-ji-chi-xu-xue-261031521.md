---
title: 'Jev-DLC: Decision-Level Continual Learning from Typed Feedback'
title_zh: Jev-DLC：基于类型化反馈的决策级持续学习
authors:
- Yangyang Feng
- Jianle Gan
- Zhuoyan Feng
- Chengwei Qin
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Sun Yat-sen University
arxiv_id: '2610.31521'
url: https://arxiv.org/abs/2610.31521
pdf_url: https://arxiv.org/pdf/2610.31521
published: '2026-10-22'
collected: '2026-10-25'
category: RecSys
direction: 持续个性化 · 类型化反馈有界状态
tags:
- Continual Learning
- Typed Feedback
- Personalization
- Decision Making
- Bounded State
one_liner: 用接受/撤销类型化反馈构建有界状态，在冻结评分器上实现低开销持续个性化决策
practical_value: '- 将用户 accept/revoke 操作抽象成“选中动作 + 被替换动作”的成对反馈，用有向关系存储，适合电商推荐“换一换”、广告主拒单/改投等场景，直接用于在线修正排序偏好。

  - 方法不存原始行为日志、不加一次 scorer 推理、不做在线反向传播，仅维护有界状态（可限制大小），对高 QPS 推荐/广告系统友好；可把该模块作为轻量级个性化插件放在已有精排模型之上。

  - 互补双通道设计（动作身份证据 + 偏好关系）比单一历史重放更抗噪声，且在反馈稀疏时仍能稳定提升；可借鉴到用户级表示更新或 pairwise ranking
  中，比单纯累积正例更有效。

  - TCPA-Bench 的时序评估方式强调“只有影响后续决策才计分”，适合用来验证持续学习/在线学习系统，避免传统离线评估高估模型效果。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：个体偏好往往在部署后才显性化——用户接受一个决策，或撤销并改为另一个。Jev 式类型化接口让这种反馈显式包含“选中动作”及“被替换动作”。现有方法多依赖重放历史或在线更新模型，带来额外存储/计算开销，且难以把纠正因果地传递到后续决策。

**方法关键点**：Jev-DLC 把每次纠正同时看作两类信号：动作身份是否反复出现，以及“偏好动作 vs 拒绝动作”的有向关系。它在冻结的 scorer 之上使用两个有界通道分别保存这两类信号，组合两者分数影响下一次决策。整个过程不保留原始交互历史、不增加 scorer 调用、不做运行时语言模型反向传播，适合低延迟在线服务。

**关键结果**：在 TCPA-Bench 的 TCPA-Repeat 子集上，Jev-DLC 整体 user-macro accuracy 达 44.83%，比 Recent-4 history replay 高 2.43 个百分点；在至少两次先验反馈后，准确率提升至 56.07%，比最强对比高出 7.54 个百分点，验证了显式类型化纠正可压缩为轻量因果状态用于持续个性化。
