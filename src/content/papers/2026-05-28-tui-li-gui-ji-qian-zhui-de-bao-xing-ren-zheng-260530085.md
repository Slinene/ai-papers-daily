---
title: Conformal Certification of Reasoning Trace Prefixes
title_zh: 推理轨迹前缀的保形认证
authors:
- Matt Y. Cheung
- Ashok Veeraraghavan
- Hanjie Chen
- Guha Balakrishnan
affiliations:
- Rice University
arxiv_id: '2605.30085'
url: https://arxiv.org/abs/2605.30085
pdf_url: https://arxiv.org/pdf/2605.30085
published: '2026-05-28'
collected: '2026-05-30'
category: Reasoning
direction: 推理可靠性 · 保形风险控制
tags:
- Conformal Prediction
- Reasoning Traces
- Prefix Certification
- Risk Control
- Process Supervision
- LLMs
one_liner: 提出 CROP 方法，为推理步骤序列提供前缀污染风险的有限样本边际控制，保留有效中间推理以提升下游修复
practical_value: '- 在多步 Agent 决策中，可用 CROP 对已执行的步骤序列进行风险认证，返回风险可控的“安全前缀”，将剩余步骤交给人工审查或更高精度的修复模块，避免全盘回滚。

  - 生成式推荐（GenRec）在生成物品序列（如购物车推荐）时，可以用类似前缀认证思路，将生成过程按步骤拆分，用 process reward model 标注风险，仅保留低风险前缀再继续生成，提高推荐列表的整体可信度。

  - 工程实现上，CROP 是 verify-agnostic 的轻量校准层，只需将任意步骤级风险评分（PRM、logits、heuristics）输入即可获得保形保证，可直接插入现有的
  LLM 推理管线，无需修改模型。

  - 实验揭示了“步骤 AUROC 高 ≠ 前缀实用性好”这一重要现象，可迁移至电商搜索排序中：离线排序指标（如 AUC）可能无法反映线上截断位置的效用，评估应直接面向最终截断策略校准。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：语言模型的推理轨迹往往是“前半段正确、后半段崩掉”，但现有不确定性量化方法要么对整个回答做二元接受/拒绝，要么单独认证每个声明，无法给出“保留哪一部分步骤是安全的”统计保证。这导致错误传播后，有用的中间推理被丢弃，下游修复缺乏可靠的起点。

**方法关键点**：
- 定义 clean-prefix certification 问题：给定一个推理实例（问题+推理步骤）和步骤级误差标注，希望在控制“保留前缀包含错误”的边际概率 ≤ α 的情况下，返回最长的连续前缀。
- 提出 CROP（Conformal Reasoning Output Prefixes）：利用任意步骤级风险代理（如 PRM 分数、似然度、表面特征），通过保形风险控制（CRC）校准一个阈值，使得超过该阈值的步骤被截断，保证前缀污染风险 ≤ α。
- 理论保证：在实例级可交换性假设下，对边际前缀污染风险提供有限样本控制，且不要求风险代理本身校准良好。
- 算法简单：对校准集计算每个阈值下的前缀污染损失，选最大可行阈值，应用到测试实例上。

**关键实验**：在 Arithmetic、GSM8K、ProcessBench、Math-Shepherd、PRMBench、PRM800K 六个过程标注数据集上评估。实验表明：
- 标准步骤级 AUROC 不能完全预测固定风险下保留的前缀长度，存在高 AUROC 但保留更少前缀的倒挂情况。
- 在 Arithmetic 上，CROP 的前缀边界偏差仅 1.1%，远低于全量拒绝（4.6%）和仅提问（95.8%），且过保留和欠保留均极低。
- 下游修复精度：在多数模型上，CROP 前缀比整段喂入或仅提问输入带来显著提升，例如在 Arithmetic 上 DeepSeek-R1-0528-Qwen3-8B 修复准确率从 78.8% 提升到 85.0%。

**核心洞见**：错误步之前保留的连续前缀是高质量可复用上下文，用 CROP 可以在统计保证下精准定位信任边界，将传统“要么全信要么全扔”的二值化决策改为细粒度安全前缀输出。
