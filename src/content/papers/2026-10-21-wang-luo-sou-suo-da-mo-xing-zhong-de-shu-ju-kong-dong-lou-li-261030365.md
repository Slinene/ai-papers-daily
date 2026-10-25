---
title: Data-Void Exploits in Web-Searching LLMs
title_zh: 网络搜索大模型中的数据空洞漏洞利用
authors:
- Michele Guerra
- Wuyeh Jobe
- Sanjana Nambiar
- Christina Pöpper
- Azza Abouzied
affiliations:
- New York University Abu Dhabi
arxiv_id: '2610.30365'
url: https://arxiv.org/abs/2610.30365
pdf_url: https://arxiv.org/pdf/2610.30365
published: '2026-10-21'
collected: '2026-10-25'
category: LLM
direction: LLM 安全 · 数据空洞攻击与防御
tags:
- data voids
- web-searching LLMs
- disinformation
- prompt tone
- adversarial retrieval
- LLM security
one_liner: 仅需一个攻击者页面即可在31%的联网LLM回答中植入内容，提示语气与模型选择防御效果有限
practical_value: '- 对引入 LLM 联网搜索或 RAG 的电商问答、商品摘要、客服系统，需检测检索结果是否落入“数据空洞”（长尾/稀疏 query），对低权威源降权或强制多源交叉验证。

  - 在 RAG pipeline 中实现对引用来源的域名权威度、数量与多样性阈值，避免单页攻击操纵合成答案；可设计“来源稀缺度”指标作为 abstain 或 flag
  条件。

  - 用户侧提示词（如“请怀疑”）仅有微弱防护，不能依赖 prompt 防御；需要在检索后排序/过滤层做硬约束，例如黑名单、域名信誉、时间/一致性校验。

  - 生成式推荐/Agent 若使用 Web 检索来丰富商品信息或热点内容，攻击者可在小众商品/关键词下埋内容；上线前用红队模拟数据空洞攻击，评估模型引用行为。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：联网搜索 LLM 用合成答案替代链接列表，但可能掩盖答案依赖稀疏、未验证或对抗性来源。虚假信息者可在“数据空洞”中发布叙事，诱导 LLM 检索并引用其页面，形成新的推理时攻击面。

**方法**：实验同时变化用户提示语气（怀疑/兴奋/中立）、LLM 类型（ChatGPT/Gemini/Sonar Pro）和三类攻击者控制——五种数据空洞填充策略、内容托管域名可见度高低、以及生成式优化引擎特征。统计攻击者内容出现在 LLM 回答中的比例及警告标记。

**关键结果**：仅单个攻击者页面即可完成利用；所有条件下攻击者内容出现在 31% 的 LLM 回答中。怀疑语气仅轻微降低成功率并略微增加标记，提示语气和模型选择均无显著大效应。数据空洞被证实为实用的推理时攻击面，亟需防御。
