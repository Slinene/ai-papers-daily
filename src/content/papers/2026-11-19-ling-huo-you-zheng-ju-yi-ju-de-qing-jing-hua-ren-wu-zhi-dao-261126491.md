---
title: 'FLUID: Flexible, Evidence-Grounded Situated Task Guidance'
title_zh: 灵活、有证据依据的情境化任务指导
authors:
- Yunqi Zhao
- Run Peng
- Ze Dong
- Ryan Lu
- Yinpei Dai
- Joyce Chai
affiliations:
- University of Michigan
arxiv_id: '2611.26491'
url: https://arxiv.org/abs/2611.26491
pdf_url: https://arxiv.org/pdf/2611.26491
published: '2026-11-19'
collected: '2026-11-22'
category: Agent
direction: 多模态任务指导 Agent
tags:
- Agent
- Multimodal
- Task Guidance
- Evaluation
- Real-time
- Egocentric
one_liner: 提出 FLUID 统一框架，用证据、必要性与时机灵活性建模指导干预，并构建实时多模态 agent 实现综合最优
practical_value: '- 在实时导购/客服 Agent 中，放弃固定 ground-truth 回复，改为标注“该不该说、说什么、何时说窗口”，用必要性/时机灵活度作为软监督，可减少过度干预。

  - 把干预决策拆成三个子问题：是否干预（必要性分类）、何时干预（时机回归/窗口预测）、说什么（条件生成），分别评估干预精度、及时率、响应正确率；推荐系统中的“何时推/推什么/是否打扰”可复用该评估框架。

  - 多模态端侧助手需同时优化正确率与响应延迟；可借鉴其在正确性、干预精度、及时性与延迟上的综合平衡思路，把“不说话”也作为有效动作，避免频繁打扰用户。

  - 处理语音重叠的缺陷提醒：实时语音交互需显式做打断检测/VAD 与 turn-taking 策略，否则正确回复也会损害体验。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：实时任务指导（例如佩戴智能眼镜完成手工操作）本质灵活：同一时刻可能有多种合理回复与时机，有时最佳策略是保持沉默。现有基准常使用合成对话作为固定目标，忽略了这种灵活性。

**方法**：FLUID 基于自然人类-人类指导数据（WTaG、HoloAssist），将每次干预（intervention）用三个要素建模：支持证据（supporting evidence）、干预必要性（necessity）、时机灵活性（timing flexibility）。该表示既用于评估灵活指导，也用于构建实时多模态 agent。Agent 接收用户第一视角视频流，持续判断是否干预、何时干预以及说什么，并对“沉默”动作显式建模。

**关键结果**：在与其他评估系统的对比中，FLUID agent 在响应正确性、干预精度、及时指导和响应延迟上取得最强的总体平衡；但在避免语音重叠（speech overlap）方面仍有明显改进空间。
