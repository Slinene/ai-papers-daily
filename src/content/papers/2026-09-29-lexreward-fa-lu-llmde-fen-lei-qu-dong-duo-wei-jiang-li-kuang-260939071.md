---
title: 'LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models'
title_zh: LexReward：法律LLM的分类驱动多维奖励框架
authors:
- Yida Cai
- Xin Dai
- Bingxiang He
- Huiyuan Xie
- Yuxiao Ye
- Zhenghao Liu
- Yang Bai
- Zhiyuan Liu
affiliations:
- Peking University
- Northeastern University
- Tsinghua University
arxiv_id: '2609.39071'
url: https://arxiv.org/abs/2609.39071
pdf_url: https://arxiv.org/pdf/2609.39071
published: '2026-09-29'
collected: '2026-10-05'
category: Training
direction: LLM对齐 · 多维奖励建模
tags:
- Reward Modeling
- DPO
- RLHF
- Legal LLM
- Taxonomy
- Preference Optimization
one_liner: 提出按Style/Element/Chain三维分解的法律奖励框架，用rubric构建偏好数据训练DPO和奖励模型
practical_value: '- 把整体质量奖励拆成多个可诊断维度（如表达质量、关键要素、推理链），分别建模与优化；推荐/搜索生成式场景可类似拆成相关性、多样性、新颖性、转化意图等维度，避免单一粗粒度打分掩盖短板。

  - 用 rubric 定义评估标准，让 LLM 对候选输出打分并构造偏好对，替代昂贵的人工标注；在电商文案生成、推荐理由、搜索 query 改写中可低成本生产
  DPO 偏好数据。

  - 维度专用 reward model 支持 RL 优化且不需要 reference answer，适合在线反馈稀疏、缺乏标准答案的生成任务；可在强化学习推荐或对话式推荐中作为
  reward shaping 组件。

  - 论文的维度分析思路可迁移到上线前评估：先对模型输出做多维自动评测，定位具体短板维度，再针对性做 DPO 或 RL 优化，而不是全局调参或重新训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：法律LLM的输出质量不仅取决于答案正确性，还涉及法律要素完整性、推理链合理性和表达规范。现有奖励方法多为整体粗粒度判断，缺乏领域针对性和可解释性，难以定位具体质量问题。

**方法关键点**：提出LexReward，将法律回答质量分解为三个互补维度：Style（词汇与句法质量）、Element（法律主体、事实、法条、判决等要素）、Chain（推理顺序、完整性、正确性、非冗余）。每个维度设计rubric，明确评估标准和质量等级。基于rubric为候选回答打分，构造成对偏好数据，用于DPO训练策略模型和训练奖励模型LexRM。LexRM支持下游RL优化，奖励时不需要参考回答。

**关键结果**：实验表明rubric奖励能可靠区分不同质量的法律回答；DPO训练在Style、Element、Chain三个维度均带来性能提升；各维度专用奖励模型通过RL分别提升对应维度策略表现，验证了taxonomy和奖励构造的有效性。
