---
title: 'SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue'
title_zh: SpeakerMem-R1：面向多方对话的以说话人为中心双轨记忆
authors:
- Haobo Zheng
- Tan Tang
- Yan Chen
- Weijie Wang
- Yingcai Wu
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
arxiv_id: '2609.26780'
url: https://arxiv.org/abs/2609.26780
pdf_url: https://arxiv.org/pdf/2609.26780
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: 多方对话长期记忆 · 双轨记忆与RL训练
tags:
- Multi-party dialogue
- Long-term memory
- Dual-track memory
- Speaker attribution
- GRPO
- Reinforcement learning
one_liner: 双轨记忆+RL训练Writer-R1，解决多方对话长期记忆的消息归属与关系理解瓶颈
practical_value: '- **双轨记忆可迁移到电商多方会话场景**：售后群聊、直播互动、多人协作等场景中，用户与客服/主播/其他买家发言交错，现有记忆系统易丢失人物关系和观点归属；借鉴
  SpeakerMem-R1 的 verbatim track + structured track，将原始消息与提取出的 person-level/group-level
  状态分开存储，查询时按 entity/event/time 融合，能显著提升关系类问题的回答质量。

  - **用小模型做结构化记忆写入更贴合生产环境**：论文训练 Writer-R1 负责从对话中抽取说话人归属和状态更新，而非直接调用超大模型做长时间维度的记忆管理；电商客服/Agent
  团队可以对自有会话数据做 SFT+GRPO，训练一个轻量记忆写入器，降低 API 成本和延迟，同时满足数据隐私要求。

  - **speaker-conditioned GRPO 可用于归属纠错**：将说话人信息作为奖励条件，结合 SpeakerLevenshtein 惩罚归属错误，比单纯
  SFT 更能提升消息归属准确率（控制实验中 57.38%→68.20%）；在训练自己的对话总结或状态抽取模型时，可借鉴这种领域可验证的 RL 奖励设计。

  - **person-level 与 group-level views 互补**：对电商推荐中的用户画像建模有启示——同时维护个体兴趣状态和群体共享状态，避免只关注个人历史而丢失群组上下文（如家庭采购群、企业采购团队）。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多方对话的长期记忆不只是检索相关过去内容，还要区分谁说了什么、每句话针对谁、个体之间如何相互看待、群体共享哪些信息、状态如何随时间变化。现有通用 LLM 记忆系统常丢失人物与群体关系，或难以整合分散在多个成员、群体和时间线中的线索，暴露出消息归属与关系理解、交错历史状态重建两大瓶颈。

**方法关键点**：SpeakerMem-R1 采用双轨记忆：一条轨道存储带说话人标记的原话，另一条存储派生出的结构化状态，并组织为 person-level 和 group-level 两类视图；查询时按实体、事件、时间融合两条轨道的证据。为降低结构化记忆构建中的归属与更新错误，同时支持本地部署，训练了 Writer-R1，使用 SpeakerLevenshtein 和 speaker-conditioned GRPO 进行强化学习优化。

**关键结果**：在 GroupMemBench、SocialMemBench、EverMemBench 上 binary accuracy 分别达到 47.9%、69.2%、61.9%，相比主流框架最好结果分别高 3.3、12.4、9.4 个百分点；在 EverMemBench 公开榜单上取得 62.33%，为当前最佳。在 LoCoMo 全部 1,986 题上达到 70.85%。控制评估中，RL 将 SFT Writer 的平均准确率从 57.38% 提升到 68.20%。消融实验表明 verbatim 与 structured 轨道、person-level 与 group-level views 在标准化评估接口下互为补充。
