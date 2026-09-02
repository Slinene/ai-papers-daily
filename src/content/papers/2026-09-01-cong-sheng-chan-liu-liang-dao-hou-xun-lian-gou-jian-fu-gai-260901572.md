---
title: 'From Production Traffic to Post-Training: Building a Self-Hosted LLM That
  Covers the Corporate Request Mix'
title_zh: 从生产流量到后训练：构建覆盖企业请求的自托管 LLM
authors:
- Olga Tsymboi
- Dmitrii Stoianov
- Ramil Latypov
- Danil Taranets
- Daniil Dryabin
- Mikhail Gashkov
- Viktor Zelenkovskiy
- Aleksandr Fida
- Gleb Alektorov
- Nikita Gulyakov
affiliations:
- T-Tech
arxiv_id: '2609.01572'
url: https://arxiv.org/abs/2609.01572
pdf_url: https://arxiv.org/pdf/2609.01572
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: LLM 后训练 · 模块化 RL 与权重合并
tags:
- LLM post-training
- GRPO
- SLERP
- function calling
- instruction following
- reward hacking
one_liner: 以模块化 GRPO 专家 + 两阶段 SLERP 融合替代联合多目标 RL，32B 模型在内部流量上超越约 7 倍参数基线并承接 50% 请求
practical_value: '- 模块化 RL + 权重合并：在电商 Agent/工具调用/指令遵循等多目标后训练中，不要把所有 reward 联合训练；按能力轴独立
  GRPO，再 SLERP 合并。新增能力只需训练一个专家、做 eval-only 融合系数搜索，避免重复调联合超参。

  - 多语言 Function Calling 数据：不要直接翻译英文 FC 数据，要基于业务 API schema 原生生成（含本地语言参数值）；对 over-calling
  可通过在训练数据里注入 synthetic irrelevance 抑制，而不是只改 reward。

  - 面向线上真实流量构建离线 benchmark：用模板感知采样（mask 变量 token、LSH 分组、√count 预算）避免模板流量造成的伪多样性；评测按任务类型路由，分类/抽取用
  reference verifier，开放生成用人工校准的 checklist judge，可显著提升评测与人工一致度。

  - 自托管部署成本：32B 非 reasoning + FP8 vLLM 可覆盖大多数企业流量，较 235B 级别模型降低 2.8-3.9 倍 token 成本，适合做统一底座；但前沿
  agentic 能力需保留大模型兜底。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**

企业在数据驻留约束下必须自托管 LLM，但持续引入新模型而不退役旧模型导致 GPU 池碎片化、成本上升。目标是用单个模型覆盖 200+ 内部应用的请求混合，同时保留泛化能力。生产流量错误分析显示，指令遵循/格式错误合计占 37.9%，函数调用流量约占 12%，是主要质量缺口。

**方法关键点**

- 构建生产流量分层 benchmark：模板感知采样（mask 变量 token、LSH 分组、√count 预算）兼顾多样性与代表性；任务分类器路由后，分类/抽取用 reference-based verifier，开放生成用 checklist + pairwise SBS，与人工标注 κ 从 0.62 提升到 0.85。
- 后训练分三轴：通用对齐、指令遵循、函数调用；先共享 SFT，再分叉为三个独立 GRPO 专家，最后两阶段 SLERP 合并。
- 避免联合多目标 RL：联合训练出现跨域 reward 干扰，需要 fragile 超参搜索；合并时先融合两个可验证 reward 专家，再合并通用专家。
- 各专家有特定 reward hacking 修复：IF 可验证 reward 加 prompt-specific RM quality penalty 防语义塌缩；FC 用 Tool-N1 exact-match 但通过数据注入 synthetic irrelevance 防 over-calling；通用 RL 加长度惩罚和高 KL 系数防 verbosity hacking。
- FC 数据用 schema-aware 原生生成，避免英文数据翻译带来的结构风险。

**关键结果**

最终 Qwen3-32B 非 reasoning 模型在内部 Arena 以 69.6 对 65.8、内部 IFEval 以 0.85 对 0.83、内部 BFCL 以 0.79 对 0.77，均超过约 7 倍参数的 Qwen3-235B-A22B-Instruct；AceBench 73.5 vs 70.2，ruWildChat 从 52.0 提升到 80.7，SmartSearch F1 从 0.478 提升到 0.557。生产上单模型承载 116M 月请求、200+ 内部服务，FP8 单 GPU vLLM，95% 延迟 3.2s，TTFT 0.3s，成本降低 2.8-3.9 倍。

**最值得记住的一句话**：企业后训练要模块化，每个弱轴单独训练 RL 专家再合并，而不是联合多目标优化；这样可独立修复 reward hacking，且新增能力只增加一个专家和 eval-only 系数搜索。
