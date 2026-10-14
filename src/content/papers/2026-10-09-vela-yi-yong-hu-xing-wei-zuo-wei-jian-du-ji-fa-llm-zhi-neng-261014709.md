---
title: 'Vela: User Behavior as Supervision Sparks LLM Intelligence'
title_zh: Vela：以用户行为作为监督激发 LLM 智能
authors:
- Yang Xiao
- Yusong Sun
- Haoyi Wu
- Wenyang Hui
- Weiqiang Hang
- Luqing Wang
- Zejian Wang
- Zirui Tu
- Jingsheng Mao
- Shaobo Hu
affiliations:
- AllSpark Team
arxiv_id: '2610.14709'
url: https://arxiv.org/abs/2610.14709
pdf_url: https://arxiv.org/pdf/2610.14709
published: '2026-10-09'
collected: '2026-10-14'
category: Training
direction: LLM 训练 · 用户行为监督
tags:
- User Behavior
- LLM Fine-tuning
- Behavior Supervision
- Personalization
- SFT
- RL
one_liner: 用10万用户真实行为构造可见历史/隐藏未来任务微调LLM，同步提升用户理解与通用能力
practical_value: '- 可直接借鉴「可见历史/隐藏未来」的构造方式：把电商/广告日志按时序切分，将浏览、搜索、购买、收藏、负反馈作为可见上下文，用未来购买/点击/广告互动作为
  ground truth，自动生成预测式 SFT 数据，省去人工标注。

  - 对用户画像摘要、搜索 query 生成、广告文案等 free-form 输出，用 Rubric 类模板 + LLM scorer 做任务特定 criteria
  自动评估，例如「证据是否来自历史」「是否避免无据属性」，既可用于离线评测，也可作为训练信号。

  - 用基座模型多次采样估计难度，只保留 0.2–0.8 中间难度任务，再选高分轨迹做 SFT/RFT；这套筛选在 AdRecommendation、ProfileSummary
  等任务上带来稳定 OOD 提升，成本低，适合业务个性化模型训练。

  - 先做用户行为 SFT 再做 RL，比从基座直接 RL 高 7.7 分；在电商/Agent 的 RLHF/GRPO 流程前，可先加入一批行为监督 SFT，作为个性化能力的更强初始化。迁移时需按业务事件
  schema 重新设计模板，并注意行为数据隐私合规。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 在个性化、长周期、证据约束场景中能力不足：通用训练语料不包含个体行为如何随时间的演化，合成数据也难以模拟真实用户偏好漂移。与此同时，内容平台和个人助理已积累大规模真实行为序列，其中「用户之后实际做了什么」是一个天然的监督信号。论文提出 user behavior as supervision，用真实未来行为训练 LLM 理解用户，并检验其是否同时改善通用智能。

## 方法关键点
- 数据：10 万匿名用户行为记录，覆盖 Views / Searches / Purchases / Posts / Follows / Dislikes 六类事件。
- 任务构造：按时序将行为分为可见历史 H<t 和隐藏未来 H≥t；基于 91 个模板生成任务，分 Predictive（Objective 候选选择、Open-prediction 自由文本预测）和 Rubric（Open 用户摘要、Attribution 解释未来行为）两族。
- 防泄漏设计：同一未来事件不同时生成 Predictive 和 Attribution 问题。
- 评分：Predictive 用 set-F1，Open-prediction 的语义等价由 LLM scorer 处理；Rubric 用多条 criteria 平均分。
- 数据筛选：用基座模型采样 4 次估计难度，保留均值 0.2–0.8 的任务；每个任务生成 4 条轨迹，仅接受高于难度均值的高分轨迹，形成 Vela-Instruct（约 75K）和 Vela-RFT（9,375）。
- 模型：以 Qwen3.6-35B-A3B 为基座，packed seq len 131,072，2 epochs，lr 1e-5；composer/scorer 用 Qwen3.8-2.4T-A95B 的 xhigh thinking level。

## 关键实验与结果
- 在 VelaBench（982 held-out 任务）上，Vela-35B-A3B 比基座 +11.5 分，超过更大规模的 DeepSeek-V4-Flash 和 Qwen3.8-2.4T-A95B。
- 用户相关 OOD 平均 +6.2 分，其中 AdRecommendation +11.2、ProfileSummary +10.1。
- 通用 OOD 平均 +4.0 分，IFBench +6.7、CL-bench Life +5.6。
- 数据扩展：4.7K→75K 样本，VelaBench 从 59.2 升到 63.0，用户 OOD 从 43.5 升到 47.5，通用 OOD 从 55.8 升到 58.2，仍在上升。
- RL 实验：行为监督 SFT 初始化后再做 GSPO，比基座直接 RL 在 VelaBench 和 ProfileSummary 上均高 7.7 分。

## 最值得记住的一句话
真实用户行为中的未来动作可以成为 LLM 用户维度智能的规模化监督信号；中间难度过滤 + 高分轨迹筛选是关键，它让个性化理解与通用能力同步提升。
