---
title: 'MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes'
title_zh: MetroLLM-Bench：评估语言模型作为交通售票机运行时的基准
authors:
- Remco Hendriks
affiliations:
- Continker
arxiv_id: '2609.10016'
url: https://arxiv.org/abs/2609.10016
pdf_url: https://arxiv.org/pdf/2609.10016
published: '2026-09-08'
collected: '2026-09-12'
category: Eval
direction: LLM 工具调用与策略决策基准评估
tags:
- benchmark
- tool_calling
- PEFT
- structured_output
- LLM_judge
- policy_layer
one_liner: 955 例交通售票机工具调用基准，4B PEFT 模型在 Tier1 上超越 GPT-5.6 且部署成本极低
practical_value: '- 规则引擎 + LLM 补充：先用确定性规则覆盖标准场景，仅将政策调整、复合场景、无障碍等边界 case 交给 LLM，可降低延迟与成本，同时利用
  LLM 灵活适应业务规则变化。

  - 小模型 PEFT 已够用：在特定领域工具调用任务上，4B 模型经 PEFT 可匹配甚至超越大模型，且 PEFT 增益随模型尺寸增大而递减；业务中可优先微调小模型而非追求大参数量，显著降低硬件与部署成本。

  - 分层评估体系：将任务分为确定性 Tier1（自动评分）和语义 Tier2（LLM judge），并发布标准化 harness；在电商 Agent、推荐解释生成等场景可借鉴，先保证结构化动作正确，再评估语义质量。

  - 机器可渲染终端状态：要求模型输出结构化、可直接执行的状态（如 action、quote），避免自由文本；这对生成式推荐（如直接生成 Semantic ID
  或排序指令）有直接参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：交通售票机传统采用状态机编码，运营变更需走代码部署周期，论文探索用 LLM 替代策略层，使 kiosk 能直接理解政策文本并调用工具生成结构化终端状态。

方法关键点：发布 MetroLLM-Bench，含 955 个用例，覆盖 6 个真实地铁系统（37 到 414 站）和 11 类任务：路线、票价计算、中断、无障碍、对抗输入等。每个用例要求模型调用结构化工具并提交机器可渲染的 terminal state（结果、票价、kiosk action）。评分分两层：Tier1 为 14 个确定性组件自动评分，Tier2 为 8 个语义质量组件（6 个用 LLM judge）。717 例用于训练数据生成，238 例 held-out 评估。

关键结果：评估 26 个模型（6 个厂商，23 个排名）。4B Qwen 3.5 经 PEFT 后在 held-out 集 Tier1 达 91.3，超过 GPT-5.6 两种配置（90.6/90.0），与 GPT-5.4 full at maximum reasoning effort（91.4）持平，模型仅 2.6 GB Q4_K_M。9B 和 27B 学生模型在 Tier1 上无进一步提升。PEFT 增益随基础模型增大而递减：2B 增益 +7.03，27B 为 -0.91。确定性规则基线 Tier1 为 84.6，LLM 优势集中在政策适配、复合场景、无障碍和时间推理。Muse Glimmer 30B 综合排名第一；服务配置可导致 Qwen 3.5 与 3.8 比较移动 2.7 分。
