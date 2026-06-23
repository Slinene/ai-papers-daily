---
title: 'World Action Models: A Survey'
title_zh: 世界行动模型综述
authors:
- Qiuhong Shen
- Shihua Zhang
- Yue Liao
- Qi Li
- Zhenxiong Tan
- Shizun Wang
- Shuicheng Yan
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2606.20781'
url: https://arxiv.org/abs/2606.20781
pdf_url: https://arxiv.org/pdf/2606.20781
published: '2026-06-17'
collected: '2026-06-23'
category: Agent
direction: 具身预测行动模型设计空间
tags:
- World Models
- Video Generation
- Embodied AI
- Action Prediction
- Model-Based RL
- Survey
one_liner: 对具身预测-行动模型给出统一分类与设计权衡，强调“少预测未来、多聚焦控制”
practical_value: '- 构建推荐环境用户仿真器（世界模型）时，可借鉴“生成更少未来，只保留控制所需信息”的设计原则，用潜在状态预测替代完整行为序列生成，降低计算与数据成本。

  - 解耦预测基座与行动策略的设计模式可用于推荐 Agent：例如用轻量 Transformer 预测用户短期意图，将重计算留给策略决策，平衡延迟与丰富度。

  - 从交互性、因果性、持久性等维度评估世界模型，可迁移到推荐系统 A/B 测试前的离线模拟器质量检查，特别关注分布外鲁棒性。

  - 论文对视频生成 VS 潜在预测 VS 无生成推理的分支梳理，提示在搜索推荐 Agent 中也可根据场景（实时改价 vs 长期策略）选择不同程度的“未来预测”实现。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视频生成、世界模型与视觉-语言-动作策略快速交叉融合，概念边界模糊，亟需统一术语与设计空间。  
**方法**：定义世界行动模型（WAM）为“使预测未来直接服务于行动”的具身模型，并沿两条轴组织现有工作。一是按生成输出分类：完全渲染的未来帧、只在潜在空间预测未来、完全跳过视频生成的动作推理。二是按解剖结构分解：预测基座（视频/语言/多模态）、骨干网络、动作耦合方式（策略头、扩散条件等）、部署机制（离线训练 vs 在线规划）。在此框架下讨论交互性、因果性、持久性、物理合理性等关键属性，并剖析计算开销与标签成本间的权衡。  
**结果**：发现 WAM 并非简单“视频生成器+动作头”，而是设计者在表现丰富度与效率（内存、延迟、标注代价）间的权衡。趋势走向“少预测未来，多聚焦控制：只生成控制必需的信息，而非多余的视频感知细节。”
