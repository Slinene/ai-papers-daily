---
title: Trust Region On-Policy Distillation
title_zh: 信任区域在线策略蒸馏
authors:
- Xingrun Xing
- Haoqing Wang
- Boyan Gao
- Ziheng Li
- Yehui Tang
affiliations:
- Samsung Research, Beijing, China
- University of Oxford
- Peking University
arxiv_id: '2606.01249'
url: https://arxiv.org/abs/2606.01249
pdf_url: https://arxiv.org/pdf/2606.01249
published: '2026-05-30'
collected: '2026-06-03'
category: Training
direction: 在线策略蒸馏稳定化训练
tags:
- On-Policy Distillation
- Trust Region
- Knowledge Distillation
- Small Reasoning Models
- KL Divergence
- Policy Gradient
one_liner: 通过信任区域划分、异常值前向KL估计和离线指导，解决在线策略蒸馏中分布不匹配导致的训练不稳定问题，显著提升小推理模型性能。
practical_value: '面向电商/推荐/Agent 从业者的可借鉴点：

  - 信任区域思想可迁移至多智体策略更新：仅在教师与学生策略一致性高的区域执行在线策略蒸馏，避免极端策略梯度导致的训练崩溃，类似推荐系统中用置信度过滤不可靠的在线信号。

  - 离线指导（Off-Policy Guidance）机制可借鉴：用教师前缀引导学生生成，并用前向KL模仿学习，适合在推荐对话或Agent任务中利用高质量模板引导小模型探索有效路径。

  - 异常值前向KL估计提供了一种廉价的信息保留方式：当教师-学生分布严重不匹配时，用top-k前向KL替代完全丢弃或裁剪，可在电商搜索query改写等场景中保留多样性信号。

  - 混合目标设计与资源权衡：TrOPD同时使用K1估计器（O(n)内存）和top-k前向KL（O(nk)内存），为生成式推荐中的长序列推理蒸馏提供了内存可控的参考，尤其在序列推荐或文案生成等需要长输出的场景下。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
在线策略蒸馏（OPD）通过直接训练学生生成的轨迹减少暴露偏差，是小推理模型后训练的核心技术，广泛应用于Agent学习、多任务增强和模型压缩。然而，当教师与学生分布差距较大时，基于学生样本的反向KL估计器（K1估计）会产生极端策略梯度，导致优化不稳定甚至崩溃。现有方法如熵过滤或奖励裁剪效果有限，亟需更可靠的监控机制。

**方法关键点**  
- **信任区域划分**：按教师-学生解码一致性比例动态区分“信任区域”与“异常值”，仅在可信区域使用K1反向KL优化。
- **异常值估计**：对异常值区域，改用top-k前向KL估计保留监督信息，避免完全丢弃有价值信号。
- **离线指导**：用教师前缀+学生延续的混合生成方式，通过前向KL仿效教师轨迹，鼓励向可信区域探索。
- **统一目标**：集成信任区域反向KL、异常值前向KL和离线指导前向KL，并用余弦退火逐渐减小离线部分，最终转入全在线策略。

**关键实验**  
- 设置：数学、代码、STEM多领域，教师模型Skywork-OR1-Math-7B / Qwen3-Nemotron-4B，学生模型DeepSeek-Qwen2.5-1.5B / Qwen3-SFT-1.7B。
- 结果：TrOPD在数学领域平均提升3.06点，通用域提升2.63点；多域蒸馏平均提升4.62点和3.44点。相比OPD、REOPOLD、EOPD等，均取得一致最优。
- 消融：仅异常值前向KL即优于掩码或裁剪；加入离线指导进一步增益，且与同期AOPD正交，组合后进一步提升。

**核心结论**  
“当教师与学生的分布不匹配时，不是所有在线样本都值得信任——仅在教师可验证区域内蒸馏，并利用教师视角的前向KL补足异常值信息，才能稳定且高效地传导推理能力。”
