---
title: 'LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured -- Reinforced
  Polarizer Keeps a Frozen LLM from Being Confidently Misled by the Wrong Evidence'
title_zh: LODESTAR：可信熵是导航而非测量——强化极化器防止冻结 LLM 被错误证据自信误导
authors:
- Po-Jen Ko
- Che-Cheng Wu
- Hung-Chun Hsu
- Li-Yang Chang
- Chuan-Ju Wang
affiliations:
- Research Center for Information Technology Innovation, Academia Sinica, Taiwan
arxiv_id: '2608.11922'
url: https://arxiv.org/abs/2608.11922
pdf_url: https://arxiv.org/pdf/2608.11922
published: '2026-08-12'
collected: '2026-08-13'
category: RAG
direction: RAG 答案选择 · RL 训练提示干预
tags:
- RAG
- Entropy
- Answer Selection
- Reinforcement Learning
- Frozen LLM
- Prompt Optimization
one_liner: 用 RL 训练固定 prompt 干预串，提升冻结 LLM 在 RAG 答案选择中对误导证据的鲁棒性
practical_value: '- 生成式推荐/搜索候选重排：用 frozen LLM 的预测熵筛选候选时，注意低熵可能因上下文误导而不可靠。可在 prompt
  前加一个固定的“polarizer”提示串（如“请先检查证据可信度”类），用离线 RL 训练，不改模型权重，在线零成本提高鲁棒性。

  - 训练技巧：RL 奖励可来自 gold 标签与 LLM judge 组合，离线构建标签，推理时不依赖 judge。适合业务中无实时标注但离线有部分人工/gold
  数据的场景。

  - 架构选择：保持 LLM 冻结，只优化一个短的自然语言干预，比 fine-tune LLM 成本低且易于 A/B 测试；推荐系统可对不同候选池/域分别训练 polarizer
  字符串。

  - Agent 检索后答案融合：在 Agent 的 retrieve-then-answer 流程中，对多个检索证据采用基于熵的选择时，可引入干预提升对误导证据的韧性；消融实验证明能降低误导段落被读取概率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：检索增强问答中，预测分布熵低是强选择规则：冻结 LLM 生成的候选答案最低熵能提升 F1（从 0.4769 到 0.5148）。但误导段落会使模型自信错误，熵低反而误导选择。现有方法或规避或仅记录未修复。
方法关键点：LODESTAR 首次对文本干预（prompt 前插入的固定自然语言串 polarizer）用第三方冻结 responder 的预测不确定性评分，跨同一问题候选比较；用 RL 离线训练 polarizer，标签由 gold answers 和两个 LLM judge 构建，推理无需 gold 和 judge；polarizer 插入 prompt 不改权重。
结果：在 5,008 问题上，LODESTAR 最高 mean F1 0.5339（基线 0.5148），最高 EM 0.4136，最高 GPT-4o judge 0.6435；三 seed 平均赢全部 70 个 method-by-dataset F1 cells，对 14 个已发表配置显著；消融显示 polarizer 使 respondent 读误导段落比例从 30.3% 降到 26.0%。
