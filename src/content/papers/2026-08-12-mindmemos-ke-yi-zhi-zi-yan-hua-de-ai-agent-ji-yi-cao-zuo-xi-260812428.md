---
title: 'MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents'
title_zh: MindMemOS：可移植自演化的 AI Agent 记忆操作系统
authors:
- Kaichao Liang
- Yuqi Cui
- Hao Kong
- Xinyuan Huang
- Guohaotian Hou
- Qingcan Kang
- Liang Chen
- Yiyang Yin
- Ke Ye
- Jiaquan Guo
affiliations:
- Noah's Ark Lab, Huawei Technologies
arxiv_id: '2608.12428'
url: https://arxiv.org/abs/2608.12428
pdf_url: https://arxiv.org/pdf/2608.12428
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 记忆操作系统与自我演化
tags:
- agent memory
- self-evolving
- memory consolidation
- skill evolution
- schema evolution
- LLM agents
one_liner: 提出实体-属性-时间三维记忆结构与四类自演化机制，实现可移植、自演化的 Agent 记忆层
practical_value: '- **用户画像与偏好演化**：借鉴 3D entity-property-time 结构，把电商/推荐场景中的用户、商品、偏好事件建模为实体、属性、时间线，支持偏好变更、冲突版本管理与时序推理。相比纯文本记忆，更适合追踪用户兴趣漂移（例如
  LOCOMO 的 temporal/multi-hop 问题）。

  - **离线记忆压缩与冲突解决**：Dreaming 机制把线上增量写入造成的冗余、过期、冲突记录离线合并、归档并保留 provenance。在推荐/广告场景可用于定期压缩用户行为记忆，保证活跃记忆库不过度膨胀，同时保持检索质量（论文中
  AMCR 约 20%，准确率反升）。

  - **隐式反馈分类与记忆修正**：将用户对 Agent 的纠正按持久性分为 task-temporary / scenario-specific / long-term，避免把一次性指令写入长期记忆。电商导购、对话式推荐中可据此捕获用户隐含偏好与约束，减少重复推荐错误，尤其适合处理“这次不要”、“以后都这样”等模糊纠正。

  - **轨迹驱动的技能演化**：MindSkillEvolve 将 Agent 执行轨迹提炼为可复用、版本化的技能，可通过 unsupervised 或 score-guided
  方式持续改进 SOP。可迁移到客服/导购 Agent 的流程能力迭代：用真实对话与任务执行日志自动总结高效策略与失败模式，生成可回滚的技能版本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有 LLM Agent 记忆系统大多在部署后保持固定，难以适应新场景、维护增量写入带来的冗余与冲突，且记忆内容与程序技能分离，无法将执行经验转化为可复用能力。MindMemOS 旨在提供一个可移植、自演化的记忆操作系统层。

## 方法关键点
- **三维记忆结构**：以实体（entity）、属性（property）、时间（time）为三个维度组织记忆，支持关系与时间线追踪，统一表达事实、画像、偏好与事件。
- **双模式记忆写入**：MindVanilla 不依赖 schema 进行粗粒度提取；MindSchema 利用可配置 schema 进行细粒度实体-属性抽取、实体融合与图合并。
- **紧凑搜索**：混合 BM25 + 稠密语义检索，支持前向/后向图遍历与实体/属性多键增强，由 LLM 控制器迭代规划。
- **四类自演化机制**：
  1. MindMemEvolve：用验证驱动的进化搜索优化记忆 schema，通过错误诱导变异、随机变异与交叉发现一阶/高阶属性；
  2. Dreaming：离线合并冗余、解决冲突、归档过期记忆，保留溯源关系；
  3. Feedback：显式与隐式反馈将用户纠正转化为记忆增删改操作，并按持久性分类；
  4. MindSkillEvolve：从执行轨迹中提炼可复用技能，支持无监督与有监督演化。

## 关键实验
- LOCOMO 长程对话记忆：MindSchema 总体准确率 94.03%，超过 EverOS 的 93.05%，在 Single-hop、Multi-hop、Temporal、Open-domain 均最优。
- PersonaMem 个性化：MindSchema 总体 70.63%，比 EverOS 高 3.06 个百分点，Recall Shared 与 Suggest 提升显著。
- MemoryAgentBench 冲突解决：Dreaming 在 gpt-5-mini 下整体准确率 0.545→0.585，同时压缩约 22.5% 活跃记忆。
- SpreadsheetBench 技能演化：MindSkillEvolve-Sup 相对 Init-skill 提升 9.2 个百分点（48.0→57.2），相对 No-skill 提升 5.9 个百分点。

## 最值得记住的一句话
通过显式实体-属性-时间结构、验证驱动 schema 演化、离线 dreaming 与隐式反馈分类，实现记忆系统的可移植与自演化。
