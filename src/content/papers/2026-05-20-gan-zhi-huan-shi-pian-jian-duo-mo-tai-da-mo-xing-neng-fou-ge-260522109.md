---
title: 'Perception or Prejudice: Can MLLMs Go Beyond First Impressions of Personality?'
title_zh: 感知还是偏见：多模态大模型能否超越人格第一印象？
authors:
- Caixin Kang
- Tianyu Yan
- Sitong Gong
- Mingfang Zhang
- Liangyang Ouyang
- Ruicong Liu
- Bo Zheng
- Huchuan Lu
- Kaipeng Zhang
- Yoichi Sato
affiliations:
- The University of Tokyo
- Shanda AI Research Tokyo
- Dalian University of Technology
arxiv_id: '2605.22109'
url: https://arxiv.org/abs/2605.22109
pdf_url: https://arxiv.org/pdf/2605.22109
published: '2026-05-20'
collected: '2026-05-23'
category: Multimodal
direction: 多模态大模型人格推理评估
tags:
- MLLM
- Personality Perception
- Grounding
- Benchmark
- Bias
- Evaluation
one_liner: 发现MLLM人格评分准确率与证据接地率严重脱节，51%正确评分非基于证据，提出接地人格推理基准揭示偏见差距。
practical_value: '- **借鉴接地评估范式**：在推荐或Agent用户建模中，不仅要评估预测准确率，还应强制模型提供行为证据，检查预测是否基于真实线索而非表面统计相关，避免模型学到虚假关联。

  - **多智能体+人工验证数据构建**：本文使用多智能体管道生成带时间戳行为观察和证据分析的数据集，可复用于电商评论分析或Agent行为理解的训练数据构建，确保证据对齐。

  - **失败模式诊断指标**：偏见率、虚构率、整合失败率等指标可直接迁移到推荐解释或Agent决策可解释性评估中，监控模型是否在“猜对答案却用错理由”，提升系统可信度。

  - **接地型推理链设计**：评分→推理→接地的链条可嵌入推荐理由生成或Agent的决策解释模块，要求模型关联具体行为证据，缓解幻觉和刻板印象。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态大模型（MLLM）人格评测仅关注Big Five数值预测，未检验模型是真正理解行为还是依赖表面刻板印象。亟需考察模型能否将评分锚定于可观测证据。

**方法**：提出接地人格推理任务（Grounded Personality Reasoning, GPR），要求模型依次进行评分、推理、证据接地。为此发布MM-OCEAN数据集，包含1104段视频、5320道多选题，由多智能体管道生成并人工验证，提供时间戳行为观测、证据驱动特质分析和七类线索接地题。设计三层评估（评分、推理、接地）及四个细粒度失败指标：偏见率（Prejudice Rate）、虚构率（Confabulation Rate）、整合失败率（Integration-failure Rate）和整体接地率（Holistic-grounding Rate）。在27个MLLM（13闭源、14开源）上测试。

**关键结果**：发现显著的“偏见差距”——整体上，51%的正确评分并未基于模型检索到的证据；模型最佳整体接地率仅33.5%，多数模型接近0。这表明模型常“得分对但推理错”，暴露出现有MLLM社会认知的表面化。
