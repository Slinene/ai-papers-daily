---
title: 'OpenCoF: Learning to Reason Through Video Generation'
title_zh: OpenCoF：通过视频生成学习链式帧推理
authors:
- Xinyan Chen
- Ziyu Guo
- Renrui Zhang
- Dongzhi Jiang
- Hongsheng Li
affiliations:
- ByteDance Seed
- CUHK MMLab
- CUHK IMIXR
arxiv_id: '2607.08763'
url: https://arxiv.org/abs/2607.08763
pdf_url: https://arxiv.org/pdf/2607.08763
published: '2026-07-08'
collected: '2026-07-11'
category: Reasoning
direction: Chain-of-Frame 推理
tags:
- Video Generation
- Chain-of-Frame
- Reasoning
- Multimodal
- Fine-tuning
- Reasoning Tokens
one_liner: 提出 Chain-of-Frame 推理范式，通过多样化时序监督和显式推理 token 增强视频生成模型的推理能力
practical_value: '- 该工作主要面向视频生成与多模态推理，与电商/推荐系统的直接关联较弱，但其中 **Chain-of-Frame 的时序展开思想**
  可启发序列推荐中的多步状态建模：将用户行为序列或物品状态变化视为“推理帧”，利用视频生成模型进行未来交互的预测。

  - **显式推理 token 机制**（视觉 token 捕获低级线索，文本 token 编码高级语义）在设计多模态推荐模型时可借鉴：将商品图像、描述等异构信息分离处理，再融合决策，避免特征纠缠。

  - 论文强调的 **多样化时序监督** 对推荐系统同样有启示：在训练序列模型时，增加不同粒度和任务的时序预测目标（如下一步行为、长期兴趣）可提升模型对时序依赖的理解。

  - 整体上，该方法属于基础研究，工程落地成本高，业务可借鉴点有限，但可关注后续是否向智能体环境模拟、A/B 测试方案生成等方向拓展。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频生成模型缺乏针对 Chain-of-Frame (CoF) 推理的多样化监督和专门设计，而 CoF 将推理步骤展开为时间相连的帧，比静态 Chain-of-Thought 更具动态表达力，但直接套用通用视频生成模型效果受限。

**方法**：提出 OpenCoF 框架，包含两个核心组件：
1. **OpenCoF-17K 数据集**：覆盖 11 类推理任务（如物理推理、因果推断），提供多样化时序监督；
2. **Wan-CoF 模型**：基于 Wan2.2-I2V-A14B 微调，注入 CoF 推理能力。
进一步设计 **视觉与文本推理 token**，其中视觉 token 负责捕获帧间低级视觉线索（如物体移动），文本 token 编码高级语义先验（如任务目标），二者协同进行时空推理。通过注意力分析和消融实验，探究 token 在不同网络深度、去噪步和时空维度上的作用模式。

**关键结果**：在四个视频推理基准上，Wan-CoF 显著超越基线；引入推理 token 后性能进一步提升，验证了显式组织中间推理状态的必要性。源码、数据、模型均已开源。
