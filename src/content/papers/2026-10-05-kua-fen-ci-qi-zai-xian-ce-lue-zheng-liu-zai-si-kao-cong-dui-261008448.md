---
title: 'Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage
  to Supervision Reliability'
title_zh: 跨分词器在线策略蒸馏再思考：从对齐覆盖到监督可靠性
authors:
- Bingxi Hou
- Guochao Jiang
- Guofeng Quan
- Weiqing Li
- Wenfeng Feng
- Guohua Liu
- Yuewei Zhang
affiliations:
- Alibaba Cloud Computing
arxiv_id: '2610.08448'
url: https://arxiv.org/abs/2610.08448
pdf_url: https://arxiv.org/pdf/2610.08448
published: '2026-10-05'
collected: '2026-10-07'
category: Training
direction: 跨 tokenizer 蒸馏优化
tags:
- Cross-Tokenizer
- On-Policy Distillation
- Reverse KL
- Shared Vocabulary
- Gradient Diagnostics
- LLM Distillation
one_liner: 跨 tokenizer 在线蒸馏中，严格 1:1 对齐已覆盖多数 token；学生选 top-16 共享词表即可保留大部分收益，补 mismatch
  span MSE 反而降精度
practical_value: '- 做跨 tokenizer / 跨模型蒸馏时，可先只对严格 1:1 对齐位置做 shared vocabulary 上的 reverse
  KL，并让学生自选 top-k（如 top-16）词表子集；这能压缩计算和显存，同时保留大部分蒸馏收益。适合生成式推荐中不同 tokenizer 的 Semantic
  ID 序列蒸馏。

  - 新增辅助监督（如 mismatch span MSE、多任务损失）前，先做梯度方向与相对幅度诊断：计算 g_mis 与 g_strict 的 cosine
  和 norm ratio；若 cosine 接近 0/负、norm ratio 随训练上升，大概率引入冲突信号，应降低权重或丢弃。

  - 评估“监督覆盖”不要只看静态词表 Jaccard，要看 student rollout 上 strict token coverage 以及共享词表实际概率质量；工程上采样几十条
  rollout 即可快速判断是否值得做复杂对齐。

  - 在 Agent 或推荐 LLM 的蒸馏中，若希望提升 teacher 信号覆盖，不要盲目追求全位置覆盖；优先保证主损失梯度干净，可先在小支持集上验证收益再扩展。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：跨 tokenizer 在线策略蒸馏（OPD）需要在序列和词表两个层面对齐 teacher 与 student 的预测。已有方法（如 SimCT、Byte-Prefix Marginalization）试图扩大对齐覆盖，恢复更多 mismatch 区域的监督；但“覆盖更多”是否等价于“学得更好”并不清楚。论文用三对异构模型检验严格对齐已保留多少监督，以及恢复被排除目标的实际学习价值。

**方法关键点**：
- 将响应按共同 token 边界切分为 strict 1:1 groups（一个 student token 对一个 teacher token，直接可比较）和 mismatch groups（至少一侧需要多个 token 覆盖同一 span）。
- 严格损失只在 strict 位置、共享词表上做 reverse KL，即 `KL(¯πθ ∥ ¯πT)`，双方分布均 restricted + renormalized。
- mismatch 监督采用 span log-probability 的 MSE：对每个 mismatch group 内的 token 路径概率取 log 后计算平方差，与 strict loss 加权组合。
- 提出 student-selected top-k support：在每个 strict 位置，由学生分布从共享词表中选 top-k 个最高概率 token，仅在该子集上做 reverse KL。
- 用概率质量测量 + 梯度诊断（gradient cosine、norm ratio）解释新增监督为何有害。

**关键实验与结果**：
- 模型对：Qwen2.5-7B-Instruct→Llama-3.2-3B-Instruct、Granite-4.1-8B→Phi-4-mini-instruct、Granite-4.1-8B→Qwen2.5-7B-Base；任务为数学推理和代码生成。
- 静态词表 Jaccard 只有 39.49–64.87%，但学生 rollout 上 strict token coverage 达 85.57–96.98%；共享词表保留 teacher 概率质量 99.69–99.90%、student 98.99–99.81%。
- 学生选 top-16 共享词表子集保留至少 93.54% teacher mass、94.55% student mass；在 full-average 上 top-16 保留至少 96% 的 strict full 相对 Base 的提升，且比 ULD、Extended ULD、GOLD、SimCT 高 0.51–1.05pp。
- 给 mismatch span 加 MSE 后，所有 18 个正权重设置 accuracy 均低于 λ=0，下降 0.27–1.20pp；梯度诊断显示 mismatch 梯度与 strict 梯度 cosine 接近 0 或为负，而 span-to-strict norm ratio 随训练上升（如 Qwen→Llama 从 0.294 升至 1.942）。

**最值得记住的一句话**：跨 tokenizer OPD 的价值瓶颈不是对齐覆盖，而是监督可靠性；在严格位置做紧凑的 top-k 监督，胜过通过弱对齐 span 损失追求全位置覆盖。
