---
title: 'RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing'
title_zh: 自适应证据路由：学习计算正确上下文
authors:
- Yilun Hao
- Krishna Sayana
- Isabella Ye
- James S Ren
- Sukhdeep Sodhi
- Craig Boutilier
- Chuchu Fan
affiliations:
- MIT
- Google Research
arxiv_id: '2610.10507'
url: https://arxiv.org/abs/2610.10507
pdf_url: https://arxiv.org/pdf/2610.10507
published: '2026-10-07'
collected: '2026-10-08'
category: RAG
direction: 自适应证据路由 · RAG 与计算融合
tags:
- RAG
- Evidence Routing
- Tool Synthesis
- GRPO
- SFT
- LLM
one_liner: 提出RECAST，将证据构建视为检索与计算操作的序列决策，用轻量RouterLM迭代选择/合成操作，在6个基准上平均准确率达75.6%，超最强基线15.9%
practical_value: '- 把检索和计算统一为证据操作：在电商推荐/搜索场景中，不要只把用户历史或商品池当作检索对象；可把 SQL 聚合、Python
  特征计算、代码合成作为等同的“证据获取”原语，让系统从原始数据中派生可用的上下文，而不仅仅是召回已有片段。

  - 用轻量 RouterLM 做调度，冻结大模型做编译和回答：业务上可显著降低大模型调用成本；LoRA 微调小模型即可超过更大黑盒模型，适合需要在低延迟下做复杂证据构建的场景。

  - SFT+GRPO 训练技巧可复用：从成功轨迹中选 SFT 专家，再用混合成败轨迹做 GRPO，配合 reward shaping（正确性 0.9 + token
  F1 0.08 + 结构 0.02）和 mixed-outcome filtering，比仅用正确性奖励提升明显，且样本效率更高。

  - 规则化预处理 + compact source profile：将异构数据（表、文本、用户画像）统一为 records 并生成紧凑概要，避免把完整 source
  塞进 prompt，能降低 token 成本并让路由模型更聚焦于证据需求。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
LLM 越来越需要基于长异构信息源进行推理，但传统 RAG 只做相似性检索，假设证据已经显式存在于某个片段中。许多任务所需的证据必须通过过滤、聚合、计算或跨多个源项派生而来，例如从月度营收和营业利润计算三个月营业利润率增幅最大区间。迭代检索或 Agentic RAG 虽然能自适应调整查询，但仍以检索为中心，缺乏对派生证据的构建能力。

## 方法关键点
RECAST 将证据构建形式化为一个序列决策过程，核心由三个组件构成：轻量 RouterLM、冻结 CompilerLM 和冻结 AnswerLM。
- **预处理**：用规则化方法将异构 source 统一为 records 列表，并生成 compact source profile，避免 RouterLM 接收完整 source。
- **动作空间**：RouterLM 每轮选择 CALL_PRIMITIVE（Lexical/BM25、Semantic/BGE-M3、Relational/SQL）、SYNTHESIZE（CompilerLM 将定制化规范翻译成 Python 代码并执行）或 ACCEPT_CONTEXT（判定证据充足并交给 AnswerLM）。
- **训练**：先 SFT，从生成的成功轨迹中选取专家轨迹，并做 capped upsampling；再用 GRPO，基于混合成败轨迹组进行相对优化，reward 由正确性（0.9）、token F1（0.08）和结构合法性（0.02）加权组成。仅 LoRA 训练 RouterLM，其余模块冻结。

## 关键实验与结果
在 DataBench、FinQA、HiTab、HotpotQA、LaMP、MultiHiertt 六个异构基准上，RECAST 平均成功率达 75.6%，比最强基线（Gemini-based Interact-RAG 59.7%）高 15.9%。训练后的 Qwen3.5-9B RouterLM 超过训练自由 Gemini 3.5 Flash RouterLM 5.0%。在三个未见过基准（2WikiMultiHopQA、TAT-QA、WikiTableQuestions）上，RECAST 平均 79.3%，比最强基线高 15.0%。消融显示，primitive 与 synthesized 操作互补，SFT 与 GRPO 互补，reward shaping 和 mixed-outcome filtering 均带来稳定提升。

**最值得记住的一句话**：把“检索什么”升级为“计算什么”，并用可训练的轻量 RouterLM 学习选择与合成证据操作，是应对异构数据长上下文推理的高效路径。
