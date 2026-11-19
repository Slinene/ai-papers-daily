---
title: 'ReflectRec: Cycle-Consistency Preference Verification for LLM-based Recommendation'
title_zh: ReflectRec：循环一致性偏好验证驱动的 LLM 推荐
authors:
- Dae Kyoo Kim
- Heejung Cho
- Sungmoo Hong
- Eunil Park
affiliations:
- Sungkyunkwan University
- NAVER Corp.
- KIAT
- KT Corp.
- Jaume I University
arxiv_id: '2611.23969'
url: https://arxiv.org/abs/2611.23969
pdf_url: https://arxiv.org/pdf/2611.23969
published: '2026-11-18'
collected: '2026-11-19'
category: GenRec
direction: LLM 推荐 · 偏好验证与协同检索
tags:
- LLM Recommendation
- Cycle-Consistency Verification
- Retrieval-Augmented
- Chain-of-Thought
- Collaborative Filtering
- Self-Verification
one_liner: 用偏好→历史回译召回验证 LLM 推荐偏好，对低分偏好条件重生成，并注入相似用户未来行为协同提示，Hit@10 大幅提升
practical_value: '- 在电商用户兴趣摘要 / push 文案生成中，可引入回译验证：让 LLM 从真实历史与负样本混合池里选出用户可能做过/买过的商品，以
  recall 作为摘要或选品理由的忠实度分数；不要用 1-5 分自评，低分样本再重生成，保留最高分尝试。阈值需按候选池大小与正负比重新标定。

  - 条件重生成是便宜的质量守门：只对低 ValScore 样本增加采样预算，可避免全局重生成过度锐化；业务上可作为 guard 模块接在 LLM 画像之后，先验证再决定是否重跑。

  - Forward-Look 检索碎片池值得迁移：用“相似行为序列”检索，但注入其后续真实行为（购买/点击/播放的 next 5 item）作为协同提示，与语义偏好解耦；检索
  query 用行为历史而不是偏好文本，避免过锐化候选；需要系统提示明确这是协同过滤信号，否则 LLM 会把提示块当干扰。单 aspect embedding 即可，不必做复杂多视角。

  - 离线评估可引入随机 future 对照组和 paired bootstrap，按 ValScore 分桶分析模块收益，能更清楚定位哪个模块在哪个子群体生效，适合做消融汇报。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM CoT 推荐中，偏好 note 被当作可信中间结果直接进入 ranker，没有任何验证；且 ranker 只看单用户历史，缺少行为相似用户的协同信号。LLM 对 prompt 敏感、会幻觉偏好，长历史中 attention 不均衡（lost-in-the-middle）。因此需要一个可操作的偏好质量信号，同时引入面向下一项预测的协同证据。

### 方法关键点
- **Stage-1 语义偏好抽取**：单 LLM 调用，围绕 genre / mood / theme / era / narrative style 五维描述 60–100 词，禁止出现历史标题，避免与原始历史冗余。
- **Cycle-Consistency Verifier**：将偏好文本与 50 候选（10 真实历史 + 40 随机负）交给 LLM 选择可能已看项，recall 作为 ValScore。该分数承担测量、门控、选择、诊断四角色；阈值 τ=0.4。
- **条件重生成**：仅 ValScore<0.4 的 LOW 样本重生成最多 2 次，温度 0.5，保留最高分；LOW 桶收益集中。
- **Forward-Look 检索**：从训练集构造 (5-item history, next 5 items) 片段池，用 BGE-large 基于历史相似度检索 top-10，注入其 future 观看项作为协同 hint；检索目标与预测任务对齐而非偏好；需协同感知 system prompt 防止被当噪声。

### 关键实验与结果
在 MovieLens-100K / ML-1M 上，full pipeline Hit@10 达到 31.67% / 39.93%，较 CoT4Rec-ICL 提升 +16.25 / +4.46 pp；Stage-1 单独最大增益 ML-100K +12.34 pp；Forward-Look 贡献 +3.32 / +3.53 pp；三个 backbone（Qwen3-30B、Qwen2.5-72B、Llama-3.3-70B）下均 full > Stage-1，最大 +11.03 pp。Amazon Electronics 低桶也观察到一致的再生方向。

### 最值得记住的一句话
用“偏好→历史回译召回”替代 LLM 自评，作为可观测、可门控、可选择的验证信号；条件重生成与向前看协同检索按 ValScore 分桶互补，是 LLM 推荐中间结果治理和协同信号注入的组合拳。
