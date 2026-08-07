---
title: 'The Next Screenshot Knows: Gated Hindsight Distillation for Mobile GUI Agents'
title_zh: 下一帧截图知道答案：门控后见蒸馏训练移动GUI代理
authors:
- Weiwei Li
- Junzhuo Liu
- Tong Chu
- Hengfu Yu
- Wen Li
affiliations:
- 电子科技大学
arxiv_id: '2608.06065'
url: https://arxiv.org/abs/2608.06065
pdf_url: https://arxiv.org/pdf/2608.06065
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: GUI Agent · 后见知识蒸馏
tags:
- GUI Agent
- Distillation
- GRPO
- Hindsight
- Privileged Information
- Gating
one_liner: 利用下一帧截图作为特权信息，通过门控蒸馏将未来知识注入前缀策略，显著提升GUI代理任务成功率。
practical_value: '- 序列决策任务（如推荐多轮交互）中，可模仿GHD，将用户事后真实行为（点击、购买）作为“未来状态”，通过teacher-student蒸馏，将事后知识注入仅依赖当前上下文的前缀策略，提升决策合理性。

  - 门控机制“仅学生犯错且教师纠正时蒸馏”能有效过滤噪声样本，保证蒸馏信号的可靠性；类似地在推荐agent训练中，可只蒸馏那些模型在当前状态下给出差动作而事后信息能给出更好动作的case。

  - 将强化学习（GRPO）与token级分布蒸馏结合，提供稠密的token级监督，比传统基于动作标签的模仿学习更高效；该训练范式可迁移到任何需自然语言推理+行动的agent场景。

  - 动态采样（最多三次尝试寻找有效蒸馏样本）在不大幅增加训练开销的情况下显著提升有效监督密度，适合在离线数据有限时提升RL训练效率。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

## 动机
标准GUI代理离线训练将成功轨迹分解为前缀-动作对，模型仅根据当前屏幕和历史预测动作，丢弃了后续观察。很多动作的正确理由（如某个设置藏在哪个菜单后）只有在动作执行后的下一屏幕才显现，因此前缀中缺乏可学习的推理依据，导致推理监督信号缺失，模型难以学到界面知识。

## 方法关键点
- **特权后见蒸馏**：训练时引入一个与student共享参数的teacher，teacher额外接收下一帧截图作为特权信息，对student的rollout进行位置级别的token分布重打分；student仅使用前缀信息。
- **门控机制**：仅在student动作失败（奖励低于阈值）且teacher的位置级贪心解码动作与演示动作匹配时，才对该rollout计算蒸馏损失，过滤不可靠信号。
- **动态采样**：对同一前缀最多尝试三次rollout，选择至少含一个被门控接受的响应的那批进行训练，提高有效监督密度。
- **联合训练**：结合GRPO强化学习损失和蒸馏损失，蒸馏权重λ=0.1，蒸馏损失采用对称Jensen-Shannon散度，在top-K token上计算。
- **完全解耦**：推理时仅使用前缀条件student，无需teacher、未来截图或任何额外模块。

## 关键实验
- 数据集：AndroidWorld和AndroidLab两个移动GUI代理基准，训练数据来自OpenMobile的困难子集（SFT模型一次尝试无法解决的任务）。
- 基座：Qwen2.5-VL-7B和Qwen3-VL-8B，均从SFT checkpoint开始训练。
- 对比基线：SFT、GRPO，以及消融各组件（仅门控、仅门控+动态采样、替换特长信息的STaR、GUI-Shift辅助任务）。
- 核心结果：8B模型在AndroidWorld上GHD达到66.47% Pass@1（GRPO 61.35%），AndroidLab上54.11%（GRPO 37.43%），7B同样大幅提升。消融表明未来截图是主要增益（+3.17点），动态采样和门控各提供+0.71~2.43点增益。

## 一句话
**将“下一步应该做什么”的困难预测转化为“根据结果必须做了什么”的简单推理，通过门控蒸馏将事后界面知识注入前缀策略。**
