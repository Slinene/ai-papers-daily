---
title: 'Seer: Guiding Small Deep-Research Agents with Shared Decision Models'
title_zh: Seer：用共享决策模型引导小型深度研究智能体
authors:
- Yuhao Zhou
- Yang Zhou
- Yuanxi Li
- Jindi Lv
- Dan Si
- Qing Ye
- Jiancheng Lv
affiliations:
- Sichuan University
- University of Illinois at Urbana-Champaign
- Lenovo Group Limited
arxiv_id: '2611.26423'
url: https://arxiv.org/abs/2611.26423
pdf_url: https://arxiv.org/pdf/2611.26423
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 推理期引导 · 共享决策模型
tags:
- deep-research agents
- model-based planning
- value estimation
- LoRA
- inference-time guidance
- tool-use
one_liner: 将动作提议与工具响应模拟、价值估计解耦，训练可跨模型复用的决策模型，在推理期引导小模型深度研究智能体
practical_value: '- 在搜索/推荐 Agent 中做候选动作比较时，可训练轻量 tool-response simulator + value estimator，用额外本地推理替代真实搜索
  API、详情页抓取等工具调用，降低 tool call 成本与延迟。

  - 价值估计器用 HL-Gauss 分类头 + 折扣终端正确性标签（γ=0.95），对交互历史前缀做过程监督，比直接回归更容易训练；标签只需终端 outcome，适合迁移到电商问答/导购
  Agent 的中间决策评估。

  - 推理期可用 PUCT/depth-one imagined search 选动作，只执行被选中的动作并把真实响应写入历史，避免模拟响应污染上下文；候选宽度
  k 不是越大越好，需按 agent/task 用线上 A/B 或离线诊断选择。

  - simulator 和 estimator 不绑定具体 agent 模型，可跨不同 size/厂商模型复用，适合多模型、多租户的电商搜索/广告 Agent
  部署，避免重复适配成本。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：端侧部署 deep-research Agent 受本地算力与 tool call 费用约束，小模型能力有限；逐模型训练适配成本高。推理时引导虽可避免更新模型，但候选动作真实执行会浪费搜索/抓取调用，prompted self-evaluation 受 agent 自身判断限制，模型专用 critic 又难以跨模型复用。

**方法关键点**：
- 从共享真实研究轨迹语料训练两个可复用决策模型：tool-response simulator Wφ 学习 call→response 预测；value estimator Vθ 在历史前缀上学习折扣终端正确性标签（γ=0.95）。
- 两个模型均以 Qwen3.5-9B 初始化并用 LoRA 训练；estimator 使用 HL-Gauss 分类头，201 bins，离线训练后跨 agent 复用。
- 训练数据通过 Monte Carlo branching 收集，得到 0.7M call-response pairs 与 1M value samples；simulator 只学习 call→response，不依赖轨迹是否成功，未成功轨迹也能提供有效工具输出。
- 推理时 agent 提出候选动作，simulator 预测响应构建 imagined histories，estimator 打分；用 PUCT 做 depth-one imagined search，选择访问次数最多的根边动作。只有选中动作真正执行，真实响应进入历史，丢弃候选不产生 tool calls。

**关键结果**：在 GAIA、BrowseComp-200、BrowseComp-ZH、SEAL-0、XBench-DeepSearch 上，Seer 相比 Base/BoN@4/AV@4 显著提升：Qwen3.5-4B 在 GAIA 上从 13.6% 提升到 41.7%（S32），Qwen3.5-9B 从 22.3% 提升到 50.5%；跨 6 个 Qwen/Gemma 模型，S32 在 30 个设置中 26 个超过 Base。对更大模型也有效，如 Qwen3.5-397B 在 BrowseComp-200 从 34.5% 到 42.5%。工具调用成本接近 Base，明显低于 BoN/AV 的多轨迹执行。消融显示：加 estimator 比 prompted scoring 提升明显；加入 simulator 在 k=4 时可能降精度，但节省真实调用；扩大候选宽度可补偿模拟噪声，但过度加宽受 estimator 噪声限制，需要按模型/任务选 k。

**最值得记住的一句话**：用共享的 tool-response simulator + 折扣终端正确性 value estimator 做推理期候选搜索，以额外本地推理替代被丢弃候选的真实执行，能在不增加 tool call 成本的前提下显著提升小模型 deep-research Agent。
