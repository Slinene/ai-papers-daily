---
title: 'LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use
  Agents'
title_zh: LEASH：面向计算机使用智能体的不确定性感知弱到强升级与监督
authors:
- Qingni Wang
- Changdae Oh
- Yuzhe Yang
- Sharon Li
- Jiachen Yang
- Ang Li
- Xin Eric Wang
affiliations:
- Simular
- University of Wisconsin–Madison
arxiv_id: '2610.22280'
url: https://arxiv.org/abs/2610.22280
pdf_url: https://arxiv.org/pdf/2610.22280
published: '2026-10-14'
collected: '2026-10-17'
category: Agent
direction: Agent 弱到强升级与不确定性监督
tags:
- weak-to-strong escalation
- uncertainty estimation
- computer-use agents
- Mahalanobis distance
- latent representation
- black-box oversight
one_liner: 用弱模型隐藏状态的不确定性同时驱动升级决策与黑盒强模型监督，无训练实现高效成本-精度平衡
practical_value: '- 在电商/推荐 Agent 工作流中，可用廉价的本地小模型作为默认执行器，利用其隐藏状态计算不确定性（如马氏距离到历史成功/失败样本）决定是否升级到昂贵的大模型，无需训练额外监控模型，节省推理成本。

  - 对于黑盒 API 大模型（如 GPT/Claude）的调用，可复用白盒弱模型作为“影子观察者”，定期对强模型轨迹打分，高不确定性时触发反思或回滚干预，保留对黑盒输出的控制。

  - 表示库方法：记录弱模型在任务查询和动作生成时的最后层隐藏状态，按成功/失败标注，用相对马氏距离作为不确定性分数，计算开销低（无额外前向传播），适合长程多步任务。

  - 门槛校准：通过参考集的经验分位数设置升级阈值以匹配预算，将升级率作为 budget 代理，可实现可调节的成本-精度权衡，对在线服务很有用。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

长程计算机使用任务（如 GUI 自动化）中，每一步都用前沿模型成本高昂，而轻量开源模型单独执行成功率很低。弱到强升级（weak-to-strong escalation）是折中方案，但核心挑战在于：1) 需要一个足够廉价的信号决定何时升级；2) 升级后黑盒强模型仍可能出错，却无法访问其内部状态进行监控。

## 方法关键点

- **训练免费的不确定性估计**：从弱模型隐藏状态构建参考表示库，记录任务查询令牌和动作令牌的最后层表示，并标注成功/失败。
- **分数计算**：标准化后使用共享协方差 Gaussian 判别模型，计算到成功/失败类质心的马氏距离之差，分数越大表示越接近失败样本。
- **三层结构**：初始任务不确定性路由、步骤级运行时升级、以及升级后影子监督（shadow observer）。
- **影子监督**：强模型接管后，弱模型从 actor 转为 observer，每 k 步（k=3）对强模型轨迹评分，高不确定性触发反思干预，丢弃待执行动作并重新决策。
- **门槛校准**：根据目标升级预算设置经验分位数阈值，无需训练。

## 关键实验结果

在 OSWorld 基准上，用四个开源弱模型（EvoCUA-8B、Qwen3.5-35B-A3B、Nemotron-3-Nano-Omni、Qwen3.8-27B）和 Claude Opus 5 作为强模型。LEASH 在匹配升级率下比随机升级高 6.55–11.94 个百分点；Qwen3.5-35B-A3B 配置达到 73.66% 成功率，成本 $0.4117/任务，比 always-on Opus 5（72.90%，$0.5094）降低 19.2% 成本；恢复 75–102% 的弱到强性能差距。消融显示升级和影子监督各有增益。

**最值得记住的一句话**：一个统一的潜在不确定性信号可以同时驱动升级决策和黑盒强模型监督，且完全训练免费、计算开销极低。
