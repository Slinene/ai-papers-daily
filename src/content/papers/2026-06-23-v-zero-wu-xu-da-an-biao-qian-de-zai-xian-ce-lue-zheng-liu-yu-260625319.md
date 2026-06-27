---
title: 'V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence
  Gating for Fine-Grained Visual Reasoning'
title_zh: V-Zero：无需答案标签的在线策略蒸馏与对比证据门控细粒度视觉推理框架
authors:
- Haoxiang Sun
- Zhihang Yi
- Langxuan Deng
- Yuhao Zhou
- Peiqi Jia
- Jian Zhao
- Li Yuan
- Jiancheng Lv
- Tao Wang
affiliations:
- Sichuan University
- Xi'an Jiaotong University
- TeleAI of China Telecom
- Peking University
arxiv_id: '2606.25319'
url: https://arxiv.org/abs/2606.25319
pdf_url: https://arxiv.org/pdf/2606.25319
published: '2026-06-23'
collected: '2026-06-27'
category: Reasoning
direction: 视觉推理 · 无监督蒸馏
tags:
- On-Policy Distillation
- Contrastive Evidence Gating
- Visual Reasoning
- MLLM
- Answer-Label-Free
one_liner: 将在线策略蒸馏重新解释为负例无关的stop-gradient对齐，并提出对比证据门控解决轨迹级判别缺失，显著提升细粒度视觉推理效率
practical_value: '- **在线策略蒸馏（OPD）替代标注**：在商品图文理解、多模态推荐 Agent 中，可借鉴 OPD 让 MLLM 从自身生成的推理轨迹中学习，彻底摆脱人工标注答案标签的依赖，大幅降低标注成本。

  - **对比证据门控机制**：用问题相关的区域裁剪（正例）与无关区域（负例）构成视觉对比对，自动评估推理轨迹质量并门控 token 级蒸馏。可用于电商详情页细粒度问答、广告图文一致性校验等场景，提升模型对局部证据的利用能力。

  - **训练效率跃升**：V-Zero 比 SFT 方法快 5 倍以上，比 RL 基线快 10 倍以上，直接节省计算资源。在搜索推荐 Agent 的视觉子任务训练中，可优先考虑此类免探索、免标注的高效蒸馏方案。

  - **与 Agent 框架的集成**：方法天然适合 Agent 的多步推理，可将对比证据门控作为内部信号，指导 Agent 在搜索、推荐过程中更精准地聚焦可解释的视觉证据，并实现自我改进。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有细粒度视觉推理方法依赖强化学习的可验证奖励或大量标注推理链，成本高且探索效率低。作者发现在线策略蒸馏（OPD）能提供有效的 token 级校正，但缺少轨迹级判别能力，性能上限受限。

**方法**：提出 V-Zero 框架，完全无需文本答案标签。训练时为每个问题构造一个相关的区域裁剪正例和一个无关的视觉负例，然后利用学生模型采样推理轨迹，通过正/负视觉视图下的生成概率对比来评估轨迹质量，并以此设计**对比证据门控**，控制稠密 token 级蒸馏的强度。整个过程是负例无关的 stop-gradient 对齐，既保留 OPD 的 token 纠偏能力，又引入轨迹级判别信号。

**结果**：在多个细粒度视觉推理基准上，V-Zero 持续提升推理性能并保持强泛化能力。训练速度比有监督微调方法快 5 倍以上，比强化学习基线快 10 倍以上。
