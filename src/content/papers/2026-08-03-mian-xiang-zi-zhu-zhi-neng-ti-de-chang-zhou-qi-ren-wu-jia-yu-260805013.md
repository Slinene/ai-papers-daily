---
title: 'OneDayAgent: Towards a Long-Horizon Harness for Autonomous Agents'
title_zh: 面向自主智能体的长周期任务驾驭框架 OneDayAgent
authors:
- Jingsheng Zheng
- Xinyuan Fang
- Jintian Zhang
- Zhengke Gui
- Huajun Chen
- Ningyu Zhang
affiliations:
- Zhejiang University
- Ant Group
- Independent Researcher
arxiv_id: '2608.05013'
url: https://arxiv.org/abs/2608.05013
pdf_url: https://arxiv.org/pdf/2608.05013
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: 长周期 Agent 执行框架
tags:
- long-horizon agent
- task decomposition
- execution memory
- verification
- LLM-agnostic
- AgentIF
one_liner: 统一分解、记忆与验证的长周期 Agent 框架，跨多后端 LLM 泛化并达 SOTA 0.821
practical_value: '- **长周期任务自动化**：借鉴子任务分解策略，将电商中复杂的营销活动策划、竞品报告生成等拆解为收集、整理、编辑、交付等有界步骤，避免单一推理超出上下文窗口。

  - **跨工具与多模态记忆**：参考其执行记忆的上下文压缩方案，在推荐场景中维护用户历史状态时，可对不同工具调用产生的长轨迹进行摘要式压缩，防止 KV cache
  溢出。

  - **最终交付验证**：引入验证-修复环，可用于 Agent 生成推荐理由、自动推送文案后的质量把关，降低幻觉与不一致。

  - **模型无关的框架设计**：该 harness 跨 5 个 LLM 无需调整，表明对业务后端快速替换或升级友好，可减少对不同模型精调的工作量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 智能体越来越多处理日常长周期、跨环境、多模态任务（如收集网页证据、编辑文件、生成报告），但单个请求常因目标漂移、状态丢失、上下文溢出而失败，现有工作往往孤立解决某一问题。

**方法**：OneDayAgent 将开放式请求转化为受管理的执行过程，包含三个关键机制：
- **任务分解**：将长任务切分为有界子任务，确保每个步骤不超出上下文窗口。
- **执行记忆**：在上下文压力下通过压缩与摘要维护关键状态，防止信息丢失。
- **验证修复**：对最终交付物自动检查，不合理时触发修复，保证输出质量。

**结果**：在 AgentIF-OneDay 基准的 104 个任务上，以 GLM-5.2 为后端取得 **0.821 总分**，新 SOTA。同一框架未经调优在 5 个不同后端 LLM（跨 3 个模型家族）上均有效，展示了良好的泛化性，但不同模型会产生不同的执行风格。
