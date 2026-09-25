---
title: 'Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy
  Changes'
title_zh: Augur：预演产品与政策变更反应的合成决策实验室
authors:
- Rahul Khedar
- Mayank Malhotra
- Avinash Karn
affiliations:
- PayPal AI
arxiv_id: '2609.29952'
url: https://arxiv.org/abs/2609.29952
pdf_url: https://arxiv.org/pdf/2609.29952
published: '2026-09-24'
collected: '2026-09-25'
category: Eval
direction: LLM 评估与合成人群模拟
tags:
- LLM evaluation
- synthetic personas
- LoRA-SFT
- prompt sensitivity
- decision making
- over-doom bias
one_liner: 构建合成决策实验室，发现开放权重模型与前沿模型的差距多源于评估欠规范而非能力差异
practical_value: '- 评估生成式推荐/Agent 决策时，先审计 prompt 是否公平，尤其决策 taxonomy 是否显式给定；固定权重、样本、scorer
  做 matched ablation，报告 paired McNemar + Holm 校正，否则会误判自研小模型与闭源大模型差距。

  - 可在发版前用 grounded persona 市场模拟用户/商户/平台三方反应，对定价、广告政策、推荐策略变更做离线预演；用变更文档构建 persona，比通用角色扮演更能暴露真实争议点。

  - 注意 LLM 合成用户容易系统性“过度悲观/over-doom”，别直接以负面比例做上线否决；要校准、与真实反馈对照，且 teacher agreement
  高不代表决策准确率提升。

  - 离线部署 LoRA-SFT 开放权重模型服务于决策 memo，在公平评估下可与 frontier 模型无显著差异，适合电商内部高 QPS 决策审计场景。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：产品/政策变更上线前最关键的是用户反应，但反应在决策前不存在。Augur 用合成方式生成该证据：从变更文档构建类型化知识图谱，填充有依据的 persona 市场，模拟交互，输出包含五选一行动建议的可审计决策备忘录。评估用 Gold-50：50 个已知真实结果的产品/政策事件，对照公开记录判定五分类发布结论。

方法关键：核心不是提出更强模型，而是做对比诊断。固定权重、案例、打分器，LoRA-SFT Qwen3-32B 仅换 prompt 封套，正确率 0% → 73%；2×2 消融中，仅在 prompt 中定义决策 taxonomy 就使所有前沿模型 +24~34pp。欠规范 prompt 下，离线 LoRA-SFT Qwen3-32B 显著超过三个前沿模型；prompt 公平后，无显著差异。与蒸馏教师的一致性上升但准确率不跟随，完整 pipeline 放大系统性“过度悲观”偏差。

关键结果：合成反应层经四模型家族盲评，能恢复公众实际提出的 67–90% 关切；预注册消融显示其价值在决策最难时最大，接近天花板时冗余。
