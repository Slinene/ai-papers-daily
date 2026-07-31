---
title: 'Beacon: Knowing When and How to Perform Agentic Visual Reasoning'
title_zh: Beacon：让视觉推理模型知道何时及如何调用工具
authors:
- Qixun Wang
- Yang Shi
- Letian Cheng
- Zhuoran Zhang
- Yan He
- Yuqi Tang
- Qi Zhang
- Xinlei Yu
- Ruizhe Chen
- Tianrun Xu
affiliations:
- Peking University
- Kling Team
- HKUST(GZ)
- CUHK
- ZJU
- THU
arxiv_id: '2607.28595'
url: https://arxiv.org/abs/2607.28595
pdf_url: https://arxiv.org/pdf/2607.28595
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: Agent 视觉推理中的自适应工具调用与强化学习
tags:
- Agentic Visual Reasoning
- Tool Use
- Adaptive Reward
- Reinforcement Learning
- GRPO
- RLVR
one_liner: 提出必要性感知自适应奖励与提示引导能力扩展，使模型能自适应调用工具并获真实性能增益
practical_value: '- **自适应奖励设计借鉴**：NAAR（必要性感知自适应奖励）可为电商/广告Agent中的工具调用决策提供参考——当纯文本推理即可解决问题时，对不必要的工具调用赋予较低奖励，但仍保留部分正向反馈（如0.25），避免抑制正确但冗余的工具使用；当纯文本失效时，正确工具调用获满奖励。这种软偏好平衡了效率与效果，有利于线上成本控制。

  - **困难样本的专家引导训练**：HCE（提示引导能力扩展）展示了如何利用教师模型生成子目标提示，引导策略在困难样本上探索，训练后再去掉提示使模型独立求解。这类似于在推荐Agent中处理长尾/冷启问题：先用强模型生成中间推理步骤的提示，帮助学生模型学习有效工具组合，最终摆脱对强模型的依赖。

  - **在线标注避免分布偏移**：NAAR 基于当前策略的组内正确性动态标注样本是否需要工具，而非固定教师模型。在动态变化的推荐场景（如季节性偏好）中，这种在线标注方式可让工具调用策略随模型能力同步进化。

  - **混合策略优化与重要性采样**：同时训练普通采样和提示引导采样的轨迹，并对提示轨迹使用重要性采样校正（将提示输入替换为原始输入），实现能力迁移。这一技巧可迁移到任何需要将外部知识注入策略训练的Agent场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 Agent 视觉推理模型常盲目调用工具，缺乏对任务必要性的判断，导致工具带来的收益被无效调用引入的错误所抵消。为量化这一现象，该工作定义了两个维度：Mode Adaptiveness（MA，模式自适应性）和 Tool Effect（TE，工具效应），发现多数模型缺乏自适应工具调用行为，且工具收益净增长几乎为零。

**方法关键点**
- **评价框架**：MA 衡量模型在工具非必需时避免调用、在必需时主动调用的能力；TE 分解为 Tool-Gain（工具解决硬样本的收益）和 Tool-Harm（工具损害简单样本的损失）。
- **数据建设**：从16个基准中选取困难样本，利用 Gemini 3.1 Pro 生成并精炼代码辅助推理轨迹作为 SFT 数据；RL 阶段进一步筛选仍未解决的样本。
- **必要性感知自适应奖励（NAAR）**：若 rollout 组中存在正确纯文本应答，则对正确纯文本应答给满分1，对正确代码应答仅给0.25；若组内无正确纯文本，则正确代码应答得满分。以此软偏好促进自适应工具调用。
- **提示引导能力扩展（HCE）**：对全体错误 rollout 的样本，用专家模型生成不含答案的步骤提示，重新采样生成轨迹；训练时移除提示但保留生成的轨迹，通过重要性采样将提示引导的能力迁移到无提示策略。
- **训练框架**：基于 GRPO，混合正常组和提示组的优势计算，格式奖励与自适应奖励加权求和。

**关键结果**
在13个涵盖高分辨率搜索、空间推理、图表理解的基准上，Beacon 平均准确率 58.98%，超过所有开源模型，比基座 Qwen3-VL-8B 平均提升 6.07 个百分点。MA 和 TE 指标显著改善：平均 MAmean 58.83%（其他模型 ~50%），Tool-Gain 与 Tool-Harm 之差达 +3.14%（其他模型接近零），表明工具调用更精准有效。

**一句话总结**
“告诉模型何时该用工具，比让它狂用工具更重要。”
