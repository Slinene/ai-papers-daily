---
title: 'Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge
  Poisoning in Generative AI Systems'
title_zh: 可信 RAG：检测生成式 AI 系统中错误信息与知识中毒的评估代理
authors:
- Balkrishna Giri
- Md Toufique Hasan
- Jussi Rasku
- Muhammad Waseem
- Pekka Abrahamsson
affiliations:
- Tampere University
arxiv_id: '2608.21095'
url: https://arxiv.org/abs/2608.21095
pdf_url: https://arxiv.org/pdf/2608.21095
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: RAG 评估 · 知识中毒检测
tags:
- RAG
- Evaluation Agent
- Knowledge Poisoning
- Trust Index
- NLI
- Guardrails
one_liner: 用 NLI 与加权中毒信号构建生成前评估代理，Trust Index 在 TruthfulQA 上达 91% 准确率和 100% 精确率
practical_value: '- 在电商/广告/搜索 RAG 场景中，检索到的商品信息、商家文案可能被恶意污染，可把 NLI 事实校验 + 多信号加权评分做成生成前
  guardrail，先丢弃低 Trust Index 的检索块，降低事实错误与合规风险。

  - 采用中间件/Agent 形式实现，不改 LLM 主干，适合线上生成式推荐/客服 Agent 的风险拦截；但阈值必须按业务领域和生成风格单独校准，不要直接跨域复用，FEVER
  结果表明跨数据集泛化需要 domain-specific calibration。

  - 对指令注入类攻击，该方案召回高且易阻断；对实体替换、语义弱化等 subtle poisoning 仍难检测，电商场景应额外补充商品属性一致性校验或细粒度事实比对。

  - 五信号检测器 + relevance-weighted aggregation + 高污染非线性阻尼可工程化为特征打分模块，适合作为检索后、生成前的风控层，优先处理高风险
  query 和长尾商品知识。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG 系统默认检索到的文档可信，但语义相关性高不代表事实真实，存在安全-可靠性缺口。攻击者可通过知识中毒插入恶意文档，诱导 LLM 生成定向错误信息。

**方法关键点**：构建 Evaluation Agent 中间件，在生成前检测被污染上下文，而非评估模型是否采纳错误信息。核心包括：NLI 事实验证；五信号中毒检测器，使用 relevance-weighted aggregation；Trust Index `T = 0.4F + 0.35C + 0.25(1-P)`，并对高污染上下文加入非线性阻尼。检测结果用于决定是否阻断检索内容。

**关键结果**：在 TruthfulQA 上配合 Llama 3.3 70B，准确率 91%、精确率 100%，指令注入召回 100%；实体替换等就地编辑仍难检测。三个 LLM 上 Trust Index 的 ROC-AUC 为 0.73–0.81，生成风格影响大于模型规模，per-LLM 阈值校准可恢复 baseline 竞争力；FEVER 数据集泛化较弱，需领域校准。软件工程安全编码助手场景中，阻断不安全建议的指令注入 F1 达 92%，但矛盾与微妙语义弱化仍难检测。
