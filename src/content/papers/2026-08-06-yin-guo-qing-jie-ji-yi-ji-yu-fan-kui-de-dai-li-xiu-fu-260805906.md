---
title: Causal Episodic Memory for Feedback-Driven Agent Repair
title_zh: 因果情节记忆：基于反馈的代理修复
authors:
- Khang Nhat Hoang Vo
- Tam Minh Chu
- Anh Trac Duc Dinh
- Thuyen Vinh Ha Bui
- Tho Quan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Ho Chi Minh City University of Technology (HCMUT)
arxiv_id: '2608.05906'
url: https://arxiv.org/abs/2608.05906
pdf_url: https://arxiv.org/pdf/2608.05906
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 反馈驱动修复 · 因果记忆
tags:
- Causal Memory
- Dual-Polarity
- Text-to-SQL
- Training-Free
- Hybrid Retrieval
- Failure Repair
one_liner: 利用双极性因果记忆与类型条件检索，使冻结LLM在修复时复用过往成功修正，提升Text-to-SQL准确率
practical_value: '- 电商对话代理或搜索助手可将每次修复后的最终成功方案存入正例记忆，同时记录曾尝试但无效的修改方向作为负例，后续相似问题直接检索复用，避免重复推理。

  - 在推荐系统的生成式修复（如商品推荐查询改写、筛选条件修正）中，可引入粗粒度失败类型分类器（如“意图理解错误”、“约束冲突”），据此条件化检索历史案例，提升修正速度与准确率。

  - 采用混合检索（BM25词汇匹配+稠密向量相似）来召回相关历史经验，既能捕捉表层词重叠，又能挖掘语义相近的跨场景模式，适用于电商Agent的案例库构建。

  - 无需模型更新，仅靠记忆即插即用，适合快速迭代的线上代理系统，特别适合在推荐对话、售后引导等需持续从错误中学习的场景部署。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM代理在利用外部反馈进行自我修复后，往往丢弃最终成功的修正方案，导致后续相似问题需重新试错。本文研究如何在不更新参数的情况下，将已完成的修复成果传递给未来的Text-to-SQL任务，提高代理的修复效率。

**方法**：提出MERIT，一个无训练代理。核心是维护**双极性情节记忆**：正例记忆存储经oracle验证的最终修正SQL；负例记忆记录曾尝试但无效的修改方向。修复时，按**因果时序**（仅允许检索在发起查询前已完成修复的记忆），通过确定性分类器对当前失败进行粗粒度类型标注，再依据类型条件化**混合检索器**（BM25+稠密向量）召回相关正/负例，最后由冻结LLM参考检索结果生成新的修复尝试。

**结果**：在Spider测试集上，执行准确率从无记忆修复的66.34%提升至69.79%（BIRD上从47.35%到48.44%）。Spider上的提升统计显著，BIRD上信号较弱。消融显示负记忆贡献有限，类型条件与混合排序的价值随数据集变化，schema局部经验提供最一致增益。
