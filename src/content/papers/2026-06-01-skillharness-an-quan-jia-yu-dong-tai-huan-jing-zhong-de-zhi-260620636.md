---
title: 'SkillHarness: Harnessing Safe Skills for Computer-Use Agents'
title_zh: SkillHarness：安全驾驭动态环境中的智能体技能
authors:
- Yurun Chen
- Biao Yi
- Keting Yin
- Shengyu Zhang
affiliations:
- Zhejiang University
arxiv_id: '2606.20636'
url: https://arxiv.org/abs/2606.20636
pdf_url: https://arxiv.org/pdf/2606.20636
published: '2026-06-01'
collected: '2026-06-24'
category: Agent
direction: Agent 安全技能学习 · 动态环境
tags:
- Computer-Use Agents
- Skill Learning
- Safety Constraints
- Dynamic Environments
- Skill Boundary
- Selective Reuse
one_liner: 通过技能边界与选择性重用机制，在动态交互中安全学习技能，不安全率降低57.1%
practical_value: '- 借鉴 skill boundary，为推荐 / 广告 Agent 的动作空间设置多源监督信号（如业务指标、用户反馈），自动识别并过滤高风险策略。

  - 在动态推荐场景中引入 selective skill reuse，根据实时上下文（如用户状态、时段）分解任务，仅激活安全的策略子集，避免冷启动或探索期的危险操作。

  - 自完善安全约束机制：从历史交互轨迹中持续学习安全边界，在线更新约束，预防模型漂移或对抗攻击（如 prompt 注入）导致的推荐灾难。

  - 工业部署时，可在 Agent 决策后增加类似 skill boundary 的安全校验层，对推荐结果进行二次审核，降低线上事故率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
计算机使用智能体（CUA）在动态交互环境中需要持续学习新技能，但现有方法假设环境静态安全，忽略了 prompt 注入、弹窗等风险，导致学到的技能不安全且执行脆弱。如何安全地学习和利用技能成为关键问题。  

**方法**  
提出 SkillHarness，将技能学习与利用建模为安全约束的交互过程。核心包括：  
- **技能边界（skill boundary）**：利用多源监督信号从交互轨迹中识别安全技能，构建自进化的安全约束，贯穿技能的创建、存储与复用全生命周期。  
- **选择性技能重用（selective skill reuse）**：根据当前上下文将任务分解，仅激活安全的技能子集来协作完成任务，避免全局技能库的盲目调用。  

**结果**  
在动态环境测试中，SkillHarness 将所学技能的不安全率**降低 57.1%**，执行稳定性显著优于基线，且能持续适应环境变化。
