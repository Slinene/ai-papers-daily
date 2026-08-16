---
title: How Can Rhetoric Reward-Hack AI Reviewers? Dissecting Rhetorical Sensitivity
  in AI-Based Peer Review
title_zh: 修辞如何奖励攻击 AI 评审？解剖 LLM 评审的修辞敏感性
authors:
- Ming Li
- Chenguang Wang
- Xirui Li
- Xinyue Zeng
- Dianqi Li
- Peng Shi
- Dawei Zhou
- Tianyi Zhou
affiliations:
- University of Maryland
- Virginia Tech
- MBZUAI
- University of Waterloo
arxiv_id: '2608.08975'
url: https://arxiv.org/abs/2608.08975
pdf_url: https://arxiv.org/pdf/2608.08975
published: '2026-08-09'
collected: '2026-08-16'
category: Eval
direction: LLM 评估 · 修辞敏感性
tags:
- LLM evaluation
- rhetorical sensitivity
- reward hacking
- peer review
- robustness
- scoring bias
one_liner: 揭示 LLM 评审对修辞的敏感性呈结构化层级，证据框架与新颖性立场影响最大，重写者决定变异分离而评审者决定分数效应
practical_value: '- 若业务中用 LLM 做内容质量打分、创意评审或排序（如广告文案、商品描述、评论审核），需警惕修辞偏差：证据呈现方式、新颖性措辞可能显著影响评分。可仿照论文构建内容不变但修辞正反变换的对照集，对
  LLM 评估器做敏感性审计。

  - 评估鲁棒性工程：在 prompt 中加入严格评分协议只能降低平均分，不一定降低修辞敏感性；建议增加校准步骤、集成多个评审模型或对中间分数段样本做额外人工复核。

  - 论文发现低分样本趋升、高分样本趋降，中间分数段修辞对比最清晰。在排序/评估流水线中，可重点监控中间档位的样本，对修辞敏感的特征做正则化或去偏。

  - 如果业务流程涉及“LLM 改写 + LLM 评估”的闭环，注意改写模型主要决定变体之间的分离度，评估模型决定分数波动的幅度和符号；优化时应分开诊断，而不是笼统调整整体流程。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 越来越多参与科学评价，可能存在 reward hacking——在科学内容不变时，修辞选择影响 AI 评审判断。论文系统研究这种修辞敏感性及其在不同评估条件下的变化。

**方法**：从 120 篇匿名 ICLR 2026 投稿构建 4200 篇完整论文语料。两个 LLM 重写者沿六个修辞维度（如证据框架、新颖性立场、范围框架等）进行正反方向变换，五个 LLM 评审者在标准和严格协议下评分。还测试了联合重写、递归重写、评审者引导重写。

**关键结果**：修辞敏感性结构化而非均匀。证据框架和 novelty stance 对总评的正负对比最大；scope framing 形成较弱的第二梯队；其余维度效应较小或不稳定。该层级跨人类质量水平保持，但分数移动依赖原始分数：低分趋升，高分趋降，中间范围对比最清晰。更复杂的工作流未必带来更大增益：联合重写强依赖重写者，评审者引导不总是优于未引导的二遍重写，重复重写收益递减且依赖配置。重写者主要决定相反变体之间的分离，评审者决定分数效应的大小和符号。严格评审使平均 OA 降低 1.36 分，但未一致改变修辞敏感性。
