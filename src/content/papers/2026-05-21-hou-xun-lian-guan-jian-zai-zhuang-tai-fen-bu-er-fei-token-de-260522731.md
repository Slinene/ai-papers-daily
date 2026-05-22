---
title: 'Post-Training is About States, Not Tokens: A State Distribution View of SFT,
  RL, and On-Policy Distillation'
title_zh: 后训练关键在状态分布而非Token：SFT、RL与在线蒸馏的状态视角
authors:
- Dong Nie
arxiv_id: '2605.22731'
url: https://arxiv.org/abs/2605.22731
pdf_url: https://arxiv.org/pdf/2605.22731
published: '2026-05-21'
collected: '2026-05-22'
category: Training
direction: LLM后训练状态分布视角
tags:
- Post-training
- State Distribution
- On-policy
- Distillation
- SFT
- RL
one_liner: 提出状态分布视角统一SFT、RL和在线蒸馏，实验显示学生可超越退化教师且on-policy方法更稳定
practical_value: '- **用状态源/信号源拆解训练策略**：将推荐Agent的训练明确分为“状态采自哪里”和“监督信号从哪里来”。离线数据（如用户历史日志）提供固定状态，但Agent部署后可能遇到未覆盖的状态分布，借鉴on-policy采样（RL或在线蒸馏）能减轻分布不匹配造成的性能退化。

  - **在线蒸馏时让学生控制状态分布**：在电商场景中，Teacher模型可能在某些上下文（如长对话或冷门商品）表现差，但局部Token预测仍可用。让学生Agent在自身状态上请求教师指导（如生成短续写），类似DAgger，可以保留教师局部能力的同时避免复制教师的全局错误轨迹，实现学生超越教师。

  - **避免单纯用标量漂移判断遗忘**：业务监控时，不要仅靠rollout状态的MMD等单一距离指标下结论。论文显示，两个模型可能有相近的全局状态漂移但遗忘程度迥异。应结合状态来源分析——是在模型自身可达状态上做更新（如RL/OPD），还是在与模型当前策略偏离的固定状态上做密集离线更新（如stress
  SFT）。

  - **轻量在线RL可作为能力保留手段**：在追求目标指标提升时，可以先跑一轮温和SFT注入基础能力，再用在线RL（如带分组相对奖励的GRPO）在模型自身轨迹上小步优化，既能提升主任务，又可抑制遗忘。对电商搜索排序或对话Agent，可设定简单的验证性奖励（如用户点击、转化），用on-policy采样来微调，保持通用知识不退化。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
现有LLM后训练（SFT、RL、蒸馏）的分析多聚焦于损失函数形式，但难以解释为何SFT有时导致灾难性遗忘，而RL能保留能力，甚至学生能超越教师。本文提出状态分布视角：自回归模型的状态是“提示词+生成前缀”，训练时的状态来源决定了更新作用的位置。SFT在固定数据集状态上做密集更新（off-policy），当这些状态与模型自身采样状态差距大时，可能破坏原有能力；RL和在线蒸馏（OPD）在模型自身诱导的状态上更新（on-policy），更新更局部、稳定。

## 方法关键点
- 将post-training分解为状态源（采样自何处）和信号源（标签/奖励/教师logits）；SFT状态源=数据集，信号=黄金Token；RL状态源=当前策略，信号=奖励；OPD状态源=学生策略，信号=教师提供的Token或短续写。
- 实验基于Qwen3-0.6B-Base+LoRA，对比mild SFT、stress SFT、OPD（从mild或stress教师蒸馏）和轻量on-policy RL（GRPO风格）。OPD采用学生采样状态、教师生成短续写的方式，避免单步KL导致的崩溃。

## 关键结果
- **SFT双面性**：mild SFT将GSM8K从0.448升至0.512，几乎无遗忘（retention ratio 1.0008）；stress SFT则使GSM8K降至0.420，同时TruthfulQA和MMLU分别从0.300/0.436降至0.245/0.364，造成严重遗忘。
- **OPD超越退化教师**：以stress SFT为教师（GSM8K 0.420, TruthQA 0.245, MMLU 0.364），OPD学生达0.466/0.275/0.430，全面超越教师，证明学生可从教师局部能力获益而不继承其全局轨迹错误。
- **RL保持能力**：轻量RL将GSM8K提至0.472，遗忘仅0.002，保留能力极好，支持on-policy局部更新的稳定性。
- **漂移并非全貌**：stress SFT与OPD的MMD漂移几乎相同（约0.0109），但遗忘差距大（0.0635 vs 0.0155），说明仅凭标量漂移无法解释遗忘，需关注状态来源、局部性及可达性。

最值得铭记的一句：“后训练不仅关乎Token目标或标量分布漂移，更关乎监督信号被施加在模型状态空间的何处。”
