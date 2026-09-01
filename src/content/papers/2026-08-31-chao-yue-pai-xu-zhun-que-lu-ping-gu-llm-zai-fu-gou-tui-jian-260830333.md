---
title: 'Beyond Ranking Accuracy: Evaluating LLM-Cited Feature Rationales for Next
  Basket Repurchase Recommendation'
title_zh: 超越排序准确率：评估 LLM 在复购推荐中引用的特征理由
authors:
- Yanan Cao
- Anay Dombe
- Murali Mohana Krishna Dandu
- Shreeranjani Srirangamsridharan
- Sinduja Subramaniam
- Yogananth Mahalingam
- Evren Korpeoglu
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.30333'
url: https://arxiv.org/abs/2608.30333
pdf_url: https://arxiv.org/pdf/2608.30333
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 可解释推荐 · LLM 特征理由评估
tags:
- Explainable Recommendation
- Next-Basket Recommendation
- LLM
- Feature Attribution
- Repurchase
- Evaluation
one_liner: 提出跨模型特征掩码协议，证明 LLM 不适合作复购排序器但可作经验证的推荐解释层
practical_value: '- 生产复购推荐不建议用 LLM 直接打分排序；保留 XGBoost/VNN 等监督排序，LLM 只做解释层。若要尝试，先在小样本验证
  LLM 分数是否超过 personal-frequency 等轻量 baseline，不要期望超越监督模型。

  - 复购场景解释应引用结构化行为特征（cadence/frequency/recency/user context/item popularity），并约束 LLM
  输出 exact feature names；这能把解释绑定到特征，方便 audit 和后续特征消融。

  - 用“跨模型特征掩码”评估解释特征质量：对 LLM 引用 top-3 特征做训练集中位数替换，在目标模型上看 Precision/Recall/NDCG 下降；比只看排序分更接近
  outcome-grounded，可以与 TreeSHAP/IG 对比，但需注意数据集差异。

  - 证据卡建议加 percentile 视图（同用户内/全局 item 分布）帮助 LLM 判断相对强度；文本解释需单独做 groundedness check（group
  precision/numeric consistency），防止流畅但不可靠的解释。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
复购推荐通常只优化排序准确率，但用户看到推荐后还需要知道“为什么现在买”。LLM 能把结构化行为证据翻译成可读理由，但流畅解释可能引用看似合理却与未来复购无关的特征。因此需要超越 ranking accuracy，评估 LLM 引用的特征理由是否真正携带 outcome-grounded 排序信号。

## 方法关键点
- 构造 28 个可解释行为特征，覆盖 cadence、frequency、recency、user context、item popularity；用同一特征集训练监督 ranker 并生成 LLM evidence card。
- LLM 输入 evidence card，输出 support score、top-3 精确特征名、用户解释和分析理由；对比 base prompt 与 norm-prompt（加入 percentile 视图，区分同用户/全局分布）。
- RQ1 比较 LLM 与 personal-frequency、XGBoost、VNN 在 Instacart、DC、proprietary 三个数据集上的 Precision/Recall/NDCG。
- RQ2 提出跨模型特征掩码协议：LLM 引用 top-3 特征与 TreeSHAP、integrated gradients、random 比较；将被选特征用训练集中位数替换，分别在 XGBoost 和 VNN 上测量排序指标下降。
- 补充 Instacart 文本到证据的 groundedness 检查。

## 关键结果
- LLM 分数普遍低于监督 ranker；GPT-4o 在 Instacart 上部分指标超过 personal-frequency，但 DC 和 proprietary 上基本不及。norm-prompt 未提升排序性能。
- 特征掩码实验中，LLM 引用特征有时携带排序信号；norm-prompt 在 proprietary 上 18/18 指标优于 base GPT-4o，但在 DC 上出现零或负 gap，与归因 baseline 一致程度因数据集而异。
- Instacart 解释文本 group precision 0.951、numeric consistency 0.996，但 recall 0.740；说明生成文本准确表达已选特征，选对特征仍是难点。

最值得记住的一句话：排序质量和解释质量可以分离——LLM 不宜直接做复购排序，但作为经特征掩码验证的解释层是可行的混合设计。
