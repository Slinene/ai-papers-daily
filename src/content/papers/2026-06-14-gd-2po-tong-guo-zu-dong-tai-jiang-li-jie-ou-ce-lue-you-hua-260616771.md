---
title: 'GD^2PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled
  Policy Optimization'
title_zh: 'GD^2PO: 通过组动态奖励解耦策略优化缓解多奖励冲突'
authors:
- Haotian Liu
- Yihao Liu
- Jingwei Ni
- Siyuan Huang
- Xinpeng Liu
- Pengyu Cheng
- Jiajun Song
- Ruijin Ding
- Junfeng Li
- Zhechao Yu
affiliations:
- Alibaba
- Renmin University of China
- Peking University
- ETH Zürich
- The Chinese University of Hong Kong
arxiv_id: '2606.16771'
url: https://arxiv.org/abs/2606.16771
pdf_url: https://arxiv.org/pdf/2606.16771
published: '2026-06-14'
collected: '2026-06-17'
category: RecSys
direction: LLM多奖励RL训练的冲突过滤
tags:
- Multi-Reward RL
- Conflict Filtering
- SNR
- GRPO
- Tool Calling
- Helpfulness-Safety
one_liner: 提出冲突感知过滤与查询级重加权机制，防止多奖励RL训练中梯度抵消，显著提升工具调用和对齐性能。
practical_value: '- 多目标优化中，用 **硬过滤（符号一致性）或信噪比过滤（SNR）** 剔除梯度方向冲突的样本，避免优势项正负抵消，可用于推荐系统中同时优化点击率、转化率、多样性等目标。

  - 引入 **查询级重加权** 动态调整更新量：根据一个 query 下留存非冲突样本的比例自动降权，类似推荐中根据用户信号质量调整学习率。

  - SNR 一致性比率公式简单，可作为 **训练中实时监控指标**，检测多目标间的冲突程度。

  - 方法对阈值不敏感，超参数鲁棒性强，适合在线学习场景，可直接集成到基于 GRPO 的推荐策略优化中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
多奖励强化学习（如同时优化 helpfulness 和 harmlessness）中，不同维度奖励的梯度方向常互相矛盾，直接聚合会导致更新信号相消，阻碍训练。现有方法（如 GDPO）虽将优势解耦到各维度，但最终仍通过加权和聚合成单一标量，未能解决样本级冲突。同时，DAPO 等动态采样证明过滤无效样本（如全对/全错组）能提升效率，但未针对多奖励冲突设计。该工作旨在从样本粒度检测并抑制多奖励优势信号的不一致性，避免瓶颈。

## 方法
- **组动态冲突感知过滤**：在 GDPO 的优势解耦基础上，对每个 rollout 的多维度优势进行一致性判断。提供两种规则：
  - **硬过滤**：若任意两维优势符号相左，则直接屏蔽该 rollout。
  - **SNR 过滤**：计算聚合优势绝对值与各维优势绝对值之和的比值（类似于信噪比），低于阈值则丢弃，更柔性。
- **查询级重加权**：计算每个 query 下被保留的 rollout 比例，将其作为权重缩放该 query 的损失，以降低因大量 rollout 被屏蔽导致更新不可靠的查询的影响。
- 最终目标函数同时集成过滤与重加权，使训练聚焦于多维度信号一致的 rollout 和 query。

## 实验结果
- 任务：工具调用（API-Bank）和有益-无害对齐（HH-RLHF、PKU-SafeRLHF、Alpaca）。
- 基线：GRPO、GDPO，模型从 1.5B 到 8B。
- 工具调用双奖励（正确+长度）下，GD2PO-Hard 在 Qwen2.5-3B 上整体 Correct Acc 提高 1.31 个百分点（61.57→62.88）。
- 三奖励（正确+格式+长度）下，GD2PO-SNR 将 Correct Acc 再提升约 2 个百分点（60.50→61.97，Llama3.1-8B 从 55.44 升至 58.79）。
- 有益-无害对齐中，GD2PO 同时提升 Useful 和 Harmless 分数，未出现一升一降的权衡，保持了训练稳定性。
- 冲突比率监控显示，多奖励优化中冲突现象普遍存在，且动态变化，验证了过滤的必要性。
