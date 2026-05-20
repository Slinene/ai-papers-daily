---
title: 'CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization'
title_zh: CEPO：基于对比证据策略优化的强化学习自蒸馏方法
authors:
- Ahmed Heakl
- Abdelrahman M. Shaker
- Youssef Mohamed
- Rania Elbadry
- Omar Fetouh
- Fahad Shahbaz Khan
- Salman Khan
affiliations:
- MBZUAI
- Linköping University
- Australian National University
arxiv_id: '2605.19436'
url: https://arxiv.org/abs/2605.19436
pdf_url: https://arxiv.org/pdf/2605.19436
published: '2026-05-18'
collected: '2026-05-20'
category: Training
direction: 强化学习验证奖励 · 对比证据信用分配
tags:
- RLVR
- Self-Distillation
- Credit Assignment
- Contrastive Evidence
- GRPO
- Multimodal Reasoning
one_liner: 用正确与错误答案的对比信号锐化token级信用分配，保留安全保证并显著提升多模态数学推理
practical_value: '- 在Agent多步决策或生成式推荐推理链中，可借鉴CEPO对比正确与错误示例，自动识别并放大关键决策token的梯度，抑制填充词干扰，提升训练效率和推理质量。

  - 负参考直接从已采样的错误rollouts中提取答案，无需额外采样成本，适合在线RL训练，可直接迁移到电商对话Agent或推荐解释生成中的reward shaping。

  - CEPO的stop-gradient和方向锚定设计避免了因引入特权信息（如最终答案）而导致的信息泄漏和训练崩溃，为在线自蒸馏提供安全的模板，适用于任何依赖最终正确标签的序列级强化学习场景。

  - 超参数（λ线性衰减与ε_w裁剪）表现出强鲁棒性，且对比信号集中出现在关键推理步，可解释性强，有利于在业务中监控和调试信用分配质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
RLVR（如GRPO）对正确轨迹的每个token给予相同奖励，无法区分决定性推理步与语法填充词，导致信用分配粗糙、收敛慢。利用正确答案作为teacher进行自蒸馏能提供稠密信号，但现有方法或产生信息泄漏（OPSD、SDPO），或受限于单参考证据（RLSD），无法有效区分关键token（流利度混淆、单侧证据）。

## 方法关键点
- **对比证据delta**：将RLSD的单一证据比 $P^+_T/P_S$ 替换为对比比 $P^+_T/P^-_T$，其中 $P^-_T$ 以当前batch中得分最低的错误答案 $r^-$ 为条件，消除流利度混淆。
- **差分信念更新**：该比值等于token同时提升对 $r^+$ 信度、降低对 $r^-$ 信度的量，自然锐化决定性token的信号。
- **安全集成**：权重只用于缩放GRPO优势幅度，符号仍由verifier决定；stop-gradient确保无词汇表级梯度泄漏，理论上降级包含RLSD。
- **精准条件**：仅当 $P^-_T(y_t) < P_S(y_t)$ 时CEPO才比RLSD给正确token更激进信用，证明其锐化仅限于正确-错误教师意见相左的语义重要位置。

## 关键结果
- 在Geo3k上训练，5个多模态数学推理基准测试（DynaMath, LogicVista, MathVision, MMMU, WeMath）上，2B模型平均准确率43.43%（GRPO 41.17%），4B模型60.56%（GRPO 57.43%）。
- OPSD/SDPO因信息泄漏跌到基线以下，证实结构性安全的必要性。
- Token级热力图显示CEPO将信用集中在代数推导与答案token，而对填充词权重近1，动态范围更大。
- 仅比GRPO增加约10%训练时间，无需额外采样。
