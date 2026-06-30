---
title: 'Thinking While Speaking: Inference-Time Knowledge Transfer for Responsive
  and Intelligent Conversational Voice Agents'
title_zh: 边说边想：推理时知识迁移实现高响应智能语音助手
authors:
- Vidya Srinivas
- Zachary Englhardt
- Shwetak Patel
- Vikram Iyer
- Maximus Powers
affiliations:
- Paul G. Allen School of Computer Science & Engineering, University of Washington
arxiv_id: '2511.07397'
url: https://arxiv.org/abs/2511.07397
pdf_url: https://arxiv.org/pdf/2511.07397
published: '2026-06-22'
collected: '2026-06-30'
category: MultiAgent
direction: 多智体协作 · 推理时知识迁移
tags:
- conversational infill
- voice agent
- multi-agent
- latency reduction
- small language models
- knowledge transfer
one_liner: 提出对话填充技术，用小模型即时生成响应并流式融合大模型知识，实现毫秒级首响应且精度接近前沿模型。
practical_value: '- 在延迟敏感的电商客服或语音推荐场景中，可部署双模型架构：小模型（如 135M-1.7B）作为前台，秒级生成自然语言响应；大模型作为后台异步推理，输出精准结果后再流式更新小模型后续生成内容，平衡响应速度与答案质量。

  - 借鉴「对话填充」任务设计，构建合成数据集训练小模型：用大模型生成的多轮对话作为 Reasoner 输出，让 Talker 学习在生成中途插入新事实而不中断话语流，此训练范式可直接复用于回复改写、澄清追问等场景。

  - 工程实现上，可复用 ConvFill 的流式知识整合机制，让实时推荐结果（如补货提醒、优惠信息）在语音播报进行中动态插入，避免用户等待完整生成，提升感知流畅度。

  - 用户研究结果显示，小模型方案在检索类任务中尤为受欢迎，提示在需要外部知识检索的对话推荐（如根据用户实时 query 调取商品知识库）中，该方案能同时满足低延迟和高准确率要求。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
语音助手面临根本矛盾：大模型推理、检索、工具调用过程迭代慢，而对话交互要求毫秒级响应。现有方案只能牺牲响应速度或能力。

**方法与关键点**
提出「对话填充」（conversational infill）范式：用小型 Talker 模型立即生成上下文恰当的初步响应，隐藏大模型 Reasoner 的推理延迟；同时监听 Reasoner 流式输出的新知识，并在生成过程中流畅嵌入，实现“边说边想”。收集涵盖 6 个领域、共 290,571 个示例的合成对话数据集，训练 Talker 完成此填充任务。在 7 款 135M 到 1.7B 参数的小模型上验证了可学性。

**关键结果数字**
系统 ConvFill 在 Apple M2 SoC 上实现毫秒级首响应时间，精度与对应前沿 Reasoner 的差距缩小到 6.3% 以内。18 人用户研究中，ConvFill 综合评分与前沿模型持平，在检索密集型任务上更受偏好，响应速度评价显著更高。结果表明该方法在延迟-能力帕累托前沿上开辟了新空间。
