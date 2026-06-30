---
title: 'MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM
  Post-Training'
title_zh: 多教师同策略蒸馏：LLM后训练中的能力整合
authors:
- Wenhan Ma
- Jianyu Wei
- Liang Zhao
- Hailin Zhang
- Bangjun Xiao
- Lei Li
- Qibin Yang
- Bofei Gao
- Yudong Wang
- Rang Li
affiliations:
- Peking University
- LLM Core, Xiaomi
- University of Hong Kong
- Renmin University of China
arxiv_id: '2606.30406'
url: https://arxiv.org/abs/2606.30406
pdf_url: https://arxiv.org/pdf/2606.30406
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: 多教师同策略蒸馏·RL能力整合
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Reinforcement Learning
- LLM Post-Training
- Capability Integration
one_liner: 提出多教师同策略蒸馏（MOPD），将领域RL教师模型在学生自身rollout上蒸馏，避免曝光偏差并集成多种能力
practical_value: '- **统一多技能代理的训练方案**：电商搜索/推荐场景中，常需一个模型同时具备搜索意图解析、商品描述生成、议价对话等能力。可借鉴MOPD，先为每个技能单独用RL训练教师，再通过同策略蒸馏融合成一个学生模型，避免多任务联合RL的耦合与冲突。

  - **稳定的稠密监督信号**：在将教师知识整合给学生时，使用学生自身rollout与教师分布做token级KL散度损失，替代稀疏奖励，训练更平稳，适合推荐系统这类输出空间大、奖励稀疏的任务。

  - **解除领域间迭代耦合**：MOPD支持各领域教师并行独立优化，大幅提升多个业务线同时快速迭代的效率；电商公司可让不同团队独立优化“搜索式推荐”、“售后话术”等教师，定期蒸馏更新统一的前向模型。

  - **缓解灾难性遗忘**：同策略蒸馏直接从教师分布学习，而非仅靠稀疏RL奖励，可更完整地继承每个教师的能力，在扩展到新推荐场景或增加新任务时保护已学技能。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现代LLM通过RL在特定领域取得能力提升，但将多个领域的RL技能整合到单一模型仍困难。现有Mix-RL等方法在训练效率和最终性能上都存在不足，亟需一种解耦且高效的多能力融合范式。

**方法**：提出多教师同策略蒸馏（MOPD），分两步：1）对每个目标领域独立运行专业的RL流水线，得到领域教师模型；2）让学生模型在自己的rollout轨迹上，通过最小化与教师分布间的token级KL散度来蒸馏所有教师。这种“同策略”蒸馏消除了训练与推理时的分布偏移（曝光偏差），并提供了稠密的优化信号，比单纯依赖RL奖励更稳定高效。

**关键结果**：基于Qwen3-30B-A3B的实验表明，MOPD全面超越Mix-RL、Cascade RL、Off-Policy Finetune和参数合并等基线，几乎无损地继承每个教师的能力。MOPD还实现了领域教师的并行独立开发，消除了传统多领域post-training中的跨域耦合。该方法已成功部署于工业级模型MiMo-V2-Flash的后训练中，验证了其在大规模系统中的实用价值。
