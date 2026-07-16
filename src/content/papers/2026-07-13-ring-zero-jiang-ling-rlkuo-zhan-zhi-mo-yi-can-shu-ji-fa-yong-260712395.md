---
title: 'Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning'
title_zh: Ring-Zero：将零RL扩展至万亿参数，激发涌现推理
authors:
- Xinyu Tang
- Gangqiang Cao
- Yurou Liu
- Yuliang Zhan
- Xiaochong Lan
- Yifan Li
- Yuchen Yan
- Han Peng
- Zican Dong
- Zhenduo Zhang
affiliations:
- Renmin University of China
- Ant Group
- Tsinghua University
- Zhejiang University
arxiv_id: '2607.12395'
url: https://arxiv.org/abs/2607.12395
pdf_url: https://arxiv.org/pdf/2607.12395
published: '2026-07-13'
collected: '2026-07-16'
category: Reasoning
direction: RL训练大规模LLM涌现推理
tags:
- Zero RL
- Emergent Reasoning
- Scaling Law
- CoT
- Training Pipeline
- 1T Parameters
one_liner: 通过算法与系统优化，将Zero RL稳定扩展到1T参数，发现涌现的高级推理行为。
practical_value: '- 训练稳定性技巧：裁剪重要性采样、训练-推理比例校正、混合精度控制等trick可直接用于业务中Agent/LLM的RL微调，防止训练崩溃。

  - 涌现行为无需手工启发式：观察到自我验证、结构化格式等自发行为，说明在推荐/搜索的CoT提示工程中，可减少人工设计，依赖模型自身涌现。

  - CoT质量评估框架：从可理解性、可复现性、效率三维度评估推理轨迹，可用于评估商品推荐解释、搜索意图理解的中间过程。

  - 大规模RL的样本效率：1T参数下样本效率显著提升，提示对资源受限的场景，可优先采用更大的预训练模型进行少量RL微调。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Zero RL利用可验证奖励训练模型进行思维链推理，但现有研究受限于小模型，未能探索大规模下的训练动态和涌现能力。直接扩展会遇到可读性差、token冗余、推理深度不足等问题。

**方法关键点**：
- 提出稳定高效的训练pipeline，集成算法与系统优化：裁剪重要性采样、训练-推理比例校正、混合精度控制。
- 在万亿参数模型（Ring-2.5-1T）上进行数学推理训练。

**关键结果**：
- 验证“苦涩教训”：扩展至1T参数显著提升样本效率和性能上限；训练过程经历“发现”和“锐化”两个阶段。
- 模型自发涌现拟人化、结构化格式、自我验证、并行推理、上下文焦虑等高级认知行为，使手工启发式变得多余。
- 在7个数学基准上取得有竞争力的表现。
- 提出CoT质量评估框架（可理解性、可复现性、效率），模型在生成结构化、简洁推理轨迹方面优势明显。
