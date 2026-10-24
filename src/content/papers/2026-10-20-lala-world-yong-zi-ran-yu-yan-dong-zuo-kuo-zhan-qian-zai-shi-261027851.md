---
title: 'LaLa-World: Scaling Latent World Models with Natural Language Actions'
title_zh: LaLa-World：用自然语言动作扩展潜在世界模型
authors:
- Junha Song
- Geonmo Gu
- Jeongeun Park
- Heejeong Nam
- Lucas Maes
- Byeongho Heo
- Dongyoon Han
- Sangdoo Yun
affiliations:
- NAVER AI Lab
- Georgia Institute of Technology
- Brown University
- Mila & Université de Montréal
arxiv_id: '2610.27851'
url: https://arxiv.org/abs/2610.27851
pdf_url: https://arxiv.org/pdf/2610.27851
published: '2026-10-20'
collected: '2026-10-24'
category: Agent
direction: 语言条件潜在世界模型与规划
tags:
- Latent World Model
- JEPA
- LLM
- MPC
- Language Actions
- Policy Fine-tuning
one_liner: 用语言描述动作与视觉变化，让单一LLM潜在世界模型跨异构数据训练，实现高效规划与策略初始化
practical_value: '- 将异构用户行为数据（点击、购买、曝光、反馈）和场景特征统一为自然语言描述，可联合训练单一世界模型，支持跨域推荐和冷启动场景下的行为预测。

  - 用LLM作为环境状态预测器，替代像素/隐向量级别的生成，既能理解语言条件，又能大幅降低训练与推理成本，适合在线实时规划（如MPC）和反事实推演。

  - 预训练的用户行为世界模型可作为下游策略（如RL推荐策略）的初始化，加速收敛，类似LaLa-Policy的思路可以迁移到Agent策略微调。

  - 语言化动作和状态对措辞变化具有鲁棒性，适合处理自然语言形式的用户意图或Agent指令，增强系统对模糊输入的容错。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：JEPA风格的潜在世界模型（LWM）通常按领域或任务单独训练，难以跨异构数据源扩展。本文通过采用视频生成模型的语言条件接口，让单一LWM联合学习仿真、机器人轨迹以及通用图像视频数据。

**方法关键点**：
- 将数值动作和视觉变化都用自然语言描述，从而消除异构数据集之间的格式差异，支持联合训练。
- 预测器基于语言模型构建，在预测未来潜在状态的同时理解语言条件。
- 得到的LaLa-World用于MPC规划，并作为LaLa-Policy的预训练初始化，后者联合预测动作和未来视觉表征。

**关键结果**：
- LaLa-World的平均MPC规划性能优于按域/任务分别训练的现有LWM。
- 加入通用图像和视频数据可进一步提升平均规划性能，并增强对动作措辞变化的鲁棒性。
- 相比RAEv2-based视频生成模型基线，规划性能相当，训练成本降低6倍，规划速度提升13.9倍。
- LaLa-Policy在LIBERO和RoboCasa上与Cosmos Policy性能竞争，推理速度最高提升5.5倍。
