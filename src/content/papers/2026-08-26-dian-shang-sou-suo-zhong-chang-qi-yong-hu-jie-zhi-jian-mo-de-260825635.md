---
title: 'DCEO: Direct Causal Effect Optimization for Long-Term User Value Modeling
  in E-commerce Search'
title_zh: 电商搜索中长期用户价值建模的直接因果效应优化
authors:
- Junzhao Zhang
- Tao Zhang
- Liren Yu
- Feiyi Dong
- Zhixuan Zhang
- Dan Ou
- Haihong Tang
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.25635'
url: https://arxiv.org/abs/2608.25635
pdf_url: https://arxiv.org/pdf/2608.25635
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 电商搜索 · 长期价值建模 · 因果优化
tags:
- long-term user value
- causal effect
- actor-critic
- multi-objective fusion
- e-commerce search
- ranking
one_liner: 用 actor-critic 直接优化代理指标对长期 GMV 的相对因果效应，学习个性化 item 级融合分数
practical_value: '- **用相对因果效应替代预测关联做跨粒度对齐**：不要只学「代理指标能预测长期目标」，而是学「代理指标上升时长期目标上升多少」。在业务里可以把
  critic 对干预前后的预测差作为训练信号，减少纯相关性代理带来的误导。

  - **actor 输出融合权重而非直接输出分数**：让 actor 从用户/请求特征生成多个上游预测分数的凸组合权重，既保留可解释性，又稳定优化。在线只部署
  actor，把学习到的代理分数作为新增项加入现有排序公式，原有权重不动，风险可控。

  - **用户级聚合要做曝光次数校准**：代理指标按用户聚合时，不同用户曝光量不同会带来混杂。固定参考曝光次数并用校准模型做归一，能更干净地刻画代理指标与长期目标的关系。

  - **加条件归一化排序损失作为正则**：因果效应损失非凸不稳定，可以加一个把代理指标和长期目标归一化到同一分布后的 pairwise ranking loss，提升训练稳定性，类似业务多目标融合里可以复用。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：工业电商搜索的终极目标是用户级长期价值（如 4 天累计 GMV），但排序是 item 级分数，存在粒度差距。现有多目标融合依赖人工设定的一组全局权重，个性化弱，且在线调参成本高。需要一个数据驱动的方法直接从用户级目标学习 item 级代理分数。

**方法关键点**：
- 定义 item 级代理分数由 actor 生成：actor 输入用户特征和请求特征，输出一组非负归一化权重，对上游预测分数（impr2click、click2pay、不同金额档位 GMV 等）做凸组合。
- 将代理分数按用户聚合为 \(P_u\)，并通过校准模型 \(g_\psi\) 校准到固定参考曝光次数 \(C=100\)，得到用户级代理指标，消除曝光量混杂。
- 用 critic \(h_\phi\) 估计给定代理指标下的终极目标 \(Y_u\)。训练 actor 时，冻结 critic，计算干预前后差异作为因果效应损失：\(L_{CE}=-\mathbb{E}[h(z,(1+\delta)P)-h(z,P)]\)，直接优化相对因果效应 RCE 的近似。
- 增加条件归一化排序损失 \(L_{CNR}\)：用模型估计均值和方差，把 \(P_u\) 和 \(Y_u\) 归一化到同一分布后做 pairwise ranking，作为稳定正则。
- 训练时联合优化 actor、critic、校准模型、归一化模型；在线只部署 actor，把代理分数作为新项加入原有多目标融合公式，原有权重和分数不变。

**关键结果**：
- 离线实验显示，用预测关联优化 RCE 仅 0.022，改用因果效应损失提升到 0.031，加上条件归一化排序损失后达到 0.053，相对提升 2.41 倍。
- 消融显示加入交易价值分档和转化漏斗等 17 个上游分数时 RCE 最高；仅用 impr2gmv 只有 0.027。
- 权重分析表明：目标为 4 天点击时 actor 几乎全部分配给 impr2click；目标为 4 天 GMV 时权重明显分散到 click2pay100/300/1000 等高价值分档，且目标窗口从 1 天到 4 天，impr2click 权重上升，体现对探索的鼓励。
- 41 天在线 A/B 测试中，DCEO 相对传统 GMV 代理提升 GMV +0.36%，点击 +0.36%，购买 +0.12%。

**最值得记住的一句话**：直接优化代理指标对终极目标的相对因果效应，而不是预测关联，才能学到真正对齐长期用户价值的 item 级排序信号。
