---
title: 'KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux
  with Runtime-Free Verifiable Rewards'
title_zh: KaliBench：面向 Kali Linux 的细粒度网络安全工具调用基准与免运行时可验证奖励
authors:
- Pengfei Li
- Naufal Suryanto
- Sicheng Zhang
- Muzammal Naseer
affiliations:
- Khalifa University
- University of Western Australia
arxiv_id: '2610.02206'
url: https://arxiv.org/abs/2610.02206
pdf_url: https://arxiv.org/pdf/2610.02206
published: '2026-09-30'
collected: '2026-10-03'
category: Eval
direction: LLM 工具调用评测与可验证奖励训练
tags:
- LLM
- Tool Use
- CLI
- Benchmark
- Verifiable Reward
- Cybersecurity
one_liner: 构建 8,504 条自然语言到 CLI 的细粒度基准，用可验证奖励把 8B 模型训练到接近 685B MoE 水平
practical_value: '- 在电商/广告 Agent 中，若需要模型生成参数化工具调用（如推荐 API、搜索 API、营销活动配置），可仿照 KaliBench
  构建「意图 → 结构化调用」的细粒度评测集。对工具名、参数名、枚举值做 canonicalization 和别名归一化，能定位到 flag 绑定、参数顺序等细粒度错误，而不是只看端到端失败率。

  - 设计“无运行时可验证奖励”：用 gold 命令/参数与预测结果做确定性匹配（可包含语义等价的 alias 映射）作为 RL 奖励，避免每次 rollout
  都跑真实线上环境；适合用 8B 级小模型做工具调用训练，压缩到接近大 MoE 效果，降低推理成本。

  - 构建训练数据时采用多阶段验证：LLM 初判 + 沙箱/模拟器执行 + 人工复核。对业务中高价值的 Agent 工具调用数据，这一组合能显著降低不可执行或错误参数样本进入
  SFT/RL 集。

  - 结果显示无工具 schema 提示时模型 exact 匹配很弱；在业务 Agent 中应尽量提供结构化 tool schema、枚举约束或 few-shot
  示例，把生成空间从自由文本 CLI 转向受约束 JSON 调用，以提升可执行率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：网络安全任务依赖严格 CLI，细微 flag/参数顺序错误都会导致命令无效；现有评测偏知识问答或端到端 agent，不直接测自然语言到可执行命令的翻译能力。

**方法**：提出 KaliBench，包含 8,504 条 query–command 对，覆盖 1,642 个 Kali 工具、23 个能力维度和 5 个安全阶段。构建流程基于文档/手册，采用确定性命令规范化与别名感知评测，支持细粒度检查工具选择、flag–value 绑定、参数顺序。通过 LLM 校验、沙箱终端执行和人工修正的多阶段验证保证数据质量。基于细粒度确定性信号，KaliBench 还能提供免运行时可验证奖励用于训练。

**关键结果**：在 3 种评测模式下，24 个通用和安全开源模型在无工具提示设置中 exact-command 准确率均未超过 42%；用 KaliBench 奖励做 SFT + RL 后，8B 模型性能接近 685B MoE。
