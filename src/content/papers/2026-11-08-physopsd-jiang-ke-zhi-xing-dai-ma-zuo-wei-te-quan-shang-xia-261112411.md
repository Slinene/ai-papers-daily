---
title: 'PhysOPSD: Code as Privilege for Physically Plausible Video Generation'
title_zh: PhysOPSD：将可执行代码作为特权上下文提升视频生成物理合理性
authors:
- Harold Haodong Chen
- Rui Peng
- Lingteng Qiu
- Kejie Qiu
- Chao Xu
- Zilong Dong
affiliations:
- HKUST
- Alibaba Token Hub, Alibaba Group
arxiv_id: '2611.12411'
url: https://arxiv.org/abs/2611.12411
pdf_url: https://arxiv.org/pdf/2611.12411
published: '2026-11-08'
collected: '2026-11-12'
category: Multimodal
direction: 多模态视频生成 · 后训练特权蒸馏
tags:
- PhysOPSD
- OPSD
- Video Generation
- Privileged Context
- Physical Plausibility
- Post-training
one_liner: 以可执行代码作为特权物理上下文，结合 OPSD 在仅 3K 样本下显著提升视频物理合理性
practical_value: '- 生成商品动态展示/广告短视频时，物理合理性直接影响真实感。可将材质、质量、碰撞、力等物理属性编码为可执行代码或仿真参数，作为生成条件，比纯文本提示更可控，适合按卖点做参数化
  A/B 测试。

  - OPSD 的 on-policy rollout + 稠密蒸馏纠错信号可迁移到创意/文案生成后训练：避免 SFT 离线样本与在线生成分布不匹配，尤其适合需要强化真实性、合规性、点击感等可评估维度的场景。

  - dual-level physical privilege + intermediate bottleneck 可以理解为“先压缩再注入”：在商品视频生成中，把
  3D 结构/物理参数映射到低维 latent 或语义 token 再融合，能减少冗余、提升训练稳定。

  - shared rollout noise + controlled variations 可用于干净地剥离因果因子：在创意生成评估中，固定随机噪声，仅改变关键参数，能更准确地归因某个因素对生成结果或业务指标的影响。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前视频生成模型视觉质量高，但物理动态与交互仍易出错。针对性后训练必要，但 SFT 存在离线状态不匹配，RL 受稀疏、难定义物理奖励限制。OPSD 通过 on-policy rollout 与稠密纠错反馈缓解该问题，核心难点转向设计有效特权上下文。文本提示偏声明式，参考视频将物理规律与外观纠缠且不可参数化。

**方法关键点**：PhysOPSD 用可执行代码作为特权物理上下文，PhysOPSD-Engine 将真实物理场景转为可验证仿真程序；设计 dual-level physical privilege，通过 intermediate bottleneck 桥接信息差距；在 shared rollout noise 下引入 controlled physical variations，暴露因果动态偏移。

**结果**：在多种 backbone 上以仅 3K 样本提升物理合理性，超过 SFT 与 RL baseline，同时保持通用视频生成质量。
