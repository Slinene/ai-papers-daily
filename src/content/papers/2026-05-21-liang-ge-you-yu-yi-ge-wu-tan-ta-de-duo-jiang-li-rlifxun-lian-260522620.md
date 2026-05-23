---
title: 'Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework'
title_zh: 两个优于一个：无坍塌的多奖励RLIF训练框架
authors:
- Shourov Joarder
- Diganta Sikdar
- Ahsan Habib Akash
- Binod Bhattarai
- Prashnna Gyawali
affiliations:
- Bangladesh University of Engineering and Technology
- West Virginia University
- University of Aberdeen
- Fogsphere (Redev.AI Ltd)
- University College London
arxiv_id: '2605.22620'
url: https://arxiv.org/abs/2605.22620
pdf_url: https://arxiv.org/pdf/2605.22620
published: '2026-05-21'
collected: '2026-05-23'
category: LLM
direction: 无监督强化学习推理训练优化
tags:
- RLIF
- multi-reward
- entropy collapse
- GDPO
- KL-Cov
- reasoning
one_liner: 将内部反馈分解为答案级和完成级互补奖励，结合GDPO归一化与KL-Cov正则化，稳定无监督RL推理训练，性能逼近监督方法
practical_value: '- **多奖励分解思路可迁移至电商Agent策略训练**：将单一奖励拆分为任务完成质量（如订单转化）与过程合理性（如对话轮次、信息获取效率），利用类似GDPO的归一化避免信号尺度失衡，防止策略被单一指标劫持。

  - **KL-Cov正则化可缓解生成式推荐中的“多样性坍塌”**：当使用RL微调生成模型（如推荐标题、理由生成）时，显式惩罚低熵token分布，保留探索能力，防止模型输出千篇一律的高概率套路。

  - **内部反馈在缺少强监督时构建训练信号**：在无法获得真实用户反馈或黄金标准答案的冷启动场景下，利用模型自身的投票（如聚类投票）和自信度作为奖励，可驱动Agent或推荐模型自改进。

  - **方法对长程推理的稳定效果可启发多步决策智能体设计**：若Agent需执行多步工具调用或逻辑推理，借鉴“答案级+完成级”的双层内部奖励，配合针对性正则化，有望提升长序列决策的鲁棒性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有无监督强化学习内部反馈（RLIF）方法常依赖单一内部奖励，易引发奖励黑客、熵坍缩与推理结构退化，导致训练不稳定及性能下降。  
**方法**：提出多奖励RLIF框架，将训练信号解耦为两个互补组件——**答案级奖励**基于对多次采样结果的聚类投票衡量最终答案一致性，**完成级奖励**基于token级自信度评估推理过程质量。为稳健融合两个奖励，采用**GDPO引导的归一化**消除尺度失衡。同时引入**KL-Cov正则化**，针对低熵token分布（主要熵坍缩来源）施加惩罚，保持探索，防止后期性能坍塌。  
**结果**：在数学推理与代码生成基准上，方法在稳定性和鲁棒性上均超越以往无监督RL方案，性能接近有监督RLVR方法，验证了互补内部奖励与定向正则化可支持长程推理的稳定训练，无需外部真实监督。
