---
title: Token Time Continuous Diffusion for Language Modeling
title_zh: Token时间连续扩散语言建模
authors:
- Parikshit Bansal
- Sujay Sanghavi
affiliations:
- UT Austin
arxiv_id: '2607.14106'
url: https://arxiv.org/abs/2607.14106
pdf_url: https://arxiv.org/pdf/2607.14106
published: '2026-05-06'
collected: '2026-07-18'
category: LLM
direction: 扩散语言模型 · 连续空间与每token时间步
tags:
- diffusion model
- language model
- continuous space
- per-token time
- self-distillation
- conditional generation
one_liner: 提出连续空间上token级时间可变的扩散语言模型，解决高加速比下离散模型并行采样不准确问题
practical_value: '- **低延迟文本生成**：TTCD 的确定性连续扩散避免了多 token 并行采样的因子分解误差，在高加速比（少步生成）下质量稳定，适合电商搜索推荐中的实时文案生成、对话
  Agent 响应等场景，可直接移植其连续演化思想。

  - **可控多字段生成**：每 token 可独立设置扩散速度，允许“确定度高的 token 先到位”；在生成式推荐中，可用于先生成核心语义 ID 或关键属性，再填充细节，提升生成质量和可控性。

  - **自蒸馏训练技巧**：论文采用自蒸馏提升最终生成质量，此方法可应用于工业界小模型（如移动端或边缘设备上的轻量 LM）的训练中，无需额外数据即可优化。

  - **连续空间避免误差累积**：若系统涉及多轮迭代生成（如 Agent 规划链式输出），连续扩散可降低离散采样带来的级联错误，可考虑在内部协议生成或 API
  参数生成中借鉴该框架。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：离散空间扩散语言模型在高速生成（少步）时，并行去噪多个 token 会因使用边际分布乘积近似联合分布而导致质量严重下降（因子分解问题），限制了实际部署中的加速潜力。

**方法**：提出 Token Time Continuous Diffusion (TTCD)，核心创新有两点：① Token 嵌入在连续空间中从高斯噪声确定性演化至干净嵌入，整个过程无需额外采样步骤；② 引入**每 token 独立时间步**，允许不同 token 以不同速度去噪，模型可让高置信度 token 更快收敛，并学习不同 token 之间的差异化影响。训练时，使用 160M 参数模型在 OpenWebText 上进行自蒸馏，进一步提升性能。

**结果**：在高加速比设定下，TTCD 的无条件生成质量与同规模自蒸馏模型的离散扩散模型相当，但在**条件生成任务（如 Sudoku 求解）上显著超越**同类模型，验证了连续空间与每 token 时间机制对条件建模的增益。
