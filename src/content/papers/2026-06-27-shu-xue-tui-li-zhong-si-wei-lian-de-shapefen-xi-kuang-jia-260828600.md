---
title: SHAPE of Chain-of-Thought in Math Reasoning
title_zh: 数学推理中思维链的SHAPE分析框架
authors:
- Jonghyun Song
- Sangjun Song
- Minjae Oh
- Haesung Pyun
- Sungsik Lee
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
- Department of Mathematics Education, Seoul National University
arxiv_id: '2608.28600'
url: https://arxiv.org/abs/2608.28600
pdf_url: https://arxiv.org/pdf/2608.28600
published: '2026-06-27'
collected: '2026-09-01'
category: Reasoning
direction: 数学推理CoT分析与后训练
tags:
- Chain-of-Thought
- Math Reasoning
- Heuristics
- Semantic Spaces
- Post-training
- RL
one_liner: 用语义空间与启发式分析数学CoT，发现启发式更能解释正确性且可通过多样化后训练提升推理
practical_value: '- 将Agent推理诊断从表面特征转向结构化技能分析：可借鉴SHAPE的二维编码（语义空间+启发式），对搜索推荐Agent（如意图理解、召回策略选择、排序解释）的推理轨迹打标，定位模型在哪些解释框架或动作上出错，而不是只看最终效果。

  - 警惕RL微调中的模式坍缩：该研究发现RL使启发式使用趋于mode-seeking。在训练对话式推荐或query改写Agent时，若仅使用结果奖励，模型可能只学会一种固定策略，建议加入策略多样性正则或覆盖多个启发式的过程奖励。

  - 通过构造多样化策略数据提升模型泛化：后训练时显式促进启发式多样性可提升数学推理准确率，迁移到业务可构造包含不同改写策略（如扩写、纠错、意图切换）的query推荐数据，让模型学习多种解法而非单一模板。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有CoT分析多停留在长度、困惑度等表面特征，无法解释模型是否真正掌握数学技能。SHAPE引入数学教育中的两个概念：语义空间（问题被解释为代数、几何等不同表征）和启发式（具体行动如化简、反向推理），对CoT轨迹进行结构化编码。

方法：用SHAPE分析多种模型的推理轨迹，比较启发式与传统特征对答案正确性的解释力；检查模型在语义空间上的注意力分布；进一步分析强化学习后训练对启发式使用模式的影响；最后通过显式促进多样化启发式进行后训练以提升准确率。

关键结果：数学启发式比长度等CoT表面特征更能解释最终正确性；模型倾向于集中在少数语义空间可提高正确率；RL导致启发式使用出现mode-seeking（收敛到少数模式）；通过鼓励启发式多样性进行后训练可有效提升数学推理准确率。
