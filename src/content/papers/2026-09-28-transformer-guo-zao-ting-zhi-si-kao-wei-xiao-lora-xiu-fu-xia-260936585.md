---
title: Transformers Stop Thinking Too Early, and a Tiny LoRA Fixes It
title_zh: Transformer 过早停止思考，微小 LoRA 修复上下文链跟随
authors:
- Zehao Jin
- Ruixuan Deng
- Junran Wang
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.36585'
url: https://arxiv.org/abs/2609.36585
pdf_url: https://arxiv.org/pdf/2609.36585
published: '2026-09-28'
collected: '2026-10-03'
category: Reasoning
direction: LLM 链式推理深度与轻量 LoRA 干预
tags:
- LoRA
- reasoning
- context following
- mechanistic interpretability
- long-chain
one_liner: 发现基础模型在上下文引用链上仅能跟随1.4–3.6行，早期层加rank-8 LoRA可扩展至数十行，默认答案低估了计算能力
practical_value: '- 在搜索/推荐 Agent 处理多跳规则、属性继承或长会话状态时，先评测基础模型在长链条上下文跟随上的真实上限；若出现早期断裂，可在单个早期
  Transformer 层加 rank-8 LoRA 做任务微调，冻结主模型，低成本解锁长链推理。

  - 利用论文的冻结模型测量方法定位“最后有效干预层”，将 LoRA 插入该层附近，而不是每层都加 adapter，可减少训练参数与调参成本，并快速诊断现有 LLM
  的推理瓶颈。

  - 对需要循环迭代的 agentic 工作流（多轮检索/重写、复杂促销规则计算），可复用“同一 LoRA 在每次循环生效”的结论，通过 Loop+LoRA 扩展可达深度，无需重训大模型。

  - 注意这是任务特定 LoRA，不同业务任务需单独训练，但释放的潜在能力提示应重新评估默认模型输出，避免因默认早停而低估 LLM 的可用计算深度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：预训练 transformer 在上下文引用链（如 A=B, B=C, ... print）上仅能可靠跟随 1.4–3.6 行（13 个基础模型，中位数 2.2），额外预训练循环增益很小，说明默认计算早停，模型潜在能力被低估。

**方法关键点**：在某一早期层插入任务训练的 rank-8 LoRA，冻结全部主模型权重；通过分析发现 LoRA 启动“接力”：程序行在中间层短范围内传递链身份，冻结的注意力头逐步读取更远的链，且移除父行注意力会终止接力；还提出冻结模型测量方法定位最后有效干预层。

**关键结果**：Qwen3-8B 在 24 行链上从 15.5% 提升至 99% 精确匹配；更长训练的 LoRA 可达 50 行；Ouro-1.4B 4 循环达 60 行，8 循环至少 160 行；多个模型在 MuSiQue 上 EM 提升 9.4–17.9 分；测量方法在四个留出模型中的三个成功定位有效层。
