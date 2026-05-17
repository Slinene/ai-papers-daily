---
title: 'RW-Post: Auditable Evidence-Grounded Multimodal Fact-Checking in the Wild'
title_zh: RW-Post：面向真实场景的可审计多模态事实核查基准
authors:
- Danni Xu
- Shaojing Fan
- Harry Cheng
- Mohan Kankanhalli
arxiv_id: '2605.10357'
url: https://arxiv.org/abs/2605.10357
pdf_url: https://arxiv.org/pdf/2605.10357
published: '2026-05-11'
collected: '2026-05-17'
category: Multimodal
direction: 多模态事实核查 · 可审计证据基准
tags:
- Multimodal Fact-Checking
- Evidence-Grounded
- Benchmark
- LLM-assisted Annotation
- Visual Misinformation
- Auditability
one_liner: 提出后对齐的多模态事实核查基准RW-Post，提供可审计推理与证据链接，暴露现有模型在证据忠实度上的不足
practical_value: '- 电商内容审核可借鉴：构建商品图文不符的核查数据集，要求模型输出可审计的证据链接，提高审核结果的可靠性和可解释性。

  - 多模态Agent设计：引入证据检索与验证步骤，如AgentFact基线，将推理链与外部证据结合，适用于需高可信度的推荐解释场景。

  - 评估范式启示：区分闭卷、证据限定和开放网络三种设置，可在推荐系统的知识增强评估中应用，诊断模型对背景知识的依赖程度。

  - 标注流程复用：利用LLM辅助提取和审计人类事实核查文章生成标注，可复用于电商领域生成大规模监督信号，降低人工成本。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态虚假信息日益依赖图像误导，现有事实核查基准缺乏真实场景下的可审计推理与证据链接。

**方法**：构建RW-Post，一个后对齐的文本-图像基准，通过LLM辅助从人类事实核查文章中抽取推理痕迹和证据项，并经过人工审计确保质量。每个实例包含原始社交媒体帖子、推理链及显式证据链接。基准支持闭卷、证据限定和开放网络三种评估协议，便于系统诊断视觉接地与证据利用能力。同时提供AgentFact参考基线，结合证据检索与多步验证。在多个强开源LVLM上统一评测。

**结果**：实验表明当前模型在证据忠实度上存在显著短板；证据限定设置能同时提升准确性和忠实度，揭示了证据接入的重要性。
