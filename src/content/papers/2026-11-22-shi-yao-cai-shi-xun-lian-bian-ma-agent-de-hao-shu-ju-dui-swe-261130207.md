---
title: What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym
title_zh: 什么才是训练编码 Agent 的好数据：对 SWE-Gym 的系统审计
authors:
- Yikai Zhang
- Mai Xu
- Yunbei Zhang
- Qirui Jin
- Kenan Li
- Yuwen Jia
- Jinwei Yao
- Xiangyu Zhang
- Jielun Tan
- Jin Pan
affiliations:
- AMD
- University of Michigan
- Tulane University
- Georgia Institute of Technology
- University College London
arxiv_id: '2611.30207'
url: https://arxiv.org/abs/2611.30207
pdf_url: https://arxiv.org/pdf/2611.30207
published: '2026-11-22'
collected: '2026-11-24'
category: Training
direction: RL 训练数据质量审计
tags:
- RL
- Coding Agent
- Data Quality
- Reward Label
- SWE-bench
- False Negative
one_liner: 系统审计 SWE-Gym 奖励标签，发现未解决任务多为假阴性，修复后训练策略在 SWE-bench 提升 2.4/2.7 点
practical_value: '- 训练前先审计 reward label：推荐/Agent 的 RL 奖励信号（点击、转化、任务成功）常含假阴性和假阳性。可仿照本文用多个模型交叉验证，并保留执行证据，再进入训练。

  - 不要粗暴丢弃“从未成功”的样本：实验显示仅移除 never-solved 任务无提升，而修复标签后提升明显。对应推荐中长期无正反馈的 item/query，可能是曝光不足或标签错误，应诊断而非直接降权。

  - 构建可回放的审计 pipeline：将每个 reward 判定与其证据（执行日志、离线指标）绑定，支持复现与数据版本管理，便于发现隐在 pass rate
  背后的标签噪声。

  - 注意“正确率”与“奖励正确性”脱钩：pass rate 只说明有 reward，不代表 reward 对。可引入额外测试或 gold 行为抽检，尤其对 Agent
  任务先验证测试集能否识别错误。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RL 训练 coding agent 时依赖隐藏测试决定 reward，但多数任务集合只用 reference fix 验证测试，可能导致 reward label 错误。SWE-Gym 被广泛用于训练，但缺少对标签正确性的系统审计。

**方法关键点**：用两个 LLM 家族对 SWE-Gym 做审计，只有执行能复现的错误才计数；将任务按 9B base model 是否从未解决分组，检查假阴性（测试拒绝正确 fix）和假阳性（错误 patch 通过测试）。修复或移除问题任务，并在相同规模和难度匹配下对比训练效果。

**关键结果**：74% 的 never-solved 任务存在假阴性测试，而有时解决的任务仅 20%；经审计的数据训练后，在 SWE-bench Verified 和 Pro 上分别提升 2.4 和 2.7 点，而简单丢弃 never-solved 任务无此收益。错误通过的 patch 约占总通过 patch 的 25%；新增测试能捕捉其中 1/4，但 held-out 分数未见可检测变化。发布 SWE-Gym-Verified，包含 1,087 个审计任务、执行证据和完整审计 pipeline。
