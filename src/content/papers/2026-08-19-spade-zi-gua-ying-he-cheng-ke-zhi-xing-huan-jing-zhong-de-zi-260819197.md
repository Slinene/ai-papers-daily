---
title: 'SPADE: Self-Play in Adaptive Synthetic Executable Environments'
title_zh: SPADE：自适应合成可执行环境中的自博弈
authors:
- Bo Liu
- Simon Yu
- Yiding Jiang
- Ao Qu
- Andrew Zhao
- Zichen Liu
- Junsu Kim
- Zijian Zhou
- Seungone Kim
- Tongzheng Ren
affiliations:
- University of Washington
- Stanford University
- Northeastern University
- Carnegie Mellon University
- Massachusetts Institute of Technology
arxiv_id: '2608.19197'
url: https://arxiv.org/abs/2608.19197
pdf_url: https://arxiv.org/pdf/2608.19197
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 自博弈强化学习 · 可执行环境生成
tags:
- Self-Play
- Environment Generation
- RLVR
- GRPO
- Hint-based Regret
- Agentic RL
one_liner: 提出 SPADE 框架，让 LLM 在环境设计者与推理智能体双角色间自博弈，通过 hint-based regret 生成能力前沿的代码环境，实现开放自我改进
practical_value: '- **模拟用户/环境生成**：在电商多轮对话、推荐 Agent、搜索工具调用等场景，可用可执行代码环境（Gym reset/step）生成可验证的多轮交互任务，统一单轮与多轮
  RL 训练。用商品数据库、用户行为日志构建沙盒，设计者生成任务，推理智能体进行工具调用；hint-based regret 自动调整难度，比固定难度或纯对抗更稳定。

  - **语料库 grounding + 记忆**：从真实用户日志、商品描述、搜索日志中采样作为环境生成条件，保持生成任务多样性，防止模式崩溃；用 memory
  buffer 存储高 regret 任务或难样本，避免重复生成已掌握场景。电商推荐中可用于生成多样化的用户目标/场景，持续提供训练信号。

  - **稳定化训练技巧**：双角色共享同一模型但独立优势归一化；延迟生成器更新并配合截断重要性采样；asymmetric clipping (ε_low=0.2,
  ε_high=0.28) 保留探索；regret 信号 floor 到 0 并混合难度锚点。这些在联合训练生成模型和策略模型的 RL 中可直接复用。

  - **可验证奖励设计**：工具使用环境包含状态检查和确定性 reset gate，确保任务可解且可验证；在电商多轮交互中可设计类似的成功准则检查，过滤无效环境，提高
  RL 数据质量。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：语言智能体能力提升后，训练环境池固定成为瓶颈。手工或合成环境不会随智能体进步而更新，智能体耗尽环境后停止提升。自博弈有望持续提供新环境，但之前方法生成的是单轮任务且容易模式崩溃。

**方法关键点**：
- SPADE 让一个共享 LLM 交替扮演环境设计者和推理智能体。设计者生成 Gym 风格 reset/step 的完整 Python 可执行 MDP，包括状态转移、奖励和验证代码，统一单轮与多轮。
- 设计者奖励是 hint-based regret：推理智能体在有特权提示 vs 无提示下的平均回报差，使设计者偏向既可解又处于能力前沿的环境。推理智能体奖励为任务是否完成，两者都通过 GRPO 更新。
- 生成时从大型预训练语料采样文档作为 grounding，保持多样性；并维护环境记忆 buffer（高 regret 种子和负样本）避免重复。
- 训练稳定化：两个角色优势分别归一化；设计者更新延迟、使用截断重要性采样；asymmetric clipping 等。

**关键实验与数字**：
- 三套 Qwen3 主干（4B/8B/30B-A3B），games 和 tool-use 两设置。
- 30B-A3B games 平均 +8.1 over base，+5.3 over fixed-env RLVE；tool-use BFCL v4 multi-turn +5.7，ACEBench-Agent +13.9。
- 消融：去掉 corpus、memory 或冻结设计师均导致下降；无 corpus 时环境多样性 Vendi/n 从 0.68 降到 0.04，并连续生成同一任务 41 次。

**最值得记住的一句话**：可执行代码环境与 hint-based regret 把环境设计变为可学习组件，是迈向开放自我改进的关键。
