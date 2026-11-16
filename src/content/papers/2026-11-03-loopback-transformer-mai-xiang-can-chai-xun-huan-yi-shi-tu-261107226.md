---
title: 'Loopback Transformer: Towards a Unified View of Residual Looped Transformers'
title_zh: Loopback Transformer：迈向残差循环Transformer统一视图
authors:
- Xuan Ouyang
- Zefan Cai
- Chenlong Zhang
- Cheng Luo
- Ke Wan
- Junjie Hu
affiliations:
- University of Wisconsin–Madison
- University of California, Santa Barbara
- California Institute of Technology
- Microsoft
arxiv_id: '2611.07226'
url: https://arxiv.org/abs/2611.07226
pdf_url: https://arxiv.org/pdf/2611.07226
published: '2026-11-03'
collected: '2026-11-16'
category: LLM
direction: 高效Transformer架构 · 循环残差设计
tags:
- Loopback Transformer
- Looped Transformer
- Parameter Efficiency
- Language Modeling
- Residual Connections
one_liner: 分离输入与循环更新路径，用几何衰减和注意力加权各次更新，以标准Transformer 40-75%参数量获得更低验证损失和更高下游精度
practical_value: '- 如果业务中需要部署大型Transformer（如用户行为序列编码器、内容理解塔），可将多层堆叠改为循环共享权重，保留输入残差直连，对循环块输出更新做几何衰减+注意力加权；在推荐模型序列塔中可减少40-60%参数量并保持效果。

  - 对电商长周期用户兴趣建模，把残差连接视为“记忆”并分离输入路径，可独立控制历史信息保留强度，几何衰减提供时间衰减先验，比完全依靠注意力学习更稳定，适合行为序列近期偏好加权。

  - 同等训练预算下更低损失意味着可用更少参数达到相同/更好线上指标，降低推理延迟与显存，利于广告/推荐系统在资源受限时升级模型。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：循环Transformer通过重复共享块减少参数，但参数共享本身并不决定重复计算的结果如何被重用；需要从残差连接的深度-记忆视角分析存储了哪个表示以及后续读取如何加权。

方法关键点：Loopback Transformer将共享栈的输入保留在单独路径上，单独读取每次循环的更新，从而分离控制输入强度、总更新权重和更新间分配。几何衰减设定总更新权重并提供最近性先验，注意力机制学习如何分配该权重到各次更新。

关键结果：在ClimbMix预训练中，Loopback在191M到3B参数规模下，以标准Transformer 40-75%的参数量（不含token embedding和输出头）达到更低验证损失，且训练token数与执行深度匹配。在1.4B与3B规模，13个下游任务平均精度更高。在191M、374M、778M规模，它在标准Transformer和七种循环残差设计中取得最低验证损失和最高13任务平均精度。
