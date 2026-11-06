---
title: 'Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training'
title_zh: Harness-S：从兄弟脚手架学习训练可泛化智能体
authors:
- Kangning Zhang
- Wenxiang Jiao
- Bowen Fang
- Shuai Shao
- Jiachen Zhu
- Rong Shan
- Shijian Wang
- Hao Wang
- Yuan Lu
- Weiwen Liu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- Zhongguancun Institute of Artificial Intelligence
- Southeast University
- Carnegie Mellon University
arxiv_id: '2611.04277'
url: https://arxiv.org/abs/2611.04277
pdf_url: https://arxiv.org/pdf/2611.04277
published: '2026-11-02'
collected: '2026-11-06'
category: Agent
direction: Agent 训练 · 脚手架进化与路由
tags:
- Agent Training
- Harness Evolution
- Reinforcement Learning
- LLM
- Sibling Harness Pool
- Harness Routing
one_liner: 提出 Harness-S 框架，通过方向性脚手架进化与互补救援训练，利用兄弟脚手架修复失败并迁移能力到单一策略
practical_value: '- 将智能体的执行环境（prompt、工具接口、规则）视为可进化组件：针对不同失败模式构建多个专门化“兄弟 harness”，类似多环境训练，能提升策略在原始环境下的泛化能力，适用于电商导购助手、客服
  Agent、广告优化 Agent 等场景。

  - 只在基础环境全部尝试失败时才启动救援训练，避免对原始行为过度干预，同时用辅助环境生成的互补轨迹替换失败组进行强化学习，可提高样本效率与训练稳定性。

  - 借鉴 Adaptive Harness Router 的思路：用 LLM 投票与策略感知的行为画像动态选择辅助环境或 prompt 配置，可迁移到线上模型路由、AB
  测试配置选择等工程实现，提升鲁棒性。

  - 维护固定的 Sibling Harness Pool 且在策略训练期间不更新，降低非平稳性带来的训练波动；电商场景下可按商品类目、用户意图构建不同的交互脚本作为“兄弟
  harness”。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：智能体行为由模型策略与 harness（提示、工具接口、上下文与执行规则）共同决定，harness 变体存在局部性、互补性与非平稳性：不同变体修复不同失败，其效用随策略学习而变化，不存在普遍最优的 harness。

**方法关键点**：Harness-S 由三部分构成。Directional Harness Evolution 沿不同修复方向开发专门化兄弟 harness，形成可复用的 Sibling Harness Pool，策略训练期间该池固定不变。Complementary Harness Rescue Training 仅在基础 harness 下所有初始尝试失败时调用池中的辅助 harness，由同一策略在选定的辅助 harness 下生成新 rollout，替换失败轨迹组用于强化学习。Adaptive Harness Router 基于 Harness Behavior Profiles 与多 LLM 投票选择 Top-k 变体，并通过 policy-aware profile re-anchoring 随策略学习刷新证据。

**关键结果**：在 AppWorld、SWE-Gym、DBBench 三个基准上，训练后的策略返回原始基础 harness 时显著优于仅策略训练；行为分析与留出案例表明 harness 诱导的能力迁移到了策略本身；将路由器复用于 Rank-1 推理，在相同 executor rollout 数下获得额外增益。
