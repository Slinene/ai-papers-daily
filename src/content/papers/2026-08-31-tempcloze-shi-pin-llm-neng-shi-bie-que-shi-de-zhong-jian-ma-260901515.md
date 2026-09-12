---
title: 'TempCloze: Can Video-LLMs Identify the Missing Middle?'
title_zh: TempCloze：视频 LLM 能识别缺失的中间片段吗？
authors:
- Wenqi Pei
- Henry Hengyuan Zhao
- Yilai Liu
- Jiahao Meng
- Han Chen
- Ziyu Wang
- Hongyang Du
affiliations:
- The University of Hong Kong
- National University of Singapore
- Peking University
arxiv_id: '2609.01515'
url: https://arxiv.org/abs/2609.01515
pdf_url: https://arxiv.org/pdf/2609.01515
published: '2026-08-31'
collected: '2026-09-12'
category: Eval
direction: 视频LLM时间推理评测
tags:
- Video-LLM
- Temporal Reasoning
- Benchmark
- Cloze Test
- Evaluation
- Multimodal
one_liner: 提出 TempCloze 视频填空基准，评估 Video-LLM 视觉时间推理并揭示时间对齐是主要瓶颈
practical_value: '- 评测设计可借鉴：在评估多模态推荐/Agent 的时间推理时，减少文本选项中介，采用填空式视觉任务（给定前后片段选缺失中间片段），迫使模型依赖视觉时序而非语言措辞；电商直播切片理解、视频商品描述生成等场景可迁移此范式。

  - 困难负样本构造：按语义、时序对齐、过程进展三个维度生成同源干扰项，并共享场景与对象以削弱外观线索，可直接用于商品视频对比学习或用户行为序列的负采样，提升模型对精细时间差异的判别力。

  - 模型选型提示：Alignment 是主要瓶颈，说明在短视频/直播理解等时间敏感任务中不能只看语义匹配，应专项评估时间对齐能力；选择 Video-LLM 基座或微调时优先考察该维度。

  - 工程权衡依据：论文分析 candidate order、context direction、visible span、frame density 和 test-time
  scaling 对性能的影响，可用于在推理成本受限时决定是否增加帧密度、上下文长度或采样步数，平衡时间推理效果与计算开销。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
视频 LLM 时间推理评测多通过文本选项或字幕中介，存在语言捷径：模型可利用选项措辞、答案相关性或语言先验而非真实视觉时间理解。  

**方法**  
TempCloze 是一个视频 cloze 基准，给定视频开头与结尾片段，要求模型从四个候选中间片段中选出真实缺失段。包含 1,521 个视频，来自 7 个数据源，以长镜头和第一视角视频为主。干扰项与正确项来自同一视频源，沿三个维度构造：Semantic 干扰事件内容，Alignment 干扰发生时机，Progression 干扰展开方式，并共享场景与物体以削弱外观线索。评测覆盖 10 个闭源与 21 个开源 Video-LLM。  

**结果**  
发现 Alignment 是主要瓶颈——模型能识别合理语义内容和局部事件推进，但难以判断时间对齐。在 TempCloze-Mixed 与 TempCloze-Hard 上进一步分析错误模式与行为敏感性，考察候选顺序、上下文方向、可见跨度、帧密度及测试时扩展对模型选择的影响。
