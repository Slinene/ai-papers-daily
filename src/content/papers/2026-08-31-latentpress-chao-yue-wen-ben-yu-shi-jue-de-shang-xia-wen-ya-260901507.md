---
title: 'LatentPress: Context Compression Beyond Text and Vision'
title_zh: LatentPress：超越文本与视觉的上下文压缩
authors:
- Zhengze Zhou
- Hejian Sang
affiliations:
- Cornell University
- Iowa State University
arxiv_id: '2609.01507'
url: https://arxiv.org/abs/2609.01507
pdf_url: https://arxiv.org/pdf/2609.01507
published: '2026-08-31'
collected: '2026-09-04'
category: LLM
direction: LLM 上下文压缩 · 连续 soft tokens
tags:
- context compression
- soft tokens
- memory tokens
- LLM
- long context
- adapter
one_liner: 将对话历史与长文档压缩为连续 memory tokens，直接输入冻结解码器，无需文本重建，4-16倍压缩且性能优于文本摘要与OCR压缩
practical_value: '- 可借鉴的架构：用一个小 writer 将长对话历史、行为序列、工具调用记录压缩成 continuous memory tokens，作为
  frozen LLM 的输入 embedding 直接读取，省去文本重建和检索排序，适合电商对话助手/Agent 的记忆模块。

  - 训练成本极低：只训练 4.2M-26.2M 参数的 adapter（约 decoder 0.1%），frozen decoder，可快速迭代，适合业务场景频繁更新。

  - 压缩比选择：4-8 倍压缩在 QA 上可匹配或超过 raw context，16 倍明显退化；在线 Agent 历史压缩建议先用 4-8 倍，在时延与精度间取平衡。

  - 写入耗时 43ms/对话，读取快 5-9 倍，比文本摘要或 OCR 重建快一个数量级，能满足在线低延迟要求；零样本跨域迁移表现说明 soft tokens
  有潜力作为通用行为表征。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：长运行 assistant/agent 累积的对话、工具调用、文档远超可重读范围，但默认机器接口仍是离散文本，文本摘要或 OCR 压缩需要解码重建，低效且损失信息。

方法关键点：LatentPress 训练一个小 writer，将对话历史和长文档直接写成连续 memory tokens，通过 frozen decoder 的输入 embedding 接口读取，推理时不做文本重建。只训练 adapter（4.2M-26.2M 参数，约 decoder 0.1%），压缩比 4-16 倍。

关键结果数字：LongMemEval 上 7.70 倍压缩下精度 0.504，超过未压缩 evidence 的 0.490，大幅优于文本摘要（0.184）和 OCR 压缩（0.426→0.312）。LongBench-QA 上，域内 writer 在 4-8 倍压缩时匹配或超过 raw context，16 倍落后。写入只需 43ms/对话，比文本摘要或 OCR 重建快约一个数量级；读取比 raw context 或缓存 OCR 快 5-9 倍。零样本迁移实验（UltraChat→LongMemEval、LongMemEval→未见文档域）验证了直接 soft tokens 可作为实用的 machine-facing context interface。
