---
title: 'PreSTO: Predictive Subtree Prefetching for Fast LLM Power Sampling'
title_zh: PreSTO：预测子树预取加速 LLM 幂采样
authors:
- Nan Jiang
- Panagiotis Theodoropoulos
- Wei Deng
affiliations:
- University of Texas at El Paso
- Georgia Institute of Technology
- Morgan Stanley
arxiv_id: '2610.13171'
url: https://arxiv.org/abs/2610.13171
pdf_url: https://arxiv.org/pdf/2610.13171
published: '2026-10-08'
collected: '2026-10-12'
category: LLM
direction: LLM 推理加速 · 幂采样预取
tags:
- Power Sampling
- Metropolis-Hastings
- Prefetching
- LLM Inference
- Test-time Scaling
one_liner: 将 MH 串行接受/拒绝展开为决策树批量预取，不改转移核，加速 LLM 幂采样 1.7-2.3 倍
practical_value: '- 若业务在 LLM 推理中采用 self-consistency / best-of-n / 拒绝采样（含 MH 接受/拒绝），可将串行“提出-判断”展开为决策树，用一次
  batch 请求预取多个可能分支，再沿原始接受规则回放，分布不变但大幅减少模型调用轮次；适用于生成 item 标题、搜索 query 改写、广告文案等多候选投票场景。

  - 预测性子树遍历规则：用轻量模型预测哪些分支更可能带来更多有效转移，优先预取高收益子树，减少无效 KV cache 与计算；在 Agent 多轮推理、RAG
  多跳 query 改写中可借鉴“先预测路径价值，再决定 speculative 分支”的思路。

  - 工程核心是 batch 内做子树级 speculative execution 并保证 kernel 不变，无需改模型或采样器；已有推理框架若支持 batch
  prefill/continue，可低成本实验。

  - 整体偏学术，若业务对延迟不敏感或没有大规模 MH 采样，直接收益有限；主要价值在 LLM inference optimization 的方法论。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Power sampling 通过对 base LLM 分布做锐化采样，能在测试时提升推理能力，但 PowerMH 采样器的 Metropolis–Hastings (MH) 更新串行执行，每个 accept/reject 决定下一个 proposal，导致模型调用次数多。已有工作通过替换采样器（SMC、lookahead）或蒸馏来加速。

方法：PreSTO 保持 MH transition kernel 不变，将未来 MH 结果视为 accept/reject 决策树；每次模型调用批量生成预取子树里的多个 proposal，并沿实际路径按原始 MH 规则回放。观察到 MH 实际只触及稀疏且接近单链的部分，进一步提出 predictive traversal rule，选择预测能完成最多有效转移的子树。

结果：在 7 个数据集、5 个 base LLM 上，相对 PowerMH、EntropyCut、MultiTryMH 分别取得中位 1.71×、1.91×、2.33× 加速；前两者中位减少 3.9× 次模型调用，每次调用仅变长 2.1×。在 LCB V6 + Qwen3.5-9B 上，预测遍历比默认广度优先再快 1.25×–1.37×。
