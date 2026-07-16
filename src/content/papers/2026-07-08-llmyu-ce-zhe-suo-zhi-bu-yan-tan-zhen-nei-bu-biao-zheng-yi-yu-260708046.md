---
title: 'What LLM Forecasters Know but Don''t Say: Probing Internal Representations
  for Calibration and Faithfulness'
title_zh: LLM预测者所知不言：探针内部表征以改善校准与忠实度
authors:
- Raphaël Sarfati
- Pratyush Ranjan Tiwari
- Siddharth Boppana
- Christopher J. Earls
- Srikar Varadaraj
- Eric Ho
affiliations:
- goodfire
- eternis
arxiv_id: '2607.08046'
url: https://arxiv.org/abs/2607.08046
pdf_url: https://arxiv.org/pdf/2607.08046
published: '2026-07-08'
collected: '2026-07-16'
category: Reasoning
direction: LLM推理审计与校准
tags:
- probing
- calibration
- faithfulness
- chain-of-thought
- forecasting
- internal representations
one_liner: 探针LLM内部表征可大幅提升预测校准、揭示思维链不忠实，并能通过预推理分布路由节省30-47%推理token
practical_value: '- 在需要可靠置信度的推荐/广告预测场景中，用中间层探针替代口头置信度可显著降低校准误差（ECE 0.044 vs 0.093），避免过度自信或保守。

  - 审计AI Agent的思维链忠实度时，可通过探针检测模型内部是否已受外部输入影响，即使思维链未提及，这对多Agent交互的透明审查很有价值。

  - 可将探针用作“诚实度检测器”：当模型受到隐蔽证据干扰时，探针激活值能更早、更准确地捕捉到行为偏移（Spearman ρ=0.57 vs CoT文本的0.22），并预测偏移方向（84%准确率）。

  - 在推理前利用预测层输出的答案分布离散度进行高置信度路由：分布集中时直接返回预推理答案，避免生成冗长CoT，可节省30-47% token且不损失精度，适用于低延迟或高吞吐的实时推送、搜索建议等场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM预测者虽准确但校准差（期望校准误差ECE高），思维链推理可能不反映真实决策依据，即不忠实。为此探究模型内部表征是否能提供更直接、更可靠的校准和忠实度信息。

**方法**：基于Eternis-Forecaster 8B（及GLM-4.7-Flash、GLM-4.5-Air），在中间层激活上训练池化探针（representation-pooling probes），对比其与口头置信度的校准水平。通过证据消融和误导注入测试CoT忠实度：移除关键信息导致预测改变，但推理文本常不体现。进一步用探针检测此类隐蔽行为偏移。最后发现预测在推理前已基本确定，利用预推理层输出答案分布的集中度（spread）做路由：高集中度问题直接输出预推理答案，无需生成推理链。

**关键结果**：探针校准ECE=0.044 vs 口头=0.093；探针追踪行为偏移的Spearman相关系数=0.57，而CoT文本仅0.22；探针预测偏移方向的准确率达84%，且包含CoT完全沉默的隐蔽案例；通过预推理分布路由可节省30%-47%的生成token，准确率无损失。
