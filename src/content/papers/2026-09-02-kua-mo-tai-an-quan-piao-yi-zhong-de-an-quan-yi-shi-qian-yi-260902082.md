---
title: Transfer Safety Awareness for Cross-Modal Safety Drift in Multimodal Large
  Language Models
title_zh: 跨模态安全漂移中的安全意识迁移（多模态大语言模型）
authors:
- Tianqi Xiao
- Shiyao Cui
- Minghao Zhang
- Junxiao Yang
- Renmiao Chen
affiliations:
- Tsinghua University
- Beijing University of Posts and Telecommunications
- Northwestern Polytechnical University
arxiv_id: '2609.02082'
url: https://arxiv.org/abs/2609.02082
pdf_url: https://arxiv.org/pdf/2609.02082
published: '2026-09-02'
collected: '2026-09-06'
category: Multimodal
direction: 多模态安全对齐 · 表示迁移
tags:
- MLLM Safety
- Cross-modal
- Safety Alignment
- Representation Transfer
- Security
one_liner: 提出安全感知表示迁移（SRT），冻结 MLLM 骨干下通过方向修正缓解跨模态安全漂移，提升安全性并保持通用能力
practical_value: '- 多模态场景（如商品图+咨询文本、广告图文审核）不能只做纯文本安全过滤，需评估图文联合语义风险；可参考该工作构建图像-文本联合安全评估集，专门测“良性文本+风险图片”的请求。

  - 若线上 MLLM 需要快速安全加固，可借鉴 SRT 思路：不微调大模型，仅在隐藏表征上学习一个安全方向偏移，用少量不安全样本训练轻量适配器，便于部署和回滚。

  - 论文发现视觉风险线索注意力不足导致拒答弱，提示可在注意力层加监督/正则，或使用视觉 token 重要性加权，增强对风险区域的感知。

  - 对于 Agent/推荐系统接入多模态 LLM，建议在 system prompt 中显式加入跨模态安全指令，并在离线评估中加入跨模态攻击样例，防止“文雅提问+危险图片”绕过策略。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**  
MLLM 引入视觉后，良性文本查询在图像语境下可能隐含有害意图，称为跨模态安全漂移。初步实验显示，这类请求的安全响应率显著低于显式不安全文本请求。

**方法关键点**  
先通过实证分析识别典型不安全响应模式；解释模型表征与注意力后发现，视觉风险线索获得的注意力有限，难以有效触发拒答。基于“文本不安全信号可迁移”的观察，提出安全感知表示迁移（SRT）：冻结 MLLM 骨干，只学习表征方向修正，轻量且无需大规模再训练。

**关键结果**  
在多个基准和多种模型上，SRT 在跨模态场景下显著提升安全响应率，同时保持通用能力（utility）不下降。
