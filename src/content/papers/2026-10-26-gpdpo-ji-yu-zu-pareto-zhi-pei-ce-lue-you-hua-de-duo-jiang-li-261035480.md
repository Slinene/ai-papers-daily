---
title: 'GPDPO: Learning from Reward Conflicts via Group Pareto-Dominance Policy Optimization'
title_zh: GPDPO：基于组 Pareto 支配策略优化的多奖励冲突学习
authors:
- Zixuan Xu
- Haoxuan Chen
- Jiangxin Sun
- Jian-Fang Hu
affiliations:
- Sun Yat-sen University
- University of Trento
arxiv_id: '2610.35480'
url: https://arxiv.org/abs/2610.35480
pdf_url: https://arxiv.org/pdf/2610.35480
published: '2026-10-26'
collected: '2026-10-27'
category: Training
direction: 多奖励 RL 冲突过滤与 Pareto 偏好恢复
tags:
- Multi-reward RL
- Pareto Dominance
- Conflict Filtering
- Policy Optimization
- LLM Alignment
- Tool Calling
one_liner: 从被冲突过滤的 rollout 中利用 Pareto 支配恢复成对偏好监督，零额外采样提升多奖励 LLM 对齐
practical_value: '- 多目标 RL 场景（相关性/转化/格式/延迟等）若采用 GD2PO 式冲突过滤，不要直接丢弃被过滤 rollout；用 Pareto
  支配在 filtered 与组内其他响应间构造偏好对，加入辅助 loss。只复用已有 reward 与 log-prob，无需额外采样。

  - 冲突 gate 对 group 大小和组成敏感：论文中组大小 4→64 有 16%–27% 标签翻转；在线采样 batch 不稳定时，优先考虑 pairwise
  比较或增大组内响应数来降低优势标签噪声。

  - 使用标准 Pareto 而非 strict domination，允许单维 reward tie，能多产生约 88% 的比较边；对二值/离散 reward（如格式合规、广告合规）尤其关键，可缓解辅助信号稀疏。

  - 辅助偏好 loss 中对 retained 端点做 stop gradient，只让 filtered 侧更新；若两端都 filtered 再同时更新，避免干扰已稳定样本，这是稳定多奖励
  RL 的重要工程 trick。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
多奖励 RL 对齐 LLM 时，不同奖励维度常对同一响应给出冲突的 group-relative advantage，导致更新方向抵消。现有 GD2PO 等用 conflict gate 直接过滤这些响应，但响应级过滤过于粗糙：被丢弃的响应仍可能与其他响应形成明确一致的关系。论文实证显示约 86%–88% 的被过滤响应至少与一个组内 peer 存在一致的 Pareto 比较，约 23%–27% 甚至匹配 ground-truth tool-call。

**方法关键点**
- 保留 GD2PO 的 conflict gate，将每组采样响应分为 retained / filtered。
- 在组内按多维 reward 判定 Pareto 支配：yw dominates yl 当且仅当所有 reward 维度不差且至少一维更好。
- 只选择至少一端为 filtered 的支配边构造 pairwise preference loss：-log σ(β[uθ(yw|x)-uθ(yl|x)])，其中 uθ 是 token-level 平均 log-prob ratio。
- 对 retained 端点 stop gradient 作为固定锚点；若两端均 filtered 才同时更新。
- 联合标准 clipped policy loss：L = L_standard + λ L_pair，λ=0.1，β=0.1；无需额外采样或 reward 评估。

**关键结果数字**
- 任务：API-Bank 工具调用；训练集 RLLA-4K 3,920 样本；Qwen3-1.7B / 4B；2R（正确性+长度）与 3R（+格式）设置。
- GPDPO 在 Correct Acc 与 Overall 上均优于 GRPO/GDPO/GD2PO。2R：1.7B 正确率 64.99% vs GD2PO 62.48%，4B 66.00% vs 64.66%；3R：1.7B 63.32% vs 62.48%，4B 65.33% vs 63.32%。
- 消融：标准 Pareto 比 strict domination 高 1.51 点；scalarized reward ordering 掉到 61.81%；fixed reference 62.81%；Pareto-guided advantage adjustment 63.82%，不如直接优化 preference margin 的 64.99%。
- GPDPO 训练后期 conflict rate 更低且 policy entropy 更高，表明提升不是以更快的策略塌缩为代价。

**最值得记住的一句话**：group-level 冲突过滤不等于没有 pairwise 监督，用 Pareto 支配从被过滤样本中恢复偏好对是零额外成本提升多奖励 RL 的关键。
