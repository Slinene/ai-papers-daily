---
title: 'SkillBrew: Multi-Objective Curation of Skill Banks for LLM Agents'
title_zh: 面向LLM智能体的多目标技能库优化框架
authors:
- Wentao Hu
- Zhendong Chu
- Yiming Zhang
- Junda Wu
- Ming Jin
- Xiangyu Zhao
- Yilei Shao
- Yanfeng Wang
- Qingsong Wen
affiliations:
- City University of Hong Kong
- Squirrel Ai Learning
- University of Science and Technology of China
- University of California, San Diego
- Griffith University
arxiv_id: '2605.29440'
url: https://arxiv.org/abs/2605.29440
pdf_url: https://arxiv.org/pdf/2605.29440
published: '2026-05-28'
collected: '2026-05-30'
category: Agent
direction: LLM Agent 技能库的多目标全局优化
tags:
- skill bank curation
- multi-objective optimization
- LLM agents
- Pareto optimization
- counterfactual replay
one_liner: 提出SkillBrew，通过效用-多样性-覆盖度多目标全局优化解决技能库膨胀与冗余问题
practical_value: '- 技能库不应只增不减，可引入效用、多样性和覆盖度三目标联合评价，避免冗余或低效技能挤占检索槽位。

  - 通过反事实重放（leave-one-out replay）量化单个技能的边际贡献，为编辑决策（KEEP / REWRITE / REMOVE）提供细粒度信号，可在Agent日常运行中低成本积累证据。

  - 双层 propose-then-verify 循环可分隔提议与验证，避免过拟合：用支持集产生编辑候选，在查询集上帕累托选择，保证推广性。

  - 技能库跨模型迁移能力强，可为电商对话Agent或推荐Agent构建通用决策知识库，通过持续 curation 提升推荐逻辑的稳定性与覆盖度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
LLM Agent 在长期任务中常依赖技能库（skill bank）来积累可复用的流程知识，但现有方法大多是“只增不减”或基于单一标量评分管理技能，造成技能库膨胀、冗余甚至有害技能污染。单纯依靠效用一个维度无法平衡技能的多样性、覆盖度，而这三个目标天然相互制衡——扩大覆盖会引入冗余降低多样性，严格剪枝又会损失覆盖。亟需一种全局、多目标的技能库管理范式。

**方法关键点**  
- 形式化为带约束的多目标优化：最大化效用、多样性、覆盖度，并以效用作为最低阈值约束，多样性和覆盖度作为结构化正则。  
- 采用双层 **propose-then-verify** 循环：内层从支持集轨迹中通过反事实重放诊断每个技能（KEEP/REWRITE/REMOVE），并生成候选编辑；外层在查询集上评估候选库的效用、多样性和覆盖度，用帕累托前沿选择，并引入“空候选”允许无变更传递。  
- 反事实评估：对每个被检索技能执行 leave-one-out 重放，计算技能移除前后的任务奖励差，得到细粒度的边际贡献。  
- 多样性用技能嵌入 Gram 矩阵的行列式体积度量；覆盖度由检索密度和技能使用率乘积定义。  
- 编辑计划器综合三种操作（ADD/REWRITE/REMOVE）组合生成多个候选库，并保留 KEEP 技能作为保护槽。实验中使用 GPT‑5.4 驱动蒸馏、诊断和计划器，Agent 工作器固定为 ReAct 风格。

**关键实验**  
- 数据集：ALFWorld（6 类家庭任务）和 WebShop（在线购物模拟），均采用训练/支持/查询/测试划分。  
- 基线：Zero‑Shot、ReAct、4 种记忆基线（Reflexion、Mem0、MemP、SimpleMem）、4 种技能基线（Voyager、ExpeL、EvoSkill、Skill‑Pro）。  
- 所有方法使用相同冻结的 Qwen2.5‑7B‑Instruct 工作器。SkillBrew 在 ALFWorld 平均成功率达 59.0%（比最强技能基线高出 9.7%，比 ReAct 高 27.8%）；WebShop 得分 59.3%，完全匹配率 38.4%。跨工作器迁移实验中，GPT‑4o 搭配 SkillBrew 将 ALFWorld 成功率从 46.4% 提升至 88.1%。  
- 消融显示，仅用效用目标时成功率为 45.8%，加入多样性和覆盖度后提升到 59.0%；三种编辑操作全部使用方能达到最优。

**最值得记住的一句话**：技能库应当作为一个全局的多目标优化对象，而不是孤立评估技能，这样产生的流程知识才真正有效、多样且覆盖广泛。
