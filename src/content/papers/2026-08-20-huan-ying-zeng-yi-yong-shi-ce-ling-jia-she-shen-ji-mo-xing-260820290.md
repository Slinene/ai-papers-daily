---
title: 'Phantom Gains: Auditing Self-Improvement Against a Measured Null'
title_zh: 幻影增益：用实测零假设审计模型自提升
authors:
- Cheng Xu
- Nan Yan
- Liming Chen
- M-Tahar Kechadi
affiliations:
- University College Dublin
- Georgia Institute of Technology
- Dalian University of Technology
arxiv_id: '2608.20290'
url: https://arxiv.org/abs/2608.20290
pdf_url: https://arxiv.org/pdf/2608.20290
published: '2026-08-20'
collected: '2026-08-22'
category: Eval
direction: LLM 自提升评估审计
tags:
- self-improvement
- measurement
- null hypothesis
- LoRA
- evaluation
- statistical testing
one_liner: 审计 Qwen3-8B 的 LoRA 自训练，发现 7 类测量失效会反转结论，需为每个统计量单独测量零假设
practical_value: '- 在电商/推荐模型迭代中，从只看平均 AUC/转化率转向 query/item 级别的“得与失”时，必须先建立实测零假设：同管线推一个
  frozen control，否则推理 batching、贪心解码等工程差异会制造伪提升。

  - 对外部蒸馏、自训练等“提升长尾/困难场景”的宣称要小心：需要用回归检验整体增益是否掩盖不对称性，避免把大增益的副产品误判为针对长尾的能力获取。

  - 如果业务中做 LLM 自训练（如从用户反馈或生成数据中蒸馏），保留 baseline replicates 并用精确检验 + FDR 控制，能零成本识别伪获取；不要用单一
  greedy decode 或扩展统计直接下结论。

  - 工程实现中固定推理 batch 或记录 batch 配置，否则不同 batch 会让未训练模型出现虚假能力变化，干扰离线评估。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：自提升评估越来越多关注逐题/逐样本的得与失，而不仅是平均准确率。但这类差值由两个噪声估计相减得到，容易受测量伪影影响，导致假阳性结论。

方法：作者对 Qwen3-8B 进行三轮 rank-32 LoRA 自训练，同时使用一个冻结控制模型通过完全相同的推理与评估管线，审计七类测量失效。他们用基线重复构建每问题精确检验，在 false-discovery-rate (FDR) 控制下对比 pooled baseline；并在多臂阶梯设计中匹配流、数据量和评估方式，比较外部蒸馏与三种自训练。

关键结果：单一贪心解码账本会在未训练模型上制造能力变化，主要是推理 batching 造成的伪影；扩展统计（区分获取与锐化）给同一未训练模型分配了 0.280 的获取率。自然阈值修复无法复现，估计其零假设非零。新提出的精确检验在任意保留重复上检测不到任何信号，且对多重检验规则、错误率和池大小不敏感。应用该审计发现外部蒸馏改善了基础模型很少达到的问题，而三种自训练没有；回归分析拒绝这种不对称性只是蒸馏更大整体增益的副产品（p<1e-8）。在基础模型从未达到的更小子集上证据不足，同时自训练破坏已解决样本的速率远高于实测底层。结论：transition-level 评估需要为每个统计量单独测量零假设，这些零假设可利用多臂研究已有的基线重复构建，但现有样本量往往不足。
