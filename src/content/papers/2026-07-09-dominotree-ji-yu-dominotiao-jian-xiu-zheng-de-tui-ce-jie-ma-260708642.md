---
title: 'DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative
  Decoding'
title_zh: DominoTree：基于Domino条件修正的推测解码树形起草
authors:
- Saw S. Lin
- Jyh-Shing Roger Jang
affiliations:
- National Taiwan University
arxiv_id: '2607.08642'
url: https://arxiv.org/abs/2607.08642
pdf_url: https://arxiv.org/pdf/2607.08642
published: '2026-07-09'
collected: '2026-07-10'
category: Other
direction: 推测解码 · 条件树起草
tags:
- speculative decoding
- draft tree
- Domino
- conditional scoring
- GPU-native builder
- training-free
one_liner: 利用Domino的GRU路径依赖校正构建非因子化草稿树，在Qwen3-4B上平均加速达4.81倍，接受长度最高10.7 tokens
practical_value: '- 推测解码中的树形搜索思想可迁移至推荐/Agent的候选生成：当评分函数依赖于已选序列（如用户行为路径）时，可借鉴DominoTree的条件堆展开方式，用轻量级修正网络（GRU）替代重跑完整encoder，降低分支成本。

  - 将per-node昂贵的全词表投影限制到top-M候选（候选限制）是工程化关键技巧，在电商搜索的语义ID生成树或推荐多轮交互中，可类似使用预筛选缩小搜索空间。

  - GPU-native builder（CUDA graph捕获与回放）展示了如何在不改变算法正确性的前提下，消除Python kernel launch开销，对需要频繁调用小算子的推理服务有直接参考价值。

  - CondAdaptive的失败教训表明：若草稿模型的路径概率与目标模型接受率校准不当，自适应预算规则会退化为固定预算，提示我们在做动态裁剪时需验证概率估计的准确性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
推测解码通过草稿模型生成多个候选token，再由目标模型并行验证来加速LLM推理。块扩散草稿器（如DFlash）能一次并行产出整个块，但仅建模边缘分布，忽略token间的条件依赖；Domino引入GRU序列修正，使每个位置的logits依赖已采样路径，但仍只生成单条链，未能利用树形验证提升接受长度。DDTree等树方法要求分布因子化，无法直接应用于Domino的条件修正。本文填补了这一空缺。

**方法关键点**  
- 利用Domino的GRU修正头构造**条件评分的最佳优先堆**：每个树节点的子节点评分需重算路径依赖的修正logits，而非共享边缘分布。  
- **候选限制**：将每个节点的修正投影限制在边缘top-M词汇（M=64），大幅减少每节点FLOPs，使条件树构建可行。  
- **GPU原生构建器**：将per-node修正算子封装为CUDA graph，消除Python启动开销，在位等价于Python实现的前提下，将构建时间从3.67ms降至2.31ms。  
- **CondAdaptive（负结果）**：尝试将CaDDTree的自适应预算规则迁移到条件树，但因GRU修正概率过度自信，规则退化为固定预算16，未能获得增益。

**关键实验结果**  
- 在Qwen3-4B的8个基准（数学、代码、对话）上，DominoTree平均加速比4.81倍，平均接受长度7.98，在所有温度下均高于DFlash/DDTree/CaDDTree/Domino。  
- 对比DDTree，T=0时整体吞吐提高+7.67%，T=0.5时+5.18%，T=1时+2.55%（成对bootstrap 95% CI），并超越其自身底层的Domino链式解码器9-10%。  
- 消融实验表明，在相同预算和树结构下，仅将评分函数从边缘改为条件即带来+9.2%的整体吞吐提升。
