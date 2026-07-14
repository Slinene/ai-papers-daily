---
title: 'Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge
  Bias'
title_zh: 深入不公正法官：LLM评判偏差的机制可解释性分析
authors:
- Zixiang Xu
- Sixian Li
- Huaxing Liu
- Xiang Wang
- Shuai Li
- Zirui Song
- Xiuying Chen
affiliations:
- AMAP, Alibaba Group
- Mohamed bin Zayed University of Artificial Intelligence
- University of Southern California
- University of Michigan, Ann Arbor
arxiv_id: '2607.11871'
url: https://arxiv.org/abs/2607.11871
pdf_url: https://arxiv.org/pdf/2607.11871
published: '2026-07-13'
collected: '2026-07-14'
category: Eval
direction: 机制可解释性 · 评估偏差
tags:
- bias
- mechanistic interpretability
- LLM-as-judge
- steering
- hidden states
- evaluation
one_liner: 从隐藏状态几何揭示LLM评判偏差的可控子空间，实现因果转向与失败预测，超越文本方法
practical_value: '- 使用线性探针（linear projection）在隐藏态上检测评分偏差，无需修改提示，可实时监控在线评估系统的公平性，例如在电商搜索排序的LLM打分环节预警。

  - 通过激活向量偏向子空间的方向进行“激活转向（activation steering）”，无需重新训练或注入few-shot示例即可校正偏见，低成本提升推荐理由生成、对话评估等场景的客观性。

  - 将偏见建模为低维子空间可作为特征用于失败预测，在未见数据上大幅超越纯文本方法，可集成到推荐系统的离线评估pipeline中自动标注可疑打分。

  - 方法跨评判模型、跨偏见类型通用，适合在广告创意评分、商品评论有用性评估等多场景复用，减少人工校验成本。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**  
现有LLM评判偏见研究大多停留在输入-输出层面，通过扰动输入测量评分变化或改进提示词。本文提出从隐藏状态表征层面解读偏见，揭示其几何结构、因果可控性和预测价值。  
**方法关键点**  
在7个评判模型、7种偏见类型、9个基准上，分析隐藏激活的几何特性：无偏输入形成紧致流形，有偏输入沿低维类型特定子空间偏离，该子空间随网络深度增强且被多种估计器一致恢复。通过沿此子空间进行激活转向，可双向调控评分——正向转向将无偏输入推向偏见评分，反向转向恢复原始评分，效果远超随机方向（幅度大一个数量级）。进一步，仅用线性投影到偏差方向特征，就能预测评判器在3个新基准上的失败案例，显著优于基于文本的检测方法。  
**关键结果**  
- 几何：偏差方向可解释且稳定，激活空间中存在可复用的偏见子空间。  
- 因果：激活转向实现±0.5~1.0分的评分操控，随机方向影响可忽略。  
- 操作：线性探针的失败预测AUROC达0.75~0.85，超越文本方法10~20个百分点。  
框架将几何结构、因果控制和操作预测统一，提供了超越输入-输出的新分析范式。
