---
title: 'From Interaction to Capability: Task Advancement as State and Supervision
  for GUI Agents'
title_zh: 从交互到能力：以任务推进为状态与监督的 GUI 智能体记忆
authors:
- Ziyang Chen
- Qian Li
- Chengwei Qin
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Shandong University
arxiv_id: '2610.37482'
url: https://arxiv.org/abs/2610.37482
pdf_url: https://arxiv.org/pdf/2610.37482
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: Agent 任务状态与经验记忆
tags:
- GUI Agents
- Memory
- Task State
- Experience Reuse
- Long-Horizon
- LLM Agents
one_liner: 将已验证任务进展作为在线状态与离线监督，从跨应用长程任务中学习可复用操作
practical_value: '- 在电商导购/任务型 Agent 中，把用户已确认的约束（预算、尺码、偏好、收货地址）作为 verified task progress
  绑定到剩余决策节点，后续只推进依赖已满足的目标，避免跨商品页/订单页重复询问。

  - 从成功与失败的会话中抽取「局部有效操作」作为可复用算子：定义入口输入、期望结果、验证条件，例如「给定尺码+偏好筛选候选商品」或「根据地址+支付方式完成下单」，即使整单未成交也能沉淀有效环节供后续会话复用。

  - 区分 draft/attempt/confirmed：在推荐流程中只把「加入购物车」「提交订单」等强确认信号作为状态更新依据，不把生成过程或中间点击误判为已完成结果，减少错误状态对后续决策的污染。

  - 借鉴 Evidence Cache 和按依赖召回：为多轮推荐对话缓存商品详情图、用户历史 SKU 属性等结构化证据，按剩余需求的 input dependencies
  按需读取，降低上下文 token 并提高信息可用性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
长程 GUI 智能体需要跨应用传递已获得信息，并积累可复用操作。但动作日志难以判断哪些进展已被确认，最终成功/失败信号无法定位局部有效操作：失败任务可能包含可复用成功，成功任务也可能包含无效尝试。现有经验记忆多绑定完整轨迹，接口变化后难以适应；仅用最终结果监督会丢失中间局部成功。

## 方法关键点
- 将 **task advancement** 定义为 GUI 观测确认某个需求从 UNRESOLVED 变为 ESTABLISHED，例如读取到会议时间或创建了日历事件。
- 任务开始时用 LLM 编译器把指令编译为需求图 Q=(V, EQ)，每个需求带依赖 Rq 与验证条件 Vq。
- **Task Advancement State**：在线维护每个需求的状态、绑定值与支持证据；当某需求被验证满足，则从剩余任务中移除，其值仍保留供后续需求使用，实现 task reduction。
- **Advancement Frontier** 识别依赖已满足、分支条件成立的可推进需求，据此检索相关证据与算子。
- **Evidence Cache** 保存源截图或裁剪，跨界面时恢复已获取信息，不以纯文本丢失视觉证据。
- **Advancement supervision**：任务结束后回顾候选交互段，只保留产生已验证局部结果的步骤，抽象出 Advancement Operator ⟨Rκ, Δκ, Vκ, Bκ, Γκ, Aκ⟩，记录入口需求、期望结果、验证条件、对象角色、可适用条件与 GUI 路线。即使整体任务失败，局部成功也能被保留；成功任务中的无效尝试不进入算子。
- 算子语义与 GUI 实现分离：检索时先按任务语义匹配，再检查当前界面是否兼容已有路线；界面变化时算子仍可提供目标与验证方式。

## 关键实验
- **MobileWorld GUI-only 117 任务**，Qwen3-VL-32B-Instruct，与 AWM、Mobile-Agent-E、StructAgent、GUI-explorer、MemGUI-Agent 比较：TAM 成功率 34.2%，比最强基线 29.1% 提升 5.1 pp，比无记忆底座 12.0% 提升 22.2 pp；EQA@50 29.2% 最高；每解决任务生命周期 token 0.771M，比 ConAct 1.257M 低 38.7%。
- 多应用任务上优势更大：3-app 组相对 ConAct 提升 14.3 pp，支持跨应用信息保留的价值。
- **SPA-Bench English Level 3** 单应用，GPT-4o：TAM 成功 57.0%，超过 GUI-explorer 的 53.7%，为当前报告最高。
- 消融：仅 Task Advancement State 已达 28.2%，加上 Operator Graph 到 32.5%，完整 TAM 34.2%；State 贡献最大，算子提供额外经验复用。
- 机制分析：review 将保留操作段中位从 20.0% 压缩到 7.7% 的源轨迹，证明学习集中在局部有效操作；相比 flat state，TAM 的状态可用性 77.8% vs 55.6%，目标正确使用 77.8% vs 66.7%。

## 最值得记住的一句话
把记忆组织为「已验证任务进展 + 可复用算子」，让已完成结果显式供给剩余需求，并从局部成功中学习，是长程 Agent 提升完成率、降低成本的关键。
