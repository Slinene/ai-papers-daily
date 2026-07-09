---
title: Future Confidence Distillation in Large Language Models
title_zh: 大语言模型中的未来置信度蒸馏
authors:
- Sahil Kale
affiliations:
- University of California, Los Angeles
arxiv_id: '2607.07626'
url: https://arxiv.org/abs/2607.07626
pdf_url: https://arxiv.org/pdf/2607.07626
published: '2026-07-08'
collected: '2026-07-09'
category: Eval
direction: LLM 置信度校准的时序提前预测
tags:
- confidence distillation
- calibration
- linear probe
- metacognition
- LLM
- pre-solution
one_liner: 利用回答后隐藏状态训练探针作为教师，将置信度信息蒸馏到回答前表征，实现低延迟高校准的置信估计
practical_value: '- 在 RAG、工具调用或 Agent 决策中，可在生成回答前用模型中间层 hidden state 快速预判置信度，决定是否触发检索或回退，大幅降低时延

  - 训练一个轻量线性探针，以回答结束后的正确性探针（教师）产生的置信度为蒸馏目标，样本效率极高，少量标注即可获得校准良好的提前置信度估计

  - 探针只需预解层表征，可用于流式推理或早期退出，适合对延迟敏感的生产环境，如电商搜索中的即时置信判断

  - 方法在域内数据集间具有迁移性，可在部分 query 类型上训练，泛化到同类场景，降低维护成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有 LLM 置信度估计通常只关注最终回答，忽略了置信信息在生成过程中逐渐演化的特性。在检索增强生成、工具使用和自适应计算等置信感知系统中，需要尽早且可靠地判断答案可信度，但回答前置信（Feeling-of-Knowing, FOK）往往校准较差。

**方法关键点**：
1. 对比分析前沿与开源 LLM 的回答前（FOK）与回答后（Judgement-of-Learning, JOL）置信度，发现后者的校准和区分能力显著更优。
2. 在隐藏表征上训练的线性探针能提取出比模型口头表达丰富得多的置信相关信息。
3. **未来置信度蒸馏**：用回答后正确性探针产生的教师置信度，训练一个仅依赖回答前隐藏状态的预测器。推理时无需生成完整回答即可获得高校准置信度。

**关键结果**：蒸馏预测器仅使用回答前表征，就恢复了大部分回答后置信度的校准提升，且具备极高的样本效率，能够在同一领域的不同数据集间迁移。这证明置信度信息可在回答生成完成前被有效预测，实现了低成本、高可靠且低延迟的置信估计。
