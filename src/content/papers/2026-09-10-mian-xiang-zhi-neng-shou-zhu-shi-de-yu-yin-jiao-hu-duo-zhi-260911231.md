---
title: 'A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture
  Design and Key Technologies'
title_zh: 面向智能手术室的语音交互多智能体系统：架构设计与关键技术
authors:
- Tianxiang Zhou
affiliations:
- Wuhan United Imaging Surgical Co., Ltd. (UIS)
arxiv_id: '2609.11231'
url: https://arxiv.org/abs/2609.11231
pdf_url: https://arxiv.org/pdf/2609.11231
published: '2026-09-10'
collected: '2026-09-12'
category: MultiAgent
direction: 多智能体语音交互 · KV Cache 优化
tags:
- LLM
- Multi-Agent
- Voice Interaction
- KV Cache
- Task Planning
- Low Latency
one_liner: 用 LLM 多智能体实现手术室语音控制与报告生成，重点优化 KV Cache 前缀复用、流式解析并行执行与渐进式提示披露
practical_value: '- **KV Cache prefix warming 可直接用于 Agent 长 system prompt 或设备状态频繁变化场景**：将稳定的前缀（角色定义、技能列表、历史上下文）缓存，每次请求只重算变化部分。对电商导购
  Agent，用户切换商品详情或筛选条件时，不必重算整个对话前缀，可把首字延迟从几百毫秒降到几十毫秒。

  - **流式 partial JSON 解析 + 提前并行执行是降低端到端时延的有效工程 trick**：LLM 以流式输出任务数组时，不用等完整 JSON 结束，解析到单个完整任务对象就立即调度执行。对广告文案批量生成、多商品并行推荐解释、多工具调用编排，能带来约
  30% 的时延下降。

  - **渐进式技能提示披露适合工具多的 Agent 系统**：按用户角色、可用设备/工具、当前阶段动态裁剪 system prompt，只保留当前上下文最相关的技能说明。电商场景可复用为：按用户等级、可用的推荐/营销工具、会话阶段动态注入工具
  schema，避免上下文浪费，提升长会话下的指令跟随稳定性。

  - 多智能体架构与设备管理层解耦，可参考其 skill registry、task planner、device manager 的分层设计，在推荐系统中把“用户意图理解”“策略编排”“召回/排序执行”拆成独立模块，便于管控和低延迟并行执行。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：传统手术室设备控制依赖物理按钮、触摸屏或脚踏开关，存在交叉污染与无菌中断风险。希望利用 LLM 实现语音交互，完成设备控制、术中记录和手术报告生成，并满足手术室实时性要求。

**方法关键点**：系统采用分层架构：语音流水线（唤醒→ASR→轮次检测→Agent 推理→TTS）与 Agent 核心（技能注册表、技能路由、任务规划器、任务调度器、设备管理器）。基于 Qwen3-27B 与 llama.cpp/sglang 实现。三项关键技术：1）KV Cache 前缀预热：利用字节级最长公共前缀复用，避免设备状态变化导致的前缀重复计算，将额外重算开销从约 500ms 降至数十毫秒；2）流式部分 JSON 解析：在 LLM 流式输出过程中检测完整任务数组并立即启动并行执行，端到端延迟降低约 30%；3）渐进式技能提示披露：根据用户角色、已连接设备与手术阶段动态过滤系统提示，在有限上下文窗口内最大化信息密度。

**关键结果**：系统在 16,384 token 上下文限制内有效运行，前缀预热命中率达到预期，多设备并行控制响应时间满足手术室实时要求。
