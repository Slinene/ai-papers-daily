---
title: Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models
title_zh: 成本感知的 Agentic 特征优化系统：面向大规模排序模型舰队
authors:
- Chang Yang
- Yao Xuan
- Wendan Yan
- Nhat Le
- Jiang Liu
- Longhao Jin
- Zhen Peggy Yao
- Alireza Vahdatpour
- Djordje Gligorijevic
affiliations:
- Meta
arxiv_id: '2611.26531'
url: https://arxiv.org/abs/2611.26531
pdf_url: https://arxiv.org/pdf/2611.26531
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: Agent 驱动特征选择与资源约束优化
tags:
- Feature Selection
- LLM Agents
- Cost-aware Optimization
- Ads Ranking
- Pareto Optimality
- Multi-task
one_liner: 用 LLM agent 生成交叉特征并与 Pareto 特征混合、资源约束搜索，在舰队级排序模型上提升 NE 0.31%、在线指标 0.20%
practical_value: '- 特征生成用两段式：LLM 粗召回 + 确定性 FI 精排，解决交叉特征候选组合爆炸；电商/广告特征池大、cross feature
  候选多时可直接复用，并用历史 FI 分数持续微调共享 generator。

  - 多任务特征排序不要加权求和每任务 importance，改用 Pareto front 选择，避免 task weight 人工调参；对电商多目标（CTR/CVR/GMV）尤其适用，能保留单目标高价值但全局不突出的特征。

  - 把特征选择参数化为 per-category volume 和 blending mixture，用 LLM Researcher 做 10-25 次异步试验并固定
  winner 规则，而不是手动增删特征；起步可先固定 mixture 只搜 volume，快速拿到重平衡收益。

  - pipeline cost trimming 的共享成本定义很有价值：同一预算下其他模型已使用的特征不新增成本；多模型共用特征流水线时按 budget 归属裁剪并用同类已用特征回填，能降本且不改变
  feature counts/FLOPs。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
大型平台运行大量广告排序模型，每个模型从数万级共享特征池里选特征。特征在不同模型上表现不同，且有不同的 serving 成本与 pipeline 成本。手工增删特征效率低，难以在预测质量和成本间做系统性权衡。已有的 LLM 特征选择工作只处理单模型，缺少跨模型共享预算与资源约束的机制。

## 方法关键点
- **Agentic Feature Creation**：用 LLM 从原始信号生成 cross features。候选组合空间可达数千万，先用一个 fleet 级共享的 retrieval LLM 做粗召回，再用确定性 feature importance（FI）做精排。该 retrieval LLM 用多模型的历史 FI 结果持续 fine-tune，特征创建质量随优化模型数量增加而提升。
- **Feature Ranking**：用一次训练在全量候选池上计算多种 FI，包括 permutation importance、Shapley value sampling、Kernel SHAP，以及 segment-aware 变体（只在高价值流量切片上打分，挖掘全局重要性会埋没的特征）。
- **Feature Blending**：多任务场景不用加权求和每任务 FI，而是按 Pareto 最优性选择特征，天然避免 task weight 调参。多个 ranking 源（incumbent + estimators）通过 mixture π 分配预算合并，按 dense/sparse/transform/embedding 类别分别取 counts。
- **Agentic Feature Selection**：LLM Researcher 代理在 observe-reason-act 循环中提出 hypothesis，搜索 per-category volume 和 blending mixture。调度异步进行，对超资源 cap 的 trial 提前终止；pipeline cost 通过 trimming 在训练前裁剪，只移除/替换导致预算超支的新特征，保持类别数量不变、FLOPs 基本不变。共享 pipeline 预算下，已被同预算其他模型使用的特征不新增成本。

## 关键实验
在特征搜索的 25 次试验中，Pareto 前沿从最快 trial（+1.47% NE at 1.10× QPS）延伸到最准 trial（−1.08% NE at 0.77× QPS），且 greedy、exploration、evolutionary 都在后期贡献新最优。另一个 production 转化模型在 1.2× FLOPs cap 下，将 embedding 翻倍、sparse 减 14% 的 recipe trial 降低 NE 0.17%，说明跨类别 volume 重平衡是关键。跨 7 个高影响模型，系统平均降低 NE 0.31%；pipeline-cost trimming 平均降 pipeline 成本 2.3%，主任务损失无明显回归；在线 A/B 主要指标提升 0.20%。

## 值得记住的一句话
核心收益来自跨特征类别的 volume 重平衡，而非简单扩量；把共享 pipeline 成本定义为“同预算下已被其他模型使用的特征不新增成本”，是舰队级特征优化的关键机制。
