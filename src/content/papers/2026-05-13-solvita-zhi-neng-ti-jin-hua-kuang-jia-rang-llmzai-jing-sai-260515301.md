---
title: 'Solvita: Enhancing Large Language Models for Competitive Programming via Agentic
  Evolution'
title_zh: Solvita：智能体进化框架让LLM在竞赛编程中持续积累经验
authors:
- Han Li
- Jinyu Tian
- Rili Feng
- Yuqiao Du
- Chong Zheng
- Chenyu Wang
- Chenchen Liu
- Shihao Li
- Xinping Lei
- Yifan Yao
affiliations:
- Nanjing University
- Tsinghua University
- Independent Researcher
arxiv_id: '2605.15301'
url: https://arxiv.org/abs/2605.15301
pdf_url: https://arxiv.org/pdf/2605.15301
published: '2026-05-13'
collected: '2026-05-18'
category: MultiAgent
direction: 多智能体协作与经验持续进化
tags:
- Agentic Evolution
- Knowledge Network
- REINFORCE
- Code Generation
- Competitive Programming
- Patch Repair
one_liner: 通过四个专用智能体与可训练图知识网络，用REINFORCE将执行结果转化为路由权重更新，实现无需微调的持续编程能力提升
practical_value: '- **可训练知识网络替代静态RAG**：每个Agent（Planner、Solver、Oracle、Hacker）配有图结构记忆，边权重由任务成功/失败信号通过REINFORCE动态调整，而非仅靠语义相似度检索。电商Agent可借鉴此模式，将用户交互反馈（如点击、转化）转化为知识检索的路由策略，实现经验驱动的动作选择。

  - **闭环多智能体反馈联动**：Oracle的测试认证、Hacker的对抗攻击结果不仅独立使用，还通过事件总线更新其他Agent的知识网络。在推荐/审核/风控的多智能体系统中，可设计类似的失败信号广播机制，让不同角色共享教训，避免重复错误。

  - **补丁式修复节省Token与提升稳定性**：Solver不重写整个程序，而是生成SEARCH/REPLACE补丁，仅修改出错部分，大幅降低计算开销（实验中Token节省达86%–91%）。业务流程自动化（如代码修复、规则调整）可优先采用增量修补而非全量重试，提高效率并保持核心逻辑不变。

  - **无模型微调的性能持续提升**：LLM权重完全冻结，仅更新外部知识网络，系统性能随使用时间单调增长。这对业务中模型更新成本高或数据隐私严格的场景（如私有化部署的推荐系统）很有价值，可用轻量级外部记忆实现持续迭代。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**

现有代码生成LLM多采用静态单次生成或多步流水线（如AlphaCodium、MapCoder），缺乏从历史解题中积累经验的能力。即使有检索增强，也仅是静态相似度匹配，无法根据执行结果调整推理策略。人类程序员能通过练习逐渐掌握题型与调试技巧，本文旨在让多智能体系统也具备这种持续进化的能力，且不更新模型权重。

**方法关键点**

1. **四角色闭环架构**：Planner将问题形式化为数学规范并选择策略；Solver用补丁式修复迭代生成/修正代码；Oracle构建带认证的内部测试集；Hacker发起对抗攻击寻找遗漏缺陷。错误信号通过事件总线广播，统一更新所有Agent的知识网络。
2. **可训练图知识网络**：每个Agent背后有一个异构图记忆（如Solver的Query-Method-Skill三层网络），边权重由REINFORCE根据任务结果（pass/fail、认证质量、漏洞发现）动态更新，实现从经验中学习路由策略，而非静态检索。
3. **补丁修复替代全量重生成**：Solver在迭代时仅输出SEARCH/REPLACE块修正错误，并要求回归测试通过，既保持正确部分不变，又大幅节省Token。
4. **对抗反馈作为训练信号**：Hacker的攻击结果（如复杂度极限、哈希碰撞）被量化为奖励，用于更新自身和其他Agent的知识网络，促使系统主动暴露并吸收边界案例。

**关键实验结果**

在CodeContests上，GPT-5.4 backbone的pass@1从单次生成的40.0%提升至82.4%，接近翻倍；APPS和AetherCode上均有显著提升，建立代码生成智能体的新SOTA。在Codeforces真实比赛中，Solvita的三个backbone均稳定收敛到Legendary Grandmaster级别（≥3000分），而裸模型仅在高Grandmaster波段。消融表明，多智能体闭环在不带知识网络时已拉近与全系统的差距，但三个知识网络均贡献持续提升，其中Solver网络增益最大；补丁修复相比全量重生成，在CodeContests上将Solve率从75.76%提高到82.42%，且平均迭代次数更少。Oracle与Hacker联合诊断可检测92.8%的错误解答，并发现17.9%的更强测试用例。
