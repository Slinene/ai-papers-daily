---
title: When Does Model Collapse Occur in Structured Interactive Learning?
title_zh: 结构化交互学习中模型崩溃何时发生？
authors:
- Yuchen Wu
- Kangjie Zhou
- Weijie Su
arxiv_id: '2605.20151'
url: https://arxiv.org/abs/2605.20151
pdf_url: https://arxiv.org/pdf/2605.20151
published: '2026-05-19'
collected: '2026-05-20'
category: Other
direction: 多模型交互下的训练稳定性分析
tags:
- model collapse
- interactive learning
- directed graph
- synthetic data
- statistical inference
- theoretical guarantee
one_liner: 用有向图建模多模型交互，给出避免模型崩溃的图拓扑充要条件及有限样本保证
practical_value: '- 多模型协同训练（如多智能体、GAN、互蒸馏）时，可借鉴有向图刻画信息流，识别会导致崩溃的循环依赖或吸收结构，主动打断有害反馈回路。

  - 在推荐系统中用合成数据（如负样本生成、数据增强）时，可通过限制模型交互次数或引入新鲜真实数据比例，防止性能退化。

  - 对于多智能体强化学习中的自博弈，可基于交互图设计经验回放池的采样策略，避免分布塌陷。

  - 生成式推荐中若多个模型相互提供知识，可构建类似拓扑并监控误差传播，设定安全更新频率阈值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：生成式AI普及使模型不仅从真实数据学习，也从其他模型产生的合成数据学习，导致多模型交互训练环境。这种互动可能引发模型崩溃（性能逐代退化），但已有研究只考虑单模型自循环，无法刻画一般多模型交互场景。

**方法**：提出用有向图形式化模型间的交互结构，节点代表模型，边代表数据流动。每个模型接收邻居的输出及真实数据作为训练集，迭代更新参数。在一般交互图下推导模型参数估计的稳态误差，并分析其收敛/发散行为，给出模型崩溃（误差发散）的充要条件：条件与图的邻接矩阵谱半径严格小于1相关，本质要求交互结构不具备导致误差放大的正反馈回路。

**结果**：在线性回归设定下，得到有限样本的精确误差界限和崩溃阈值；在一般M估计量框架下建立渐近理论。数值实验验证了不同图拓扑（完全图、环、星形等）对崩溃快慢的影响，与理论一致。
