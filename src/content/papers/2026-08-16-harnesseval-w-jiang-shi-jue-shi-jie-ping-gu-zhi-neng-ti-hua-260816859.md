---
title: 'HarnessEval-W: Agentifying the Evaluation of Visual Worlds'
title_zh: HarnessEval-W：将视觉世界评估智能体化
authors:
- Weiliang Chen
- Haowen Sun
- Jun Gao
- Jiawei Chi
- Hanyang Wang
- Qiyu Dai
- Yihao Li
- Hao Li
- Jingnan Gao
- Yi-Hsin Hung
arxiv_id: '2608.16859'
url: https://arxiv.org/abs/2608.16859
pdf_url: https://arxiv.org/pdf/2608.16859
published: '2026-08-16'
collected: '2026-08-19'
category: Eval
direction: 多智能体分层评估世界模型
tags:
- Evaluation
- World Models
- Multi-Agent
- Visual Reasoning
- Benchmark
one_liner: 提出分层多智能体评估流程，把世界模型评估转化为可验证的证据树
practical_value: '- 借鉴其分层 agent 评估架构：将复杂评估任务拆解为多个可测量子问题，每个子问题交给专门的子 agent 处理，父 agent
  汇总证据。适合评估生成式推荐或搜索 Agent 的输出质量，例如分解「推荐相关性」「文本流畅性」「商品属性一致性」等维度并行诊断。

  - 强调推理链与证据树：评估结果必须能追溯到具体证据，而非仅给出分数。在业务中可用于 user study 自动化替代，或对推荐理由、搜索改写结果做可解释的质量审计。

  - 子 agent 配备定制上下文与诊断工具：可针对不同评估维度注入业务规则、商品知识图谱、历史 CTR 等工具，让评估更贴近业务场景。

  - 开源 pipeline 可作为内部评测框架的基础，尤其适合多模态生成（如商品图、短视频、虚拟主播）的质量评估。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有世界模型评估只输出标量分数，缺乏支撑评分的推理链，无法验证判断依据。人类能自然识别物理、因果、世界状态演化错误，但没有自动化的方法保留可检查的推理过程。

**方法关键点**：
- 提出 HarnessEval-W，将 LLM 生态中的 harness 范式引入世界模型评测。
- 不再使用固定 rubric，而是让父 agent 解读评测案例上下文，将评测问题分解为可测量的子问题。
- 生成专门的子 agent，每个子 agent 配备定制上下文和诊断工具，独立推理各自子问题。
- 父 agent 验证子 agent 收集的证据，汇总成最终判定，形成透明的证据树。
- 每个评测结果都有完整推理链，可验证、可细粒度诊断。

**关键结果**：
- 在 18 个代表性世界模型、330 个评测案例上，HarnessEval-W 的判断与人类偏好高度一致。
- 对每个生成 rollout 提供可验证的细粒度诊断。
- 开源完整 pipeline，支持社区扩展新技能和评测案例。
