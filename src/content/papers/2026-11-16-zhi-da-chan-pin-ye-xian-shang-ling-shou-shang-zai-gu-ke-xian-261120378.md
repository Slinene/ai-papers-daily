---
title: 'Straight to the Product: What Online Retailers Miss When Shoppers Ask AI First'
title_zh: 直达产品页：线上零售商在顾客先问 AI 时错过了什么
authors:
- Michael Iannelli
- Alan Ai
affiliations:
- Scrunch AI
arxiv_id: '2611.20378'
url: https://arxiv.org/abs/2611.20378
pdf_url: https://arxiv.org/pdf/2611.20378
published: '2026-11-16'
collected: '2026-11-17'
category: Eval
direction: AI 购物助手效果测量与归因
tags:
- LLM shopping assistants
- product follow-through
- attribution
- user behavior
- conversational recommendation
- e-commerce
one_liner: 通过同源面板量化 AI 助手推荐后用户到店访问指名产品行为，并提出 product follow-through 评估指标
practical_value: '- 不要只依赖 referral link 做 AI 归因：89% 的访问没有助手链接痕迹，54% 走 web search；请把产品名搜索词（search
  console 中的 product-name queries）和产品页 direct/search 到达纳入 AI 影响评估，建立 product follow-through
  指标，否则只能看到约 1/9 的到访。

  - 优化产品页与站内搜索对“被 AI 命名的产品名”的可发现性：28% 的首访前搜索直接使用答案产品名，产品名可视为 Semantic ID，需在 title/URL/site
  search 中保持精确匹配，避免流量被搜索引擎或站内检索漏掉。

  - 评估 Agent/推荐助手时，不止于答案质量或点击率，应加入产品级 follow-through：24h 内是否访问被命名产品；该指标无需 referral
  link 或平台日志，可在自有 panel 或自营数据中复现，且可逐助手比较（如 ChatGPT +2.2 pt vs Gemini +1.0 pt）。

  - 区分 AI 推荐带来的新客与老客行为：过去一周未访问该店的用户点击链接比例 27% vs 老客 12%，但老客更可能搜索或直接访问；产品页应保留相关推荐和类别入口，因为用户会继续浏览非命名产品（查看两个以上产品
  +5.2 点）。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
消费者在购买前先问 AI 助手，零售商通常只能看到最后的搜索或直接访问，无法看到推荐对话。传统 referral 归因严重漏报：89% 的访问没有助手链接痕迹。现有研究多止步于答案质量，缺少从对话到产品页的产品级行为证据。

## 方法关键点
- 基于 opt-in panel，同一用户在 2026 年 2–6 月和 7–10 月两个时期的 ChatGPT/Gemini/Claude/Perplexity/Grok 对话和 20 家大型零售商浏览记录，完成产品级链接。
- 用 LLM judge 对答案分类：命名具体产品 / 仅建议商店 / 仅提及；判断访问产品页是否匹配答案中命名的产品，允许尺寸、颜色、包装变体。
- 三重对照：同一人过去 14/21/28 天访问作为 earlier-week baseline；交换他人 matched answer 控制流行度与品类；无答案的 matched moments 控制在线活跃度和时段。
- 提出 product follow-through：答案命名具体产品后 24 小时内访问该产品页的占比，无需 referral link 或平台日志，可逐助手计算。

## 关键结果
- 有产品页访问的天数中，44% 展示自己答案中的产品，他人 matched answer 仅 1.5%；复现期 42% vs 1.2%。
- 命名产品页访问从 0.02/100 答案升至 2.07/100 答案（+2.0 pt）；产品名搜索从 0.4 升至 9.3（约 24×）。
- 89% 的到访无助手链接痕迹，54% 通过 web search；首访前 30 分钟的搜索中，28% 直接使用答案产品名，此前仅 1%。
- 到店后继续浏览：31.4% 的访问查看两个以上产品，比本人其他访问高 5.2 点；被命名产品是 34% 访问的第一页。
- 链接使用差异：过去一周未访问该店的用户通过链接比例 27% vs 最近访问者 12%；但总体仅 11% 通过链接。

## 最值得记住的一句话
The chat names the product; the store logs a search.
