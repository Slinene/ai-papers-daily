---
title: 'Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason
  Beyond Their Parametric Knowledge'
title_zh: 知道何时思考不够：教小推理模型超越参数知识进行推理
authors:
- Chanuk Lee
- Minki Kang
- Sangwoo Park
- Woongyeong Yeo
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2609.34327'
url: https://arxiv.org/abs/2609.34327
pdf_url: https://arxiv.org/pdf/2609.34327
published: '2026-09-27'
collected: '2026-09-29'
category: Reasoning
direction: 小模型推理 · 选择性外部查询
tags:
- small reasoning models
- knowledge bottleneck
- selective querying
- cost-aware RL
- test-time scaling
one_liner: 区分执行瓶颈与知识瓶颈，训练小模型只在知识瓶颈时查询强模型，4B 超越 14B 且成本低 2.7 倍
practical_value: '- **区分内部执行瓶颈与外部知识瓶颈**：在 LLM 驱动的搜索/推荐 Agent 中，当模型反复反思但答案不变、或继续生成也拿不到正确结果时，不要只加长推理；可监控中间状态的成功率/答案熵，识别知识缺口并触发商品知识库、检索或更强模型。

  - **把强模型封装成多深度查询工具**：让策略学习是否问、问什么、用哪个成本档，比固定检索或开场就查更省；外部模型只接收子查询而不看完整问题，避免答案委派和泄露。

  - **两阶段训练可落地**：先用 SFT 合成“救援轨迹”教会小模型调用工具，再用 cost-aware GRPO 校准查询时机和深度；仅对成功轨迹惩罚成本，能学到多轮廉价查询，接近深后端性能、接近浅后端成本。

  - **经济性设计值得借鉴**：在电商导购、政策问答等知识密集场景，可复用其 pass@k 与单位成本曲线评估，通过 GPU/API 价格扫描验证成本优势的稳健性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
测试时计算缩放对小推理模型很有吸引力，但更多思考并不总是有效。作者通过干预中间推理状态，发现失败分两类：执行瓶颈——正确解仍可达，反思能恢复；知识瓶颈——继续内部推理不够，需要外部信息。小模型频繁表达不确定性却很少转化为进展，反思主要巩固已可达解；且小模型参数知识更少，利用外部信息的能力也更弱。

**方法关键点**  
- 引入 FlyBy，训练 4B/8B 模型先推理，再诊断是否遇到知识瓶颈，仅在需要时查询更强模型。
- 外部模型作为 multi-depth query 动作：模型决定是否查询、问什么、选哪个深度；深度 1/2/3 对应不同强度和成本的 DeepSeek 后端。
- 外部模型只接收短查询，不接触原始问题，防止答案委派。
- 两阶段优化：SFT 从失败轨迹合成“救援轨迹”引导查询动作空间；再用 cost-aware GRPO 校准查询时机与成本，奖励只在成功轨迹上扣成本。

**关键实验**  
在 6 个 benchmark 的 1,158 道 hard problems 上，FlyBy-4B 达到 45.96% pass@8，超过 Qwen3-14B 的 41.64%，且服务成本低 2.7 倍；FlyBy-8B 进一步提升至 51.81%。在 Qwen3-4B 16 次采样全失败的问题上，FlyBy-4B 仍取得 28.7% pass@8。RL 让模型从单次委派变成多轮廉价查询，实现接近深后端性能、接近浅后端成本。

**最值得记住的一句话**  
有效的测试时缩放，不只是让模型思考更久，而是让模型知道何时思考不够，并有能力用最低成本获取缺失的外部知识。
