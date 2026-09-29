---
title: 'Surprising Success, Repeated Failure: Entropy-Guided Credit Assignment for
  Exploration in LLM Reasoning'
title_zh: 意外的成功，重复的失败：熵引导信用分配用于LLM推理探索
authors:
- Woongyeong Yeo
- Minki Kang
- Chanuk Lee
- Sangwoo Park
- Jinheon Baek
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2609.33781'
url: https://arxiv.org/abs/2609.33781
pdf_url: https://arxiv.org/pdf/2609.33781
published: '2026-09-26'
collected: '2026-09-29'
category: Training
direction: RLVR token级信用分配 · 熵引导探索
tags:
- RLVR
- Credit Assignment
- Entropy
- LLM Reasoning
- Exploration
- Policy Optimization
one_liner: 提出EAPO，利用策略熵与response advantage符号不对称分配token级信用，强化高熵成功、惩罚低熵失败并保留失败中的探索机会
practical_value: '- 在电商/导购Agent的RLVR微调中，可直接利用每步生成时的策略熵作为信用分配信号，无需额外reward model或人工标注；将成功轨迹中高熵决策（如“不确定时尝试新工具/新query”）给予更强正反馈，鼓励探索新策略。

  - 对失败轨迹区分“确定性错误”与“探索性失败”：低熵token（模型很自信却错，如错误价格比较结论）施加更强惩罚，快速纠正重复错误；高熵token（模型尝试不确定路径，如生成长尾query）减轻惩罚，保留未来恢复可能性。

  - 若在生成式推荐/搜索query改写上做RL，可借鉴EAPO的token-level advantage redistribute：用response-level奖励按熵加权到token，避免对整条失败样本均匀惩罚，有助于维持候选多样性。

  - 工程实现上，EAPO只用现有rollout信号（entropy/advantage），可轻量嵌入PPO/GRPO等在线RL流程；适合稀疏reward场景（如用户最终购买/点击），提升覆盖与多样性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR用outcome奖励提升LLM推理，但细粒度信用分配往往需要辅助模型、额外采样或特权信息。政策熵虽免费可用，但现有方法在成功和失败上都优先不确定位置，会把惩罚集中在失败但仍可恢复的位置，压制探索。

**方法关键点**：基于观察“不确定下的成功不易复现，而自信的失败容易重复”，提出EAPO。将归一化策略熵与response advantage的符号耦合：成功响应中对高熵token加强正反馈（奖励“意外成功”），失败响应中对低熵token加强惩罚（纠正“重复失败”），同时衰减失败中高熵位置的惩罚以保留恢复备选。这样直接从现有rollout信号得到token级credit，无需额外监督。

**关键结果**：在多种推理任务、base和reasoning backbone上验证，整体性能最优；提升探索效果，扩大问题覆盖，生成更多样候选答案。
