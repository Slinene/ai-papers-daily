---
title: 'SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability
  Research?'
title_zh: SAEScientist-Bench：AI智能体能否自主进行SAE可解释性研究
authors:
- Yuqiao Tan
- Shizhu He
- Jun Zhao
- Kang Liu
affiliations:
- The Key Laboratory of Cognitive Intelligence, Institute of Automation, CAS
- School of Artificial Intelligence, University of Chinese Academy of Sciences
arxiv_id: '2609.09113'
url: https://arxiv.org/abs/2609.09113
pdf_url: https://arxiv.org/pdf/2609.09113
published: '2026-09-07'
collected: '2026-09-10'
category: Eval
direction: Agent 自主可解释性研究评估
tags:
- SAE
- Interpretability
- AI Agents
- Benchmark
- Mechanistic Interpretability
- LLM
one_liner: 提出 SAEScientist-Bench 基准，评估 AI 智能体利用稀疏自编码器进行自主机制可解释性发现的能力，揭示其与专家水平的差距
practical_value: '- 在 LLM 用于电商/广告文案生成或搜索推荐场景中，可借鉴 SAE 做特征级可控生成：提取概念特征（如价格敏感、品牌偏好、促销意图），通过
  causal steering 干预输出，实现更细粒度的生成控制。

  - 自动化特征挖掘流程值得迁移：参考本 benchmark 中 agent 设计 contrastive probes 的方法，对候选语义特征进行激活排名、选择性测试和因果扰动验证，可减少推荐系统中人工审核特征重要度的成本。

  - 评估体系可直接复用：使用激活排名、概念选择性和因果 steering 三个维度评估特征与目标概念的相关性，适合用于模型审计、特征归因以及内容安全检测。

  - 注意 agent 在实验测量解释上存在明显错误，实际落地时需加入人工校验或强约束规则，避免因误读实验数据导致错误结论。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：递归自我改进（RSI）主要自动化了模型训练，但缺少事后监控与审计来理解模型学到的内容并确保安全对齐。稀疏自编码器（SAE）作为机械可解释性的基石，能隔离可解释特征，用于模型检查与 steering。论文评估 AI 智能体能否像科学家一样利用 SAE 工具进行自主机制发现。

**方法关键点**：构建 SAEScientist-Bench 基准，给定目标概念，智能体需设计对比探针，在 Gemma-2-9B-IT 的 Gemma Scope 字典（超过 131K 特征）中导航，发现最优特征。评估与 Neuronpedia 上人工整理的专家参考特征对齐，包含三个维度：激活排名、对比文本上的概念选择性、因果生成 steering。测试了 10 种智能体配置，共 20 个任务。

**关键结果**：前沿智能体展示了真实的发现能力，在不同评估维度上各有领先，但整体仍落后于专家基线：在分离目标概念与对比控制上接近专家水平（如某些 agent 的 activation 维度可达较高分），但在因果生成 steering 上差距显著。进一步分析发现，智能体能设计对比以排除虚假候选，但频繁误读实验测量结果。总体而言，该工作将实验模型理解确立为闭环自主 AI 研发的可测量能力。
