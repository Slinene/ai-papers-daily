---
title: Reflection-aware Generative Novel View Synthesis
title_zh: 反射感知的生成式新视角合成
authors:
- GeonU Kim
- Shin Dong-Yeon
- Tae-Hyun Oh
affiliations:
- KAIST
arxiv_id: '2609.05382'
url: https://arxiv.org/abs/2609.05382
pdf_url: https://arxiv.org/pdf/2609.05382
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 生成式NVS · 反射几何虚拟视图
tags:
- Generative NVS
- Mirror Reflection
- Multi-view Diffusion
- Training-free
- Virtual View
- Attention
one_liner: 提出免训练反射感知多视图扩散方法，将镜中影像视为互补视图实现镜面场景一致新视角生成
practical_value: '- 若业务涉及商品 3D/多视图生成（如家具、镜面或反光商品），可借鉴“虚拟视角 + 注意力门控”思路，对镜面/反射面显式建模，在不微调现有多视图扩散模型的情况下提升反射一致性。

  - Ref-GeNVS 的 Mirror-gated attention 与 Reflection injection 两阶段注入反射关系，提供了一种 training-free
  的条件控制范式：利用几何先验（镜像平面、虚拟相机）引导生成，可迁移到其他需要物理约束的生成任务。

  - 对 AI 生成商品创意/短视频，反射面常导致脏图、leakage，可尝试在生成前检测镜面并构造虚拟相机轨迹，作为 layout/pose 条件喂给扩散模型，减少后期修图成本。

  - 学术贡献为主，与搜索/推荐/Agent 直接耦合低，但虚拟视图几何增强与 training-free adapters 思想可复用到多模态商品理解/生成 pipeline。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有多视图扩散模型在含镜面场景中常将镜面当普通平面，导致反射内容错乱、漏出伪影，无法利用镜中可见区域。

**方法关键点**：将镜中影像视为两个互补视图。先从输入估计镜面平面，将相机位姿关于镜面反射生成虚拟视图；基于该虚拟视图，提出两阶段生成：Mirror-gated attention 与 Reflection injection，显式利用反射关系进入多视图扩散模型。无需微调，继承基础模型泛化能力。

**关键结果**：在合成与真实含镜场景上优于近期生成式 NVS 方法（如 FlexWorld、SEVA），生成反射一致、上下文连贯的新视角，并能揭示仅通过镜子可见的场景结构。
