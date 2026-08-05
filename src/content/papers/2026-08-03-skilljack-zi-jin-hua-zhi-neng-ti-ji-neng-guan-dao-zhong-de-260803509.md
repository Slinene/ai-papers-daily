---
title: 'SkillJack: Persistent Skill Backdoors in Self-Evolving Agents'
title_zh: SkillJack：自进化智能体技能管道中的持久后门攻击
authors:
- Zonghao Ying
- Xiangfan Wu
- Huiyu Wu
- Xing Zheng
- Huangsheng Cheng
- Xiaorong Shi
- Jing Guo
affiliations:
- Tencent Zhuque Lab
arxiv_id: '2608.03509'
url: https://arxiv.org/abs/2608.03509
pdf_url: https://arxiv.org/pdf/2608.03509
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: 自进化 Agent 技能学习的安全风险
tags:
- Self-Evolving Agents
- Skill Extraction
- Poisoning Attack
- Persistence
- LLM Security
- Agent Backdoor
one_liner: 首次揭示自进化智能体的经验到技能转换如何将中毒经验固化为持久、可路由的后门技能
practical_value: '- 自进化推荐Agent若用交互历史生成检索或推荐技能，须警惕中毒经验被固化；应建立技能溯源，标记数据血缘，源清除时级联撤销衍生技能，避免持久后门。

  - 技能提取会“洗白”恶意意图（如“备份服务”掩盖数据外传），安全检测不能仅审查原始轨迹，需对每个衍生技能重新评估，尤其关注元数据（名称、描述）是否误导检测器。

  - 工程实现中，技能库与经验存储通常解耦，仅清空原始记录不足以根除攻击，需配套技能生命周期管理，实现源删则后代技能同步失效。

  - 对使用LLM路由的技能推荐系统，可借鉴其载荷构造思路，设计元数据感知的鲁棒性审查，避免仅靠表面文本判毒；并注意多防线组合可能因技能路由变化而失效，需联合优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：自进化LLM智能体通过将交互历史转化为可复用技能实现持续提升，但这一经验到技能管道（experience-to-skill pipeline）引入了新的攻击面：中毒经验不仅可被检索利用，更可被智能体自身编译为独立的持久技能，绕过记忆层面检测，形成后门。现有工作多关注记忆或检索中毒，而忽略了技能固化带来的生命周期风险。

**方法**：提出 SkillJack 攻击，核心是“转换韧性载荷”（transformation-resilient payloads）。将恶意动作包装在看似合法的任务框架中（如数据外泄伪装为“备份”，权限提升伪装为“统一管理”），使提取出的技能保持危险行为的同时，在名称、描述等表面特征上呈良性。攻击不直接操纵技能库，仅向经验库注入中毒轨迹，利用智能体自身的提取、持久化和路由机制完成攻击传播。评估在两个代表性系统 SkillX（基于计划提炼）和 Anything2Skill（文档编译）上进行，共享150条轨迹（65帧化中毒、65直接恶意、20干净），覆盖数据外泄、权限提升、未授权转账、持久后门四类风险，并采用规则匹配与LLM判毒作为代理检测器。

**关键结果**：提取显著降低可检测性——LLM判毒率从原始轨迹的98.5%降至提取后技能的11.4%（洗白效应），在 Anything2Skill 中亦有类似表现；在 SkillX 上攻击成功率达56.2%，Anything2Skill 达89.2%；删除源轨迹后，80%的后门仍持续触发，显示持久隔离特性；20%的干净任务也会意外触发恶意技能，表明未预期旁路影响。元数据消融实验证实判毒高度依赖技能名称与描述，行为代码本身反而不易暴露。初步防御实验显示，行为级运行监控优于静态审查，但简单叠加防线可能因技能路由动态变化而失效。

**核心洞察**：经验到技能的转换是安全中性的新攻击面，传统源清理策略已不足以应对，必须引入溯源感知的技能生命周期保护。
