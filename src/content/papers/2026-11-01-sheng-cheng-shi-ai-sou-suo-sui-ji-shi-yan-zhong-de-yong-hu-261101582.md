---
title: 'Measuring User Success in Randomized Search Experiments: Interpreting Good
  Abandonment in Generative AI Search'
title_zh: 生成式 AI 搜索随机实验中的用户成功度量：解读良好放弃
authors:
- Minha Hwang
- Shavak Agrawal
- David Chen
- Carto Wong
- Xin Du
- Tiannan Wang
- Georg Buscher
- Zheng Chen
affiliations:
- Microsoft
- Simplex AI
arxiv_id: '2611.01582'
url: https://arxiv.org/abs/2611.01582
pdf_url: https://arxiv.org/pdf/2611.01582
published: '2026-11-01'
collected: '2026-11-03'
category: Eval
direction: 搜索随机实验 · 用户成功度量
tags:
- Good Abandonment
- Search Metrics
- Randomized Experiments
- LLM Search
- User Success
- Online Evaluation
one_liner: 提出 Session Success Rate (SSR)，用人类标注会话训练可解释模型区分点击与放弃中的成功/失败，在线实验灵敏度约为 Sessions
  per User 的 2.5 倍
practical_value: '- 在电商/推荐场景不要单看点击/无点击：点击集合中有约 6.5% 失败，无点击集合中约 53.2% 是成功（论文样本）。因此应构建区分点击与放弃内部异质性的度量，而非直接把
  CTR 当成功。

  - SSR 的可解释决策树结构可以迁移：把 query/session 按 clicked/abandoned 分支，分别用下游互动时长、页面浏览/滚动深度、语义改写（struggling
  reformulation）等组合条件判断成功，避免长 dwell 被一概视为正向。

  - 采用 human-labeled ground truth 做离线评估，报告中用 balanced accuracy 而非原始准确率，因为成功样本占多数；采样时对困难
  session（多 query、移动端）过采样，线上按 inverse sampling weight 恢复人群率。

  - 在线实验平台可借鉴 SSR 提高指标灵敏度：在约 4000 个生产实验中，SSR 的 binary sensitivity 是 Sessions per User
  的 2.5 倍，可在固定流量预算下降低单实验流量、提高实验吞吐；但上线前要设置 coverage checks，当 treatment 改变页面/语义输入时 fallback。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

生成式AI搜索直接在结果页回答信息需求，点击状态无法区分成功：点击后可能不满意，无点击可能是“良好放弃”（用户成功消费答案）。已有研究表明 dwell、滚动、query 改写等行为信号需在上下文中解读。因而随机搜索实验需要一个能区分点击与放弃内部异质性的用户成功指标。

方法关键点：
- SSR 从 query 级建模，输入三类信号：事件信号（query 顺序、点击、下游互动、时间）、页面交互信号（结果页 dwell、相对可见度、滚动）、语义旅程信号（struggle 类 query 改写）。
- 决策结构显式分离 clicked 和 abandoned 查询，用联合行为条件判断成功/失败；例如点击后较长下游互动且无挣扎改写视为成功，而放弃时需结合有意义的页面互动、非深度扫描、无挣扎改写。
- 人类标注：训练法官基于隐私保护的互动证据和视频记录标注完整 session；至少两人标注 query 和 session 级标签。
- 聚合简单透明：Session SSR 为 query 成功预测平均值。
- 分层采样：按设备、session 长度、query 频率分层，对多 query 和移动端过采样，恢复人群率时用 inverse sampling weights。

关键实验：
- 标注样本 6,904 queries / 3,216 sessions；其中 53.2% 的放弃是成功，6.5% 的点击是不成功。
- 模型 out-of-sample balanced accuracy：query 级 0.750，放弃分支 0.680（对比 prior abandonment rule 0.450），session 级 0.680。
- 12 个在线随机实验（7 ranking + 5 非 ranking）与 Sessions per User 比较：7 个方向一致，4 个不确定，1 个不一致；ranking 类一致性最强。
- 生产实验 portfolio 约 4000 个实验：SSR binary sensitivity 是 Sessions per User 的约 2.5 倍，支持固定流量预算下降低单实验流量、提高实验吞吐。

最值得记住的一句话：点击与放弃都不能单独代表成功，SSR 通过人类标注学习上下文行为信号，将放弃分解为成功/失败，从而在随机实验中更稳健地测量生成式 AI 搜索的用户成功。
