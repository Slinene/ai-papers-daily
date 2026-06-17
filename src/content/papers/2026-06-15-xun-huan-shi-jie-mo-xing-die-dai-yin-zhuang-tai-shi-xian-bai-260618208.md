---
title: Looped World Models
title_zh: 循环世界模型：迭代隐状态实现百倍参数效率
authors:
- Hongyuan Adam Lu
- Z. L. Victor Wei
- Qun Zhang
- Jinrui Zeng
- Bowen Cao
- Lingwei Meng
- Mocheng Li
- Zezhong Wang
- Haonan Yin
- Naifu Xue
affiliations:
- FaceMind Research Asia
arxiv_id: '2606.18208'
url: https://arxiv.org/abs/2606.18208
pdf_url: https://arxiv.org/pdf/2606.18208
published: '2026-06-15'
collected: '2026-06-17'
category: Other
direction: 世界模型 · 循环架构 · 参数效率
tags:
- World Models
- Looped Architecture
- Reinforcement Learning
- Parameter Efficiency
- Adaptive Computation
one_liner: 通过参数共享的 Transformer 块迭代优化隐状态，世界模型获得高达 100 倍参数效率并自适应深度
practical_value: '- 参数共享的循环 Transformer 可迁移到用户行为序列预测，大幅减少长序列建模时的参数量和推理成本

  - 自适应深度机制可根据输入复杂度动态分配计算，适合推荐系统中用户状态复杂多变的场景

  - 迭代隐状态更新思想可用于长期兴趣演化模拟，替代传统的固定循环网络

  - 主要是学术贡献，业务可借鉴点有限：当前仅在标准世界模型基准验证，缺乏推荐场景直接证据'
score: 7
source: huggingface-daily
depth: abstract
---

动机：当前世界模型在长时预测中面临计算深度与累积误差的根本矛盾。深网络能提升保真度，但部署昂贵且易在自回归推演中发散。

方法：提出 LoopWM，第一个使用循环架构的世界模型。核心是用一个参数共享的 Transformer 块反复更新隐环境状态。每次迭代将上一步输出与新观测/动作拼接后输入同一块，通过循环次数控制“隐式深度”。训练时采用随机循环深度策略迫使模型学会不同深度的预测，推理时可通过评估收敛性来自适应终止循环。模型总体参数量极低（与单层 Transformer 相当），但等效于极深网络的效果。

结果：在标准的 DeepMind Control 任务上，LoopWM 与 DreamerV3 等基线相比，参数效率提升高达 100 倍（如 0.1M 参数量达到传统模型 10M 参数量的性能）。自适应计算机制自动为复杂状态分配更多循环轮次，在保障预测质量的同时显著降低平均计算开销。该工作开辟了“迭代隐深度”这一新的 scaling 轴，与模型尺寸/数据规模正交。
