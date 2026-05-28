---
title: 'Learn from Weaknesses: Automated Domain Specialization for Small Computer-Use
  Agents'
title_zh: 从弱点学习：小型计算机代理的自动领域特化框架
authors:
- Suji Kim
- Kangsan Kim
- Sung Ju Hwang
affiliations:
- KAIST
- Samsung Electronics
- DeepAuto.ai
arxiv_id: '2605.28775'
url: https://arxiv.org/abs/2605.28775
pdf_url: https://arxiv.org/pdf/2605.28775
published: '2026-05-26'
collected: '2026-05-28'
category: Agent
direction: Agent 领域特化与自动化数据生成
tags:
- Computer-Use Agent
- Domain Specialization
- Weakness-aware Data Generation
- Preference Optimization
- LoRA
one_liner: 自动识别学生模型弱项生成针对性训练数据并纠正错误，大幅提升小型CUA在特定软件上的任务成功率。
practical_value: '- 自动化弱项发现：用强模型与学生执行对比，生成弱项报告，可迁移到电商客服Agent的定向问题数据收集，降低人工标注成本。

  - 弱项驱动的数据合成：生成任务时附加弱项描述与代表性截图，使数据直接瞄准模型能力缺口；推荐系统可模仿此机制，针对用户长尾偏好生成训练样本。

  - 错误类型感知的偏好优化：区分规划错误（函数类型错）与执行错误（参数错），通过掩码DPO只更新错误相关动作token，避免过度纠正，提高训练稳定性与效率，适用于Agent微调。

  - LoRA多领域模块化部署：共享基座 + 领域特定LoRA适配器，轻量切换，电商多场景Agent（搜索、推荐、客服）可复用此架构，快速扩展新领域。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
部署大型专有计算机使用代理（CUA）成本高，小型开源CUA虽经济但领域特定任务成功率低，且简单扩大训练数据效果微弱。领域特化需要自动化方法，既节省人工标注，又能精准修复学生模型的薄弱环节。

**方法关键点**
- **弱项感知数据生成（LEARNWEAK-GEN）**：利用强教师模型与学生模型执行同一任务，收集学生失败而教师成功的情况，汇总失败原因生成弱项报告；结合代表性截图与弱项报告，迭代生成新查询，平衡弱项聚焦与探索性任务，无需人类标注。
- **错误类型感知偏好优化（LEARNWEAK-DPO）**：在教师成功轨迹上重放学生模型，抽取步骤级偏好对（教师正确动作 vs 学生偏差动作），将错误分为规划错误（函数类型错）与执行错误（参数错），训练时通过掩码仅对动作描述和工具执行部分施加偏好信号，保持推理部分不受影响，实现精细化纠正。
- **模块化部署**：冻结基座模型，用LoRA适配器注入领域知识，实现多领域共享特化。

**关键结果**
在OSWorld 8个软件域（如LibreOffice、VSCode等）上，EvoCUA-8B和OpenCUA-7B经LEARNWEAK特化后平均成功率分别提升11.6和11.1个百分点，且特化后的EvoCUA-8B在多个域内超越教师模型；相比其他自动化数据生成基线，LEARNWEAK数据集训练的模型平均胜出5.58个百分点；错误感知DPO比标准SFT/DPO平均提高9.62个百分点。
