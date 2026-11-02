---
title: MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation
title_zh: Muon-RT：复用教师轨迹的无动量 Muon 用于 LLM 自蒸馏
authors:
- Aryan Das
- Vinay Kumar Verma
- Aakansha Mishra
affiliations:
- IIT Kanpur
- Amazon
arxiv_id: '2610.41104'
url: https://arxiv.org/abs/2610.41104
pdf_url: https://arxiv.org/pdf/2610.41104
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM 自蒸馏优化器内存优化
tags:
- Muon
- self-distillation
- memory-efficient optimizer
- EMA teacher
- LLM fine-tuning
- momentum-free
one_liner: 复用 EMA 教师-学生位移替代 Muon 动量缓冲，在自蒸馏微调中省显存并提升准确率
practical_value: '- 如果业务中已在用自蒸馏/EMA teacher 做 LLM 对齐（SDFT/SDPO），可去掉 hidden weight
  矩阵的 Muon 动量 buffer，直接复用 teacher-student 位移；在 Qwen2.5-7B 上平均准确率比 AdamW 高 2.6 点，同时持久显存省
  42%，适合 7B 级线上微调。

  - Muon-RT 保留 Newton-Schulz 正交化，但对 teacher 位移做去径向分量 + spectral normalization，再与当前梯度混合；这种“复用历史更新方向去噪”的思路可迁移到推荐模型的大
  embedding/MLP 权重优化，尤其是 LoRA/全参微调受显存限制时。

  - 相比 momentum Muon 平均提升 5.4 点、持久显存少 27%；在 Olmo-3-7B SDPO 上比 AdamW 提升 2.0 点，说明策略优化/RL
  自蒸馏场景也能作为 AdamW 替代。

  - 注意边界：收益依赖局部模型、正则与对齐假设，且主要针对 hidden weight 矩阵；建议先在小规模微调中验证内存与收敛，再在推荐/搜索 LLM 训练中推广。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

动机：自蒸馏方法（如 SDFT/SDPO）通常用 EMA teacher，已经保存学生更新的历史；Muon 优化器却为 hidden weight 矩阵额外维护 momentum buffer，增加持久显存。

方法关键点：Muon-RT 复用 teacher-student 位移来替代 momentum buffer。该位移被证明编码了已应用更新的指数加权历史，并能在局部模型下平滑时间不相关噪声。Muon-RT 去掉位移的径向分量，做 spectral normalization，再与经过 Newton-Schulz 正交化后的当前梯度混合。理论分析在显式正则性和对齐假设下，证明期望目标差距上界线性收缩到一个残差误差水平。

关键结果：在 Qwen2.5-7B-Instruct 上做 SDFT，Muon-RT 比 AdamW 平均准确率高 2.6 点，持久显存省 42%；比 momentum Muon 高 5.4 点，持久显存省 27%。在 Olmo-3-7B-Instruct 上做 SDPO，比 AdamW 平均准确率高 2.0 点。
