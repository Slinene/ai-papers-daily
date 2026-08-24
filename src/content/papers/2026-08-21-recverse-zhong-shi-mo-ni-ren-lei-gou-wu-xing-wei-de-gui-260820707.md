---
title: Towards Faithful Simulation of Human Shopping Behavior
title_zh: RecVerse：忠实模拟人类购物行为的 GUI Agent
authors:
- Jiakai Tang
- Yan Mi
- Jing Yu
- Yang Zhang
- See-Kiong Ng
- Qi Cao
- Fei Sun
- Xu Chen
- Wen Chen
- Jian Wu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- University of Chinese Academy of Sciences
- National University of Singapore
- Alibaba Group
arxiv_id: '2608.20707'
url: https://arxiv.org/abs/2608.20707
pdf_url: https://arxiv.org/pdf/2608.20707
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: 用户行为仿真 · GUI Agent · RL
tags:
- User Simulation
- GUI Agent
- Reinforcement Learning
- Hierarchical Memory
- E-commerce
- Benchmark
one_liner: 提出融合三级认知记忆与轨迹级 RL 的 GUI 用户仿真 Agent，显著提升行为保真与意图一致性
practical_value: '- 在 LLM 驱动的用户模拟 / 智能导购中，不要直接拼接长历史，可采用三级记忆：Working Memory 保留最近 K
  步视觉与心态、Episodic Memory 记录会话事件、Preference Memory 蒸馏高层购物意图；把记忆写入作为动作交给 RL 学习，能自动决定“何时记、记什么”，缓解长会话上下文爆炸。

  - 训练用户模拟器别只做 next-action 模仿或 step-level reward，改用 trajectory-level RL：宏观奖励对齐动作类型分布（CTR/ACR/CVR/IPVR
  等），微观奖励用三级类目层次做意图匹配，可避免过度探索或过度被动。

  - 如果业务有真实页面截图，尽量让仿真/评估 Agent 走 GUI grounding，而不是纯文本元数据；论文显示 GUI 比 text 的类别意图一致性
  HCO 从 19.03 提升到 30.00，RL 后进一步到 32.64。

  - 评估用户模拟器时同时报告行为保真和意图一致性，防止 hit 率被过度交互撑高；可借鉴其指标：ATL 偏差、行为统计与真实分布的比值、类目重叠 HCO。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商用户行为模拟是离线评估、反事实分析和 RL 训练推荐策略的基础。长会话浏览跨越数十页，现有模拟器或丢弃历史丢失长期依赖，或朴素拼接导致上下文爆炸、质量下降；且普遍采用 next-action 模仿或 step-level 奖励，无法对齐整条轨迹的行为分布与真实购物意图，生成会话常表现为过度探索或过度被动。

**方法关键点**
- **GUI-grounded 观察**：以页面截图为输入，与真实用户感知模态一致。
- **三级认知记忆**：Working Memory 保留最近 K 步视觉印象、心态与动作；Episodic Memory 维护会话内事件文本痕迹；Preference Memory 蒸馏高层用户偏好（如“偏好红色低价连衣裙”）。
- **记忆即动作**：将 Episodic/Preference Memory 的更新作为动作空间一部分，通过 RL 学习“何时写、写什么”，避免人工启发式。
- **轨迹级 RL**：IL 预热后，用 GRPO 优化；奖励 = 宏观行为分布对齐（动作类型计数差异）+ 微观意图对齐（三级商品类目层次匹配，按动作强度加权）+ 格式奖励。
- **USB 基准**：5,274 条真实截图轨迹、90,095 商品、3 级类目、8 种动作，支持交互式多轮 RL 训练与评估。

**关键结果**
与最强 GUI baseline STA 相比，RecVerse-GUI RL 的 Item-level F1 从 4.27 提升到 7.19，HR 从 5.92 到 10.45，HCO 从 23.11 到 32.64，且行为统计更接近真实用户分布。人工评测中 RecVerse vs STA 偏好率 92%，真实用户 vs RecVerse 偏好率 74%。消融显示：去掉 micro reward 最伤意图指标；去掉 Preference Memory 或只留 Working Memory 显著下降。

**最值得记住的一句话**
用户模拟不应只学习下一步动作，而应通过层次化记忆与轨迹级双重奖励，同时对齐用户行为分布和购物意图。
