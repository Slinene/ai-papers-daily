---
title: 'IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation
  and Editing'
title_zh: IterCAD：面向视觉引导CAD生成与编辑的迭代多模态智能体
authors:
- Tao Hu
- Jiaxin Ai
- Licheng Wen
- Xueheng Li
- Shu Zou
- Siqi Li
- Nianchen Deng
- Xinyu Cai
- Hongbin Zhou
- Pinlong Cai
affiliations:
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
- Shanghai Innovation Institute
- Wuhan University
- The Australian National University
arxiv_id: '2606.13368'
url: https://arxiv.org/abs/2606.13368
pdf_url: https://arxiv.org/pdf/2606.13368
published: '2026-06-11'
collected: '2026-06-13'
category: Agent
direction: CAD 生成与编辑 · 多模态 Agent · 闭环几何推理
tags:
- CAD Generation
- Multimodal Agent
- Reinforcement Learning
- Code Generation
- Geometric Reasoning
one_liner: 提出迭代多模态Agent框架，通过多视图工程图闭环交互与几何感知RL，实现鲁棒CAD代码生成与编辑
practical_value: '- **闭环Agent交互范式**：借鉴“思考-执行-观察”的多轮交互协议，强制模型输出结构化推理和代码块，并给予格式奖励，可用于电商复杂查询Agent或对话式购物助手的设计，提高多步决策的可靠性。

  - **数据合成与训练流程**：先用专家模型合成高质量多轮交互轨迹进行SFT冷启动，再通过几何感知强化学习提升自校正能力，此两步走训练策略可直接复用到需要长程推理和纠错的业务场景（如多轮推荐对话、任务型Agent）。

  - **信用分配掩码（GVPM）**：为解决多轮RL中后期失败惩罚前期有效动作的问题，引入前缀掩码，只对有效前缀进行强化，可迁移到任何多轮交互的RL训练中（如多步召回策略优化、对话策略学习）。

  - **幸存者偏差消除评估**：提出的CD-TR曲线和AUC-TR指标将代码执行成功率与几何精度联合评估，类似思路可引入到生成式推荐或SQL生成任务中，把生成失败记为最低分，避免仅统计成功样本而导致的评价失真。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

**动机**
当前CAD自动化方法多为单步开环生成，缺乏迭代纠错能力，且训练数据以简单拉伸为主，缺少倒角、抽壳等高级特征。评估协议仅统计成功执行样本的几何误差（幸存者偏差），掩盖了代码可执行性问题。

**方法**
IterCAD将CAD生成与编辑建模为一个多模态Agent与CAD沙箱之间的多轮闭环交互过程，支持工程图转代码、文本转代码和交互式编辑三类任务。
- **交互协议**：每轮Agent基于历史观察输出结构化动作（推理跟踪 + 可执行代码或<DONE>），沙箱返回编译器报错、视觉反馈及自动从几何体投影出的尺寸标注视图。
- **数据合成管线**：通过SolidWorks COM接口从参数化零件自动生成标准多视图工程图，构建复杂操作空间（含fillet/chamfer/shell等高级特征）；利用专家LLM在沙箱中展开多轮交互轨迹，经格式、逻辑一致性、几何正确性三重过滤得到冷启动SFT数据。
- **训练策略**：先进行渐进式SFT：第一阶段用专家轨迹建立基本代码生成能力，第二阶段用教师模型修复模型自身失败案例获得迭代精化数据。之后采用GSPO强化学习，以几何Chamfer Distance、格式合规性、进度奖励组成序列级回报，并引入**几何可行前缀掩码（GVPM）**：当检测到连续执行错误或几何停滞时，掩蔽后续回合的token，避免将下游失败归咎于前期动作。
- **评估指标**：提出**CD-TR曲线**和**AUC-TR**指标，将所有测试样本（含执行失败样本）按CD容忍度计算召回率，消除幸存者偏差，统一衡量代码有效性与几何精度。

**关键结果**
在自建的IterCAD-Bench（1000工程图+200编辑任务）上，IterCAD在闭环Agent模式下仅用2.48平均轮次即达到0.30%的无效生成率和0.61 AUC-TR，远超Qwen3.5-4B基线的62.30% IR，也优于GPT-5等更大模型。在Text2CAD和CADPrompt外部基准上，无效率低至0.64%和2%，中位CD分别为0.10和2.42，大幅领先专用模型。消融实验证实GVPM对降低无效率和提升几何精度至关重要。
