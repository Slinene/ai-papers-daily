---
title: 'Self-Improvement with Auxiliary Rewards: Learning from Verified Traces and
  Evaluating Transfer'
title_zh: 辅助奖励驱动的自改进：从验证轨迹中学习并评估迁移
authors:
- Minju Gwak
- Alan Ritter
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.41296'
url: https://arxiv.org/abs/2610.41296
pdf_url: https://arxiv.org/pdf/2610.41296
published: '2026-10-29'
collected: '2026-11-03'
category: Training
direction: 小模型推理自改进 · 轨迹级辅助奖励
tags:
- Self-Improvement
- Auxiliary Rewards
- RLVR
- Reasoning Traces
- Offline Weighted SFT
- Small LM
one_liner: 提出用置信度/熵辅助轨迹偏好区分同等正确推理，提升小模型自改进与跨任务迁移
practical_value: '- 业务 LLM 生成推荐理由/query/文案时，常只有点击/转化等弱反馈；可引入置信度（SC）或熵变化+局部平滑度（UID-Conj.）作为辅助奖励，对正反馈轨迹打分，筛选高质量样本做
  SFT，在标注有限时提升迁移表现。

  - 离线加权 SFT 比在线 TTRL 更稳定且证据更强：同一响应池按辅助奖励加权训练，较均匀加权提升 1.93 点（CI [0.44,3.44]）。业务可优先做离线加权精调，成本低、便于上线。

  - 辅助奖励选择依赖任务：SC 更适合判断指令遵循和轨迹质量；UID-Conj. 在多种训练设置中更利于下游收益。实际可两者都算，在验证集上选择权重或融合，而非只看推理偏好。

  - 评估轨迹偏好应以最终业务指标为准，而非仅看推理期排序一致性；建立下游 A/B 或离线 proxy 评估，辅助奖励要暴露学习价值。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：答案级奖励（如 RLVR 可验证结果）无法区分同样正确的推理轨迹，但这些轨迹在合理性、简洁性、指令遵循上存在差异。论文研究在有限监督下，用辅助轨迹偏好提升小语言模型自改进与跨任务迁移。

方法：比较两种辅助奖励——置信度（SC）和熵指标 UID-Conj.（结合全局熵变化与局部平滑度）。在线设置中用 TTRL 做奖励增强，在 30 道 AIME 问题上无参考答案适配 Qwen3-1.7B；离线设置用历史 AIME 题对正确响应做加权 SFT，以同一批响应比较不同权重方式，更干净地评估辅助奖励的训练价值。

关键结果：在线实验中，UID-Conj. 相比未修改的 TTRL，在适应基准和三个迁移基准的宏平均上提高 2.08 个百分点。最强证据来自离线加权 SFT：UID-Conj. 比均匀加权高 1.93 点，配对 prompt-bootstrap 95% CI 为 [0.44, 3.44]。收益依赖任务：SC 有助于判断轨迹质量与指令遵循，UID-Conj. 在多个设置中带来更强训练结果。结论是辅助偏好能暴露同等正确轨迹间的学习价值，评估应关注下游收益而非推理期偏好。
