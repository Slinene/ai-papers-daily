---
title: 'Learning More by Training Less: Uncertainty-Guided Progressive Contraction
  for Efficient Reasoning Post-Training'
title_zh: 以更少训练学习更多：不确定性引导的渐进收缩实现高效推理后训练
authors:
- Suorong Yang
- Jiaxin Wang
- Jiaming Su
- Chentao Yue
- Furao Shen
- Peng Ye
- Soujanya Poria
affiliations:
- National University of Singapore
- Nanjing University
- Fudan University
- The University of Sydney
- The Chinese University of Hong Kong
arxiv_id: '2610.12933'
url: https://arxiv.org/abs/2610.12933
pdf_url: https://arxiv.org/pdf/2610.12933
published: '2026-10-08'
collected: '2026-10-13'
category: Training
direction: LLM 推理后训练 · 数据收缩
tags:
- Uncertainty-Guided
- Progressive Contraction
- Reasoning Post-Training
- Efficient Training
- Monte Carlo Reasoning Trees
- SFT
one_liner: 用不确定性引导的渐进收缩框架，将推理监督压缩至全量SFT的0.22%训练预算，且维持或提升推理性能
practical_value: '- 在电商/推荐场景用 LLM 生成商品卖点、推荐理由或搜索 query 理由时，可借鉴「不确定性引导的数据筛选」：先对生成轨迹做蒙特卡洛树展开，计算中间步骤的
  token 概率方差或模型置信度，只保留高不确定性的样本用于 SFT，能显著降低训练数据量而不丢效果。

  - 两阶段收缩可以拆成「离线静态筛选 + 在线动态路由」：离线基于教师模型的不确定性先压缩语料，在线根据学生模型当前 loss 或梯度变化决定是否继续使用某样本，这种策略适合在增量训练或弱标注业务数据上做持续微调。

  - 弱到强泛化结果提示：用较弱/较便宜的模型先对大规模生成数据进行筛选，再用筛选后的数据训练更强模型，能降低推理数据标注成本；这在需要大量 LLM 生成内容但标注预算有限的推荐文案、对话式推荐场景很实用。

  - 过程级不确定性比只看最终结果的正确性更精细：在处理多步推理链（如购物决策解释、Agent 路径规划）时，可以定位到具体哪一步不稳定，从而针对性补充监督信号或修复
  prompt，而不是重训整个样本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 推理能力的提升依赖大规模推理语料的 post-training，但单纯扩大数据量带来显著训练成本，性能收益却很快饱和。因此需要在不牺牲能力的前提下，尽可能压缩推理监督信号。

**方法关键点**：提出不确定性引导的渐进收缩框架。不再把教师生成的 chain-of-thought 当作唯一路径，而是围绕中间推理状态构建蒙特卡洛推理树，暴露过程级不确定性。第一阶段利用该不确定性将原始语料收缩为紧凑的 teacher-informed pool；第二阶段引入 learner-aware 在线路由，在 SFT 过程中根据学生模型的学习状态动态选择样本进行优化。两阶段共同收缩监督数据和优化步骤，极大降低训练预算。

**关键结果**：在多个推理基准和不同 LLM 家族上，仅使用全量数据 SFT 优化预算的 **0.22%**，训练曝光减少超过 **450 倍**，推理性能保持或提升。方法还展现出跨异构学生模型、黑盒教师以及弱到强迁移的泛化能力，表明不仅能加速训练，还能增强推理能力。
