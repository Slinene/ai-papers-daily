---
title: 'MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training
  across Mobile and Computer Environments'
title_zh: MAI-Gym：面向移动与计算机环境的 GUI Agent 评估与 RL 训练一体化开源平台
authors:
- Panrong Tong
- Quyu Kong
- Pengxiang Li
- Tianyu Xia
- Hanzhang Zhou
- Lei Wang
- Chenglin Cai
- Long Li
- Long Chen
- Jianan Zhang
affiliations:
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2610.20939'
url: https://arxiv.org/abs/2610.20939
pdf_url: https://arxiv.org/pdf/2610.20939
published: '2026-10-13'
collected: '2026-10-17'
category: Agent
direction: GUI Agent 在线强化学习与仿真平台
tags:
- GUI Agent
- Online RL
- Synthetic Data
- Verifiable Rewards
- Open-source Platform
one_liner: 开源一体化 GUI Agent 平台，统一评估/数据/在线RL，9B模型在 MobileWorld 和 OSWorld-Verified 创下
  SOTA
practical_value: '- **构建可重置的电商/导购模拟环境**：借鉴其 mocked app 与 execution-validated task
  verifier 设计，在电商场景中搭建可重复初始化的购物、客服、售后等模拟 app，自动生成带可验证奖励的任务，低成本训练 GUI 操作型 Agent。

  - **统一 rollout pipeline 保证训练与评估一致性**：将环境交互、数据收集和在线 RL 训练纳入同一管线，避免训练/评估行为偏差；其 20K
  并行环境实例的工程架构可直接迁移到大规模在线策略训练，如导购对话策略或推荐排序策略的仿真优化。

  - **仿真 RL 到真实业务的迁移**：论文显示在 mock 火车票 app 上训练后，真实手机任务成功率从 28.8% 提升到 48.1%，证明低成本仿真环境训练的模型可迁移到真实交互场景，适合作为电商
  App 操作、订单流程等任务的试错沙盒。

  - **直接复用开源任务与合成技能**：发布的 2,000 个验证任务和自动化合成技能可作为电商/广告领域 GUI Agent 数据集的冷启动模板，结合自身业务
  UI 快速生成带 verifier 的训练任务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
在线 RL 在数学、代码等可验证奖励领域进展显著，但 GUI Agent 训练受限于交互环境成本高、现实任务稀缺，难以规模化。  

**方法关键点**  
MAI-Gym 将移动端、电脑端、Web 环境的评估、数据收集与在线 RL 训练统一到一个开源平台。通过共享 rollout pipeline，保证训练与评估的 Agent 行为一致；支持 10 个既有基准，并能扩展到 20,000 个并行环境实例。平台具备自动化合成 GUI 应用与任务的能力，包括可重置的 mocked apps、跨应用连贯世界，以及执行级验证的 task verifiers。  

**关键结果**  
基于平台训练 9B 参数模型 MAI-Gym-9B，在 MobileWorld 取得 78.4%、在 OSWorld-Verified 取得 76.2%，在 10B 以下开源 GUI Agent 中达到 SOTA。在 mock 火车票 app 上进行 RL 后迁移到真实手机，任务成功率从 28.8% 提升至 48.1%。框架、合成技能、mock apps、2,000 个验证任务及模型权重均已开源。
