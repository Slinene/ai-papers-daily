---
title: 'TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information'
title_zh: TeamGym：分布式信息下 AI 智能体团队决策的训练与评估环境
authors:
- Chanwoo Park
- Jaywoong Jeong
- Zachary Wojtowicz
- Yubin Kim
- Taekyun Lee
- Kaiqing Zhang
- Asuman Ozdaglar
affiliations:
- MIT
- KAIST
- UT Austin
- University of Maryland
arxiv_id: '2610.37571'
url: https://arxiv.org/abs/2610.37571
pdf_url: https://arxiv.org/pdf/2610.37571
published: '2026-10-27'
collected: '2026-10-29'
category: MultiAgent
direction: 多智能体分布式信息决策与协同训练
tags:
- multi-agent
- team decision-making
- communication gap
- retrieval gap
- RL training
- pivotal information
one_liner: 构建可控团队决策环境，量化并训练多智能体在分布式关键信息下的沟通与检索能力
practical_value: '- 在电商/客服/搜索多 Agent 编排中，先拆出任务的最小关键事实集合（类似 PIU），分别测量「沟通 gap」和「检索 gap」，定位问题是信息没检索出来还是没在
  Agent 间传好，而不是只看单智能体能力

  - 协调器/主 Agent 的 query 设计要宽而明确：论文显示窄 query 会让持有关键信息的 Agent 只回答部分证据；给每个专家 Agent 加
  public 的职责标签，并要求「报告所有相关证据类别」，可明显减少 gap

  - 消息 token 预算影响很大：从 32 提到 128 tokens 成功率 55.3%→78.6%，但再提不涨；在线上多做消息长度 trade-off，给关键
  Agent 设消息长度下限

  - 用最终决策 reward 做 GRPO 联合训练通信策略，即使不直接奖励协调行为，也能自动涌现轮询所有专家、短 query 等协议；可迁移到多 Agent
  推荐/问答工作流优化，但注意 held-out 域迁移可能只转移行为不转移最终质量'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
AI Agent 仍主要被单智能体训练和评测，但真实决策往往需要团队整合分散在不同参与者手中的信息。现有单智能体基准不考察团队检索与沟通能力，多智能体系统研究又多聚焦如何解决具体任务，缺少对信息分布、通信结构和训练效果的受控诊断。

## 方法关键点
- 提出 **TeamGym** 环境，从法律、金融、医学、软件工程真实语料（12 个源语料）构造团队决策问题实例。
- 从每个问题中识别 **PIU（Pivotal Information Unit）**：一组最小事实，每个都必要、联合充分，用于支撑正确答案。
- 通过控制 PIU 分布（如每个参与者一个 PIU、全部集中等）和通信结构（round robin、current-speaker selection、simultaneous responses、coordinator-selected speaker、broadcast query），分离两种损失：
  - **Communication gap**：把同一组 PIU 分散给多个参与者 vs 给单个模型，成功率的下降。
  - **Retrieval gap**：进一步要求参与者从原始材料中自己检索 PIU，而不是直接给出 PIU，带来的额外下降。
- 支持用 GRPO 对参与者/协调器策略做 RL 训练，奖励只基于最终决策质量。

## 关键结果数字
- 8 个 LLM、12 个源语料：把 PIU 分散到团队，成功率平均下降 **22.9 pp**（communication gap）；再要求从源材料检索 PIU，成功率又降 **19.9 pp**（retrieval gap）。
- 通信结构与 PIU 分布存在显著交互：在某些分布下，sequential 结构领先 simultaneous 3.9 pp，但在额外无 PIU 参与者时落后 9.8 pp。
- 消息 token 预算影响：GPT-5.5 在 CUAD/Multi-LexSum 上，消息预算从 32 提到 128 tokens，成功率由 55.3% 升至 78.6%，再提到 256 无进一步收益。
- 联合训练协调器与参与者策略：CUAD 验证 LLM-judged score 从 11.97% 提升到 22.38%，协调器查询每个参与者的比例从 80.6% 升到 100%，且平均 query 长度从 14.0 词降到 12.5 词。
- 训练共享参与者策略：FinDVer 验证分数 21.85→41.08，FinLongDocQA 测试 33.50→41.13；更多参与者发言、更多 distinct speakers，但 held-out 域上 PIU 覆盖没有显著提升。

## 最值得记住的一句话
团队决策质量不仅取决于单个模型能力，更取决于如何检索、沟通和整合分布式关键信息；通过受控信息分配与仅基于最终决策的 RL 训练，可以量化并改善多智能体的协作行为。
