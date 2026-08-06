---
title: 'SKILL-KD: Contrastive Skill Distillation for LLM Agents'
title_zh: SKILL-KD：通过对比式技能蒸馏增强冻结的LLM Agent
authors:
- Qiming Shi
- Yibo Dou
- Jiawen Zhu
- Yulong Tao
- Linbo Jin
- Zhaolu Kang
- Yunfan Zhou
- Di Weng
affiliations:
- State Key Lab of CAD&CG, Zhejiang University
- School of Software Technology, Zhejiang University
- School of Software and Microelectronics, Peking University
- Alibaba Group
arxiv_id: '2607.28048'
url: https://arxiv.org/abs/2607.28048
pdf_url: https://arxiv.org/pdf/2607.28048
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: Agent 技能蒸馏与知识迁移
tags:
- Skill Distillation
- Teacher-Student
- LLM Agents
- Contrastive Learning
- Adaptive Validation
- Drift-Aware Consolidation
one_liner: 将教师-学生行为差异蒸馏为可验证文本技能补丁，结合漂移感知整合维护紧凑技能库
practical_value: '- **电商多Agent系统的技能迁移**：可以用强模型（如GPT-5.5）为弱模型（本地部署小模型）自动生成技能补丁，直接注入prompt，无需微调权重，适合快速适配不同业务场景的规则变化。

  - **技能库的长期维护与防漂移**：维护编辑历史并追溯每次修改的原始轨迹证据，避免因局部修复导致规则冗余、冲突或退化，对管理推荐策略中的业务规则（如促销匹配、文案生成规则）有直接参考价值。

  - **自适应验证确保技能可靠**：每个生成的技能补丁需在学生的实际执行中验证有效性，失败则迭代修订，直到行为改变。这种闭环验证思路可借鉴到生成式推荐中，用于自动评估和修正推荐话术或策略模板。

  - **同异架构模型间蒸馏不依赖内部表征**：蒸馏介质为自然语言技能文本，跨模型系列（如Qwen到ChatGPT）依然有效，适合在联盟/广告主侧不同模型间传递专家知识。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有LLM Agent技能获取方法大多将技能视为经验总结、记忆条目或成功轨迹的直接摘要。当弱学生Agent因缺乏任务知识或操作策略而失败时，其失败轨迹往往不能揭示缺失的行为，而教师轨迹又过于隐式难以化为可复用的指导。SKILL-KD提出将技能视为不同能力Agent之间的显式蒸馏媒介，通过对比同一任务上教师与学生的行为差异，提取可操作的知识。

**方法**  
- **对比技能蒸馏**：学生先执行任务，若失败则用同一任务运行教师，对比两者轨迹，由整合Agent（consolidation agent）蒸馏出技能补丁（标题、内容、理由、轨迹链接）。  
- **自适应技能蒸馏**：不是一次性总结，而是迭代搜索文本技能空间。候选补丁通过学生重新执行来验证，若仍失败则结合新轨迹修订补丁，直至成功或达到最大轮次。  
- **漂移感知技能整合**：维护可追溯的编辑历史，每个补丁关联源轨迹。整合Agent通过工具调用检索历史证据，决定对当前补丁执行新增、修改、删除或跳过，防止技能漂移、膨胀和破坏性覆盖。

**关键结果**  
在SearchQA、SpreadsheetBench、DocVQA、LiveMath、ALFWorld五个基准上，使用Qwen3.5-4B/Qwen3.7-plus和Qwen3.6-35B-A3B/ChatGPT-5.5两组师生设置，SKILL-KD将平均成功率从43.5%提升至66.8%（+23.4，组1）和从57.9%提升至74.6%（+16.7，组2），显著优于EvoSkill、Trace2Skill、SkillGen、SkillOpt等基线。消融显示：自适应验证和漂移感知整合对有效性至关重要，去除整合机制时部分基准显著退化；教师失败轨迹仍能贡献38.5%的有效补丁。最终技能库仅用38条规则即实现最佳性能，远少于仅用学生轨迹回顾的96条。
