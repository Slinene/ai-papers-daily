---
title: 'MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory'
title_zh: MemEye：以视觉为中心的多模态智能体记忆评估框架
authors:
- Minghao Guo
- Qingyue Jiao
- Zeru Shi
- Yihao Quan
- Boxuan Zhang
- Danrui Li
- Liwei Che
- Wujiang Xu
- Shilong Liu
- Zirui Liu
arxiv_id: '2605.15128'
url: https://arxiv.org/abs/2605.15128
pdf_url: https://arxiv.org/pdf/2605.15128
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- Multimodal Agent
- Memory
- Evaluation
- Visual Evidence
- VLM
- Benchmark
one_liner: 从视觉证据粒度和推理方式两维评估多模态记忆，揭示现有架构在细节保留与状态变化推理上的缺陷
score: 8
source: huggingface-daily
depth: abstract
---

**动机**：现有长时多模态记忆评估常依赖文本描述即可回答视觉问题，缺乏对细粒度视觉证据保留以及随时间变化的状态推理的测试，导致对记忆能力的评估失真。

**方法关键点**：
- 提出MemEye框架，从两个维度定义记忆评估：
  1. **决定性视觉证据的粒度**（从场景级到像素级），测量需要多精细的视觉信息才能正确回答；
  2. **检索证据的使用方式**（从单一证据检索到进化式综合），测量如何整合跨时间步的视觉变化。
- 构建8个生活场景任务，覆盖不同粒度和推理模式，并通过消融驱动的验证门确保问题可回答性、抵抗捷径、视觉必需性和推理结构。
- 在4个VLM骨干上评估13种记忆方法，分析证据路由、时间跟踪和细节提取能力。

**关键结果**：当前架构在保留像素级视觉细节和推理状态变化方面仍严重不足，长时多模态记忆性能受证据路由、时间跟踪和细节提取的瓶颈限制。
