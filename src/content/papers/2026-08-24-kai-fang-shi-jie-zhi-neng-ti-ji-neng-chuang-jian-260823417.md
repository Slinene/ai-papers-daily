---
title: 'SkillAlchemy: Open-World Agent Skill Creation'
title_zh: 开放世界智能体技能创建：SkillAlchemy
authors:
- Hengjun Wang
- Shuyue Wei
- Boyi Liu
- Jun Yang
- Yongxin Tong
affiliations:
- Beihang University
- Shandong University
- Northwestern Polytechnical University
arxiv_id: '2608.23417'
url: https://arxiv.org/abs/2608.23417
pdf_url: https://arxiv.org/pdf/2608.23417
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 技能自动创建与证据准入
tags:
- Agent Skills
- Skill Creation
- Open-World
- Procedure Admission
- Evidence Grounding
- LLM Agents
one_liner: 提出基于证据准入的框架，从开放世界材料自动创建可复用 Agent 技能，性能接近人工策划
practical_value: '- **隐式需求挖掘可迁移到 query/对话推荐**：用对比探测（替换、边界、邻居）从简短 brief 或用户 query 中挖掘遗漏的操作维度，例如从“7天欧洲旅行”中识别出预算、旅客类型、出行方式等隐含条件，可用于电商领域的
  query 补全、推荐策略扩展或对话式需求澄清。

  - **证据准入机制防止过拟合到局部案例**：区分“通用指令”“局部示例”“排除项”的三分类决策，强制要求跨场景一致性证据才能推广为通用规则。在电商推荐策略生成中，可避免把某个爆款商品的特定操作误认为平台级策略，只保留有跨品类或跨场景支持的通用做法。

  - **渐进式技能包组织节省推理上下文**：借鉴 skill grammar 和文件分层（核心指令在 SKILL.md，细节放 references/scripts），在构建
  Agent 工具库或推荐策略库时，把高频核心逻辑保持精简，低频案例外部化，既能提高加载效率，又降低 token 消耗。

  - **对抗性来源鲁棒性可应用于外部数据清洗**：论文验证了无关、冲突、对抗性源材料会被现有创建器误吸收，而 SkillAlchemy 通过明确的 admission
  记录排除。在从用户评论、市场报告等开放数据提取洞察时，可以借鉴其“支持性+一致性+可复用性”的准入检查，减少噪声污染。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
现有 Agent 技能创建依赖人工编写、模型先验或执行轨迹，但在陌生任务中这些来源往往不可用。开放世界材料（文档、仓库、issue）蕴含可复用的过程知识，但直接检索容易引入过特定化或错误泛化。论文 pilot study 显示，开放世界源能提升技能创建效果，但仍与人工技能有约 14pp 差距。核心挑战有二：任务 brief 欠规格化，遗漏行为关键需求；开放世界发现缺乏范围论证，局部案例易被误认为通用指令。

**方法关键点**
将开放世界技能创建形式化为 source-grounded procedure-admission 问题，提出三阶段框架 SkillAlchemy：
1. **隐式需求发现**：通过对比证据获取，构造配对探测（替换、边界、邻居），将 brief 提升为操作框架，识别遗漏需求维度，转化为聚焦研究问题。
2. **证据准入**：将发现按过程决策分组，归纳候选过程，以支持性、一致性、可复用性三个条件判定是否准入为通用指令、局部示例或排除。只有跨上下文兼容证据支持的候选才能成为通用指令。
3. **技能包编译**：使用从公开技能语料库提取的 skill grammar 指导渲染，保持核心指令精简，细节外部化到 references/scripts，实现渐进式披露。

**关键实验**
在 SkillsBench v1.1 的 87 个任务、8 个领域、4 个 agent-model 配置上评估。对比 NoSkill、Human-Curated、Anthropic/OpenAI Skill-Creator、OpenSkill、MUSE-Autoskill。结果：SkillAlchemy 比无技能执行提升 19.9pp，比最强自动基线 MUSE-Autoskill 提升 8.6pp，聚合 avg@5 达 55.8%，与人工技能 54.4% 相当。消融显示移除隐式需求发现、结构化发现、过程准入或 grammar 均导致 5.0–15.7pp 下降。鲁棒性测试中，SkillAlchemy 不提升任何注入的无关/冲突/对抗性负载，下游通过率稳定。

**最值得记住的一句话**：可靠技能创建应将开放世界知识视为需在明确范围内准入的证据，而非可直接复制的指令。
