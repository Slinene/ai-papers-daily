---
title: 'From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous
  AI'
title_zh: 从聊天机器人到数字同事：持久自主AI的范式转移
authors:
- Yongheng Zhang
- Ziang Liu
- Jiaxuan Zhu
- Shuai Wang
- Xiangqi Chen
- Haojing Huang
- Jiayi Kuang
- Siyu Chen
- Ao Shen
- Hao Wu
affiliations:
- Tencent Youtu Lab
- Tsinghua University
- Sun Yat-sen University
- Central South University
- University of Illinois at Chicago
arxiv_id: '2606.14502'
url: https://arxiv.org/abs/2606.14502
pdf_url: https://arxiv.org/pdf/2606.14502
published: '2026-06-11'
collected: '2026-06-15'
category: Agent
direction: Agent 演进：从对话到可持久自主工作
tags:
- Survey
- Autonomous Agent
- Workspace
- Skill
- LLM Reasoning
- Task Closure
one_liner: 提出“Workspace+Skill”机制，推动LLM从单次对话转向有状态、可复用的任务执行
practical_value: '- **构建有状态的 Agent 工作区**：参考 OpenClaw 的 Workspace 概念，为电商 Agent（如自动比价、库存管理）维护持久化的文件系统、终端、浏览器状态，避免每次调用都重新获取上下文。

  - **用“技能（Skill）”封装可复用推理链**：将常见业务流程（如订单处理、退款审核）建模为可参数化的 Skill，包含规划、工具序列、中间校验与错误恢复，提升任务闭环率。

  - **评估范式从答案质量转向任务状态验证**：对于推荐或运营 Agent，不应仅看最终回答的准确性，而应检查任务是否真正改变了系统状态（如是否完成了一次广告投放调整），用“任务闭环率”作为核心指标。

  - **数据构造从指令-响应对转向状态-动作-观测轨迹**：训练电商 Agent 时，记录完整的交互轨迹（用户意图 → 动作 → 环境反馈），以轨迹级 reward
  进行强化学习，比单轮 SFT 更能培养长期规划能力。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM 正从单纯的对话生成器转向能推理、行动、记忆和自我改进的集成 AI 系统。传统 Chatbot 仅以“快速反应”模式压缩知识、生成流畅回答，但在复杂推理、长链执行、自我验证上捉襟见肘。论文提出从“聊天机器人”到“数字同事”的范式转移，核心问题是：**如何让 AI 系统将用户意图可靠地转化为完成任务**，而非仅仅生成一个好答案。

### 方法关键点
- **两维度四阶段演进框架**：认知核心维度（Chatbot → Thinking LLM），工具增强执行维度（Agent → OpenClaw），并用“Workspace + Skill”机制打通两者。
- **Workspace**：给 LLM 一个持久化的数字工作区（文件、终端、浏览器、数据库等），使任务执行有状态、可审计、可恢复，告别临时性的工具调用。
- **Skill**：将可复用的任务过程封装为参数化的“技能”，包含规划、工具排序、中间验证和纠错，从临时 prompt 升级为可组合的能力包。
- **思维 LLM 的训练范式**：通过强化学习（RLVR/GRPO）让模型内化长链推理、多路径探索与自我纠正，无需外部框架，实现推理时的“慢思考”。
- **数据与评估的对应转移**：从知识语料 → 指令-响应对 → CoT 过程奖励 → 状态-动作-观测轨迹；评估从答案正确性 → 过程验证 → 任务闭环率与工作区状态核验。

### 关键观察
- 前沿 AI Agent 可完成的中位编码任务时长从 2019 年的几秒增长到 2026 年的超过 12 小时，显示系统在长时间自主任务上的重大突破。
- DeepSeek-R1 等模型通过纯 RL 训练自发出现“Aha moment”式的自省行为，但该现象是否真实涌现仍有争议。
- 推理能力并非完全从零训练，蒸馏少量高质量 CoT 数据（如 LIMO 仅用 817 条样例）即可激活预训练模型中的潜在推理能力。

> **最值得记住的一句话**：从 Chatbot 到 Digital Colleague 的关键一跃不是更强的语言生成，而是通过 Workspace 提供状态，Skill 提供可复用操作，让 LLM 真正完成可验证的工作。
