---
title: 'ARC: Fair Relative Advantage Comparison in Open-Ended Real-World Interaction'
title_zh: ARC：开放世界真实交互中的公平相对优势比较
authors:
- Yongqi Tong
- Tan Li Hui Faith
- Choy Zhen Wen Marcus
- Zhou Jin
- Kewei Fu
- Jiang-Ming Yang
- Jianshe Li
- Xin Zhang
affiliations:
- Ant International
arxiv_id: '2608.13622'
url: https://arxiv.org/abs/2608.13622
pdf_url: https://arxiv.org/pdf/2608.13622
published: '2026-08-12'
collected: '2026-08-26'
category: Agent
direction: Agent RL 策略条件化优势估计
tags:
- RL
- GRPO
- Tool Use
- Advantage Estimation
- Agent Interaction
- Reward Fairness
one_liner: 提出策略条件化 rollout 分组的 ARC 方法，消除跨策略奖励偏差，提升 agent 工具调用 RL 训练的公平性与稳定性。
practical_value: '- 在对话式推荐/导购 Agent 中，如果存在“直接推商品”、“先反问偏好”、“确认订单/退款”等多种有效响应，可沿用 ARC
  思路：训练时给每个 prompt 注入策略指令，按策略分组计算 GRPO/PPO 优势，避免奖励模型偏好某类话术；推理时去掉指令让模型自主选择。这比单纯加 KL
  或 reward shaping 更直接解决跨风格奖励偏差。

  - INTER3 的通道分离值得迁移到电商客服/导购场景：用户可见的 <answer> 流式输出与内部工具调用解耦，可以在查询库存/优惠/风控时立即给用户进度反馈，显著降低首
  token 延迟（4.91s→1.27s）并支持用户打断；实现只需新增 <answer> 特殊 token 和后处理抽取。

  - 多通道生成（推理 + 工具 + 用户文本）训练时建议加熵正则，否则易出现模型反复输出无意义 <answer> 块导致的 entropy collapse；混合奖励可结合工具执行结果与交互格式分项打分。

  - 课程式减弱或推理时注入策略指令在 agentic 场景不可靠：策略提示应作为训练期方差控制变量保留，推理时不要依赖；这提示业务中不要试图用推断时 prompt
  策略控制模型行为，而应在训练期把策略差异纳入比较结构。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

开放域真实交互（客服、导购、任务型 agent）中，同一对话状态允许多种有效下一步：直接回答、反问澄清、进度播报、确认高风险操作。Group-based RL（PPO/GRPO/DAPO）默认同组采样可比，但若 rollouts 策略不同，奖励模型对风格、长度、曝光度的偏好会污染相对优势，使优化偏向 reward 喜欢的话术而非上下文合适策略。这就是 reward fairness 问题。

## 方法关键点

- **ARC**：训练时给每个样本注入一个策略指令（Progress Update / Clarify First / Alignment Check / Direct Answer），只在同策略组内采样 rollouts 并计算优势，消除跨策略方差；推理时去掉指令让模型自主选策略。
- **混合奖励 + 熵正则**：INTER3 多通道输出（内部推理、<answer> 用户可见、工具调用）易熵崩溃，熵正则保持探索。
- **INTER3 框架**：通道分离，用户可见 <answer> 流式输出，内部推理/工具执行延迟；TTFT 从 4.91s 降到 1.27s。
- **INTER3-86K**：来自支付平台在线客服真实日志 + 公共工具基准 + Qwen3.5-397B 合成，含策略标注共 86.8K 样本。

## 关键实验

在 tau-bench/tau2-bench 上，GRPO+ARC 平均 33.46 vs GRPO 28.09（+5.37）；tau-airline 31.33→44.00，tau-retail 40.29→50.00，tau2-airline 36.67→48.00；4B 模型同样受益（avg 22.38→34.23）。课程式移除策略指令反而降低 agentic 性能，默认训练期保留指令最优。

**最值得记住的一句话：在开放交互中，决定 RL 效果的不只是如何 reward，更是 rollouts 是否在同一策略空间内被公平比较。**
