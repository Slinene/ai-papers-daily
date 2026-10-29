---
title: 'What Outcome RL Buys: Finishing, Reliability, Rarely Reach'
title_zh: 结果奖励 RL 买到了什么：完成、可靠，很少是全新可达
authors:
- Shan Yang
affiliations:
- Individual Researcher
arxiv_id: '2610.34894'
url: https://arxiv.org/abs/2610.34894
pdf_url: https://arxiv.org/pdf/2610.34894
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: Outcome RL 训练效果分解与归因
tags:
- outcome RL
- reasoning
- pass@1
- token budget
- finishing
- reach
one_liner: 将 outcome RL 的 pass@1 提升分解为完成、可靠与可达，发现主要改善完成和稳定性，很少带来新能力
practical_value: '- 在 LLM Agent / 搜索改写 / 生成式推荐等有 token 预算或延迟上限的场景，评估应区分 `finishing`（限时内是否答完）与
  `reliability`（答完后是否做对），否则容易把超时当成不会做，误判模型能力。

  - 如果线上 LLM 生成 query、文案或推理链路经常因超时截断，优先增加 token 预算或压缩推理长度，比盲目上 outcome RL 更直接；本研究显示基础模型在更多
  token 下能自我缩小大部分 finishing gap。

  - Outcome RL 的收益主要是稳定性/一致性，而不是解决全新问题；在推荐/广告的 LLM pipeline 中，更适合用它来做排序一致性、生成候选再打分等稳定性优化，而不是期待它探索完全未见过的新
  item 或新 query。

  - 线上监控可同时跟踪 `finishing rate`、`reliability` 和 `reach` 三类指标，先定位瓶颈；例如如果 finishing 已经很高，但
  reliability 低，再考虑 RL 或样本重排等策略。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
Outcome RL 常被报告能提高 pass@1，但 pass@k 在大 k 下提升不明显，说明收益可能不是新能力，而是行为变化。论文希望在固定 token 预算下，区分 RL 带来的改变是「答得更快/更稳」还是「会做原本不会的题」。

## 方法关键点
对比 20 个已发布 RL 模型（1.5B–32B）与其 thinking base 在物理、竞赛数学上的 pass@1，把每道题的变化拆成三部分：
- **Finishing**：预算内是否答完；
- **Reliability**：答完后是否正确；
- **Reach**：RL 解决 base 八次全错的题，减去反向镜像。

## 关键结果
- 当 base 经常撞 token 预算时，82% 的 pass@1 变化来自 finishing；给 base 更多 token 就能缩小大部分差距。
- 当 base 已有足够 token 时，收益主要来自 reliability：RL 在双方都答完的题上正确率更高。
- Reach 在四个数据集中最多只增加 2.1 个百分点；检查 144 道仅 RL 解决的物理题，仅 3.5% 在重采样或人工阅读后仍成立。随机抽样中，10 个新 RL 步骤里有 9 个也出现在 base 采样中。
- 8B 小规模 RL 实验显示，新题收益主要来自 finishing，reliability 持平；提供物理 setup 未证明优于 plain RL。
