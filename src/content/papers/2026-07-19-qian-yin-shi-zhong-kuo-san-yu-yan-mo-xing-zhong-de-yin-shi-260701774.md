---
title: 'Subliminal Clocks: Latent Time Modelling in Diffusion Language Models'
title_zh: 潜隐时钟：扩散语言模型中的隐式时间建模
authors:
- Maximo Eduardo Rulli
- Thomas Vaitses Fontanari
- Simone Petruzzi
- Federico Alvetreti
- Giorgio Strano
- Donato Crisostomi
- Giorgos Nikolaou
- Tommaso Mencattini
- Andrea Santilli
- Emanuele Rodolà
affiliations:
- Sapienza University of Rome
- EPFL
- NVIDIA
arxiv_id: '2607.01774'
url: https://arxiv.org/abs/2607.01774
pdf_url: https://arxiv.org/pdf/2607.01774
published: '2026-07-19'
collected: '2026-07-25'
category: Other
direction: 扩散语言模型的可解释性分析
tags:
- Diffusion Language Models
- Latent Time Representation
- Probing
- Steering
- Interpretability
- Activation Geometry
one_liner: 发现无显式时间条件的扩散语言模型内部编码了隐式去噪时间步，可通过探针提取和方向操控来调制模型行为
practical_value: '- 对于使用扩散模型生成推荐内容（如GenRec）的场景，可借鉴隐式时间步操控来**动态调节生成的确定性与多样性**：沿时间步子空间方向移动可改变模型置信度，实现从保守推荐到探索式推荐的切换。

  - 工程实现上，可在推理时通过**简单的激活向量加法**（无须重新训练）来控制生成进度，用于A/B测试或个性化生成风格。

  - 探针方法可用于**监控线上模型的去噪状态**，例如检测异常生成或提前终止去噪步骤以节省计算。

  - 若将扩散步骤与推荐质量关联，可利用隐式时间步表征设计**自适应调度策略**，在低延迟场景下跳过部分去噪步骤。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型（DLMs）不像标准扩散模型那样显式输入时间步，其内部是否自发形成去噪进度的表征？这一表征如何影响下游生成？

**方法关键点**：
- 训练线性探针，从DLM各层残差流中解码扩散时间步，验证其存在性。
- 识别与推断时间步相关的低维子空间，通过**激活导向（steering）**沿该方向移动隐藏状态，人为加快或减慢模型的“去噪进度感知”。
- 分析该时间表征在激活空间中的几何结构，揭示其可解释的低维流形。

**关键结果数字**：
- 探针可高精度恢复时间步（文中未给出具体数值，但强调可靠提取），且跨层一致。
- 操控时间步子空间可**系统性改变模型输出置信度和熵**：模拟更早/更晚的去噪阶段。
- 时间表征呈现结构化几何：不同层的时间轴近似线性排列，且与模型对 token 的不确定性相关。
