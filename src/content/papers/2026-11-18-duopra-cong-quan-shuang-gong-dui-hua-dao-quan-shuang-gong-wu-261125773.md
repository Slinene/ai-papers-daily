---
title: 'Duopra: From Full-Duplex Conversation to Full-Duplex Agency'
title_zh: Duopra：从全双工对话到全双工任务代理
authors:
- Chiyu Chen
- Pengzhou Cheng
- Yuezhao Ma
- Xiaocheng Li
- Can Liu
- Haonan Hu
- Yao Yao
- Yifei Yang
- Yijie Lu
- Taolei Wang
affiliations:
- Shanghai Jiao Tong University
- Tencent
- Shanghai University
- University of Bristol
arxiv_id: '2611.25773'
url: https://arxiv.org/abs/2611.25773
pdf_url: https://arxiv.org/pdf/2611.25773
published: '2026-11-18'
collected: '2026-11-23'
category: Agent
direction: 全双工对话智能体 · 工具调用
tags:
- full-duplex
- tool use
- RL
- SFT
- agent
one_liner: 全双工模型 Duopra 统一前后端工具调用接口，三阶段训练将 Pass@1 从 4.7% 提升到 44.7%
practical_value: '- 在电商实时客服/语音导购等全双工场景，前后端分离代理容易出现“前端没发请求”或“请求不完整”导致任务失败。可借鉴 Duopra
  将后端封装为工具，要求请求自包含且与直接调用共享同一接口，降低前端决策到后端执行的信息损耗。

  - 三阶段训练可迁移到 LLM Agent 工具调用优化：先用 protocol SFT 冷启动请求格式，再用 RL 以“及时、完整执行”为奖励做在线调优；最后用
  projector-only 修复保持已有对话能力，避免更新 thinker 后 talker 退化，适合大模型迭代时的低成本持续训练。

  - 评估拆解值得借鉴：统计工具执行前的失败占比，区分“没发起”与“执行错”，针对性优化前端发起策略或后端解析能力；业务上可复用 Pass@1 和 takeover
  rate 作为对话 Agent 任务完成的核心指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：全双工交互模型已具备会话主动性（低延迟轮流说话、插话、反馈），但完成任务还需任务主动性：及时调用工具并根据用户纠正修改参数。常见前后端分离 Agent 中，前端只决定是否及请求什么，后端决定如何执行，导致未发送请求无法执行、不完整请求误导后端。在 FDB v3 上，多数失败发生在领域工具执行之前。

**方法关键点**：Duopra 将后端视为工具，接受自包含自然语言请求，直接调用与后端委托共享同一 action interface。三阶段训练：1) protocol SFT 学习请求协议；2) full-duplex RL 奖励及时且完整的工具执行；3) projector-only 修复，在更新 thinker 后维持 talker 条件，保护会话能力。

**关键结果**：使用相同后端，Pass@1 从 4.7% 提升至 44.7%；Duopra 直接调用工具达 47.7%（仅 SFT 后为 26.0%），接入 DeepSeek 后端达 49.3%；在 FDB v1.0 上三个接管率均优于基础模型，说明任务代理与会话能力可以共存。
