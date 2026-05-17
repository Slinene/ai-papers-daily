---
title: 'Vocabulary Hijacking in LVLMs: Unveiling Critical Attention Heads by Excluding
  Inert Tokens to Mitigate Hallucination'
title_zh: LVLM词汇劫持：排除惰性token揭示关键注意力头以缓解幻觉
authors:
- Yangneng Chen
- Junlin Li
- Weijun Yao
- Xilai Ma
- Guodong Du
- Wenya Wang
- Jing Li
affiliations:
- Harbin Institute of Technology (Shenzhen)
- Huawei Technologies Co., Ltd.
- The Hong Kong Polytechnic University
- Nanyang Technological University
arxiv_id: '2605.10622'
url: https://arxiv.org/abs/2605.10622
pdf_url: https://arxiv.org/pdf/2605.10622
published: '2026-05-11'
collected: '2026-05-17'
category: Multimodal
direction: 多模态大模型幻觉缓解
tags:
- hallucination
- visual attention
- LVLM
- training-free
- vocabulary hijacking
- multimodal
one_liner: 发现视觉token的词汇劫持现象，提出无训练注意力增强HAVAE，显著减轻LVLM幻觉
practical_value: '- 电商多模态问答/商品描述生成场景，可借鉴 HAVAE 的无训练注意力干预方法，通过加权少数关键注意力头抑制幻觉，不增加推理延迟。

  - 使用 logit lens 诊断模型注意力异常（如某个视觉 token 总是映射到相同的错误词）的思路可迁移到 LLM Agent 的行为审计，排查错误的感知模式。

  - NHAR 指标提供了一种快速量化注意力头可靠性的方法，可用于 Agent 感知模块的 head pruning 或动态路由，在有限算力下保留最关键的视觉注意力单元。

  - 论文强调的“Inert Token”分析提醒我们在多模态对齐时，图像中某些固定模式（如空白、边框）可能劫持注意力，这些 token 可在预处理阶段过滤或权重衰减。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：大型视觉语言模型（LVLM）常生成与视觉输入矛盾的内容（幻觉），以往研究多归因于视觉注意力不足。本文通过 logit lens 分析注意力机制，发现“词汇劫持”现象：某些视觉 token（Inert Token）吸收过多注意力，其隐藏状态层层投影到词汇空间时，始终解码为少量固定无关词（Hijacking Anchors），暴露刚性语义坍塌。

**方法**：提出 HABI，利用语义刚性精确定位 Inert Token；设计非劫持视觉注意力比（NHAR）指标，量化注意力头抵抗劫持的能力，识别对事实性至关重要的头；在此基础上，提出无训练的 HAVAE 干预，选择性增强这些关键头对显著视觉区域的聚焦，无需额外计算。

**结果**：在多个基准测试中，HAVAE 显著降低了幻觉率，同时保持模型通用能力，且无推理开销。分析表明，仅增强少数关键头即可有效缓解幻觉，验证了词汇劫持的普遍性与干预的高效性。
