---
title: 'Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based
  LLM Agents'
title_zh: 收敛式绕路劫持：技能型 LLM Agent 中保持任务完成的资源放大攻击
authors:
- Junliang Liu
- Ruoyu Li
- Wenxin Tang
- Jingyu Xiao
- Zhenyu Liu
- Jingheng Xu
- Laizhong Cui
affiliations:
- Shenzhen University
- The Chinese University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2608.12273'
url: https://arxiv.org/abs/2608.12273
pdf_url: https://arxiv.org/pdf/2608.12273
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: LLM Agent 技能选择与规划安全
tags:
- LLM Agent
- Skill Selection
- Prompt Injection
- Resource Amplification
- Adversarial Attack
- Cost Safety
one_liner: 提出 CDH 攻击，利用技能描述选择与指令体规划两阶段耦合，在任务完成率不变下放大 token 与执行时间消耗
practical_value: '- 在 Agent 技能平台中，不要只依赖自然语言描述做相关性选择：可增加成本/资源元数据（如预估 token、最大耗时）并在选择阶段就进行成本约束，避免“描述相似但执行昂贵”的技能被选中。

  - 监控 Agent 轨迹的 token 消耗和时间异常，尤其是任务完成但资源消耗显著高于基线的 run；可设置基于任务类型的分位数告警，检测 CDH 这类“完成但绕路”的放大攻击。

  - 对第三方技能做隔离和资源限制：即使技能指令本身无恶意，也可能通过伪造依赖关系招募多余良性工具；可在规划后对工具链做依赖校验，剔除与目标无关的中间步骤。

  - 借鉴攻击思路做成本压力测试：在评估自研 Agent 或推荐 Agent 时，故意注入“看似相关但增加绕路”的技能，检验系统是否有足够的成本鲁棒性和轨迹完整性保护。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**  
LLM Agent 越来越多地通过第三方技能扩展能力，采用渐进式披露设计：先暴露技能描述用于选择，选中后才加载完整指令体用于规划。这给不可信发布者留下两个连续控制点，现有研究分别关注选择操纵、恶意指令和工具链资源放大，但未端到端组合。  

**方法关键点**  
论文提出 CDH（Convergent Detour Hijacking）攻击：攻击者发布一个协调器技能，其描述用共享语义 cover 建立相关性，指令体复用同一 rationale 伪造可信依赖。攻击过程吸引协调器与合法技能一起被选中，招募不必要的良性技能形成有界绕路，最后重新进入原始路径以保持任务完成。整个过程是纯文本、运行时无关，不影响最终结果。  

**关键结果数字**  
在 DeepSeek-V4-Pro 上，491 个 held-out 任务中匹配协调器被选中的比例达 80.02%；在协调器命中且完成任务的 run 中，token 消耗增加 66.91%，端到端执行时间增加 92.45%，而聚合任务完成率与基线相当。说明正确结果不能保证轨迹完整性和成本安全。
