---
title: 'SpecCompact: Accelerating LLM Agent Context Compaction with Slot-Parallel
  Semantic Speculative Verification'
title_zh: SpecCompact：槽并行语义投机验证加速 LLM Agent 上下文压缩
authors:
- Yulu An
- Yifei Feng
- Xiangyang Yin
affiliations:
- New York University
arxiv_id: '2611.06876'
url: https://arxiv.org/abs/2611.06876
pdf_url: https://arxiv.org/pdf/2611.06876
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 上下文压缩 · 语义投机验证
tags:
- Speculative Decoding
- Context Compaction
- LLM Agents
- Slot-Parallel
- Semantic Verification
- LoRA
one_liner: 将 agent 上下文摘要拆成可并行生成的 slots，以行级语义验证做投机压缩，较 Hermes 获 2.04–5.63× 加速
practical_value: '- 导购/客服/长期任务 Agent 的记忆压缩可以直接复用 OpenClaw 式结构化 slots（Goal、Progress、Constraints、Next
  Steps 等），拆槽并行生成能把压缩延迟降数倍；业务上可先做模板化改造，不依赖本文框架也能获得并发收益。

  - 用 0.6B 小模型做 drafter，大面积 LoRA SFT 在目标模型生成的 slot 内容上，再让大模型仅做逐行 positive/negative
  验证和局部修复，比 token-level speculative decoding 更适合语义冗余高的摘要/状态维护；工程上可进一步叠加 shared-prefix
  caching、draft buffering、line-aware stopping，额外带来约 1.2–2.4× 加速。

  - 选型注意：drafter 与 target 能力差距过大会降低接受率，混合注意力模型（如 Qwen3.5 线性注意力层） prefix cache 难以复用，标准
  attention 或显式保存/恢复 recurrent state 会更稳；若要上线，必须对下游任务做 A/B，因为精度波动随模型不同可升可降。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM agent 需要定期 compaction 长交互历史，但大模型总结长文本会带来显著延迟；token-level speculative decoding 虽然无损，但没利用摘要的语义灵活性，单摘要串行生成也慢。论文观察到结构化 summary slots 在相互独立生成时也能保留关键信息：独立生成平均 adequacy 4.73，高于整体生成的 4.44，且改变槽顺序影响很小。因此提出把 slots 作为并行投机单元。

**方法关键点**
- 沿用 OpenClaw 六槽 schema：Goal、Constraints/Preferences、Progress、Key Decisions、Next Steps、Critical Context，每个槽从共享历史独立生成。
- 用小模型 Qwen3-0.6B 做 drafter，对 target 模型生成的 slot 内容做 SFT，LoRA 全线性层，约 50K 训练数据，每条历史生成 6 条样本。
- 在线阶段六条 slot 流并行；drafter 每次提出一行候选行，target verifier 判断该行是否被历史支持且与已接受前缀一致，输出 positive/negative，接受分数 p+/(p++p−)，阈值 η=0.7；拒绝时由 target 生成局部 replacement 并更新前缀，后续 drafting 条件在修复后的前缀。
- 系统优化：independent slot scheduling 并发调度、shared-prefix caching 复用长历史前缀、draft buffering 一次调用生成多行、line-aware stopping 在换行处停止、轻量 checks 跳过空槽/标题/重复行并设置槽级预算。

**关键实验**
在 AppWorld、τ3、LongBench、RULER 上以 Gemma4-31B-IT 和 Qwen3.5-122B-A10B 为目标模型。相对 Hermes 式摘要，SpecCompact 得到 2.04–5.63× compaction speedup：AppWorld Normal 上 Gemma4 从 38.89s 降到 8.26s（4.71×），τ3 上 Gemma4 为 4.28×，Qwen3.5 为 2.04×；LongBench 16k 上分别为 2.49× 和 1.36×。下游任务性能与模型有关：Gemma4 的 AppWorld TGC 较 Hermes 下降约 3–4 个百分点，Qwen3.5 则提升约 1.7–4.8 个百分点。集成到 Hermes 的用户研究中，median compaction latency 从 63.74s 降到 7.28s，中位加速 8.68×。

**最值得记住的一句话**：结构化 slot 并行 + 行级语义验证 + 系统缓存/调度优化，能把长历史 agent 压缩延迟降 2–5 倍，但精度存在模型相关的 trade-off。
