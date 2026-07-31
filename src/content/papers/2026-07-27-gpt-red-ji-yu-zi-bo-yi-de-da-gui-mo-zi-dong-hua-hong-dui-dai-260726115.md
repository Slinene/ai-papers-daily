---
title: 'GPT-Red: Automated Red Teaming via Self-Play at Scale'
title_zh: GPT-Red：基于自博弈的大规模自动化红队代理
authors:
- Eric Wallace
- Christopher A. Choquette-Choo
- Nikhil Kandpal
- Sam Toyer
- Dylan Hunn
- Stephanie Lin
- Yuxin Wen
- Xiangyu Qi
- Christopher Wolff
- Zizhao Wang
affiliations:
- OpenAI
arxiv_id: '2607.26115'
url: https://arxiv.org/abs/2607.26115
pdf_url: https://arxiv.org/pdf/2607.26115
published: '2026-07-27'
collected: '2026-07-31'
category: Agent
direction: 安全红队 · 自博弈对抗训练
tags:
- red-teaming
- self-play
- prompt-injection
- adversarial-training
- RL
- security
one_liner: 训练自博弈红队代理自动发现提示注入攻击，对抗训练出最强鲁棒模型GPT-5.6
practical_value: '- 对抗训练思想可迁移至推荐模型鲁棒性增强：对召回/排序模型注入对抗样本（如恶意特征序列）训练，提升生产系统抗干扰能力。

  - 自博弈架构可借鉴于生成多样化攻击样本：类似用生成式对抗网络思路，在审核/风控模型中持续进化攻击模式，扩大覆盖。

  - 红队代理作为自动评估工具：可构建面向推荐系统的“黑盒攻击代理”，在离线评估中压测模型边界，提前暴露盲区。

  - 工程上，将红队发现的高危模式加入训练集形成闭环，可系统化提升模型版本迭代的安全性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
LLM在智能体场景中需抵御对抗性提示注入攻击，但人工红队数据有限，模型易过拟合已知模式。规模化生成多样、高质量攻击样本是鲁棒性训练的关键瓶颈。  

**方法**  
提出GPT-Red，一个基于自博弈的大规模自动化红队代理。核心是设计可扩展的自博弈算法：同时训练一批攻击者与防御者代理，攻击者学习在真实红队环境中生成新颖的提示注入攻击，防御者则学习抵御，双方持续对抗进化。训练计算规模对齐最大的RL后训练流程，将红队代理自身作为攻击数据工厂。  

**结果**  
GPT-Red可靠攻破GPT-5.5及之前所有模型，攻击成功率优于人类红队专家，且泛化至未见环境、防御模型与测试工具。基于它对抗训练得到的GPT-5.6成为至今对提示注入最鲁棒的模型。实验显示，随着测试时计算增加，GPT-Red加防御者访问的攻击成功率显著优于GPT-5.5，并能在无明显防御时接近100%攻击成功。这开启了红队能力与模型鲁棒性自我增强的飞轮效应。
