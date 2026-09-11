---
title: 'T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks'
title_zh: T1：面向长程任务的终端Agent强化学习
authors:
- Junyao Yang
- Yucheng Shi
- Zhongzhi Li
- Ruhan Wang
- Zongxia Li
- Haitao Mi
- Leowei Liang
affiliations:
- Tencent Hy Foundation Model Frontier
- National University of Singapore
- University of Georgia
- Indiana University
- University of Maryland, College Park
arxiv_id: '2609.11042'
url: https://arxiv.org/abs/2609.11042
pdf_url: https://arxiv.org/pdf/2609.11042
published: '2026-09-09'
collected: '2026-09-11'
category: Agent
direction: 终端Agent强化学习与MoE稳定训练
tags:
- Agent RL
- MoE
- PPO
- Terminal-Bench
- Reward Design
- Long-Horizon
one_liner: 122B MoE终端Agent靠RL在Terminal-Bench 2.1达64%，用TITO+R3稳定训练与密集验证奖励
practical_value: '- **MoE 训练-推理一致性**：对大规模稀疏模型，记录推理时每个 token 的专家路由掩码并在训练时重放（R3），同时让训练直接消费采样时的
  token ID 而非重新渲染文本（TITO），可消除训练-推理 log-prob gap，避免梯度更新到错误的专家子网络。对推荐系统中带 MoE 的排序或召回模型同样适用。

  - **密集奖励设计**：用绝对通过断言数而非通过比例作为 RL 奖励，并固定全局尺度（S=20），保留不同难度任务/用户价值差异。在电商多目标 RL 中，可借鉴“绝对达成数”作为奖励，避免归一化掩盖长尾或高价值任务。

  - **Critic warm-up 与健康度监控**：先在有监督数据上预热 critic 一个 epoch，设置 critic 学习率为 actor 的 30x，并用
  explained variance（全局方差约减）持续监控。冷启动 critic 可能导致 EV 为负，大幅拖慢 RL 收敛。

  - **数据质量审计防 reward hacking**：用 LLM 对训练任务做语义审计，硬拒绝隐藏需求、测试泄漏、解决方案捷径、verifier 过弱等。在推荐/Agent
  任务构造中，可复用该流程过滤低质量或可被刷分的训练样本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
长程终端任务（如 coding、科学发现）要求模型在真实 shell 中执行多轮工具调用，并接受执行结果验证。终端环境最严苛：不可逆副作用、长时程、部分失败需恢复。二进制奖励过于稀疏，难以驱动 RL；同时 122B MoE 模型在训练与推理间存在 token 与专家路由双重不一致，导致梯度作用到错误的子网络。

**方法关键点**
- **训练任务池**：T1-15k，由 RST 递归合成并经 LLM 审计筛选 15k 高质量任务，与 Terminal-Bench 2.1 完全 out-of-distribution。任务分布集中于脚本自动化、软件开发、系统管理。
- **稳定 MoE RL**：TITO（token-in, token-out）保持训练 token 与推理采样完全一致，边界修复有界，loss 区域 token drift 为 0；R3（rollout routing replay）记录推理时每个 MoE 层的专家路由掩码，训练时重放该掩码，消除专家交换导致的 log-prob 偏差。两者将训练-推理 log-prob gap 从 0.021 降至 0.013，且零漂移。同时关闭 MoE load balancing 和 KL 惩罚，避免干扰路由对齐。
- **密集验证奖励**：以绝对通过断言数除以固定全局尺度 S=20 作为奖励，不使用通过比例，保留不同难度任务的信号差异。奖励放在最后 response token，GAE γ=λ=1，由 critic 分派时间信用；critic 是唯一基线。
- **Critic 稳定化**：先在 TMax-15k 上预热 critic 一个 epoch，critic 学习率为 actor 的 30 倍，用 explained variance 监控，避免冷启动时 EV 为负。
- **基础设施**：actor-critic 同驻设备、上下文并行、超时与慢尾管理，支持长时程 rollout。

**关键实验**
- Terminal-Bench 2.1：基座 43.8% → 监督 49.4% → RL 后 T1 达 64.0% resolved（相对提升 28.5%），超过 GPT-5.4（54.8%）和 DeepSeek-V4-Flash（56.9%），接近 Claude Opus 4.7（66.1%）。
- Long-Horizon Terminal Bench：27.9%，超过 GPT-5.4 和 GLM-5.1；Terminal-Bench Hard：38.0%。
- Debugging 100.0%，Sysadmin 88.9%，验证长程终端能力。

**最值得记住的一句话**
训练-推理一致性和密集验证奖励共同决定长程 MoE Agent 能否有效 RL：TITO+R3 将 log-prob gap 从 0.021 降至 0.013 且 loss 区域零漂移，绝对断言数奖励保留跨任务难度信号。
