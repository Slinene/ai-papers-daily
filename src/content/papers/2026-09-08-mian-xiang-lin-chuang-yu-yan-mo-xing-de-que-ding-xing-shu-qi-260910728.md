---
title: Towards a Deterministic Math Solver for Clinical Language Models
title_zh: 面向临床语言模型的确定性数学求解器
authors:
- Felipe Ocampo Osorio
- Sebastián Andrés Cajas Ordoñez
- Maximin Lange
- Rafi Al Attrach
- Sahil Kapadia
- Zakaria Laouabdia Sellami
- Angelo Antonio Talio
- Leo Anthony Celi
affiliations:
- MIT Critical Data
- UNC Chapel Hill
- University of Pavia
- Humanitas University
arxiv_id: '2609.10728'
url: https://arxiv.org/abs/2609.10728
pdf_url: https://arxiv.org/pdf/2609.10728
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: LLM 工具调用 · 代码执行器
tags:
- Program-Solve
- code executor
- arithmetic reliability
- tool use
- medical calculators
one_liner: Program-Solve 让 LLM 写 Python 交由受限执行器计算，32B 模型在 MedCalc-Bench 准确率从 83.47%
  提升到 90.53%
practical_value: '- 在电商/广告场景中，凡涉及数值计算（ROAS、LTV、预算分配、出价、统计显著性），不要让 LLM 直接做算术；改为让 LLM
  生成 Python 片段，由受限沙箱执行，返回确定性结果。可参考 Program-Solve 的 prompt 设计：提供公式与变量字典，要求模型只写计算逻辑。

  - 该方案对模型规模敏感：7B 提升 3.29 点但置信区间跨 0，32B 提升 7.05 点且显著。业务落地时如果用小模型，需要先验证代码生成质量，不能默认“加执行器一定好用”。

  - 工程上可复用受限本地执行器的设计：限制 import 集合、单次超时、内存上限，并将公式/变量以 JSON 传入，避免 LLM 直接输出数字；在广告出价或推荐收益预估中同样可建立公式库作为受控资产。

  - 论文提醒：公式版本和变量抽取是瓶颈，即使有 gold variables，7B 仍因代码 bug 或误解丢分。电商复用时应把业务规则（如优惠计算、佣金规则）维护为版本化配置，不依赖
  LLM 记忆；变量抽取单独做，别和计算耦合。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 在算术上不可靠，临床计算器场景中一个数值错误就会改变推荐。常规做法是逐个硬编码计算器为验证函数，成本高。

方法关键点：测试 Program-Solve interface——模型不直接计算，而是编写 case-specific Python 代码，由受限本地执行器作为确定性求解器运行；模型的任务缩减为决定如何调用求解器。在 MedCalc-Bench Verified（1100 病例、55 个计算器）上，对比直接模型算术和手写 22 计算器库，使用 Qwen2.5-7B 和 Qwen2.5-32B-AWQ；审计发现 55 个公式中有 16 个存在版本、使用或系数问题。

关键结果：在提供公式和 gold variables 且两种路线都读完整笔记的条件下，7B 模型 Program-Solve 准确率 75.31% vs 直接算术 72.02%，提升 +3.29 但 95% 区间 [-3.49, 10.38] 跨零；32B 模型 90.53% vs 83.47%，提升 +7.05 [0.47, 14.60] 显著。手写库在其支持的 440 个病例上精确但总体弃权，全量仅 40%。执行器对部分模型更有利，但无法替代验证公式和可靠变量抽取。
