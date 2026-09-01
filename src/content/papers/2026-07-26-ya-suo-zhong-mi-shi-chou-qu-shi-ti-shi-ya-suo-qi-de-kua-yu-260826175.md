---
title: 'Lost in Compression: A Controlled Cross-Lingual Audit of Extractive Prompt
  Compressors'
title_zh: 压缩中迷失：抽取式提示压缩器的跨语言受控审计
authors:
- Mantas Lukauskas
affiliations:
- Hostinger
- Kaunas University of Technology
arxiv_id: '2608.26175'
url: https://arxiv.org/abs/2608.26175
pdf_url: https://arxiv.org/pdf/2608.26175
published: '2026-07-26'
collected: '2026-09-01'
category: LLM
direction: 跨语言提示压缩审计 · 多语言安全预算
tags:
- prompt compression
- cross-lingual
- LLM inference
- multilingual
- context utilization
- evaluation
one_liner: 英语训练的抽取式提示压缩器在非英语语言上大幅失效，安全压缩预算远小于英语
practical_value: '- 在多语言电商/搜索场景中，不要直接使用英语训练的抽取式压缩器处理非英语上下文；对非英语语言采用更保守的 keep-rate（如
  ≥0.5）或改用确定性方法作为安全基线。

  - 可以借鉴 translate-then-compress 管道：将非英语上下文先翻译成英语再压缩，在三个语言上以约一半 token 成本达到或超过原生压缩效果，适合以英语为中心的模型生态。

  - 评估压缩器时需用目标模型 tokenizer 做预算匹配，并在上线前监控压缩后的 context utilization；警惕学习压缩器版本更新（如 XProvence
  v2）静默清空非英语语境。

  - 自研多语言压缩器时，训练数据的语言覆盖是跨语言迁移的关键，而非模型架构；多语言监督数据能有效消除转移差距。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：抽取式提示压缩可降低 LLM 推理成本，但多数学习压缩器以英语训练，而非英语语言本身 token 成本更高（1.3–1.8×），压缩是否会拉大语言间的性能差距？

**方法**：使用十个语言、五种文字系统的平行数据，预算匹配目标模型 tokenizer，审计四个学习压缩器（LLMLingua-2 XLM-R/mBERT、Kompress-v2、XProvence v1/v2）与四个确定性基线，在十一个目标模型上完成超过 25 万次评估。

**关键结果**：英语训练的压缩器在非英语语言上出现显著转移差距，且随 keep-rate 下降加剧——0.33 keep-rate 下英语保留 57–62% 的归一化上下文利用率，立陶宛语仅 10–24%，中文几乎为 0，尽管中文 token 溢价最小。差距与压缩监督数据语言相关，而非模型架构：多语言训练的 XProvence v1 无差距，但其 v2 重训于翻译数据后在激进阈值下清空 92% 的中文上下文。长上下文场景中，学习压缩在三个非英语语言将效用降至无上下文水平。translate-then-compress 管道在五分之三语言中以约一半 token 成本达到或超过原生压缩。
