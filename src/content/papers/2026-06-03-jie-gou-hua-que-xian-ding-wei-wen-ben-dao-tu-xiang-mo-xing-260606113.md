---
title: 'Where, What, Why, and Importance: Structured Defect Grounding for Text-to-Image
  Feedback'
title_zh: 结构化缺陷定位：文本到图像模型的诊断与对齐
authors:
- Huaisong Zhang
- Hao Yu
- Yuxuan Zhang
- Jiahe Wang
- Xinrui Chen
- Haoxiang Cao
- Feng Lu
- Wendong Zhang
- Changqian Yu
- Chun Yuan
affiliations:
- Tsinghua University
- Kuaishou Technology
- University of British Columbia
- Vector Institute
- South China Normal University
arxiv_id: '2606.06113'
url: https://arxiv.org/abs/2606.06113
pdf_url: https://arxiv.org/pdf/2606.06113
published: '2026-06-03'
collected: '2026-06-14'
category: Multimodal
direction: 结构化缺陷诊断与生成式模型对齐
tags:
- Structured Defect Grounding
- T2I Diagnosis
- GRPO
- Reward Model
- Vision-Language Model
- SDG-30K
one_liner: 将缺陷定义为(位置,类型,原因,重要性)元组，提出结构化集合预测与空间奖励对齐框架
practical_value: '- **结构化诊断范式**：将模型输出缺陷建模为实例级元组（位置、类型、原因、重要性），可借鉴用于推荐系统的错误分析，例如生成式推荐的item质量问题，用VLM对推荐结果进行定位与归因，构建结构化反馈数据提升模型可解释性。

  - **空间化奖励设计**：BoxFlow-GRPO将检测到的缺陷区域转化为带重要性权重的空间奖励，用于扩散模型微调。电商场景中可对商品图片生成缺陷进行类似的像素级反馈，指导文生图模型优化商品展示效果。

  - **VLM作通用诊断器**：使用视觉语言模型直接输出结构化预测，绕过传统热力图回归的局限性。在多模态Agent或内容审核中，可将VLM的缺陷检测能力迁移到视频帧、广告素材的异常定位与原因解释，为自动化优化提供信号。

  - **诊断到对齐的闭环**：将诊断与模型优化无缝衔接，可参考其思想在推荐系统中构建“问题诊断→奖励修正→策略更新”的迭代框架，例如用LLM分析用户负反馈并转化为强化学习奖励来调整排序模型。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：文本到图像模型生成效果逼真但仍存在局部、细微的失败（如文字畸形、几何不合理、语义错配），现有密集反馈方法使用热力图回归，难以处理变基数缺陷并绑定语义原因。  
**方法**：提出结构化缺陷定位（SDG），将诊断转化为结构化集合预测，每个缺陷建模为（位置、类型、原因、重要性）四元组。为支撑该任务，构建了SDG-30K数据集，包含30K张图像、覆盖四个现代T2I生成器，并设计SDG-Eval评估协议。在此基础上，构建诊断到对齐框架：利用视觉语言模型（VLM）作为SDG检测器，输出缺陷集合；通过BoxFlow-GRPO将预测的缺陷框转化为带重要性权重的空间奖励，对扩散模型进行对齐微调。  
**结果**：SDG检测器在结构化缺陷定位上显著超越主流商用VLM；SDG引导的奖励函数持续提升T2I模型的对齐度，并支持针对局部缺陷的细粒度图像优化。
