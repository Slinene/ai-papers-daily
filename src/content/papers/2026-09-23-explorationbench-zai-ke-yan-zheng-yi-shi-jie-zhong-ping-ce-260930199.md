---
title: 'ExplorationBench: Measuring AI Systems'' Exploration in Verifiable Alien Worlds'
title_zh: ExplorationBench：在可验证异世界中评测 AI 系统的探索能力
authors:
- Ming Zhang
- Zhenghao Xiang
- Peizhong Gao
- Yujiong Shen
- Yuhui Wang
- Zhonghan Yue
- Shihan Dou
- Zhangyue Yin
- Junjie Ye
- Shichun Liu
affiliations:
- Fudan University
- Tencent
- Tsinghua University
arxiv_id: '2609.30199'
url: https://arxiv.org/abs/2609.30199
pdf_url: https://arxiv.org/pdf/2609.30199
published: '2026-09-23'
collected: '2026-09-25'
category: Eval
direction: LLM Agent 探索能力基准测评
tags:
- Exploration
- Benchmark
- LLM Agent
- Tool Use
- Scientific Discovery
one_liner: 构建规则可执行且与预训练知识冲突的异世界沙盒，量化 AI 系统通过探索获取并应用全新规则的能力
practical_value: '- **构建规则可替换的沙盒环境来评测 Agent 的探索与适应能力**：在电商搜索推荐场景中，可以设计一个规则与线上统计常识冲突的模拟环境（例如排序收益反转、用户行为分布突变），让
  LLM Agent 通过有限次交互探索新规则，而不是直接复用历史知识或预训练记忆。

  - **提供有缺陷的手册 / 文档作为初始信息**：实际业务中的文档、API 说明、运营规则经常过时或部分错误，可借鉴论文做法，用带噪声的初始手册训练或评测 Agent
  的纠错与假设验证能力，从而提升对突发规则变更的鲁棒性。

  - **关注探索轨迹的非单调性**：论文发现持续探索会 stall 或 reverse 先前收益，提示我们在 Agent 流程中需要加入 checkpoint
  或最优轨迹回滚机制，避免在长链路任务中因过度探索而丢失已学到的高价值策略。

  - **用可执行规则替代人工标注来做自动化评测**：将搜索/推荐策略验证转化为可编程的 sandbox，每个动作都可精确判断对错，能低成本生成大规模评测集，适合对
  LLM Agent 做回归测试和版本对比。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学发现从已知问题的边界开始，AI 系统需要具备探索能力——提出假设、设计实验并根据结果迭代。但评估探索能力存在两个核心难点：如何验证一个真正的新假设是否成立，以及如何判断系统是通过探索发现规律还是仅仅复现了预训练数据中已有的相关知识。

**方法关键点**：ExplorationBench 将评估问题转化为基于“Alien Worlds”的可验证沙盒：沙盒规则可执行，因此每个答案都能被精确验证；同时规则与人类熟悉的知识冲突，仅靠召回预训练内容无法完成任务。基准包含两个沙盒：AlienCode（31 个发现目标，70 个任务）和 AlienLogic（24 个发现目标，70 个任务）。每个沙盒提供一份有缺陷的手册、任务相关的环境反馈、以及专用工具调用 schema。系统利用这些资源在沙盒中自主探索，然后用 held-out 任务测试其泛化能力。

**关键结果**：对 10 个 AI 系统进行评测，结果显示最强系统能够获取并应用陌生规则，但不同探索轨迹间性能波动很大；此外，持续探索可能出现停滞甚至逆转先前收益。性能曲线按里程碑 M0–M4 展示，每个里程碑取 Best@3 轨迹、每个 held-out 问题的三次回答均值。AlienCode 与 AlienLogic 的系统排序存在差异，反映出探索能力在不同规则空间下的不一致性。
