---
title: 'SciForma: Structure-Faithful Generation of Scientific Diagrams'
title_zh: SciForma：科学图表结构忠实生成框架
authors:
- Yuxuan Luo
- Peng Zhang
- Xinjie Zhang
- Xun Guo
- Zhouhui Lian
- Yan Lu
affiliations:
- Wangxuan Institute of Computer Technology, Peking University
- State Key Lab of CAD & CG, Zhejiang University
- Microsoft Research Asia
arxiv_id: '2607.18091'
url: https://arxiv.org/abs/2607.18091
pdf_url: https://arxiv.org/pdf/2607.18091
published: '2026-07-19'
collected: '2026-07-24'
category: Multimodal
direction: 结构保真图表生成
tags:
- scientific diagram generation
- structure-faithful
- preference optimization
- multidimensional evaluation
- image generation
one_liner: 通过结构轴分解与多维度合取偏好优化，实现科学图表的结构忠实生成，超越开源模型与GPT-Image-1.5
practical_value: '- 主要是学术贡献，对电商/广告/搜索推荐系统的直接迁移价值有限。

  - 多维度合取偏好优化（M-DPO）可借鉴到推荐系统中平衡准确率、多样性、新颖性等多目标，强制同时达标，避免单一标量奖励忽视薄弱维度。

  - 结构清单与迭代纠错的机制可迁移到 Agent 自动生成营销图文、技术架构图时的实时校验与修正流程。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学方法图的结构保真度具有合取性，单一错误（如反向箭头）即导致图表无效。当前开源模型通过 SFT 只能学习合理布局，无法可靠保证结构正确；标量奖励式后训练掩盖了具体哪个结构维度失败。

**方法关键点**：
- 将图表质量分解为**组件、箭头、文本**三个结构轴，建立结构清单。
- 收集 700K 结构化训练数据（SciFormaData-700K）和 2K 逻辑验证评估集（SciFormaBench-2K）。
- 提出**多维度合取偏好优化（M-DPO）**，强制在所有轴上同时正确，并自适应地将梯度路由到最差维度。
- 推理时利用结构清单进行迭代编辑，修正残余错误。

**关键结果**：SciForma-9B 在 SciFormaBench-2K 和 AIBench 上超过所有开源基线及 GPT-Image-1.5，使开源科学图表生成的结构保真度接近专有模型水平。
