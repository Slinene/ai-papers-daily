---
title: Data-Efficient Adaptation of LLMs via Attention Head Reweighting
title_zh: 通过注意力头重加权实现数据高效的LLM适配
authors:
- Tuomas Oikarinen
- Zixiao Chen
- Charlotte Siska
- Tsui-Wei Weng
- Chandan Singh
- Jianfeng Gao
affiliations:
- UC San Diego
- Microsoft Research
- Microsoft Security AI
arxiv_id: '2607.13425'
url: https://arxiv.org/abs/2607.13425
pdf_url: https://arxiv.org/pdf/2607.13425
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: 注意力头重加权小样本适配
tags:
- Data-efficient learning
- Attention Head Reweighting
- PEFT
- Few-shot classification
- LLM adaptation
one_liner: 提出注意力头重加权(AHR)，每个头学一个标量权重，参数减少200-1000倍，小样本分类超越LoRA
practical_value: '- **小样本意图分类冷启动**：AHR用极少量样本（如10-shot）即可适应新类别，适合电商搜索中的新型query意图识别、商品类目打标或安全审核任务，无需大量标注。

  - **极低资源部署**：可训练参数仅为头数×层数（Llama-3-8B约1000个），内存和计算开销远低于LoRA，适合在端侧或频繁更新场景下快速切换任务。

  - **可解释性辅助特征工程**：学习到的头权重直接指示哪些注意力头对任务关键，可逆向分析模型已有的语义模式，为特征设计、模型裁剪提供依据，如发现某些头专门处理价格数字、品牌词等。

  - **抗过拟合的推荐文案过滤**：在安全风控、垃圾评论检测等训练数据极不平衡的场景，AHR通过强行约束参数空间有效抑制过拟合，提高召回率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：安全等标注稀缺领域（如新型攻击检测、低资源文本分类）急需小样本学习能力。现有PEFT方法（如LoRA）在极少量样本下仍易过拟合，因为优化的参数空间仍较大。本文想利用LLM注意力头已有的功能专门化（某些头擅长句法、某些擅长语义）来进一步压缩可学习参数。

**方法关键点**：提出Attention Head Reweighting (AHR)，在冻结整个LLM的前提下，为每层每个注意力头学习一个标量权重w_{l,h}，将原多头输出加权求和。初始权重设为1.0，可正可负，相当于对注意力头进行“开关”或“增强/抑制”。训练时只优化这些标量（通常<1500个，是LoRA的200-1000分之一），使用标准交叉熵损失。推理时权重固定，完全不改变模型结构。

**结果**：在6个分类数据集（如SST-2、RTE、安全相关数据集）上，AHR在10-shot、100-shot设置下准确率平均超越LoRA，尤其在困难任务（如RTE）上优势明显。例如Llama-3-8B上，10-shot平均准确率比LoRA高5.2%，且仅修改模型约0.0001%的参数。分析学习到的权重发现，部分头被赋予负权重，即抑制其输出，且这些头往往对应于任务无关的通用模式；正权重头则与上下文学习能力高度相关。
