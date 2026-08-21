---
title: 'MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use'
title_zh: MemTrapBench：评测 LLM 记忆使用中的认知陷阱
authors:
- Mengru Wang
- Haozhe Luo
- Zhenqian Xu
- Zhixiang Cui
- Haoming Xu
- Qu Yang
- Jizhan Fang
- Junfeng Fang
- Ningyu Zhang
affiliations:
- Zhejiang University
- National University of Singapore
- Northeastern University
- Heriot-Watt University
- Tencent
arxiv_id: '2608.20202'
url: https://arxiv.org/abs/2608.20202
pdf_url: https://arxiv.org/pdf/2608.20202
published: '2026-08-19'
collected: '2026-08-21'
category: Eval
direction: LLM 记忆认知陷阱评测与缓解
tags:
- LLM Memory
- Cognitive Traps
- Benchmark
- Inference-time Mitigation
- AdaptiveMem
one_liner: 提出 MemTrapBench 评测记忆导致的推理固化与信念扭曲，发现所有记忆策略均不及无记忆，并提出 AdaptiveMem 推理时缓解
practical_value: '- 在电商/推荐 Agent 的多轮记忆系统中，不要只评估记忆检索命中率，还要评测注入记忆后下游任务性能是否下降；可借鉴 MemTrapBench
  的「无记忆 vs 有记忆」对照实验，建立内部回归测试集。

  - 历史记忆可能把模型推理带偏：例如用户历史偏好固化导致推荐多样性下降、旧兴趣覆盖当前会话意图；可参考 Reasoning Fixation 和 Belief
  Distortion 两种陷阱分类，针对性设计监测指标。

  - AdaptiveMem 的推理时元指令成本低，可直接在现有 RAG/记忆流水线上试加：「避免被检索到的历史记忆过度影响当前问题的判断」「优先依据当前用户会话信号」等
  guardrail，作为轻量缓解手段。

  - 对搜索推荐中的 query 改写/兴趣推理模块，可定期注入带干扰记忆的测试样本，检查模型是否被语义相关但误导性的历史信息带偏，提前发现认知陷阱风险。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有 LLM 记忆基准主要评估信息提取、存储、检索是否正确，忽略检索到的记忆如何重塑模型推理并影响当前任务。论文识别出「记忆诱导认知陷阱」：即使记忆被忠实记录且语义相关，也可能扭曲推理或信念，降低当前任务表现。

方法：构建 MemTrapBench，覆盖两类认知陷阱：Reasoning Fixation（推理固化）和 Belief Distortion（信念扭曲）。在两类模型家族和五种代表性记忆框架上评估。提出 AdaptiveMem，一种推理时方法，通过指令让 LLM 避开记忆陷阱。

结果：所有评估的记忆策略均低于无记忆基线，最强方法性能下降超过 10%。AdaptiveMem 在 MemTrapBench 上缓解认知陷阱，同时在标准记忆基准上保持或提升性能，且跨多种记忆框架有效。
