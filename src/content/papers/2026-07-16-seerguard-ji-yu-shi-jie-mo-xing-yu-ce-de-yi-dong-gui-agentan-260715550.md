---
title: 'SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction'
title_zh: SeerGuard：基于世界模型预测的移动GUI Agent安全框架
authors:
- Xue Yu
- Bo Yuan
- Pengshuai Yang
- Kailin Zhao
- Hong Hu
- Junlan Feng
affiliations:
- JIUTIAN Research
arxiv_id: '2607.15550'
url: https://arxiv.org/abs/2607.15550
pdf_url: https://arxiv.org/pdf/2607.15550
published: '2026-07-16'
collected: '2026-07-23'
category: Agent
direction: Agent安全框架 · 世界模型预测
tags:
- Mobile GUI Agent
- Safety
- World Model
- Next-State Prediction
- Risk Assessment
- Multi-task Learning
one_liner: 通过预执行指令筛查与动作风险评估，结合多任务世界模型，显著提升GUI Agent的安全效用并降低风险成本
practical_value: '- 在 Agent 流程中集成预执行动作风险评估模块，利用世界模型预测后续状态和风险，可拦截支付、删除等高风险操作，避免不可逆后果。

  - 借鉴多任务学习构建安全增强世界模型（SAWM），同时优化语义下一状态预测与安全评分，提升风险评估的准确性和泛化性，可迁移至电商购物 Agent 的安全审核。

  - 指令级高风险任务筛查作为第一道防线，快速拒绝“转账”“清空购物车”等敏感指令，降低系统整体风险暴露。

  - 引入安全-效用得分（SUS）和风险成本得分（RCS），为 Agent 安全与性能的平衡提供可量化的评估指标，适用于推荐或对话 Agent 的安全测试。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：移动 GUI Agent 单步误操作可能造成不可逆后果（如隐私泄露、财产损失），现有安全机制多为事后拦截，缺乏执行前风险预判。
**方法**：提出 SeerGuard 框架，包含两层防护：① 指令级筛查，快速过滤高风险任务；② 动作级风险评估，通过统一的安全增强世界模型（SAWM）预测动作后的下一状态及安全风险。SAWM 采用多任务学习，同时训练语义下一状态预测与安全风险评分，实现执行前的事前风险评估。
**结果**：在 MobileSafetyBench 上，Qwen3-VL-8B-Instruct 集成 SeerGuard 后，安全-效用得分从 0.191 升至 0.596（ω=0.8），风险成本得分从 0.347 降至 0.130（α=0.8），并成功泛化至 GPT-5.1、Gemini 等多种 Agent，消融实验验证了各模块的有效性。
