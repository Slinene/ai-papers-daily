---
title: 'From Given to Gathered Evidence: Agentic Learning for Longitudinal Medical
  Reasoning'
title_zh: 从给定证据到主动采集证据：纵向医疗推理的智能体学习
authors:
- Minye Shao
- Chaohui Yu
- Yixuan Wu
- Fan Wang
- Ling Shao
- Yang Long
affiliations:
- Durham University
- DAMO Academy, Alibaba Group
- Hupan Laboratory
- University of the Chinese Academy of Sciences
arxiv_id: '2609.39566'
url: https://arxiv.org/abs/2609.39566
pdf_url: https://arxiv.org/pdf/2609.39566
published: '2026-09-29'
collected: '2026-10-12'
category: Agent
direction: Agent 工具调用与证据采集强化学习
tags:
- Agentic Learning
- Tool Use
- Reinforcement Learning
- Vision-Language Model
- Medical Reasoning
- Self-Distillation
one_liner: 提出 CASE 角色化临床智能体与训练框架，将证据寻求策略蒸馏到 8B VL 模型，纵向医学基准超越 GPT-5.4 与 Claude Opus
  4.8
practical_value: '- 信息获取型 Agent 的环境设计：不要把用户/商品/内容/广告记录一次性塞进大 context，而是将不同数据源组织成可查询工具（历史订单、点击序列、画像、素材、库存/物流等），让策略模型自主决定“看哪个来源、看多细、是否回看”。这更适配需要跨多证据推理的选品归因、活动复盘、商品冷启动与客服工单诊断。

  - 训练框架可复用：先 SFT 蒸馏 frontier 模型的多轮工具调用轨迹，再做 on-policy RL + 特权自蒸馏 + rubric-based LLM
  反馈；关键是不规定工具调用顺序，只奖励最终结论质量与证据引用合理性。比固定 pipeline 更适合搜索推荐的动态环境。

  - 评测结构化：以真实结果（如 ICD-10 诊断）生成问题，让 Agent 在患者环境中主动取数；业务上可由真实成交/退货/投诉/复购结果构造诊断性问题，评估
  Agent 的证据检索与归因能力，而不是只看预测 AUC。

  - 8B 紧凑策略模型 + 对齐过的评估条件能超过大体量 frontier 模型，说明把前端交互策略训练好，中小模型在特定业务环境中具备落地性价比。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：传统医学基准只考察给定证据下的推理，无法评估临床智能体主动跨病历与纵向影像采集证据的能力。

方法：CASE 由角色化 Clinical Agents for Seeking Evidence、工具调用 harness 和面向紧凑 VL 策略模型的 agentic post-training 组成。新增 UK Biobank 纵向多模态基准：4,739 人、50,401 个基于 ICD-10 真实诊断的临床问题；每个问题对应患者环境，含基线与随访的多序列 MRI 等，智能体自主选择检查哪些 visits/organs/modalities/slices/tools。训练分两阶段：先用 14,734 条 frontier-model 交互轨迹做 SFT，再做 learner 自身环境交互的 agentic RL；采用 privileged on-policy self-distillation 和 rubric-based LLM feedback 优化 evidence-to-conclusion 推理，不预设工具调用顺序。

结果：在匹配评测条件下，基于 Qwen3-VL-8B 的 agent 在答案准确率上相对 GPT-5.4 提升超过 16%，相对 Claude Opus 4.8 提升超过 10%，表明从 QA 模仿走向可迁移的调查策略。
