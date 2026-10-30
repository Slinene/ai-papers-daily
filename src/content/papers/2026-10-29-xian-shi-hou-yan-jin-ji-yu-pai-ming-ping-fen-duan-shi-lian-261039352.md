---
title: 'Try Before You Evolve: Ranking-Scored Trials for Recursive Self-Improvement
  of Recommender Systems'
title_zh: 先试后演进：基于排名评分短试炼的推荐系统递归自改进
authors:
- Xu Huang
- Jiawei Feng
- Jiancan Wu
affiliations:
- University of Science and Technology of China
arxiv_id: '2610.39352'
url: https://arxiv.org/abs/2610.39352
pdf_url: https://arxiv.org/pdf/2610.39352
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 推荐系统递归自改进 · LLM 代码进化
tags:
- RecSys
- Recursive Self-Improvement
- LLM Code Evolution
- Early Ranking Feedback
- Training Recipe
- Sequential Recommendation
one_liner: RecRSI 用短训练+probe全排序NDCG@10试炼筛选LLM候选训练编辑，再full retrain最优编辑，大幅提升自进化效率与效果
practical_value: '- 在 LLM 改写训练 recipe / pipeline 的自进化流程中，不要逐条 blind full retrain；让
  LLM 生成 K=3 个覆盖 loss、sampler、optimizer、architecture 的候选 edit，先做 short trial：从同一初始化训练前
  15% steps，用 probe 用户的 full-ranking NDCG@10 打分，再只 full retrain 最高分 edit。

  - 必须做用户切分隔离：probe users 用于 early stopping 和 trial 选择，select users 用于 promote 决策，Test
  只在最终看一次；避免反复比较把验证集选到过拟合。

  - 当候选修改了 loss / negative sampler / optimizer 时，训练 loss 尺度不可跨候选比较；要用不受训练目标影响的真实业务核心指标（如
  NDCG/GAUC）做 early signal，这条对电商/广告 auto-tuning 同样成立。

  - 把 parent recipe 的 trial 分数作为 reference：如果所有候选 trial 都不超过 parent，可以跳过本轮 full retrain；论文中可省下
  5/7 次未 promote 的 retraining。静态检查 + smoke test 先过滤不能跑、可能改评测逻辑的 edit。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐系统训练 recipe（loss、sampler、optimizer、architecture）决定效果且需按数据集反复调。LLM agent 可改写训练代码实现递归自改进，但现有做法是每轮提一个 edit → full retrain → 看 ranking 决定保留；反馈在 full retrain 后才到，实验中 90 次 retraining 只有 41% 被采纳。同时训练 loss 与 full-ranking NDCG 严重脱节，且 loss/sampler 类 edit 让 loss 尺度不可跨候选比较。因此需要一个与最终 ranking 一致的早反馈来选 edit。

**方法关键点**：
- **Diagnosis-conditioned batch proposal**：LLM 基于 parent 在 probe users 的诊断（positive 掉出 top rank 比例、head/tail NDCG 等）和 memory 生成 K=3 个覆盖不同组件的 edit，并通过静态检查 / 一次 repair 过滤。
- **Short trial**：对父 recipe 和每个候选 edit 从共享初始化 θ(0)、同 seed 训练前 Ks=4000 步，约 15% full budget，再用 probe users 的 full-ranking NDCG@10 打分；同时保持 training consistency 与 ranking consistency。
- **Retrain & promote**：选 trial score 最高 edit 做 full retrain，在 select users 上提升超过 δ 才 promote，并把每轮 evidence 写进 memory。

**关键实验**：SASRec 与 HSTU 在 CDs / Office / LastFM 上，同 5 轮、每轮一次 full retrain。RecRSI 在六个 setting 全部超过 strongest baseline，Test NDCG@10 提升 16.1%–102.0%；promotion rate 77%（23/30）vs baseline 41%（37/90）。等 GPU 预算下仍显著更优。Ablation 显示 short trial 显著优于 random / LLM judge / warm-start；executed trial 与最终 select gain 相关 ρ=0.46、AUC=0.71，而 LLM judge 负相关。

**最值得记住**：在让 LLM 改写推荐训练代码的自进化流程里，不要用训练 loss 或 LLM patch 判断决定哪个 edit 值得 full retrain；要用与最终 ranking 一致的短试炼：同初始化、同训练路径、少量 steps、全排序验证集 NDCG 来选 edit。
