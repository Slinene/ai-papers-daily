---
title: Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining
title_zh: 语言模型预训练中任务无关训练数据影响度量
authors:
- Yuto Nishida
- Hirokazu Kiyomaru
- Yusuke Oda
- Takashi Kodama
- Chaoran Liu
- Daisuke Kawahara
- Yusuke Miyao
- Max Müller-Eberstein
- Masaru Isonuma
affiliations:
- Nara Institute of Science and Technology
- NII LLMC
- Waseda University
- The University of Tokyo
- IT University of Copenhagen
arxiv_id: '2608.13515'
url: https://arxiv.org/abs/2608.13515
pdf_url: https://arxiv.org/pdf/2608.13515
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: 训练数据影响分析 · 预训练动态
tags:
- training data influence
- pretraining
- gradient trajectory
- data attribution
- Pythia
- PolyPythia
one_liner: 提出一种无需下游任务或验证集的训练数据影响度量，通过梯度更新对最终参数距离的缩减来估计样本贡献
practical_value: '- 在大规模预训练或微调中，可借鉴该任务无关的影响度量：不需要人工定义验证集，只需利用中间checkpoint和最终参数的梯度投影，即可对每个训练样本的重要性打分，适合数据清洗和异常样本排查。

  - 发现的影响数据时序变化（早期文学类数据、后期STEM数据）提示课程学习策略：在推荐或Agent模型的预训练阶段，可以按数据域动态调整采样权重，初期侧重通用/文本类数据，后期逐步引入垂直领域或结构化数据。

  - 该方法只需存储中间checkpoint，计算成本低，且无需重新训练，适合工程实现中定期对训练语料进行影响审计，为数据版本管理和数据溯源提供量化依据。

  - 在生成式推荐或LLM4Rec场景中，可以利用此思路分析哪些训练样本对最终推荐生成能力贡献最大，辅助构建高质量指令微调数据集。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
现有训练数据影响度量通常依赖下游任务或验证集作为归因目标，难以反映模型通用能力，且跨训练阶段比较困难。  

**方法关键点**  
定义每个训练样本的影响为该样本梯度更新减少与最终参数平方距离的程度，直接从中间checkpoint估计，无需重新训练。该方法不依赖任何下游任务或验证集，提供任务无关的轨迹级影响度量。  

**结果**  
在Pythia和PolyPythia共18个配置上验证，发现影响数据随时间发生系统性变化：训练早期，文学相关数据更强烈地对齐最终参数轨迹；训练后期，STEM数据对齐程度上升。这一交叉趋势在多个模型配置中一致，表明预训练阶段的数据重要性存在领域层面的时序规律。
