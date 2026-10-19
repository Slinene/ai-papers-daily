---
title: 'GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization
  in Generative Search'
title_zh: GLOBE：面向生成式搜索电商商品优化的结构化智能体记忆演化
authors:
- Hyunseo Kim
- Suil Choe
- Sukkyoung So
- Daeyeon Yi
affiliations:
- AI Lab, CTO Division, LG Electronics, South Korea
arxiv_id: '2610.23709'
url: https://arxiv.org/abs/2610.23709
pdf_url: https://arxiv.org/pdf/2610.23709
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: 生成式搜索 GEO · Agentic Memory
tags:
- GEO
- Agentic Memory
- E-commerce
- LLM
- Field-scoped Behavior
- Feedback Evolution
one_liner: 把商品改写策略存成字段级行为手册，用排名反馈持续演化、去冗余并淘汰有害策略
practical_value: '- 将商品 listing 优化从整篇 prompt 改写拆成 field-scoped behavior：每个 behavior
  定义 edit operation + 允许字段（title/features/description）+ 冲突关系，可避免跨字段错误和过拟合关键词；电商可直接把
  SEO/GEO 规则落成这种结构化手册。

  - 用 rank gain 作为反馈，按 batch 聚合并更新 behavior 的 helpful/harmful/neutral 计数、score = h+
  - h-，设 probation Nmin=5 再淘汰；比逐 episode 更新更稳，适合在线排序反馈有噪声的场景。

  - Moderator 做 embedding dedup（cos > 0.9）+ LLM 功能去重，再由 Curator 提交；防止反馈演化膨胀出冗余或过拟合
  ranker 的 behavior，全流程保持 handbook compact，cross-ranker 迁移更好。

  - 推理阶段冻结 handbook，只用 active behaviors 单次编辑，无迭代搜索；训练阶段多智能体成本高但线上轻量，可考虑把 handbook
  蒸馏到小模型或作为静态规则库。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
生成式搜索正在改变电商：LLM 直接比较、排序商品，listing 的文本结构会显著影响曝光排名。商品数据本身是高度结构化的 title/features/description，但已有 GEO 方法大多把整篇 listing 当自由文本改写，既容易产生字段错位，也无法把一次成功的改写策略抽象成可复用知识。GLOBE 要解决的核心问题：如何把 episodic rank feedback 变成持久、可解释、可跨品类迁移的优化记忆。

## 方法关键点
- **结构化行为手册**：每个 behavior 含 id、name、instruction、permitted target fields、conflicts、feedback metadata。行为不是整段 prompt，而是字段级编辑策略，例如“在 features 字段命名最可能磨损点的材质”。
- **Deployment-and-Evolution 循环**：当前 handbook 固定部署在 100 个 query-product 对上，Editor 选择并应用相关 behaviors，Ranker 返回 rank gain；一个 batch 结束后再聚合反馈。
- **反馈演化三组件**：Reflector 只做 ADD/MODIFY，不直接删除；Moderator 先 embedding dedup（cos > 0.9），再做 LLM 功能去重；Curator 确定性提交。behavior 是否 active 由 score = h+ - h- 和 probation（Nmin=5）共同决定。
- **训练/推理分离**：1,000 训练 query 分 10 个 batch，推理阶段冻结 handbook，只使用 active behaviors。

## 关键实验
在 E-GEO benchmark 上，GLOBE 对比 Prompt Opt、Static HB、GLOBE w/o Mod.：MRG 1.611 vs 0.351 / 1.343 / 1.519；SR 61.6%；DSR 降到 2.172；CV 降到 0.034。cross-ranker 评测中，GLOBE 在 Qwen3.5-122B 和 Gemini-3.5-flash 上仍保持最优，而 unmoderated variant 优势消失，说明 moderation 有助于避免过拟合单一 ranker。案例中 B016 从一次失败中被抽象出来，在 185 次后续应用中保持 62% helpful、+1.90 mean rank gain。

## 最值得记住的一句话
把优化知识从 prompt/轨迹中抽出来，做成字段级、可去重、可淘汰的行为手册，才能把 transient rank feedback 变成可迁移的 agentic memory。
