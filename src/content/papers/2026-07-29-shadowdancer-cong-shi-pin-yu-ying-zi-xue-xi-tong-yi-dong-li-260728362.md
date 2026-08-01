---
title: 'ShadowDancer: Teaching Video World Models Any Action by Learning Unified Dynamics
  Representations from a Video and Its Shadow'
title_zh: ShadowDancer：从视频与影子学习统一动力学表征实现任意动作控制
authors:
- Jin Cao
- Zian Meng
- Kaipeng Zhang
affiliations:
- Alaya Lab
- Shanghai Innovation Institute
arxiv_id: '2607.28362'
url: https://arxiv.org/abs/2607.28362
pdf_url: https://arxiv.org/pdf/2607.28362
published: '2026-07-29'
collected: '2026-08-01'
category: Multimodal
direction: 视频世界模型 · 动作表征学习
tags:
- ShadowDancer
- World Model
- Action Representation
- Cross-Shadow Prediction
- Video Generation
- Dynamics Control
one_liner: 通过影子对与跨影子预测解耦外观与动作，使视频世界模型零样本复用任意演示动作。
practical_value: '- **解耦外观与行为的数据增强思路**：在电商/推荐中，用户行为序列（动作）常与内容表象（外观）纠缠。可借鉴“影子对”构造：对同一意图（如搜索同一品类）在不同
  UI 皮肤或不同设备下的交互对，训练模型剥离表面特征，得到更纯的意图表征，提升跨场景迁移能力。

  - **通过预测任务学习不变表征**：cross-shadow prediction 直接以预测配对样本为目标，隐式舍弃无关变化。推荐系统可构造类似预训练任务：给定同一用户在不同上下文下的行为序列片段，预测彼此，使模型聚焦于提取不变的用户潜在兴趣，减少
  noises 影响。

  - **无需标注的动作复用**：该方法将已有视频片段直接转化为可复用的控制信号，无需额外动作标签。对应到 Agent 或营销内容生成，可利用历史用户交互轨迹作为模板，直接在新内容上“重放”类似动线，快速生成个性化交互流程。

  - **长序列一致性控制**：block-causal 架构与统一动力学表征保证长期回放稳定。在生成式推荐（如生成购物路径）中，可借鉴该结构维持多步生成的逻辑连贯性，避免中间步骤崩塌。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：交互式视频世界模型难以精确表征多样化动作：松散的隐式编码让模型自行发挥，结构化的显式信号又难以获取且泛化差。演示视频虽能逐帧指定动态，但因外观耦合导致动作迁移失败。

**方法**：提出两大核心创新。(1) **影子对 (Shadow Pairs)**：构建重放相同动态但独立重新采样外观的视频对，通过 Shadow Library 大规模生成，使任一动态族都能以数据驱动方式变为可控。(2) **跨影子预测 (Cross-Shadow Prediction)**：从一对影子中学习统一的动力学表征 \(z_{1:T-1}\)——通过预测一个影子来自另一个影子，构造性地丢弃配对重采样部分，保留不变部分作为动作。该表征驱动一个 block-causal 世界模型，任意演示片段因此成为可复用动作资产，无需动作标签、运动估计或微调即可在新环境中回放。

**结果**：在人体动作、机器人操作、UE5 游戏等多类动态上，相比潜在动作和交互世界模型基线，动作迁移与长序列回放性能显著提升，盲评胜率平均达 86%。
