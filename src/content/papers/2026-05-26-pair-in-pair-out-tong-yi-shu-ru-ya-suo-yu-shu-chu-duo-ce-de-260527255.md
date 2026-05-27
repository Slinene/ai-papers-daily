---
title: 'Pair-In, Pair-Out: Latent Multi-Token Prediction for Efficient LLMs'
title_zh: Pair-In, Pair-Out：统一输入压缩与输出多token预测的高效LLM推理
authors:
- Wenhui Tan
- Minghao Li
- Xiaoqian Ma
- Siqi Fan
- Xiusheng Huang
- Liujie Zhang
- Ruihua Song
- Weihang Chen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- AI Platform, Xiaohongshu Inc.
- University of Electronic Science and Technology of China
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2605.27255'
url: https://arxiv.org/abs/2605.27255
pdf_url: https://arxiv.org/pdf/2605.27255
published: '2026-05-26'
collected: '2026-05-27'
category: LLM
direction: 高效推理 · 输入压缩与多token预测统一
tags:
- Multi-Token Prediction
- Speculative Decoding
- Latent Compression
- On-Policy Distillation
- Confidence Head
- LLM Inference
one_liner: 通过对称的 pair-in 压缩和 pair-out MTP 头，用 on-policy 蒸馏免费训练的置信头替代验证器，实现精度不降的推理加速。
practical_value: '- **将输入压缩与输出多token预测视为对称操作**：若业务下游需部署推理流水线，可借鉴 PIPO 将 compressor
  和 MTP head 镜像组合，降低工程复杂度，且可直接利用已有 MTP 模块。

  - **用 on-policy 蒸馏的教师分布训练置信头，无需额外成本**：在已有 OPD 流程中，教师/学生 token 概率天然提供 speculative
  decoding 的接受率标签，可零开销训练一个轻量 MLP 替代昂贵的 verifier 前传，适合电商/Agent 场景中高频推理的成本控制。

  - **通过随机 padding 注入训练，让模型学会单双token灵活切换**：业务中可能遇到不确定的 draft 质量，可参照 PIPO 的做法，在 SFT
  阶段按比例插入 padding token，使模型获得拒绝 draft 的回退能力，提升可靠性。

  - **在长上下文高吞吐场景优势明显**：PIPO 的 TTFT 加速在长 prompt 时更显著（2K→2.64× @128K），适合需要处理长文档、多轮对话或复杂推理链的电商推荐解释、Agent
  规划等任务。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM 的长推理链使自回归解码成为推理瓶颈，现有方法分别从输入侧（隐式压缩）和输出侧（投机解码/多token预测）加速，但二者独立且输出侧常需昂贵的 verifier 前传。本工作观察到隐式压缩器与多token预测头互为镜像，且 on-policy 蒸馏的教师天然扮演投机解码 verifier，从而提出统一框架 PIPO。

**方法**：
- 架构：每两个连续 token 嵌入经 MLP 压缩为一个隐变量输入，骨干网络输出 backbone token 后由 MTP 头再预测一个 draft token，实现 pair-in / pair-out，使有效序列长度减半、每步输出翻倍。
- 置信头：从骨干与 MTP 的隐状态拼接，经 MLP 输出接受概率，代替原 verifier 前传；训练时该概率的监督信号来自 OPD 中的教师/学生 token 概率比率（即投机采样接受概率），零额外开销。
- 训练：两阶段——SFT 用 next-pair 预测并随机插入 padding 模拟拒绝场景；OPD 用学生自身 rollout 进行反向 KL 蒸馏，同时训练置信头。

**关键结果**：在 AIME 2025、GPQA-Diamond、LiveCodeBench v6、LongBench v2 上，Qwen3.5-4B/9B 作为骨干，PIPO + OPD 的 pass@4 比 Regular decoding 最高提升 +7.15 pp，同时 TTFT 最高 2.64×、TPOT 最高 2.07× 加速，且 pass@4 随上下文预算增加优势扩大。

**记住**：教师分布即免费验证器——on-policy 蒸馏的副产品可训出轻量置信头，将推理时每步昂贵的验证前传替换为几乎无成本的 MLP 调用。
