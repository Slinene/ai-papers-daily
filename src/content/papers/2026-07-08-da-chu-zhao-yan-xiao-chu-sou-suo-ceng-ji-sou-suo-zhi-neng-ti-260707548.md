---
title: 'Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?'
title_zh: 大处着眼，小处搜索：层级搜索智能体的模型容量分配
authors:
- Qinnan Cai
- Yibo Zhao
- Xiang Li
affiliations:
- East China Normal University
arxiv_id: '2607.07548'
url: https://arxiv.org/abs/2607.07548
pdf_url: https://arxiv.org/pdf/2607.07548
published: '2026-07-08'
collected: '2026-07-09'
category: MultiAgent
direction: Agent 多智体角色分工与容量分配
tags:
- Multi-Agent Search
- Role Factorization
- Capacity Allocation
- Trajectory Distillation
- LLM
- Qwen3
one_liner: 在层级搜索Agent中，规划侧的容量是瓶颈，执行侧可缩至1.7B且性能不降，颠覆均匀分配惯例。
practical_value: '- 构建搜索/查询推荐多Agent系统时，将大模型集中用于任务分解（如query理解、子任务规划），检索执行等子Agent使用小模型（如1.7B），可大幅降低推理成本而几乎不损失效果。

  - 容量扫查揭示显著不对称性：执行模型从小变大提升微弱（EM仅+2.6），规划模型提升巨大（EM+11），投资重点应放在规划侧。

  - 采用**质量过滤的轨迹蒸馏**可将大模型的纠错搜索行为（多轮检索）注入小模型：保留学生正确的单步搜索轨迹，仅用教师多步搜索的成功样例训练，避免遗忘，使小模型执行器性能超越前沿大模型，且子Agent
  token消耗减少37%。

  - 答案生成与搜索分解隔离，避免答案模型参数记忆泄露；此设计可迁移至推荐系统的解释生成环节，固定生成器仅改变查询规划与召回执行，实现无偏消融评估。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
多Agent搜索系统通常让主Agent分解复杂问题为子查询，分派给多个子Agent执行并汇总证据。但现有系统几乎都用同一个模型实例化所有角色，未探究不同角色对模型容量的需求差异。如果执行侧只需很小模型就能胜任，就能大幅节省推理成本。该研究通过受控实验解答：1) 角色分解是否优于单Agent？2) 规划与执行哪个是容量瓶颈？3) 能否通过针对性训练让紧凑执行器达到前沿水平？

## 方法
- **角色分解**：将层级搜索明确划分为三个角色——委派（delegation，规划子查询）、执行（execution，检索并提取证据）、答案生成（固定不变，避免干扰）。
- **容量扫查**：固定答案生成为Qwen3-32B，独立改变委派模型（1.7B→前沿）和执行模型（1.7B→前沿）的容量，在多跳QA基准（2WikiMultihopQA、HotpotQA、MuSiQue、PopQA、Bamboogle）上评估。
- **紧凑执行器训练**：基于能力差距分析，发现小模型单步搜索已够，但缺乏多步搜索（重搜索）能力。采用**质量过滤的轨迹蒸馏**：用教师模型（DeepSeek-V4-Pro）和未训练学生（Qwen3-1.7B）在相同子查询下生成轨迹；保留两者的正确单步搜索轨迹以防止学生遗忘；仅选择教师成功的多步搜索样例（同时确保单步搜索失败）作为训练数据，用SFT注入多步搜索行为。

## 关键结果
- 角色分解相比单Agent一致提升EM 4.5~8.6点（跨6种模型规模）。
- **容量不对称性显著**：固定执行器为1.7B，缩放委派模型从1.7B到DeepSeek-V4-Flash，EM提高11.3点；固定委派模型为前沿，缩放执行器从1.7B到前沿，EM仅提高2.6点。
- **紧凑执行器达前沿**：通过轨迹蒸馏训练的Qwen3-1.7B-SFT执行器，在DeepSeek-V4-Flash骨架下EM达41.81，超过前沿执行器的41.77，同时子Agent平均tokens消耗减少37%。
- 跨骨架泛化：在GLM-5.1骨架上，紧凑执行器同样匹配前沿性能。

**核心洞察**：在层级搜索Agent中，规划（任务分解）是瓶颈，执行可大幅缩容。"大模型用在刀刃上，小模型管执行"是高效架构的设计原则。
