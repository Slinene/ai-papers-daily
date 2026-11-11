---
title: 'AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language
  Models'
title_zh: AutoScaffold：LLM 教师自动生成与自适应 RL 训练脚手架
authors:
- Zijian Zhang
- Rizhen Hu
- Jiangweizhi Peng
- Shiyang Li
- Sujay Bhatt
- Sihan Zeng
- Mingyi Hong
affiliations:
- University of Minnesota, Twin Cities
- JPMorgan AI Research
arxiv_id: '2611.14515'
url: https://arxiv.org/abs/2611.14515
pdf_url: https://arxiv.org/pdf/2611.14515
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: RL 训练自动脚手架 · LLM Teacher
tags:
- RLVR
- LLM Teacher
- Scaffolding
- Agent
- GRPO
- AutoML
one_liner: 冻结 LLM 教师从学生 RL 训练经验中自动诊断失败、生成类级策略与实例级提示，评估时移除脚手架，四域提升独立能力
practical_value: '- 在电商搜索/推荐 Agent 的 RLVR 训练中，用冻结 LLM 教师定期读 rollout 日志（工具调用失败、query
  改写失败等），自动生成类级策略作为 prompt scaffold，评估时移除，可缓解稀疏奖励和 learning cliff；教师应主动选择要看哪些失败轨迹和成功/失败对比，而不是固定采样。

  - 类级 scaffold 可按商品类目/query 类别设置注入概率 `q[C]`，强制 `qmax<1` 保留无支撑样本，避免评估时模型因缺少提示退化；这类似
  privileged information dropout，可直接用于课程式 RL。

  - 教师提出类级 scaffolds 后，先在一组 held-out 任务上对比“无脚手架/当前/提议”的成功率再部署，防止一整类任务的训练被有害提示污染；对应推荐系统可预留部分类目做离线验证或小流量
  AB。

  - 对搜索 Agent 或对话推荐中某些任务长期全部失败导致无梯度，可让教师给出实例级 partial solution/关键步骤提示，让它们进入混合成功/失败组产生训练信号；但必须随能力提升撤回支持，避免模型依赖。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
RLVR 产生丰富训练经验，但结果奖励把每次 rollout 压缩成单一数字，大量失败/成功细节被丢弃；训练时脚手架（策略、提示、部分解）可以把这些经验转化为指导，但现有方法靠人工设计、固定规则，且每个领域要重新设计。AutoScaffold 用一个冻结 LLM 教师自动、自适应地生成脚手架，评估时移除，目标提升学生独立能力。

**方法关键点**
- 双级脚手架：类级策略 `S_class[C]`（任务类共享，注入概率 `q[C]≤qmax<1`，保留无支撑样本）和实例级提示 `S_inst[x]`（针对仍然失败的单任务，如数学解前缀）；RL 算法不变，脚手架作为 prompt 的一部分。
- 教师每 `K` 步更新一次：用 `Qstat/Qtraj/Qgroup` 三种查询工具与决策记忆 `M` 主动选择证据；诊断各任务类的失败模式；提出类级策略增删改、注入概率调整、实例提示。
- 类级编辑先在 held-out 任务上对比“无脚手架/当前/提议”三种成功率，验证后再部署；教师指令只含领域描述和类列表，不写领域规则。
- 原则：二元奖励下，rollout 组只有成功与失败混合才产生梯度，类级支持应把成功率推向 0.5 附近，实例级支持把零成功任务引入训练；支持随能力提升撤回。

**关键结果**
- ALFWorld：93.9% 成功率（+7.2 vs GiGPO 86.7）；搜索 QA：46.1% EM（+4.0 vs GiGPO 42.1）；数学 4B：70.1%（+1.4）且与 SAGE 持平；1.5B：62.4%（+2.0，仅 350 步，超过 QuestA 61.1@1100 步）；KernelBench 平均 correctness +3.0，Level 2 Fast1 +5.0。
- 消融：去掉类级验证降 14.1 点；静态 Skill0 技能库降 15.3 点；`qmax=1` 低于 RL baseline；去掉查询工具与记忆降 8.6 点。
- 教师会随学生进步从逐步工作流转向针对性修复，并降低注入概率。

**一句话**：把 RL 训练经验交给冻结 LLM 教师定期诊断、生成并验证临时脚手架，可在不改变 RL 算法和评估条件下跨域提升模型独立能力。
