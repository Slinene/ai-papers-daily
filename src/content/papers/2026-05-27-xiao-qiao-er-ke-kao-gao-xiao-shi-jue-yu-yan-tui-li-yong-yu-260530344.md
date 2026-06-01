---
title: 'Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly
  Detection'
title_zh: 小巧而可靠：高效视觉-语言推理用于时间序列异常检测
authors:
- Xiaona Zhou
- Muntasir Wahed
- Tianjiao Yu
- Constantin Brif
- Ismini Lourentzou
affiliations:
- University of Illinois Urbana-Champaign
- Sandia National Laboratories
arxiv_id: '2605.30344'
url: https://arxiv.org/abs/2605.30344
pdf_url: https://arxiv.org/pdf/2605.30344
published: '2026-05-27'
collected: '2026-06-01'
category: Other
direction: 时间序列异常检测 · VLM微调
tags:
- VLM
- Time-Series Anomaly Detection
- Parameter-Efficient Fine-Tuning
- Benchmark
- Interpretable Reasoning
- VisAnomBench
one_liner: 构建带推理标注的时序异常检测benchmark并微调参数高效VLM，精准率和F1分别提升21和24个百分点以上。
practical_value: '- 电商系统监控（如流量、转化率时序）可借鉴：将时间序列可视化为图表，用微调的VLM（如LoRA）进行异常定位与解释，降低对传统统计方法的依赖。

  - 构造高质量推理标注的方法可复用：利用多个大VLM生成候选解释，再基于细粒度任务奖励筛选优质标注，提升训练数据的可解释性。

  - 参数高效微调（预计用了LoRA等）使小模型也能继承大模型的推理能力，适合资源受限场景，可迁移到电商中不用推理大模型 online。

  - 主要是学术贡献，业务可借鉴点有限，但思路可用于需要透明决策的监控类应用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉-语言模型（VLM）在时间序列异常检测中表现不佳，且公开基准仅提供区间标注，缺少自然语言推理，难以微调出可解释的检测器。  
**方法**：构建 VisAnomBench 基准，从多个大VLM生成异常解释，用细粒度任务奖励筛选高质量解释。随后在该基准上微调一个参数高效的 VLM——VisAnomReasoner，实现可解释的异常定位。  
**结果**：在 VisAnomBench 上，VisAnomReasoner 的精确率和 F1 分别比最强基线高至少 21.23 和 23.87 个百分点。在 TSB-AD-U 跨基准测试中，精确率和 F1 分别提升 9.57 和 13.39 个百分点，展现出强泛化能力。
