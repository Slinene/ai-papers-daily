---
title: 'CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World
  Model-Driven Harness'
title_zh: CoWorld Reasoner：以可进化视频世界模型工具链驱动智能体多模态推理
authors:
- Dongjie Cheng
- Ruifeng Yuan
- Ran Wei
- Ning Song
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Hangzhou Diagens Biotechnology Co., Ltd
arxiv_id: '2610.21910'
url: https://arxiv.org/abs/2610.21910
pdf_url: https://arxiv.org/pdf/2610.21910
published: '2026-10-14'
collected: '2026-10-18'
category: Multimodal
direction: Agent 多模态推理 · VWM 工具进化
tags:
- Video World Model
- Agentic Reasoning
- VLM
- Multimodal
- Tool Evolution
- Spatiotemporal
one_liner: Agentic 框架将视频世界模型作为统一视觉推理引擎，通过可进化 tool/skill 动态生成视觉证据，多基准相对提升 11.8%–13.0%
practical_value: '- 在电商多模态商品理解中，可借鉴「视觉想象作为额外证据」范式：对只有单图/短视频的商品，用世界模型生成多角度、场景变化或使用过程片段，作为
  VLM 推理补充输入，降低对完整 3D/视频采集的依赖。

  - 采用「工具 + 技能」双层 harness 控制生成行为：把生成模型封装为多个视觉操作工具（如视角合成、时序补全），用结构化 skill 描述指导 LLM
  决定是否/何时/如何生成，避免固定 pipeline 只做单一想象形式，适配标题生成、详情页卖点抽取等多任务。

  - VLM-VWM Harness Co-Evolution 的思路可直接迁移到推荐 Agent 的 tool/prompt 迭代：记录执行失败/低质量输出，用反馈让
  LLM 修订工具描述、技能文档和调用代码；模型权重冻结，可以低成本持续优化线上 Agent 的视觉工具链。

  - 在搜索/推荐多模态评测中，该方法提示：对需要时空/因果推理的任务，单纯 VLM 直接推理不足，应加入生成型证据接入和 agentic 调用框架；业务中可先在商品视频问答、用户上传视频审核等任务上试点世界模型辅助取证。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**： VLM 在静态图像理解上已成熟，但面向运动、动作、视角变化等时空推理时，仅靠输入图像往往证据不足。视频世界模型（VWM）能生成任务相关的视觉内容作为额外证据，但已有方法通常采用固定 pipeline，只支持预定义的视觉想象形式（如新视角合成），难以适配多样推理任务。

**方法关键点**：提出 CoWorld Reasoner，以 VWM 为统一视觉推理引擎。其 Video World Model-Driven Harness 通过工具暴露多种视觉操作，并用技能（skills）指导 VLM 完成四步决策：是否想象、选操作、构建生成请求、解释视觉证据。进一步提出 VLM-VWM Harness Co-Evolution，基于执行反馈联合修订工具、技能和执行代码，模型权重保持冻结。

**关键结果**：在 7 个基准上（空间智能、时序因果、感知推理）超越同 VLM 直接推理；最强变体全部 7 个基准提升，MMSI 相对精度提升 11.8%，ERQA 提升 13.0%，并在 5 个基准上超过所有 5 个 evolving baselines。
