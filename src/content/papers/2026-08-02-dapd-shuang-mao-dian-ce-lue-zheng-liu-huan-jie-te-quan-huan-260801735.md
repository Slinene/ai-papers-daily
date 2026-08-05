---
title: 'DAPD: Dual-Anchored Policy Distillation'
title_zh: DAPD：双锚点策略蒸馏缓解特权幻觉
authors:
- Jianyu Wu
- Yizhou Wang
- Encheng Su
- Chen Tang
- Shixiang Tang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- University of Science and Technology of China
arxiv_id: '2608.01735'
url: https://arxiv.org/abs/2608.01735
pdf_url: https://arxiv.org/pdf/2608.01735
published: '2026-08-02'
collected: '2026-08-05'
category: Training
direction: On-policy 蒸馏训练 · 特权幻觉缓解
tags:
- On-policy Distillation
- Privilege Illusion
- Dual-Anchored
- Multi-source Supervision
- Reasoning
- LLM Alignment
one_liner: 识别 OPSD 中信息不对称为特权幻觉根源，提出双锚点蒸馏框架 DAPD，在多个任务和尺度上大幅提升性能。
practical_value: '- **信息不对称对齐思路**：电商推荐中 teacher 模型常用用户序列等额外特征，student 却无，可构造自条件中间分布作为桥梁，添加无特权信息的对齐损失（类似
  Inference Anchor）来抑制幻觉，防止模型依赖不可见信号。

  - **双源引导设计**：在 Agent 策略蒸馏时，利用 teacher 轨迹（参考解）提供正确性监督，同时用 student 自身 rollout 提供可达性指导，通过
  DSA 动态平衡两者权重（较小模型更多信任参考，较大模型更多信任 rollout），可迁移到多臂老虎机或排序策略的学习中。

  - **工程技巧复用**：DAPD 使用 detached teacher 与共享 snapshot 减少训练开销，且仅在训练时引入额外分布而不增加推理成本，适合用于在线推荐系统的模型蒸馏。

  - **尺度适配策略**：实验发现模型越大，从自身 rollout 获取的引导越有价值，可据此设计自适应的 source 权重调度，在推荐模型随业务增长时自动调整
  teacher–rollout 信任比例。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
On-policy 自蒸馏（OPSD）在语言模型后训练中广泛应用，通过将 teacher 条件于参考解（privileged information）来提供密集 token 级监督。但 student 推理时无法访问这些信息，导致特权幻觉：student 做出无法从上下文推导的断言，损害性能。现有方法仅修改 teacher 信号，未消除 teacher 与 student 间的信息不对称，因此本文将其识别为根本原因，并提出双锚点策略蒸馏（DAPD）框架。

## 方法
- **自条件分布（Self）作为桥梁**：引入一种新分布，将 student 条件于它即将预测的完整 completion，使其信息量与 teacher 匹配，但参数与 student 共享，从而作为对齐锚点。
- **双路径锚定（DPA）**：构建两条对齐路径——无条件路径（Entangled Distillation + Inference Anchor）在无特权信息下对齐 rollout 与 reference 的 student 行为；特权路径（Privileged Anchor）在有特权信息下对齐两者，避免特权依赖行为传递到推理时的 student。
- **双源锚定（DSA）**：在 reference→rollout 和 rollout→reference 两个方向上均施加 DPA，平衡可靠参考引导与 student 可达的 rollout 引导，并通过权重 λ 控制两者的混合。

## 实验结果
- 在 Qwen3-4B 上，DAPD 在 AIME24/25、HMMT25、LiveCodeBench、BFCL 和 IFBench 六个基准上平均提升 +2.00 点（vs. OPSD）。
- 跨尺度（1.7B–32B）实验中，OPSD 的增益随模型增大几乎消失，而 DAPD 持续稳定：4B 提升 +2.69，32B 提升 +2.78。
- 消融证实双路径和双源均不可或缺，且双 rollout 或验证 rollout 变体可去掉对人工参考的依赖，仍超越 OPSD。
- 定性分析显示 DAPD 大幅减少无依据答案（错误声明降低 73%），推理行为更可信。

> 核心洞见：信息不对称是特权幻觉的根源，通过自条件锚点和多源路径对齐可直接结构性地解决该问题，为蒸馏训练提供了新范式。
