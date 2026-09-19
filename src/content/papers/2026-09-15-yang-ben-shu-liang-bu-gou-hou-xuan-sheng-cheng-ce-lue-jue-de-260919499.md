---
title: 'Sample Count Is Not Enough: Candidate-Generation Strategy Shapes the Energy
  and Performance of LLM Test-Time Scaling'
title_zh: 样本数量不够：候选生成策略决定LLM测试时扩展的能量与性能
authors:
- Mobina Kashaniyan
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2609.19499'
url: https://arxiv.org/abs/2609.19499
pdf_url: https://arxiv.org/pdf/2609.19499
published: '2026-09-15'
collected: '2026-09-19'
category: LLM
direction: LLM推理 · 多候选采样批次调度
tags:
- test-time scaling
- candidate generation
- GPU inference
- energy efficiency
- batch scheduling
- LLM reasoning
one_liner: 固定候选数下，少量大批次调用比多次小批次调用显著降低GPU能耗与延迟
practical_value: '- 在电商/广告/搜索中用 LLM 做自一致性、多候选 query 改写或商品文案生成时，优先把多个独立候选合并成一次 batched
  generation，而不是 for 循环串行调用；例如要生成 8 个候选 query，直接 batch_size=8 一次请求，可将 P95 延迟降低约 5-6
  倍、GPU 能耗降低约 4-5 倍。

  - 对多 Agent 系统，如果多个 agent 针对同一 prompt 独立产出候选（如选品、类目预测、出价策略），且相互无依赖，可以聚合为单模型单次批量推理；避免
  agent 调度器串行等结果带来的 GPU 空闲和重复调度开销。

  - 实验评估与 A/B 上线时，不要只记录候选数 N 和 accuracy；把 generation schedule（a×b）、P95 latency、GPU-hours、gross
  GPU energy 纳入日志。同一 N 的不同实现，线上成本差异可能数倍，这直接影响预算与容量估算。

  - 如果显存允许，优先扩大 batch 而非增加请求数；短输出任务和小模型也遵循同样趋势。对推荐场景里大量短文生成（搜索词、标签、push 文案）尤其适合，因为单条输出短，batch
  扩展的显存压力低。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：测试时扩展靠采样多个候选答案提升推理准确率，但通常只用候选数 N 表示预算；同样 N 可以通过一次大批次生成，也可拆成多次小批次调用，系统开销差异很大。  
**方法**：先在 GSM8K 上验证 N 从 1 增至 8 时，Phi-3-mini 和 Qwen2.5-1.5B 准确率分别提升 8.4、18.4 个百分点；然后固定 N=8，比较 1×8、2×4、4×2、8×1 四种生成调度，在 A100 上测量延迟、吞吐、GPU 小时和 GPU 设备能耗，并用 SciQ/V100 短输出任务复验。  
**关键结果**：八个串行调用相比一次批量调用，GPU 设备能耗高 4.64–4.86 倍，P95 延迟高 5.77–6.12 倍；不同节点和模型均一致。候选独立且显存允许时，少次大批次调用更高效；评测不能只看候选数和准确率，还要报告生成调度与 GPU 级系统指标。
