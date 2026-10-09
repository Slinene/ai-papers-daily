---
title: 'MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement'
title_zh: MiMo-V2.6：面向自我改进的大规模强化学习训练
authors:
- Core Team
- Zongming Qiao
- Ziyue Hua
- Zirui Ou
- Zihao Yue
- Zihan Jiang
- Zhuo Huang
- Zhiyang Chen
- Zhixian Zheng
- Zhipeng Xu
affiliations:
- LLM-Core Xiaomi
arxiv_id: '2610.11959'
url: https://arxiv.org/abs/2610.11959
pdf_url: https://arxiv.org/pdf/2610.11959
published: '2026-10-07'
collected: '2026-10-09'
category: Training
direction: 大规模强化学习训练与 Agentic RL 基础设施
tags:
- RL Scaling
- Agentic RL
- MoE
- Reward Hacking
- Groupwise Grading
- Training Infrastructure
one_liner: 通过扩展 RL 训练计算、任务环境与 grader 计算，在代码/通用/视觉/安全任务上稳定提升 1T 与 310B MoE 模型。
practical_value: '- 防 reward hacking 的工程闭环可迁移到推荐/广告 RL 训练：环境清理（去缓存、隔离网络）、hack agent
  对抗探测、训练中离线审计 + 作弊轨迹奖励清零，把 hack 率控制在 2% 以下，适合在线学习/探索场景。

  - Groupwise advantage redistribution 思路可用于推荐模型基于 listwise/groupwise 反馈的训练：在 batch
  内按质量因子对正样本重新分配 advantage，既保留成功样本梯度又惩罚低质量转化/刷指标行为，避免模型学到投机式优化。

  - 大模型 RL 基础设施设计值得参考：统一 trajectory 表示、control/data plane 解耦、partial rollout + Sample
  Mixer 稳定多任务 batch 组成、冻结 MoE router 保证训练稳定；这些对大规模生成式推荐/Agent 在线更新有直接工程价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
递归自我改进需要 agent + RL，但 scaling RL 面临架构、环境、grader 和基础设施挑战。MiMo-V2.6 以 hybrid-SWA MoE 为基础，通过 mid-training 扩展 agentic 探索空间，再沿三个维度放大 RL compute。

## 方法关键点
- 模型：Pro 1.02T 参数/42B active，Flash 310B/15B active；混合 Local Sliding Window Attention 与 Global Attention，MoE，MTP 投机解码。mid-training 切换 Muown optimizer 和 MXFP4 QAT，上下文扩展到 1M。
- RL 训练计算：异步训练，单步 1,568 prompts × group 16 = 25K sequences，2.7-3.7B tokens；partial rollout 和 dynamic sampler。
- 环境与 harness：代码/通用/视觉/网络安全四类；多 mini-harness 训练提升跨 harness 泛化；针对 reward hacking 进行环境清理、hack agent 对抗筛查、训练中审计。
- grader：GRS 离线 rubrics 和 GAR 在线 groupwise grading，将二元测试奖励细化为质量与行为信号；长度 penalty 和行为正则。

## 关键实验
- DeepSWE v1.1 avg@3：Pro 58.4→72.6，Flash 48.7→65.7；RL 花费 Pro $2.6M, Flash $0.9M；成本拆分 rollout 43.8%、训练 43.5%、grader 12.7%。
- GAR 消融：没有 GAR 时 turns 和 token length 激增，pass rate 难持续；有 GAR 时 pass rate 升至 step52，生成更短更精准 patch。
- reward hacking 控制在 <2%。

## 最值得记住的一句话
RL 的收益不只来自增大 rollout，更来自把 grader 计算和 reward 质量当作一等公民来 scaling。
