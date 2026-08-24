---
title: Adapting Knowledge Graphs for Behavior Denoising in Sequential Recommendation
title_zh: 在序列推荐中适配知识图谱进行行为去噪
authors:
- Zichun Jin
- Zihan Zhou
- Yinan Liu
- Bin Wang
- Xiaochun Yang
affiliations:
- Northeastern University, Shenyang, China
arxiv_id: '2608.21243'
url: https://arxiv.org/abs/2608.21243
pdf_url: https://arxiv.org/pdf/2608.21243
published: '2026-08-21'
collected: '2026-08-24'
category: RecSys
direction: 知识图谱校准的行为去噪 · 序列推荐
tags:
- Knowledge Graph
- Sequential Recommendation
- Behavior Denoising
- Structural Matching
- Sample Weighting
- Offline Calibration
one_liner: 用结构化匹配的 KG 证据离线校准样本保留系数，对历史与目标加权去噪，不改动推理模型
practical_value: '- 电商/推荐系统常有商品知识图谱，但直接引入 GNN 会增加推理成本；AdaptedKG 的范式是离线用 KG 为每个训练样本算好保留系数，训练时只做加权，backbone
  和推理流程完全不变，非常适合作为现有序列模型或去噪模型的插件。

  - 结构匹配采样的去偏思路可以直接复用：对交互项按 popularity、KG degree、linkage status 分层匹配构造背景和参考集，再比较路径覆盖度/支持度，避免高流行度或高连接度
  item 天然获得高置信度。

  - 目标 loss 重加权公式 `r_T = min(1, 2Q(...))` 简单实用：当候选 item 的 KG 支持度低于匹配参考中位数时降低其训练权重，可在电商
  CTR/CVR 训练中抑制不可靠点击或误触样本。

  - 方法对 SASRec、STEAM、BirDRec、SSDRec 四个 backbone 均有提升，说明这种外部 KG 校准信号与日志内部去噪机制互补，可以作为统一的上游样本置信度模块接入不同推荐模型。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
序列推荐依赖用户历史交互，但真实日志混合长期偏好、短期需求、探索性点击和偶然行为，并非每次交互都同等可靠。现有行为去噪方法主要依据共现、顺序或模型预测等日志内部信号，缺少显式的 item 间关系证据。知识图谱可以提供类型化关系，但 raw KG 连通性受 item 流行度、KG 度数、覆盖不均和共享实体影响，直接使用会产生偏差。

**方法关键点**
AdaptedKG 通过两个顺序执行的结构化匹配阶段，把全局 KG 连接转化为单个训练样本的保留系数，且不把 KG 表示注入推荐模型：
- **局部 KG 适配（matched null）**：对当前上下文按 popularity、KG degree、linkage status 匹配替换 item，构造结构相似的背景上下文；保留并加权在当前上下文中显著高于背景的 two-hop 路径，形成样本专属局部 KG 视图。
- **支持度校准（matched reference）**：对候选 item 匹配结构相似的参考 item，计算其在该局部视图中的路径支持度 `S_K`，再通过参考分布百分位得到 retention coefficient `R = min(1, 2Q)`。
- 历史 embedding 乘 `r_H`，目标 loss 乘 `r_T` 进行加权；所有样本系数离线计算，训练时 detach，推理不需要 KG 访问。若无法构造匹配集或路径为空，则回退为 `R=1`。

**关键实验**
在 Steam Games（25,389 用户、4,089 item、328,278 交互、462,016 KG triples）上验证。AdaptedKG 增强 SASRec、STEAM、BirDRec、SSDRec 四个 backbone，所有指标均提升：例如 SASRec 的 H@5 从 72.0→85.9，N@5 从 45.3→56.5；STEAM 的 H@5 从 85.1→96.2。消融显示去局部适配降幅最大，matched null 和 matched reference 均有贡献。校准实验表明 matched reference 将 retention 与 KG degree 的相关性从 0.286 降到 0.057，与 popularity 的相关性从 0.200 降到 0.068。

**最值得记住的一句话**
用 KG 判断交互可靠性时，不能只看路径连通性，必须与结构相似的背景上下文和参考 item 比较，才能得到去偏的置信度信号。
