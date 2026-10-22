---
title: 'Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic
  Commerce'
title_zh: 偏好≠许可：个性化 Agent 电商自动购买界限
authors:
- Ryotaro Shimizu
- Sai HtaungKham
- Mo Fan
affiliations:
- ZOZO Research
arxiv_id: '2610.29216'
url: https://arxiv.org/abs/2610.29216
pdf_url: https://arxiv.org/pdf/2610.29216
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 交易授权边界个性化
tags:
- agentic commerce
- personalization
- transaction authority
- LLM agents
- authorization boundary
- AI safety
one_liner: 提出个性化自动购买授权边界任务，发现16个LLM购物Agent过度承诺，个人边界可从少量标注习得
practical_value: '- 把推荐 fit 与交易授权解耦：在自动下单/Agent 购物中，不要因相关性高就 checkout；增加独立的 pre-commit
  warrant gate，读商品证据与用户明确顾虑，能大幅降低弱证据过度承诺，且比 always-confirm 少打扰。

  - 用 minimal-edit counterfactual 做 Agent 审计：固定商品/任务，只改 warrant、final sale、价格上限/异常、urgency
  等因素，观察行为变化；把动作压缩为 don''t/confirm/auto 三档，报 overreach/overcaution，而不是只看任务成功率。

  - 个性化授权边界可用简单模型 + 少量用户标注：几十个用户自己标签训练的 logistic/partial-pooling 模型即可预测 held-out auto-purchase
  线，优于大量 prompt×model 组合；但跨域不迁移，需要 in-domain 冷启动标注。

  - 将用户个人策略渲染成简短 policy card 注入 system prompt，能改善所有模型的 unsafe-auto 行为，但仍有残余；落地建议人口级
  warrant gate 做底线 + 个人边界做上层。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Agentic commerce 从推荐走向执行，但现有评测只问“哪个商品合适”，不问“Agent 能否自己买”。74% 愿意委托常规购物，仅约 10% 允许自动完成支付。偏好匹配高不等于有授权，高 fit 低 warrant 是危险区。

**方法关键点**  
- 把自动购买线形式化为三值授权边界：don't buy < confirm first < buy automatically；由 warrant、reversibility、relative price、urgency、fit 共同决定。  
- 从 Amazon 服饰/Booking 酒店真实历史构造 11 个单因素 + flash deal/interaction 的 minimal-edit counterfactual 基准；15 名标注者角色扮演委托方，生成 1,110 条人类授权参考。  
- 审计 16 个 instruction-tuned 模型、4 家厂商；在 5 档 autonomy dial、24 个释义改写、8 个 placebo 下测 warrant guard、overreach/overcaution。  
- 提出 C3-P：提交前独立小模型读商品证据与用户顾虑做 warrant gate；用 per-annotator logistic/partial-pooling 学个人边界；并测试 policy card 治理。

**关键结果数字**  
- 模型在 fit-low 仍高度 commit（0.89），而对 warrant-stripped 降至 0，表明对 warrant 更敏感；价格超用户上限时几乎全部停止。  
- 人类参考 α≈0.25，分歧结构化；个人 own-label 边界 held-out accuracy 中位 0.79（30-40 标签），F1 时尚/酒店 0.66/0.77，超过 80 种 prompt×model oracle；跨域迁移差。  
- C3-P 在全部 dial 弱 warrant 过度承诺降为 0，且打扰远低于 Always-Confirm；policy card 对 16 个模型平均降低 unsafe-auto 0.35。

最值得记住：Preference is not permission——强推荐不自动等于可下单，授权边界因人而异且可从少量个人标注习得。
