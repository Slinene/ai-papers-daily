---
title: 'Attention Dispersion in Dynamic Graph Transformers: Diagnosis and a Transferable
  Fix'
title_zh: 动态图Transformer注意力分散诊断与可迁移修复
authors:
- Jinhao Zhang
- Kangfei Zhao
- Qiuhao Zeng
- Long-Kai Huang
affiliations:
- Beijing Institute of Technology
- University of Toronto
- Hong Kong Baptist University
arxiv_id: '2605.16112'
url: https://arxiv.org/abs/2605.16112
pdf_url: https://arxiv.org/pdf/2605.16112
published: '2026-05-15'
collected: '2026-05-18'
category: RecSys
direction: 动态图Transformer注意力分布偏移诊断与修复
tags:
- Attention Dispersion
- Differential Attention
- Dynamic Graph Transformers
- Temporal Distribution Shift
- Continuous-Time Dynamic Graphs
- Graph Learning
one_liner: 诊断出动态图Transformer在时序偏移下注意力分散，提出差分注意力修复，简单有效且可迁移至多种模型
practical_value: '- 在电商推荐、社交推荐等动态图场景中，当面临时序分布偏移（如大促、季节变化）时，将标准 self-attention 替换为
  differential attention，可抑制共模噪声，突出关键历史交互节点，提升预测鲁棒性。

  - 工程实现成本低：仅需修改注意力计算（如对注意力分数做差分处理，抑制均值共模分量），可作为即插即用的 trick 快速集成到现有 Transformer 推荐模型中。

  - 可利用注意力熵等指标监测模型是否出现注意力分散，作为数据 drifted 或模型失效的诊断工具，及时触发修复。

  - 对于基于会话的推荐系统，可借鉴 DiffDyG 架构，在保持标准输入编码的同时，采用差分注意力增强对关键行为节点的聚焦，尤其适合长序列建模。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：连续时间动态图（CTDG）Transformer 在时序分布偏移下性能受限。通过对比关键邻居与随机邻居的消融实验，发现预测依赖少数关键节点，但现有 Transformer 在时序偏移时注意力对比度下降，产生过度分散的注意力分布，即使关键节点存在也无法聚焦。

**方法**：提出以差分注意力（differential attention）替代标准注意力。差分注意力通过抑制所有 token 共享的共模注意力分量，放大差异化 signal，迫使模型聚焦于更具预测性的 token。该修复简洁通用，可无缝集成到多种 CTDG Transformer 基线中。在此基础上，构建了 DiffDyG，结合标准输入编码与差分注意力，形成参考实现。

**结果**：在三个代表性基准模型（DyGFormer 等）上，差分注意力一致提升性能，且增益集中于高偏移数据集。注意力测量证实机制有效：注意力熵降低，关键节点注意力质量上升。DiffDyG 在 9 个基准、三种负采样协议下取得 SOTA，尤其在偏移最大的数据集上提升显著。
