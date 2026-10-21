---
title: 'Baseline and Incremental: User, Item, and Request Debiasing in Instagram Feed
  Ranking'
title_zh: 基线项与增量项：Instagram Feed 排序中的用户、物品与请求去偏
authors:
- Hsin-Chiang Chen
- Hao Wang
- Gedi Zhou
- Mingze Gao
- Abhishek Kumar
- Yiben Yang
- Haoyu Wang
- Hongjing Xia
- Bo Chen
- Zhengyu Su
affiliations:
- Meta
arxiv_id: '2610.27423'
url: https://arxiv.org/abs/2610.27423
pdf_url: https://arxiv.org/pdf/2610.27423
published: '2026-10-20'
collected: '2026-10-21'
category: RecSys
direction: 推荐排序去偏 · 价值模型
tags:
- debiasing
- value model
- ranking
- online experiment
- baseline-incremental
one_liner: 在排序价值模型中保留原始预测并给增量项单独权重，用一个算子统一用户、物品、请求三类去偏
practical_value: '- 排序公式里不要直接移除 bias：把原始预测 p 和增量项 Δ 分别加权，交给在线调参决定配比。电商推荐中用户历史点击率、商品热度、请求上下文都能分别构造
  baseline，避免单一权重无法平衡“习惯性点击”和“候选真实增量”。

  - 三类 baseline 成本都很低：user/item 历史均值可预计算，request baseline 直接读当前候选池的 mean 或 p75。电商搜索/推荐可以借鉴
  request baseline 处理同一 query 下候选池强弱偏差，且只需 O(N) 或 O(N log N)，不加模型推理成本。

  - 用 quantile Pearson r + Var% 做离线筛查，只当 high-recall filter，不用于排序；真正决策靠在线四臂消融（none/raw/incremental/both）。可避免离线指标误杀有潜力的
  debias 信号。

  - 媒体格式类偏差（如图片/视频尺寸）走 debiased label，流行度偏差走 VM scoring term；概率信号比较用 logit gap，回归信号用原单位
  gap；稀疏 baseline 特征要 clamp 并单独看 zero share。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

Feed 排序的价值模型是多个 engagement 预测的加权和。每个预测都混合了 baseline（该用户、物品或请求本就会产生的水平）和 incremental（该候选超过 baseline 的增量）。只用单个权重无法分别控制这两部分：like 预测与 viewer 历史 like rate 的 quantile Pearson r 高达 0.69，说明预测大量跟踪用户习惯，而不是候选本身。已有去偏方法大多直接移除 baseline，但 baseline 本身可能是真实信号，例如习惯性点赞用户和广受欢迎的内容。

## 方法关键点

- 保留 raw 预测并给增量项独立权重：`s(c) = Σ [w_rj p_j(c) + w_ij Δ_j(c)]`，让在线 tuner 决定 raw 与 incremental 的配比。
- 一个参数化算子统一三类去偏：`Δ = m(p,b)[σ(k·d(p,b)) - shift]`，自由度包括 baseline b、比较尺度 d、magnitude m、sharpness/centering (k, shift)。
- 三类 baseline 共存：viewer baseline 是用户历史动作率；item baseline 是物品跨用户平均率或格式/时长桶；request baseline 从当前候选池读取 mean 或 p75。
- 设计流程：quantile Pearson r + Var% 判断是否需要 split；形状规则决定 request baseline 统计量；item 轴流行度 bias 走 VM term，媒体格式 bias 走 debiased label。

## 关键实验

对 Instagram Feed 6 个已上线 term 做四臂在线消融：none、raw、incremental、both，生产权重。13 个判断 (term, metric) 对中，11 个 both 联合支配两个单臂；26 个直接对比中 17 显著为正，仅 1 显著为负。extShare·viewer 的 external share both vs none 达 +58.97%，both−raw +21.05%；logTS-MR·item 在 feed time spent 上 both−raw +0.359%，both−incr +0.948%。结果表明在部署点，raw 和 incremental 两项都不是冗余的。

最值得记住的一句话：**基线不是需要消除的缺陷，而是需要独立权重的第二信号；在部署点，移除任一项通常都更差。**
