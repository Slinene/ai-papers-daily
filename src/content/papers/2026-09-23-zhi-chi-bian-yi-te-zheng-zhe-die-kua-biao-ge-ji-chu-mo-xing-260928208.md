---
title: 'Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular
  Foundation Models'
title_zh: 支持编译特征折叠：跨表格基础模型以更低内存获取更多证据
authors:
- Tian Zhou
- Beverly Jin
- Xue Wang
- Linxiao Yang
- Wenwei Wang
- Bingqing Peng
- Mengni Ye
- Jinjie Gu
- Liang Sun
affiliations:
- Ant Group
- Independent Researcher
arxiv_id: '2609.28208'
url: https://arxiv.org/abs/2609.28208
pdf_url: https://arxiv.org/pdf/2609.28208
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 表格基础模型 · 特征折叠推理优化
tags:
- SCFF
- tabular foundation models
- feature folding
- memory-efficient inference
- training-free inference
one_liner: 训练免推理框架 SCFF 将宽表二次特征交互转为线性宽度工作，内存降低且精度提升
practical_value: '- 面对电商/广告场景的高基数特征宽表（用户/商品/上下文特征可达数千列），可借鉴 SCFF 的「support-ranked
  + bounded leaves」：先按特征对任务的支持度排序，再分批送入同一冻结编码器，避免全量列成对交叉带来的 Θ(TD²) 显存峰值；线上推理可把峰值显存压到可部署边界，同时保留更多证据，而不是做
  hard 特征选择。

  - 将「节省的显存预算重新投回特征证据」用于特征裁剪或特征工程：先设定峰值显存上限，按 support 排序动态保留更多高支持特征，能比固定宽度单批获得明显精度提升；适合需要长期维护且不便重训的大表模型。

  - 训练免、不改骨干的合并推理模式对业务友好：冻结的大规模表格/多模态模型升级时，只改 inference routing 和 message merging，不需要重训或新增参数，降低工程风险；可作为线上
  AB 的轻量优化。

  - 有界 working set 和 single contextual prediction 的做法可用于 serverless/批推理：避免 ensemble
  多次预测，减少 QPS 成本，同时用 merging 保证单次上下文预测质量。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：表格基础模型（Tabular Foundation Models）在宽表上做 in-context learning 时，特征编码器先对每行 D 列做 pairwise mixing，交互成本随列数二次增长 Θ(TD²)。传统特征选择省内存但丢弃证据，形成特征侧缩放困境。

**方法关键点**：SCFF 是 training-free 推理框架，不改冻结骨干。它将 support-ranked 特征通过有界 leaf 路由进原生特征编码器，对残差 evidence 做 support-check，随后把多路编码消息合并，再做单次 contextual prediction。核心是把二次特征交互工作转为线性宽度工作，并用有界局部 working set 控制峰值内存；不集成预测，也不训练新参数。

**关键结果**：在 AMLB-29、TabZilla、TabArena 的 18 个 wide-table 切片上，SCFF 对 6 个被评估骨干的 dataset-macro accuracy 和 NLL 均有改善。匹配宽度比较在 locked folds 上保持有利的 95% dataset-bootstrap intervals，相对误差最多降 26.1%。中位配对 GPU-memory 节省 2.09–2.36×，最大峰值比达 34.3×。在峰值内存上限下，SCFF 用节省的预算保留更多 support-selected evidence，在 TabICLv2 与 TabPFN-3 的 wide-Core 上比最宽可行单 leaf 分别高 4.06 和 3.72 点。
