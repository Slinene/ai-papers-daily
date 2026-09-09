---
title: Online Draft Co-Training for Speculative Decoding in Large-Scale, Long-Context
  RL Post-Training
title_zh: 大规模长上下文 RL 后训练中的在线草稿协同训练投机解码系统
authors:
- Zili Wang
- Zhaopeng Qiu
- Yuekai Zhang
- Shuang Yu
- Junjie Lai
affiliations:
- NVIDIA
arxiv_id: '2609.07108'
url: https://arxiv.org/abs/2609.07108
pdf_url: https://arxiv.org/pdf/2609.07108
published: '2026-09-06'
collected: '2026-09-09'
category: Training
direction: 训练系统 · Speculative Decoding
tags:
- Speculative Decoding
- Online Co-Training
- Long Context
- Context Parallel
- Pipeline Parallel
- RL Post-Training
one_liner: 构建端到端在线协同训练系统，解决长上下文下上下文并行分支注意力与流水线并行特征传输两大障碍，实现最高 122B 模型显著投机解码加速
practical_value: '- **RL 策略训练加速**：若团队用 RL 微调 LLM-based 推荐或 Agent 策略，rollout 生成常占大头；可借鉴
  speculative decoding 并让 draft 模型在线 co-train 以跟上策略漂移，维持 acceptance length 从而获得端到端加速。

  - **长上下文分支注意力合并**：论文扩展 zigzag ring attention，将 rank-local 分支注意力与 causal 主序列合并，解决
  CP 不支持分支注意力的问题，支持 256K tokens 强扩展并显著省显存；对长序列用户行为/会话建模的训练有直接工程参考价值。

  - **PP 跨 stage 特征解耦传输**：TapChannel 用独立通道传输中间 target features，不干扰主流水线 schedule，可用于在主模型与轻量
  draft 模型协同训练中高效传递辅助特征，避免改造现有 pipeline。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
RL post-training 时间成本由 rollout generation 主导；speculative decoding 通过 draft 模型并行加速验证，但策略不断演化会导致 draft 接受长度下降。在线协同训练可让 draft 跟上策略，但扩展到长上下文大模型遇到两个障碍：标准 causal context parallel 不支持分支注意力；pipeline parallel 下 target features 跨 stage 无法直接获取。

## 方法关键点
- 针对 CP：扩展 packed, load-balanced zigzag ring attention，将 rank-local 分支注意力合并进 causal main-sequence attention，使长上下文下 draft/target 分支可高效训练。
- 针对 PP：提出 TapChannel，通过独立路径将中间 target features 跨 stage 传输，不改变 pipeline schedule，避免对训练流程的干扰。

## 关键结果
协同训练后的 draft 模型能紧密跟踪策略 baseline；在模型规模最高 122B 上取得显著 rollout 与端到端加速。CP 设计在 256K tokens 下实现强扩展，相比此前工作显著节省显存；PP 传输带来的额外开销适中。
