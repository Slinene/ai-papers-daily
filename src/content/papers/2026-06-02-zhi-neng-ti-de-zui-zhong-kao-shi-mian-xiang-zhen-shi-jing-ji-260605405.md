---
title: Agents' Last Exam
title_zh: 智能体的最终考试：面向真实经济工作流的通用Agent评测基准
authors:
- Yiyou Sun
- Xinyang Han
- Weichen Zhang
- Yuanbo Pang
- Tianyu Wang
- Yuhan Cao
- Yixiao Huang
- Chris Duroiu
- Haoyun Zhang
- Jeffrey Lin
affiliations:
- University of California, Berkeley
arxiv_id: '2606.05405'
url: https://arxiv.org/abs/2606.05405
pdf_url: https://arxiv.org/pdf/2606.05405
published: '2026-06-02'
collected: '2026-06-10'
category: Eval
direction: Agent通用计算机使用能力评测基准
tags:
- Benchmark
- Agent
- Computer Use
- Long-horizon
- Real-world tasks
- Generalist CUA
one_liner: 覆盖55个职业子领域、1490个专家提交任务，评测Agent在长时程多模态计算机操作上的表现，最强模型整体通过率仅2.6%。
practical_value: '- 任务设计范式：将专业工作流拆解为可验证的交付物和里程碑（gate-and-score），可直接用于构建电商客服、商品上架等Agent评测，避免LLM-as-judge的不可靠性。

  - 工具使用剖析：发现Agent普遍用CLI代替GUI，导致在图形软件密集型任务上失败，提示在电商自动化（如美工、合规审查）中需显式强化GUI操作能力。

  - 模型vs框架选择：模型对性能影响是框架的3倍，且资源消耗（时间、金钱）与成功率非正比，可指导选型——先用轻量框架+最强模型，再针对性优化工具集。

  - 数据防污染：公共/私有任务池定期轮换，可借鉴到生产环境的Agent能力监控，防止过拟合或数据泄漏。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
当前AI在基准测试上屡创佳绩，但经济领域的自动化渗透有限，根源在于缺少能衡量Agent在真实、长时程、经济价值高的工作流上表现的评测。ALE（Agents' Last Exam）以此为目标，联手250+行业专家，构建了覆盖55个职业子领域、1490个任务实例的基准，旨在成为“最终考试”——一旦饱和，即意味Agent具备承担实际专业工作的能力。

**方法关键点**  
- 任务来源：所有任务均来自专家已完成的实际项目，经多轮质量审查（提交→初审→工程实现→终审），确保代表性、复杂性和可验证性。任务环境基于虚拟机，提供输入/软件/参考/输出四区隔离。
- 评测目标：通用计算机使用Agent（GCUA），要求兼具视觉感知（Eyes）、shell、代码、文件操作和长程规划能力。主流Harness通过GUI-as-Tool扩展统一CLI与GUI交互。
- 评分体系：采用确定性检查为主（哈希、数值容差、几何距离、结构性核对），少数需视觉判断的任务用证据锚定的LLM探针，整体按gate-and-score组合，避免开放LLM评分。
- 防污染：仅10%任务公开，其余私有，定期轮换，保证基准可持续性。

**关键实验结果**  
- 在14种主流Harness与模型组合（包括GPT-5.5、Claude Opus 4.7、Codex等）上，整体平均full pass rate仅2.6%，最难Last-Exam级任务多数配置0%通过，最强配置Codex+GPT-5.5也仅26.2%。
- 领域分化明显：计算数学、农业环境类得分约60%，视觉媒体、教育类低于30%，失败主因是领域知识匮乏，Agent倾向于用CLI脚本绕过专业软件。
- 在Linux子集ALE-CLI上，Codex+GPT-5.5仅25.2%通过，远低于其在Terminal-Bench上的82%，说明任务难度远高于现有终端基准。
- 模型选择对性能的影响约是Harness选择的3倍，且高消耗（时间、金钱）并不带来更高得分。

**一句话总结**  
即使最强前沿Agent，在ALE上的通过率也仅刚刚超过四分之一，这为通用Agent真正进入生产力领域划出了一条明确的能力鸿沟。
