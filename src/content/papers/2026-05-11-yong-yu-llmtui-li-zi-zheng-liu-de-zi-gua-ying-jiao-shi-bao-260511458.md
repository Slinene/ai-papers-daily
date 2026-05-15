---
title: Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning
title_zh: 用于LLM推理自蒸馏的自适应教师暴露
authors:
- Zihao Han
- Tiangang Zhang
- Huaibin Wang
- Yilun Sun
affiliations:
- ByteDance
arxiv_id: '2605.11458'
url: https://arxiv.org/abs/2605.11458
pdf_url: https://arxiv.org/pdf/2605.11458
published: '2026-05-11'
collected: '2026-05-15'
category: LLM
tags:
- Self-Distillation
- LLM
- Reasoning
- Teacher Exposure
- Reinforcement Learning
one_liner: 提出自适应教师暴露控制（ATESD），将教师所见的特权推理长度变为可学习变量，解决教师侧暴露不匹配问题
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
On-policy self-distillation（如 OPSD）让教师基于完整参考推理链提供 token 级监督，但其**教师侧暴露不匹配**问题被长期忽视：困难问题上，完整推理链远远超出学生当前能力，产生无法吸收的强目标。固定暴露扫描显示：（1）全暴露并非最优，中间暴露效果更好；（2）教师–学生分布差异随暴露量单调增长；（3）不同难度样本的最优暴露值不同。这说明教师暴露不应是固定超参数，而需作为训练时控制变量。

## 方法关键点
- **暴露建模**：将暴露率 α 定义为截断参考推理前缀的比例，保留最终答案，教师根据暴露后的参考生成监督。
- **Beta 策略控制器**：轻量 MLP 将训练状态统计（损失、mismatch EMA、探针 NLL EMA、学生自信度等）映射为 Beta 分布参数，采样一个全局 α 在 hold window（H 步）内固定。
- **延迟信用分配**：用未来 L 步学生更新的学习进展折现奖励（损失下降 + 教师对真实答案的对数概率）训练控制器，避免单步损失代理的短视；通过 REINFORCE 更新策略。
- 学生更新不动，仅改变教师评分时的上下文，公平保留 OPSD 框架。

## 关键实验
- 在 AIME 24/25 和 HMMT 25 上，用 Qwen3-1.7B/4B/8B 评测，对比 OPSD、GRPO、SFT。
- ATESD 在所有尺度上超越基线：**1.7B** Average@12 提升 0.95 至 44.35；**4B** 提升 2.05 至 65.65；**8B** 提升 2.33 至 67.13。
- 消融证实：延迟信用是有效暴露学习的必要条件；学习暴露策略优于最佳固定暴露（57.44 vs 59.17），并非仅靠随机噪声；暴露控制能明显降低正轨迹上的 teacher-student mismatch。

## 核心洞察
> 教师暴露不匹配是 on-policy self-distillation 中被忽视的瓶颈，将其变为可学习变量能持续提升推理性能。
