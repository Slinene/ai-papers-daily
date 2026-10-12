---
title: 'Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge
  Update Efficiency'
title_zh: 专家学习更快：预训练知识组织塑造更新效率
authors:
- Sheng Zhao
- Yuhao Zhu
affiliations:
- University of Rochester
arxiv_id: '2610.13835'
url: https://arxiv.org/abs/2610.13835
pdf_url: https://arxiv.org/pdf/2610.13835
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: 预训练数据组织与知识更新效率
tags:
- Pre-training
- Knowledge Update
- Temporal Ordering
- Specialist
- Generalist
- Model Editing
one_liner: 发现按时间顺序预训练得到的专家模型获取新知识所需更新步数远少于随机顺序训练的通才模型，并提出可预测的预训练数据组织策略
practical_value: '- 对于需要频繁更新知识的场景（新品冷启、新类目/实体词、实时政策词），可以尝试将近期数据按时间顺序组织进行增量预训练或微调，获得“专家”特性，使后续通过
  LoRA、模型编辑等方法更新时收敛更快、所需样本更少。

  - 为防止对历史知识灾难性遗忘，采用“近期时间顺序数据 + 少量历史重放/锚定样本”的混合组织策略；论文给出的策略在保留稳定历史知识的同时增强当前知识更新效率，可作为推荐/排序模型持续学习中的样本回放设计参考。

  - 知识更新成本可通过优化动力学预测，实践中可建立小规模探针实验，评估不同数据排序（时间、类目、热度等）对后续更新效率的影响，选择适合业务的数据组织方式，而不是默认随机
  shuffle。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：理想语言模型需要持续更新知识，但现有工作主要关注训练后更新效率，忽略了预训练阶段知识组织方式对后续更新成本的影响。

**方法关键点**：以传记知识为对象，对比按时间顺序训练（专家）与随机顺序训练（通才）。专家模型只擅长最近知识，通才模型全时间段表现均衡；但专家获取新知识所需更新步数显著更少。作者从第一性原理推导更新成本与优化动力学关系，得到可预测公式；据此设计预训练数据组织策略，保留稳定历史知识同时高效更新当前知识。

**关键结果**：该策略在真实预训练模型和现有知识更新工具上验证有效，并推广到其他知识排序。
