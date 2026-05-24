---
title: 'MotiMotion: Motion-Controlled Video Generation with Visual Reasoning'
title_zh: MotiMotion：基于视觉推理的运动控制视频生成
authors:
- Lee Hsin-Ying
- Hanwen Jiang
- Yiqun Mei
- Jing Shi
- Ming-Hsuan Yang
- Zhixin Shu
affiliations:
- University of California, Merced
- Adobe Research
arxiv_id: '2605.22818'
url: https://arxiv.org/abs/2605.22818
pdf_url: https://arxiv.org/pdf/2605.22818
published: '2026-05-21'
collected: '2026-05-24'
category: Reasoning
direction: 视觉推理驱动的运动控制视频生成
tags:
- Motion-Controlled Video Generation
- Visual Reasoning
- Causal Interaction
- Training-Free VLM
- Confidence-Aware Control
- MotiBench
one_liner: 将运动控制重新定义为推理-生成问题，利用免训练VLM预测因果连带的二次运动并引入置信度感知控制来提升自然性。
practical_value: '- **对商品视频生成**：可借鉴利用预训练VLM对稀疏的产品交互指令（如“开箱”“倾倒液体”）进行推理，自动补全液体飞溅、包装形变等二次运动，生成更符合物理常识的营销视频，减少逐帧精细轨迹的人工设计。

  - **Agent规划中的置信度调控**：将置信度感知的控制策略迁移到多智能体协作中，当规划子任务置信度低时由模型先验知识自主修正，在高置信步骤严格遵循指令，提升整体鲁棒性和任务成功率。

  - **免训练推理器的快速集成**：该方法不微调VLM，可快速适配电商多模态场景（如智能客服对复杂请求的意图推理）而不引入模型漂移，且推理成本低。

  - **构建交互基准的评测思维**：在推荐系统中可借鉴构建聚焦因果合理性的评测集（如推荐理由是否含因果矛盾），配合VLM自动化评估，减少人工评估成本。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有图像到视频的运动控制模型刚性遵循用户提供的稀疏、不精确且因果不完备的轨迹，导致生成的交互场景不合物理常识（如碰撞未产生二次位移、工具使用无因果链）。为生成自然、符合世界知识的动态，需要将运动控制升级为因果推理驱动的生成。

**方法**：提出MotiMotion框架，将运动控制重构为“先推理后生成”。核心创新：（1）引入一个训练免的视觉-语言推理器（基于预训练VLM），对用户输入的主轨迹进行图像空间坐标细化，并凭空预测出合理的二次运动（如足球撞击砖块后砖块移动、液体倒入杯子时液面上升）；（2）设计置信度感知控制机制，根据VLM输出的置信度自动调节生成过程中的引导强度——对高置信规划严格遵循，低置信时允许模型依赖内部生成先验修正伪影。该推理器无需针对视频生成训练，具备零样本推理能力。

**结果**：构建了专注于运动触发新事件的交互中心基准MotimBench，涵盖碰撞、约束变化、流体、工具机制等场景。基于VLM评估和人工偏好研究，MotiMotion相比以往方法显著提升物体行为和交互的合理性，生成的视频更符合常识和物理规律，且消融实验验证了推理器与置信度控制各自的关键贡献。
