---
title: Self-Supervised Scaling of Terminal Environments for Scientific Domains
title_zh: 面向科学领域的终端环境自监督扩展
authors:
- Zhongzhi Li
- Yucheng Shi
- Zongxia Li
- Junyao Yang
- Ruhan Wang
- Yu Wang
- Jingyuan Huang
- Jichao Yu
- Ninghao Liu
- Haitao Mi
affiliations:
- Tencent HY LLM Frontier
- University of Georgia
- University of Maryland, College Park
- National University of Singapore
- Hong Kong Polytechnic University
arxiv_id: '2610.02710'
url: https://arxiv.org/abs/2610.02710
pdf_url: https://arxiv.org/pdf/2610.02710
published: '2026-10-01'
collected: '2026-10-06'
category: Agent
direction: 终端Agent环境自动化与SFT缩放
tags:
- Agent
- Self-Supervised
- Terminal
- SFT
- Verifier
- Scientific Software
one_liner: 用现有科学软件工作流自动生成可验证的终端Agent训练样本，SFT后显著提升Terminal-Bench 2
practical_value: '- 可用现有业务软件/API工作流自动生成(SFT)训练样本：给定输入schema和公开输入输出对，让LLM重构可编辑程序，再用隐藏配置验证，避免逐任务人工标注reference
  solution，适合电商/广告中的工具调用、查询生成等Agent任务。

  - 层次化verifier思路可迁移：把语义比较、结构有效性、反捷径检查组合起来，防止模型学出表面匹配但语义错误的生成结果，对QueryRec和生成式推荐中的评估尤其重要。

  - 已验证的高质量轨迹比单纯语料规模更有效：对verified trajectories做oversampling后SFT，在matched-token对照中全面领先，说明业务数据应优先筛选行为可验证样本，而不是直接堆量。

  - 公共反馈支持迭代修订的机制可以改造成在线训练：先让Agent在公开样例上尝试，失败后根据反馈修改，最后在隐藏集上验证，类似强化学习中的self-play数据生产。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：终端Agent正从软件工程扩展到科学等专业领域，但为每个任务构建训练环境需要可执行参考行为和领域特定verifier，人工标注成本高、难以跨任务复用。

**方法关键点**：提出software-in-the-loop reconstruction自监督框架，从已有软件工作流（可执行程序，映射结构化输入到输出）获取参考输出和验证目标。具体做法：对每个工作流执行多组输入配置，将样例分成公开观察和隐藏评估；给Agent指令、输入schema和公开输入输出对，让其在看不到源工作流的情况下构造可编辑程序；在隐藏配置上对比工作流输出评估候选程序。层次化verifier结合领域特定语义比较、结构有效性和反捷径检查，并用公开样例反馈支持迭代修订。该框架可扩展新工作流和配置，无需为每个任务单独标注参考解。

**关键结果**：构建SWR，包含500个workflows、46个软件家族、覆盖6个科学领域。Qwen3.8-Max在每任务3次尝试中解出838个任务，产生1422条验证轨迹，过采样至3000条重构训练样本。用这些样本对Qwen3.8-27B做SFT，Terminal-Bench 2平均性能从47.94%提升到53.56%（三个种子），并在四个matched-token语料对照中取得最高均值。
