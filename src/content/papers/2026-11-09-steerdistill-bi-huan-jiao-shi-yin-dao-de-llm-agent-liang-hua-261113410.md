---
title: 'SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering'
title_zh: SteerDistill：闭环教师引导的 LLM Agent 量化蒸馏
authors:
- Genming Cui
- Xiangyu Li
- Zixu Hao
- Xin Ding
- Yunxin Liu
- Ting Cao
affiliations:
- Institute for AI Industry Research (AIR), Tsinghua University
- University of Science and Technology of China
arxiv_id: '2611.13410'
url: https://arxiv.org/abs/2611.13410
pdf_url: https://arxiv.org/pdf/2611.13410
published: '2026-11-09'
collected: '2026-11-13'
category: Training
direction: 低比特 LLM Agent 蒸馏
tags:
- LLM Agents
- Quantization
- Knowledge Distillation
- Teacher Steering
- W4A16
one_liner: 全精度教师闭环引导量化学生修正失败轨迹并内化，使 W4A16 Agent 接近 BF16 且推理免引导
practical_value: '- 电商/客服 Agent 低比特部署时，可用闭环 teacher steering 生成学生失败上下文中的修正数据，而不只是重放全精度轨迹；把环境执行结果作为
  verifier 过滤无效修正，类似线上用业务指标或 simulator 做 reward 校验。

  - 蒸馏目标不要直接匹配全精度教师输出，而是在纠正 turn 匹配 steered student 的预测、其他 turn 匹配教师；这样更贴近学生能力边界，避免不可学目标，且推理时不需要教师引导，适合低延迟线上
  Agent。

  - W4A16 量化在 Agentic benchmark 上与 BF16 差距可控制在 1 分内，训练 GPU 小时比 QeRL 少 67%；对需要降推理成本的高并发推荐/Agent
  服务，可作为低比特量化的可行路线参考。

  - 闭环修正后成功轨迹更短，提示可在多轮交互任务中同时优化任务成功率和路径效率，对导购、任务型对话等场景有借鉴意义。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：低比特量化能降低 LLM Agent 推理成本，但会损害任务成功率。失败轨迹显示，量化 Agent 容易忽略任务要求或环境条件，行为偏离全精度参考；而离线数据难以覆盖学生失败上下文，学生自身 rollout 在这些上下文中也缺少正确响应。

**方法关键点**：SteerDistill 是一种量化感知蒸馏方法。全精度教师对学生失败响应给出 steering prompt，学生执行后由环境验证并反馈，教师据此迭代修正，得到局部可验证的行为校正。训练时不依赖教师引导：在纠正 turn，让学生匹配 steered student 的预测；在其他 turn，匹配全精度教师。这样将修正内化到学生，推理时无需教师参与。

**关键结果**：在 5 个 agentic benchmark、3 个模型上，W4A16 下 SteerDistill 平均得分超过最强量化基线 1.67–2.18 分，与 BF16 差距在 1 分内；在 τ²-Bench 上成功率比 QeRL 高 1.84 个百分点，训练 GPU 小时减少 67%，成功轨迹也更短。
