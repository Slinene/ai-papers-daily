---
title: 'MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation'
title_zh: MERGED：通过生成专家推理蒸馏的多模态实体解析
authors:
- You-Lin Chen
- Kyoungjun Park
- Bin Xu
- Prithviraj Sen
- Pedro Herrero-Vidal
affiliations:
- Amazon
arxiv_id: '2609.01913'
url: https://arxiv.org/abs/2609.01913
pdf_url: https://arxiv.org/pdf/2609.01913
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: 多模态实体解析 · 推理蒸馏
tags:
- Entity Resolution
- Multimodal
- Distillation
- DPO
- VLM
- E-commerce
one_liner: 无需人工标注，多教师VLM生成推理标签，共识SFT+分歧DPO蒸馏7B学生，PR-AUC超32B基线6.32%且成本降6倍
practical_value: '- 关系定义频繁变化的电商场景（exact/variant/substitute），可直接用多教师 VLM 生成结构化标签与 reason；共识样本用于
  SFT，分歧样本用 meta-judge 选偏好做 DPO，无需等待人工 SOP 审核，可把新关系上线周期从月级压缩到天级。

  - 让模型输出 label+reason+confidence 的 JSON，并用 label 和 confidence 合成标量分，方便接入现有排序/召回链路；7B
  学生单样本 <1s、成本约 $600/百万，适合百万级实时商品匹配。

  - 冷启动迁移时不要从基座从头训：从已有相邻任务 checkpoint 继续做一轮 MERGED，10K 样本即可显著提升，适合跨市场/跨品类关系定义快速扩展。

  - 生成式推荐/Agent 中若需要模型自我解释，可复用 meta-judge 偏好构造思路，提升 reasoning-label faithfulness；但需评估
  meta-judge 的一次性大模型成本。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商产品实体解析中，关系定义随业务持续变化，但传统人工标注 SOP 设计重、周期长、噪声大且缺少推理；大 VLM 零样本虽能立即适应并给出推理，但成本和延迟无法支撑百万级预测。MERGED 用多教师 VLM 自动生成推理标签，再把推理蒸馏到小模型。

**方法关键点**：
- 多教师生成：2 个教师 VLM 对每个产品对输出结构化 completion（answer、reason、confidence）；教师一致样本进入高置信集，不一致样本标记为困难样本。
- 两阶段训练：共识集做 token-level SFT，让学生学习目标关系下的决策边界；分歧集经独立 meta-judge VLM 选择更符合关系定义、更基于可观察证据的 completion 作为 chosen，另一为 rejected，用 DPO 强化判别性推理并贴近 SFT 参考策略。
- 标量分：由 label 和 confidence 合成 [0,1] 分数，支持 PR-AUC。
- 适应新定义：从已有 checkpoint 重新生成少量监督并重跑 SFT+DPO，而非从头训练。

**关键实验**：
- 数据集是内部电商多语言产品对，>100K 训练、约 6K 人类标注测试，覆盖 8 语言 18 国。
- 7B 学生达 90.96% PR-AUC；比同样 backbone 用人类标签 SFT 高 13.79%；比 Qwen2.5-32B-VL 零样本高 6.32%；成本 $600/百万预测，为 32B 的 1/6。
- 消融：模型标签替代人工标签 +3.50，加入推理 +6.14，DPO 再加 +4.15；meta-judge 优于高置信正确（84.36）和更长推理（86.17）启发式。
- 推理对齐 92.82，比 32B 零样本高约 10 个点。
- 新关系 adaptation：从 exact checkpoint 用 10K variant 样本达 89.48%，比零样本高 6.97%，也超 from-scratch MERGED（85.53）。

**最值得记住的一句话**：把大 VLM 的“推理”而不只是标签蒸馏到小模型，并用“共识 SFT、分歧 DPO”的自动课程，是低成本快速适应关系定义变化的关键。
