---
title: 'Repo-To-Skill: Distilling GitHub Repositories Into AI4AI Skills'
title_zh: Repo-To-Skill：从 GitHub 仓库蒸馏 AI4AI 技能
authors:
- Jianlyu Chen
- Yuyang Hu
- Hongjin Qian
- Jiawei Liu
- Wenqing Wei
- Xiaolong Chen
- Defu Lian
- Zhicheng Dou
- Chaozhuo Li
- Qiwei Ye
affiliations:
- Beijing Academy of Artificial Intelligence
- University of Science and Technology of China
- Renmin University of China
- Hong Kong Polytechnic University
arxiv_id: '2609.02749'
url: https://arxiv.org/abs/2609.02749
pdf_url: https://arxiv.org/pdf/2609.02749
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: Agent 技能蒸馏与知识复用
tags:
- AI Agent
- Skill Distillation
- Repository Mining
- Knowledge Distillation
- LLM
- Research Agent
one_liner: 提出 DisCo 与 AREX-Skill 库，将 GitHub 仓库蒸馏为可复用技能，显著提升研究 Agent 表现
practical_value: '- 把推荐/搜索团队常用 ML 仓库、内部训练/推理框架、特征工程、评估脚本等拆成 compact, verified skill
  卡（方法族/代码用法/验证检查），挂到 rec-agent 的库中，避免每次任务重读长 repo 或浪费 trial。

  - 借鉴 task-agnostic + task-oriented 双轨蒸馏：先离线从 1k 个仓库沉淀通用技能，再按具体推荐/搜索任务（如“多目标精排调参”）定向蒸馏小技能；可显著降低
  agent 上下文长度和对长 repo 的依赖。

  - 技能组织成 capability families（类似 taxonomy）后，可用检索式挂载，只把 relevant skills 注入 prompt，而不是把整个
  repo 塞进 KV cache；这个模式对商品推荐、Query 改写、广告文案生成的 LLM/Agent 工具调用同样适用。

  - 验证/评估：每个 skill 需通过可执行测试才入库，保证“知道方法”与“能跑通”结合；在业务 agent 平台里建议引入同样的 skill 验证环节，减少错误工具调用和不可复现实验。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：Agent 做 ML 研究时缺乏领域 operational knowledge（如何把方法跑通、选对代码、检查验证），这些知识藏在 GitHub 仓库和论文里，但体量过大、面向人类，无法直接加载。

方法关键点：提出 DisCo，通过两种互补蒸馏产出可复用 skills：task-agnostic 从常用仓库压缩通用技能，task-oriented 针对具体任务生成技能；大规模应用得到 AREX-Skill Library，含 5,000+ 个经过验证的技能，来自 1,000 个常用 ML 仓库，按 20 个领域、178 个能力族组织。

关键结果数字：固定 GPT-5.5 backbone、research harness 与执行预算下，装配技能的 agent 在 MLE-bench 提高 134.3%，PaperBench 提高 34.4%，FrontierCS 提高 9.2%，PassNet 提高 14.0%。
