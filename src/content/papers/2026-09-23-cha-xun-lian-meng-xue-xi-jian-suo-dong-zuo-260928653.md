---
title: 'The Fellowship of the Query: Learning Retrieval Actions'
title_zh: 查询联盟：学习检索动作
authors:
- Mohammed Al-Maamari
- Saber Zerhoudi
- Michael Granitzer
- Jelena Mitrović
affiliations:
- University of Passau
arxiv_id: '2609.28653'
url: https://arxiv.org/abs/2609.28653
pdf_url: https://arxiv.org/pdf/2609.28653
published: '2026-09-23'
collected: '2026-09-27'
category: RAG
direction: RAG 检索动作控制 · LoRA 轨迹微调
tags:
- RAG
- trajectory fine-tuning
- LoRA
- SLM
- action prediction
- search control
one_liner: 用 teacher search traces 将 RAG 检索决策建模为 7 路动作预测，LoRA 微调小模型作为控制器，动作 F1 0.6536、端到端
  EM 0.7946
practical_value: '- 把 RAG/Agent 中隐式检索决策显式化为结构化动作空间（decompose/search/reformulate/extract/verify/stop），用
  teacher trace 构造分类数据，LoRA 蒸馏到 3B 小模型；电商客服、搜索 Agent 需要低延迟可控检索时，可用 action head 替代自由生成，提高稳定性和可观测性。

  - LoRA 监督微调小模型从 trajectory state 预测 next action，比 zero-shot prompting 高约 3.7 倍，可作为轻量路由器放在检索前，减少大模型调用；线上先判定动作类型再分发给对应工具，类似
  query 改写/意图路由。

  - TF-IDF + logistic regression 基线达到 0.5399，说明动作控制任务中词法特征很强；业务数据量小或冷启动阶段，先上线性模型做
  sanity check，再逐步上 SLM。

  - 单一小模型同时承担 controller 和 generator，端到端效果提升且减少服务编排复杂度；对资源受限、链路长的实时搜索/推荐 Agent，可考虑合并角色降低链式延迟。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：RAG/QA 需要多步检索决策（分解、搜索、改写、抽取、综合、验证、停止），大模型控制成本高、延迟大，探讨轨迹微调能否提升小模型作为 next-action controller。

方法：从 teacher search traces 构建七路动作预测任务，输入当前 trajectory state，预测下一步结构化动作；用 LoRA 监督微调多种 SLM/xSLM；另评估低资源场景下单 SLM 同时充当 controller 和 final-answer generator。

关键结果：1,646 条 held-out actions 上，Granite 4.1 3B 用 13,194 条动作训练后 macro-F1 0.6536，远高于同模型 zero-shot prompt 0.1736，也高于 TF-IDF logistic regression 0.5399。149 条 held-out trajectories 端到端评估中，微调模型双角色相比 base 双角色，Exact Match 从 0.7530 提升至 0.7946，token F1 从 0.7783 提升至 0.8295；固定 generator 时微调 controller 增加 evidence-fact recording，但 controller-only 最终答案增益不显著。整体看轨迹监督提升动作预测和证据记录行为。
