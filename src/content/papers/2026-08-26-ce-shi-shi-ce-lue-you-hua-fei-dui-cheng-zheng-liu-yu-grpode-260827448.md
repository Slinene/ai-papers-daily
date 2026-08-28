---
title: 'TTPO: Test-Time Policy Optimization'
title_zh: 测试时策略优化：非对称蒸馏与GRPO的无标签推理提升
authors:
- Aozhe Wang
- Zhengxi Lu
- Jianze Wang
- Shangke Lv
- Ying Liu
- Weiming Lu
- Jun Xiao
- Yueting Zhuang
- Hua Yang
- Qianglong Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2608.27448'
url: https://arxiv.org/abs/2608.27448
pdf_url: https://arxiv.org/pdf/2608.27448
published: '2026-08-26'
collected: '2026-08-28'
category: Training
direction: 测试时训练 · 非对称蒸馏与RL
tags:
- Test-Time Training
- Self-Distillation
- GRPO
- Majority Voting
- Token-Level Selection
- Math Reasoning
one_liner: 多数投票伪标签下，正样本蒸馏、负样本GRPO惩罚，配合token级选择，无标签测试时训练匹配有监督OPSD
practical_value: '- 无标签或延迟反馈的业务场景（如搜索/推荐结果的多步解释、Agent 任务完成率）可用模型自身多数投票/一致性产生伪标签；关键是不要直接蒸馏伪标签，而是对“与多数不一致”的样本做
  RL 惩罚，这比正向模仿伪标签更抗噪声。

  - 多步 Agent 或生成式推荐做 test-time fine-tune 时，正样本用蒸馏、负样本用 RL 惩罚，并且只对负样本中 confident errors（低概率低熵）施加梯度，避免惩罚正确的中间步骤；正样本按
  step 重要度加权，降低已收敛位置的权重。

  - 工程 trick：RL loss 需要加权重（约 0.1）平衡蒸馏 loss 的量级；固定正负样本 1:1 比动态比例更稳定；选择最短完整轨迹进入梯度更新窗口，可避免关键决策步骤落在梯度窗口外。

  - 若业务有“答案可验证但无真值”的场景，优先用多数投票路由而不是 ground-truth 路由：困难样本上 GT 路由可能正样本为空导致训练信号消失，多数投票保证两个分支活跃，形成自我进化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM 数学推理的后训练常用 RLVR 和 OPSD，但都依赖 ground-truth label。测试时训练（TTT）没有标签，现有 TTRL 用多数投票伪标签做 RL 只给序列级标量信号，错误伪标签会强化错误；若把伪标签直接替换进 OPSD，错误标签会在每个 token 上传播。关键观察是：即使伪标签错误，与伪标签不一致的 rollout 中约 79% 本身也是错的，因此惩罚分歧比蒸馏伪标签更稳健。

**方法关键点**
- 每个问题采样 K=64 条 rollout，多数投票产生伪标签，将轨迹分为正样本 P（答案与伪标签一致）和负样本 N（不一致）。
- 非对称目标：正样本用 OPSD forward KL 蒸馏，teacher 是以伪标签为条件的模型；负样本用 GRPO 惩罚，group-relative advantage 为负，只依赖“不属于多数簇”，不依赖伪标签内容。
- 正样本 token weighting：基于 student entropy 和 teacher-student KL 的 soft-OR，降低已收敛位置权重。
- 负样本 token masking：用 `-log p * (1 - normalized entropy)` 评分，选 top-50%，只惩罚 confident errors。
- 统一损失为 `Σ_P L_OPSD + λ Σ_N L_GRPO`，λ=0.1 平衡梯度；K_train=8 选最短轨迹，固定正负各半。

**关键结果数字**
- 在 OpenThoughts 有标签数据上（TTPO 不用标签），Qwen3-1.7B 平均 40.1，超过标签监督 OPSD 的 39.7；4B 58.6 vs 58.4；8B 62.6 vs 61.7。
- TTT 无标签设置：Qwen3-1.7B 从 38.0 提升到 45.2，超过 TTRL 40.2 和 OPSD-TTT 41.9；4B 57.4→61.1；8B 60.7→65.3。
- 非思考评估：1.7B +25.2、4B +30.6、8B +36.4，远高于 OPSD 的 +7.1/+5.8/+3.5。
- 交叉 benchmark 泛化验证不是过拟合；消融显示 token-level 选择和 λ 平衡都重要。

**最值得记住的一句话**
多数投票即使错误也保留可用的分歧信号：正样本蒸馏退化为 thinking-to-non-thinking 模式传递，负样本惩罚只看“不属于多数簇”，两者让模型在无标签下自我进化并突破静态伪标签天花板。
