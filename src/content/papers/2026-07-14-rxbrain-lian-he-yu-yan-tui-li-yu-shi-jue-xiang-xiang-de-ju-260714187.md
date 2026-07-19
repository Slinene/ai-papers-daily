---
title: 'RxBrain: Embodied Cognition Foundation Model with Joint Language-Visual Reasoning
  and Imagination'
title_zh: RxBrain：联合语言推理与视觉想象的具身认知基础模型
authors:
- Haotian Liang
- Mingkang Chen
- Yufei Huang
- Yuchun Guo
- Xiaomeng Zhu
- Xiangli Shi
- Kaixuan Wang
- Yunxuan Mao
- Weijie Zhou
- Ling Chen
affiliations:
- Tencent Robotics X Team
- Futian Laboratory
- Tencent Hy Team
arxiv_id: '2607.14187'
url: https://arxiv.org/abs/2607.14187
pdf_url: https://arxiv.org/pdf/2607.14187
published: '2026-07-14'
collected: '2026-07-19'
category: Agent
direction: 具身Agent联合语言-视觉规划
tags:
- embodied cognition
- multimodal planning
- visual imagination
- Mixture-of-Transformers
- robot action generation
- foundation model
one_liner: 将语言推理与视觉想象统一为一个规划序列，实现具身任务的耦合文本-视觉规划与执行
practical_value: '- **多模态规划范式可迁移**：将高层语言推理（任务分解、约束、时序逻辑）与视觉状态预测（子目标图像生成）融合成一个序列，这种“语言蓝图+视觉落地”的范式可借鉴到电商商品推荐文案生成中，先规划叙述逻辑再生成对应商品图，提升图文一致性。

  - **统一的多模态生成架构**：采用单模型支持语言、图像、视频的理解与生成，避免多模型拼接的累积误差。对于需要同时处理商品标题、详情图、视频的推荐系统，统一的
  Transformer 混合架构可简化流程。

  - **自动数据构造管线**：从视频自动分解规划步骤并对齐视觉状态，这种弱监督思路可启发我们利用用户行为序列（如点击→加购→购买）构建“推理-状态”训练数据，训练推荐模型进行因果推理或意图预测。

  - **零样本动作扩展**：模型在没有大规模动作数据预训练的前提下，仅通过语言和视觉规划直接泛化到连续机器人控制。这提示在多模态推荐中，若将动作空间也建模为序列的一部分，可能实现未见过动作的组合推荐。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：具身智能体需要将高层任务推理与物理状态连接，但现有方法要么侧重场景理解与文本决策（VLM），要么仅预测未来视觉状态（世界模型），缺乏耦合推理与视觉想象的统一规划。  
**方法**：提出 RxBrain，将具身规划表示为一个单一的多模态序列，其中语言提供抽象结构（任务分解、约束、时序、决策逻辑），视觉想象提供世界状态预测与子目标规划，将每一步规划关联到中间和最终物理状态。模型采用统一的 Mixture-of-Transformers 多模态架构，支持语言、图像、视频的理解与生成。训练数据通过自动管道构建：从具身视频中分解出规划步骤，并与视觉状态转换对齐，生成文本-视觉联合监督。并推出 RxBrain-Bench 评估联合规划能力。  
**结果**：RxBrain 在保持多模态理解和生成能力的同时，能产生耦合文本推理、世界状态预测和联合子目标规划的规划结果。进一步将模型扩展到连续机器人动作生成，在无需大规模动作数据预训练的条件下，在真实机器人上展现良好性能。
