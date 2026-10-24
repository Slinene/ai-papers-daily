---
title: 'Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for
  Diffusion Language Models'
title_zh: 不同任务不同去噪步：扩散语言模型的任务-时间感知量化
authors:
- Ofek Avivi
- Eliron Rahimi
- Avi Mendelson
- Chaim Baskin
affiliations:
- Technion – Israel Institute of Technology
- INSIGHT Lab, Ben-Gurion University of the Negev
arxiv_id: '2610.31198'
url: https://arxiv.org/abs/2610.31198
pdf_url: https://arxiv.org/pdf/2610.31198
published: '2026-10-21'
collected: '2026-10-24'
category: LLM
direction: 扩散语言模型 · 混合精度量化
tags:
- Diffusion Language Models
- Quantization
- Mixed-Precision
- Inference Optimization
- Temporal Sensitivity
one_liner: 发现扩散语言模型量化敏感性随任务与去噪步变化，提出无标签信号驱动的混合精度量化框架T2Quant
practical_value: '- 若部署扩散语言模型做生成式推荐/Agent文本生成，可对去噪过程不同时间步做混合精度量化，而非全程统一位宽：在任务敏感步分配更高精度，其他步降低精度，能在固定显存/算力预算下提升生成质量。

  - 采用无标签的敏感性信号（如全精度与量化模型输出分布的KL散度）离线为不同任务、不同时间步生成量化位宽策略，避免每个下游任务都需真实标注或评测指标，便于快速适配新业务场景。

  - 该混合精度框架可与现有量化方法叠加（即插即用），工程上只需在推理时按步动态切换激活精度，不涉及模型重新训练；对需要反复去噪的扩散generation pipeline（如商品标题、推荐理由、Agent规划）可有效降低推理成本。

  - 注意：这一结论源于扩散语言模型，若业务使用自回归LLM则借鉴有限；但若采用扩散或迭代解码架构，应避免沿用AR静态量化假设，需重新评估时间步/任务维度的敏感性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型（DLMs）通过迭代去噪生成文本，但推理需多次模型前向，量化是降低成本的关键。现有量化方法多为自回归模型设计，忽略DLM去噪过程中量化敏感性随时间和任务变化。

**方法关键点**：发现激活量化敏感性与去噪步和下游任务都相关，不同任务在不同去噪窗口对量化误差的容忍度不同；该敏感性可通过全精度与量化模型输出分布的KL散度（无标签）预测，无需任务评测指标。提出T2Quant，在固定位宽预算下，用这一无标签信号为每个去噪步分配最优激活精度，实现任务与时间感知的混合精度量化。

**关键结果**：在3个DLM和6个基准上，T2Quant使现有量化方法的平均准确率一致提升，最高达6.7个百分点，且不增加额外位宽预算。
