---
title: 'SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents'
title_zh: SkillBrowser：面向可扩展技能使用智能体的选择性技能暴露
authors:
- Jin Ye
- Yifan Jiang
- Lan-zhe Guo
affiliations:
- Nanjing University
arxiv_id: '2610.23554'
url: https://arxiv.org/abs/2610.23554
pdf_url: https://arxiv.org/pdf/2610.23554
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能选择性暴露
tags:
- Selective Skill Exposure
- Meta-Skill
- LLM Agents
- Skill Retrieval
- Agent Framework
one_liner: 提出 Meta-Skill 管理框架，让智能体按需识别能力需求并加载技能，优于静态检索和 LLM 选择
practical_value: '- 可将电商/广告/搜索推荐系统中的工具、知识库、规则引擎封装为可加载的 Skill，用 Meta-Skill 根据当前任务状态动态判断需要哪些能力，避免一次性注入大量上下文造成污染。

  - 采用“识别需求 → 生成查询 → 按需加载”的流程替代静态检索，能更好地匹配推理过程中逐渐浮现的能力需求，适合多步工具调用和长链路任务。

  - 注意权衡：选择性暴露可能漏掉有用技能（under-invocation），且增加额外查询和加载延迟；在生产环境中可设置置信度阈值或缓存常用技能组合。

  - 评估时需同时关注聚合准确率和已可解决实例上的性能退化，确保新机制不会损害原本能处理好的任务。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 依赖可复用技能扩展能力，但技能库扩大时一次性暴露全部技能会造成上下文污染，而静态检索基于初始任务查询可能无法匹配推理中后期出现的能力需求。现有渐进披露和检索方案各有不足，需要选择性技能暴露（SSE）。

**方法关键点**：提出 SkillBrowser，由 Meta-Skill 统一管理技能访问。Agent 在处理任务过程中识别当前能力缺口，构造针对性查询，按需加载相关技能内容到工作上下文。与静态检索和 LLM 直接选择技能不同，SkillBrowser 将“何时需要什么技能”的决策过程显式建模为一个元技能，实现动态、循序的技能暴露。

**关键结果**：在 SRA-Bench 的六个子集和五个 LLM 上，SkillBrowser 的聚合准确率优于静态检索和 LLM-based selection，尤其在多步工具使用任务中表现更好，同时减轻了对已可解决实例的准确率下降。限制包括模型和任务相关性、有用技能调用不足以及额外延迟。
