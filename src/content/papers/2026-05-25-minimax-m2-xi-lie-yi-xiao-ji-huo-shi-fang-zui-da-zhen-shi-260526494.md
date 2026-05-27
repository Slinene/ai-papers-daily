---
title: 'The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence'
title_zh: MiniMax-M2 系列：以小激活释放最大真实世界智能
authors:
- MiniMax
- Aili Chen
- Aonian Li
- Baichuan Zhou
- Bangwei Gong
- Binyang Jiang
- Boji Dan
- Changqing Yu
- Chao Wang
- Cheng Ma
affiliations:
- MiniMax
arxiv_id: '2605.26494'
url: https://arxiv.org/abs/2605.26494
pdf_url: https://arxiv.org/pdf/2605.26494
published: '2026-05-25'
collected: '2026-05-27'
category: Agent
direction: MoE 架构与 Agent RL 训练协同设计
tags:
- MoE
- Agentic RL
- Self-evolution
- Multi-Token Prediction
- SWE-bench
- AppDev
one_liner: 以仅 9.8B 激活参数的 MoE 架构，通过 agent 原生数据管道和 RL 系统达到 agentic 前沿性能，并初步实现自进化。
practical_value: '- **稀疏 MoE 设计**：256 细粒度专家，sigmoid gating 和可学习偏置大幅降低辅助损失，每 token
  仅激活 8 个专家。在电商推荐中可用于生成式模型，兼顾大容量与低推理成本，其负载均衡策略可迁移到多任务学习。

  - **Agent RL 训练系统 Forge**：训练-推理-agent 解耦，支持白盒/黑盒 agent，用窗口化 FIFO 和前缀树合并吸收长短轨迹差异。可直接复用到多智能体推荐系统的强化学习组件，提升离线策略优化效率。

  - **可验证轨迹数据合成**：用 GitHub PR 构造 SWE 任务，Docker + 测试用例提供硬奖励；AppDev 采用专家 meta query
  + Agent-as-a-Verifier 三层验证。推荐系统可借鉴“可执行验证”思想，为商品文案生成等任务自动合成带奖励的高质量数据。

  - **自进化能力**：M2.7 能自主调试训练、修改自身 scaffold，展示从训练到部署的自动化闭环。可用于推荐模型的在线自动纠错、特征自动更新等运维场景，减少人工介入。'
score: 8
source: huggingface-daily
depth: full_pdf
---

#### 动机
大语言模型正从短对话转向长周期 agentic 工作流（如软件工程、办公自动化），这带来两个矛盾：超长上下文造成的训练/推理成本瓶颈，以及生产级任务对模型复杂能力的极高要求。为此，MiniMax-M2 系列以 **“小激活释放最大真实世界智能”** 为核心理念，追求用极少激活参数（9.8B）匹敌前沿闭源系统。

#### 方法关键点
- **稀疏 MoE 架构**：62 层 decoder-only Transformer，256 个细粒度专家，每 token 激活 8 个（sigmoid 门控 + 可学习偏置），辅助负载平衡损失近乎归零；全注意力 GQA（48Q/8KV），192K 上下文。
- **多令牌预测 (MTP) 与推测解码**：预训练中增加 MTP 模块，后续通过权重复制扩张至 3 个，作为推测解码的 draft 通路，提升推理吞吐。
- **Agent 原生数据管道**：针对 agentic coding 构建 SWE-scaling 管道（从 GitHub PR 提取可验证任务并合成 Docker 环境）、AppDev 管道（专家 meta query + Agent-as-a-Verifier 三层验证）和 Terminal-Gym；针对 agentic cowork 覆盖深度搜索、办公任务、金融分析、幻灯片生成，全部基于真实可运行工作空间，轨迹蒸馏自强教师并经过多轴评估。
- **Agent RL 系统 Forge**：采用 CISPO 算法，将训练、推理、agent 解耦，统一支持白盒和黑盒 agent；配套窗口化 FIFO 调度、前缀树合并、定制推理内核，大幅提升训练效率和稳定性。
- **自进化探索**：M2.7 可自主诊断失败训练、修改自身 agent scaffold，在多轮 ML 工程任务上实现闭环自改进。

#### 关键结果
- M2.7 仅用 ~10B 激活参数，在 agentic coding 上达到 SWE-bench Pro 56.2，Multi-SWE-bench 52.7；在 agentic cowork 上 GDPval-AA 50.0，MM-Claw 62.7；在推理上 AIME 2026 94.2，GPQA-Diamond 89.8。与闭源旗舰（如 GPT-5.4、Opus 4.6）竞争。
- 消融实验证实：细粒度专家和 MTP 显著提升推理能力；全注意力在长上下文 agent 任务上大幅优于滑动窗口注意力；自进化使系列内基准持续提升（M2 → M2.5 → M2.7）。

**最值得记住的一句话**：mini activations can unleash maximum real-world intelligence——通过精细化稀疏激活与原生 agent 训练体系，小模型也能在真实世界任务中释放前沿智能。
