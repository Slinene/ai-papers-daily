---
title: 'DLite: History-free Speculative Decoding for Agentic AI'
title_zh: DLite：面向 Agentic AI 的无历史投机解码框架
authors:
- Jiaming Xu
- Hanzhen Wang
- Tianlang Zhao
- Jiewen Xiao
- Chengze Yuan
- Jiayi Pan
- Yongkang Zhou
- Jiancai Ye
- Yu Wang
- Guohao Dai
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Tsinghua University
- Infinigence-AI
arxiv_id: '2610.23787'
url: https://arxiv.org/abs/2610.23787
pdf_url: https://arxiv.org/pdf/2610.23787
published: '2026-10-15'
collected: '2026-10-19'
category: LLM
direction: LLM 推理加速 · 历史无关投机解码
tags:
- Speculative Decoding
- Agentic AI
- KV Cache
- LLM Inference
- Draft Model
one_liner: DLite 复用目标模型隐藏状态进行局部投机预测，避免维护历史 KV cache，在 agentic 任务中接受长度达 2-6 并超 DSpark
  最高 70%
practical_value: '- 在电商/推荐系统的多轮对话 agent（如客服、导购）中，长历史上下文会让 draft model 接受长度骤降且 KV cache
  开销大；可借鉴 DLite 的 history-free 思路：不单独维护 draft model 的历史 KV cache，直接复用 target model
  的隐藏状态做局部预测，大幅降低显存和延迟。

  - 两阶段训练策略（先对齐隐藏状态再训练 sequential head 恢复块内因果依赖）适合训练自定义轻量 draft 模块，在效果和资源间取得平衡，可复用于需要低延迟的在线推理服务。

  - 局部简单预测替代全局上下文建模，在 agentic 多轮交互中接受长度仍能保持 2-6，说明牺牲部分长程依赖换取更低的系统开销是可行的工程折中，适合高并发场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
投机解码通过轻量 draft model 生成候选 token 再由 target model 验证，是主流 LLM 推理加速技术。但在 agentic 工作负载下，长且持续演进的上下文、频繁多轮交互，导致现有 draft model 接受长度最多下降 80%，同时维护其历史 KV cache 带来显著系统开销。根因都在于不断增长的历史上下文。

**方法关键点**
DLite 提出历史无关的投机解码框架：直接复用 target model 的上下文隐藏状态，进行局部投机预测，不显式维护历史上下文，将日益复杂的全局建模转化为局部简单预测。引入轻量 sequential head 以低开销恢复块内因果依赖。针对异构历史无关架构，设计两阶段训练策略，先对齐 target model 隐藏状态，再训练 sequential head。

**关键结果**
在通用、长上下文和 agentic 基准上，DLite 接受长度达到 2~6，相比 SOTA 方法 DSpark 最高提升 70%，且避免了历史 KV cache 的维护开销。
