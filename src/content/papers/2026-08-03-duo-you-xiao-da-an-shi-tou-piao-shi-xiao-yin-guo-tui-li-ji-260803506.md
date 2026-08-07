---
title: 'When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K
  Causal Reasoning in LLMs'
title_zh: 多有效答案时投票失效：因果推理中基于符号验证的最佳选择
authors:
- Omatharv Bharat Vaidya
- Connor Thomas Jerzak
- Zayne Rea Sprague
- Fangcong Yin
- Nhat Ho
affiliations:
- The University of Texas at Austin
- New York University
arxiv_id: '2608.03506'
url: https://arxiv.org/abs/2608.03506
pdf_url: https://arxiv.org/pdf/2608.03506
published: '2026-08-03'
collected: '2026-08-07'
category: Reasoning
direction: 因果推理 · 符号验证驱动的LLM答案选择
tags:
- Causal Reasoning
- Self-Consistency
- Symbolic Verification
- LLM
- Best-of-K
one_liner: 提出 CALVER，用因果公理的符号验证器替代投票，在允许多个因果有效答案的推理中准确率大幅提升。
practical_value: '- **因果决策中的答案聚合**：在电商推荐系统的因果推断（如折扣策略效果、用户流失原因）中，用 CALVER 的符号检查替代多数投票，可避免因因果图误解导致的一致错误答案胜出，提升离线分析和策略制定的可靠性。

  - **从文本构建因果图的验证**：当用 LLM 从用户评论、商品描述或运营报告中抽取因果结构时，将 CALVER 作为轻量级后验验证器，对多个抽取结果按公理正确性评分并选最优，无需额外训练，CPU
  毫秒级可运行，适合实时管道。

  - **Agent 因果决策的稳健性**：在智能客服或推荐对话 Agent 中集成 CALVER，对 Agent 生成的因果解释（如“为什么推荐该商品”）进行符号级验证，避免因采样偏差给出看似合理但因果颠倒的解释，提升用户信任与解释质量。

  - **ATE 估计的阈值决策**：在广告因果归因或促销效果评估时，用 CALVER 对 LLM 生成的平均处理效应推理进行打分排序，替代简单置信度阈值，可更准确地识别有效干预，减少误判。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：自一致性（self-consistency）假设投票领先的答案最可靠，但在因果推理中容易失败：多次采样可能重复同一混淆错误，且当多个因果有效的答案并存时，投票会碎片化，导致无效答案胜出。

**方法关键点**：提出 CALVER（Causal Axiom-Level VERification），一种免训练的符号验证器。它对每条推理链的结构化表示进行评分，依据 Pearl 的因果准则——d-分离、后门调整和干预操作——检查公理正确性，最终选择得分最高的候选答案，无需参考答案。

**关键结果**：在 CLEAR 的“找到一有效答案”任务（允许多个图有效答案）上，CALVER 准确率达 42.1%，而多数投票、奖励模型、LLM 评判员和模型置信度均约 30%，即使将 LLM 评判员扩至 72B 参数也无法缩小差距。在审计的干净核心子集中，CALVER 选出的 21 个图有效解中有 11 个与基准标答不同但仍满足查询谓词，说明其能发现标答之外的合理答案。优势随采样预算增大而扩大，且能复现于 10 个不同的已发布贝叶斯网络、另一模型家族、以及需要从文本构建图的设置中。CALVER 还能改善阈值化的平均处理效应决策，准确度接近真实值；可推广至逻辑推理的真值表检查；评分在 CPU 上仅需毫秒。方法唯一所需是因果结构（直接给出或从文本构建），凡满足此条件，即可用因果有效性聚合选择。
