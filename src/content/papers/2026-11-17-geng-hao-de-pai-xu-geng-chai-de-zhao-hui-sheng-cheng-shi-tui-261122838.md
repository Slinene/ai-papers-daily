---
title: 'Better Rankers, Worse Retrievers: The Hidden Cost of RL Post-Training in Generative
  Recommendation'
title_zh: 更好的排序，更差的召回：生成式推荐 RL 后训练的隐性代价
authors:
- Yuheng Chen
- Fan Zhang
- Yixuan Xu
- Chao Yang
- Yang Xiang
- Can Yang
affiliations:
- The Hong Kong University of Science and Technology
- Trip.com Group
arxiv_id: '2611.22838'
url: https://arxiv.org/abs/2611.22838
pdf_url: https://arxiv.org/pdf/2611.22838
published: '2026-11-17'
collected: '2026-11-18'
category: GenRec
direction: 生成式推荐 · RL 后训练召回损伤
tags:
- Generative Recommendation
- RL Post-Training
- GRPO
- Semantic ID
- Recall Degradation
- Out-of-rollout Anchoring
one_liner: RL 后训练提升生成式推荐 top-K 准确率，却降低大 K 召回；根源是负优势惩罚了合理候选，rollout 外锚定可恢复召回
practical_value: '- 如果生成式推荐作为召回通道，给下游 ranker/reward model 传几百到上千个候选，RL 后训练不能只看 hit@10/NDCG@10；必须按部署深度评估
  hit@100/500/1000，否则会掩盖大 K recall 下降并可能拖累线上候选集覆盖。

  - GRPO/DPO 中单日志正样本会让 negative advantages 把模型 beam 内的非 target 合理候选当作 hard negatives
  惩罚；这些候选往往是相似用户的 next item。可以借鉴 dense retrieval 对 hard negatives 的审慎态度，不要简单惩罚 rollout
  内所有非 target 候选。

  - 一个低成本可插拔 trick：out-of-rollout anchoring。在 GRPO loss 里加一项 KL(q0||q_theta)，只约束 rollout
  外按语义 ID 前缀采样的 M 个 item，保持 SFT 模型的相对顺序；不动 reward，不改 rollout，能同时守住 top 收益和大 K recall，已在
  GRPO/REINFORCE++ 等配置验证。

  - 上线前风险管理：RL 前用 SFT 模型计算 rollout record，识别会被负优势反复压制的商品/ID，提前做监控；若某些目标商品大部分用户的 rollout
  record 为负，说明它们可能在 RL 后掉出候选列表，可以针对性调整负样本策略或加 anchor。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐（semantic ID + LM）已形成 SFT 后接 RL（通常是 GRPO）的标准流程，但收益大多只报告 top-10 或 NDCG@10。实际部署中，生成式模型常常作为召回通道，需要把几百甚至上千个候选交给下游排序器或 reward model，因此大 K 下的 hit@K 才是关键。论文在五个数据集上发现：RL 后训练虽然提升 top 精度，却在大 K 下降低召回，模型变成“better ranker, worse retriever”。

## 方法关键点
- 对每个测试用户做全 catalogue 精确打分排序，评估 hit@K 直到 500，而不是只看 top-10；采用 MiniOneRec 风格的 GRPO，group size=16，hit-based reward 对非 target 候选按 rank 施加负权，KL 到 SFT 参考。
- 通过受控实验归因：GRPO 给 rollout 中非 target 的候选负 advantage；但这些候选是模型自己的 plausible alternatives，且常是相似用户的下一个 item。由于只有一个 logged next item，同一个 item 被惩罚次数远多于被奖励次数，跨用户泛化会把惩罚传导到相似用户。
- 提出 out-of-rollout anchoring：保持 rollout 内 GRPO 不变，额外在 rollout 外采样 M=16 个 item（一半共享前两个语义 ID 码，一半共享第一个码），加 KL(q0||q_theta) 约束 SFT 模型的相对顺序；λ=0.1。

## 关键实验与结果
- 数据集：Office、Industrial、Beauty、Toys、Sports；backbone 为 Qwen2.5-1.5B-Instruct。
- GRPO 在 Office 上：NDCG@10 从 11.59 升至 12.55，但 hit@50 从 25.73 降至 24.22，hit@500 从 52.84 降至 47.69；五数据集均出现大 K recall 下降。
- 加 anchor 后 Office hit@500 恢复到 52.14，NDCG@10 保持 12.64；其他数据集 hit@500 回到 SFT 水平或略高。
- 只保留 negative advantages 会让 hit@500 下降 19-21 点；只保留 positive advantages 无损失但也没增益。DPO 用 beam negatives 也掉 4.1 点 recall，random negatives 几乎不损害大 K。
- 预先用 SFT rollout 计算的 rollout record 能识别高风险用户/物品；强惩罚组的 hit@500 损失从 23.4 减到 3.1。

## 最值得记住的一句话
为召回场景做 RL 后训练时，评测必须覆盖部署深度；负优势惩罚 rollout 内非 target 的合理候选是召回损失根源，保护 rollout 外的相对顺序能兼顾 top 精度与 deep recall。
