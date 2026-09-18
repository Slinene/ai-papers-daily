---
title: What Does Privileged Information Add to On-Policy Self-Distillation?
title_zh: 特权信息在在线策略自蒸馏中究竟增加了什么？
authors:
- XiuYu Zhang
- Wei Chow
- Junfeng Fang
- Zhenkai Liang
- Tat-Seng Chua
affiliations:
- National University of Singapore
arxiv_id: '2609.20612'
url: https://arxiv.org/abs/2609.20612
pdf_url: https://arxiv.org/pdf/2609.20612
published: '2026-09-16'
collected: '2026-09-18'
category: Training
direction: 训练方法 · 自蒸馏与特权信息
tags:
- self-distillation
- on-policy
- reasoning
- privileged-information
- LLM-training
- cross-mode-transfer
one_liner: 系统分离自蒸馏与特权参考的贡献，发现特权信息仅带来有限增益，核心机制是跨模式能力转移
practical_value: '- **蒸馏目标设计**：在电商/搜索的 LLM 自我蒸馏中，不必过度追求“教师看到完整推理/用户行为解释”的特权信息；无参考的蒸馏目标（只用问题-答案对）就能激活大部分跨模式迁移，可显著降低数据标注与构造复杂度。

  - **学生生成模式**：训练时学生的 rollout 模式应与评估模式一致，例如用短直接回答而非长思维链作为训练样本，否则收益可能反转为损失；这提示生成式推荐或
  QueryRec 蒸馏时，训练样本的生成风格需匹配线上推理风格。

  - **Token-level 监督的敏感性**：改变 token 级别的损失干预（如不同 mask 策略）可能对模型最终行为影响很小，实际调参时可将精力集中在宏观目标与数据分布上，而非逐
  token 细节。

  - **跨模式能力共享**：参数共享使直接回答与思考回答的能力可相互迁移，OPSD 是低成本激活已有推理能力的有效手段，适用于资源受限的推荐/广告文案生成模型升级。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
在线策略自蒸馏（OPSD）允许教师看到答案或解题过程，但很难区分“蒸馏本身”和“特权信息”各自带来的提升。作者构建 AMPLE-Math 数据集（5,319 道数学题，六个共享答案的推理视角），在无参考蒸馏的对照下剥离特权信息的净贡献。

**方法关键点**
- 教师为冻结的思考模式模型，监督学生的直接回答 rollout；对比无参考蒸馏与带不同形式参考（答案、polished solution、完整轨迹等）的蒸馏。
- 变更学生 rollout 模式（短直接回答 vs. 长思考轨迹）观察方向性影响。
- 通过教师 profiles 和 matched loss 干预，考察 token-level 监督的实际作用。

**关键结果**
- 在 Qwen3-1.7B 上，无参考蒸馏已贡献了思考评估下的大部分提升，额外参考收益总体温和；polished solution 在 Qwen 中最有效，SmolLM3-3B 在 step 50 额外获得 2 个百分点。
- 将短直接回答 rollout 替换为长思考 rollout 后，相同问题与评估下收益转为损失，且跨模型家族一致。
- 改变 token-level 监督对模型行为影响很小。

结论：OPSD 主要通过共享参数实现直接回答与思考模式间的能力转移；特权参考的价值体现在为这种跨模式转移追加的增益，而非它揭示了多少解题内容。
