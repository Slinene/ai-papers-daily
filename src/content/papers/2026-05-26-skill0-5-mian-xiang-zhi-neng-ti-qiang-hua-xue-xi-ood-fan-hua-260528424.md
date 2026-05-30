---
title: 'Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution
  Generalization in Agentic Reinforcement Learning'
title_zh: Skill0.5：面向智能体强化学习 OOD 泛化的技能内化与利用联合优化
authors:
- Jiapeng Zhu
- Jianxiang Yu
- Yibo Zhao
- Chengcheng Han
- Qi Gu
- Xunliang Cai
- Xiang Li
- Weining Qian
affiliations:
- East China Normal University
- Meituan
arxiv_id: '2605.28424'
url: https://arxiv.org/abs/2605.28424
pdf_url: https://arxiv.org/pdf/2605.28424
published: '2026-05-26'
collected: '2026-05-30'
category: Agent
direction: Agent 技能训练 · 内化与利用解耦
tags:
- Skill-based RL
- Agentic RL
- Skill Internalization
- Difficulty-Aware Router
- OOD Generalization
- GRPO
one_liner: 提出难度感知路由，将一般技能内化与任务特定技能动态利用解耦，显著提升 LLM 智能体在 ID 与 OOD 场景下的成功率。
practical_value: '- 区分一般技能与任务特定技能：在业务 Agent（如客服、导购）中，可将通用对话策略或跨域推理技能内化到模型，同时动态检索并利用不断更新的业务规则或话术，避免全量外化带来的
  prompt 膨胀和全量内化导致的知识冲突。

  - 难度感知路由思路：根据任务成功率自动分配优化策略——硬任务用特权技能做蒸馏，中等任务强化学习，简单任务强制使用技能防止捷径学习。这种课程式调度可用于多轮对话
  Agent 训练，提升对长尾和新场景的适应。

  - 抗捷径学习诊断：通过剥离特定技能后的性能对比（utilization gain）量化技能依赖，并对绕过技能的行为施加负向梯度，可迁移到基于技能/工具调用的
  Agent 训练中，确保模型真正学会利用外部能力而非记忆表面模式。

  - 解耦训练与推理上下文：训练时利用一般技能进行知识蒸馏，推理时仅保留精简的特定技能，兼顾能力深度和推理效率，可直接用于电商问答、智能推荐对话等对延迟和 token
  成本敏感的场景。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM 智能体通过注入技能（Skill）提升复杂任务表现，但现有技能增强 RL 方法要么始终将技能外挂于上下文（全外化），导致 prompt 膨胀、长上下文推理退化；要么将所有技能完全内化进模型参数，面临容量瓶颈、过拟合及知识冲突，尤其当遇到未见过的 OOD 特定技能时。为此，本工作提出区别化处理：长度大、跨域通用的一般技能应被内化以建立高效认知基础，而易变、细粒度的任务特定技能应动态利用以保证泛化。

**方法关键点**：
- 双池技能库：将技能分为一般技能池（跨域通用）和特定技能池（任务相关），训练及推理时通过嵌入检索 Top‑K 特定技能。
- 难度感知路由：根据当前任务的经验成功率（pass rate）将任务划分为三级——硬（完全失败）、中（成功率≤动态阈值）、易（超阈值）。动态阈值由滑动窗口平均 batch 成功率得到。
- 三级优化：硬任务 —— 使用含一般技能的“特权提示”作为教师，仅用特定技能的“标准提示”作为学生，通过 token 级 Jensen‑Shannon 散度蒸馏，将一般技能内化；中任务 —— 直接用 GRPO 强化成功率，利用组内优势；易任务 —— 引入无技能诊断探针，计算技能利用增益（ui = pi − pnone_i），构造全局任务级优势 Au_i，与轨迹级优势相加，惩罚捷径学习。
- 推理时仅注入特定技能，一般技能已内化于参数，保持低上下文开销。

**结果**：在 ALFWorld 和 WebShop 上按领域划分 ID/OOD 设置，Skill0.5 全面超越基于提示、记忆、RL 及技能增强 RL 的多种 baseline。ALFWorld 上 ID 平均 93.1%（+2.3% vs SkillRL），OOD 平均 58.5%（+13.2%）；WebShop 上 ID 40.4%（+2.1%），OOD 40.6%（+3.9%）。消融证实内化构建推理基础，利用解锁 OOD 适应上限，二者缺一不可。

**核心发现**：通过难度感知的解耦训练，可以在不牺牲推理效率的前提下同时获得稳固的通用能力和对新技能的快速适应。
