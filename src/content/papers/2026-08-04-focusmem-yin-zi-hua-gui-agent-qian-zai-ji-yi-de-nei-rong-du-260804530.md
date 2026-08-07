---
title: 'FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory'
title_zh: FocusMem：因子化 GUI Agent 潜在记忆的内容、读出与信任
authors:
- Zhuoran Zhang
- Bowen Li
- Jingcheng Ju
- Yang Shi
- Qixun Wang
- Haotian Wang
- Wei Chen
- Tengjiao Wang
affiliations:
- School of Computer Science, Peking University
- Key Lab of High Confidence Software Technologies, Peking University
- Institute of Information Engineering, Chinese Academy of Sciences
- Department of Computer Science and Technology, Tsinghua University
arxiv_id: '2608.04530'
url: https://arxiv.org/abs/2608.04530
pdf_url: https://arxiv.org/pdf/2608.04530
published: '2026-08-04'
collected: '2026-08-07'
category: Agent
direction: Agent记忆因子化与选择性读出
tags:
- GUI Agent
- Latent Memory
- Episodic Memory
- Working Memory
- Trust Gate
- State-Conditioned Readout
one_liner: 在潜在记忆中因子化内容保留、状态条件读出和信任门控，解决 GUI Agent 记忆压缩损失与无关干扰问题
practical_value: '- 构建对话式推荐 Agent 或任务助手时，可将情景记忆（用户长期偏好）与工作记忆（当前会话状态）分开存储并利用角色感知读出，提升多轮交互一致性。

  - 状态条件读出机制可迁移至用户序列建模，根据当前推荐场景动态聚焦历史行为，增强推荐上下文的个性化与相关性。

  - 信任门作为轻量过滤器，可集成到 RAG 管道中，抑制检索到的无关商品描述或历史交互，减少噪声，提高推理准确性。

  - 记忆模块独立训练、策略模型冻结的架构，是一种低风险、易迭代的工程方案，适合业务中快速实验与部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GUI Agent 需同时记住已完成任务的可重用经验（情景记忆）和当前交互进度（工作记忆），现有潜在记忆方法将多模态轨迹压缩为固定块，仅靠下一步动作监督，造成细节丢失、同一块服务多个决策阶段、无关记忆干扰等问题。

**方法**：FocusMem 在紧凑潜在记忆接口内进行三项因子化：(1) **角色感知内容基**分别鼓励情景记忆保留可复用经验，工作记忆保留任务进度；(2) **状态条件读出**根据当前决策状态生成对同一存储证据的决策特定视图；(3) **轻量信任门**抑制当前步骤无关的记忆块。所有组件均在冻结 GUI 策略下训练，保持原有模型不变。

**结果**：在五个 GUI agent 基准上，FocusMem 一致优于仅动作固定记忆基线及先前潜在记忆方法。消融表明：语义与功能监督互补；状态条件读出随轨迹上下文增长更稳健；信任门显著减轻无关情景证据注入的伤害。结论强调有效潜在记忆不仅依赖压缩，更取决于保留什么、暴露什么、允许什么。
