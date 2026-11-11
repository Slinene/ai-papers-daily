---
title: 'Tree-Ising: Repairing Language Models with Bit-Level Ising Edits'
title_zh: Tree-Ising：用位级 Ising 编辑修复语言模型
authors:
- Hadi Salloum
- Ammar Ali
affiliations:
- QDeep, Riyadh, Saudi Arabia
- LEAD (Lab for Efficient AI and Data), ITMO University
arxiv_id: '2611.14210'
url: https://arxiv.org/abs/2611.14210
pdf_url: https://arxiv.org/pdf/2611.14210
published: '2026-11-09'
collected: '2026-11-11'
category: LLM
direction: LLM 权重编辑 · 离散优化
tags:
- weight-space programming
- Ising model
- simulated annealing
- BF16
- model repair
- simulated bifurcation
one_liner: 将 LLM 权重编辑转化为 BF16 位级 QUBO 优化，以极低成本超越 LLM agent 的修复效果
practical_value: '- 在电商/广告等有大量已部署 LLM 的场景，可以借鉴这种**无梯度、离散权重编辑**的思路，对线上模型出现特定推理失败（如重复、逻辑循环）进行定点修复，无需重新训练或微调。

  - 工程实现上，可参考其**只用前向统计定义目标函数**的方法：通过 token 上的方向性统计（削弱循环方向、加强结论方向）构造稀疏优化问题，完全绕开反向传播，适合部署侧快速干预。

  - **成本极低**：该修复仅需 4 次前向传播、零 LLM tokens、约 0.90 美元 GPU 时间，相比用 LLM agent 读权重写代码（158
  turns, 89.7M tokens）是数量级的节省，适合在资源受限的推荐/Agent 系统中做模型热修复。

  - 用到 solver 的选择（simulated annealing / simulated bifurcation）和状态树表示（保留 BF16 组指数与尾数）的技巧，可迁移到其他需要低比特权重量化或稀疏模型编辑的场景。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：近期 MIT 提出的 weight-space programming 让 LLM agent 读取权重并直接写修复代码，但成本高昂（158 次 agent turns、89.7M tokens、50 次前向）。本文希望用纯优化方法替代 agent，实现更高效、更可控的模型修复。

**方法**：将 LLM 修复问题建模为 BF16 权重上的稀疏离散优化。基于前向传播统计定义目标：削弱导致推理循环的方向、加强正确结论方向、保持其他 productive tokens 输出不变。采用状态树表示可编辑空间，允许符号翻转和指数移位，但保留 BF16 的组指数和尾数结构，保证编辑无损。进一步将目标精确分解为独立的 QUBO（Ising）子问题，每个输出行一个，在 GPU 上用 simulated annealing 或 quantum-inspired simulated bifurcation 求解。

**结果**：在 agent 修复的两层上，Tree-Ising 在 MATH-500 达 54.6%，超过 agent edit 的 51.7%，而 base model 仅有 7.9%；simulated bifurcation 达 55.1%，统计无差异。两者在所有五个数学基准上均优于 agent edit，经多重比较校正后在 MATH-500 和 GSM8K 上显著。方法修改权重数少 13%-17%，BF16 位翻转减少 2.2-2.3 倍，只需要 4 次前向和零 LLM tokens，约 $0.90 GPU 成本。扩展到 Qwen3.5-2B，仅用 base model 选择层和剂量，GSM8K greedy 准确率从 21.6% 提升至 69.4%。另在 IBM Heron 处理器上用 QAOA 完成八变量子问题概念验证。
