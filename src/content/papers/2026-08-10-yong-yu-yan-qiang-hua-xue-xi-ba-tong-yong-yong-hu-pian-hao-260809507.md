---
title: Learning Preference Adaptation for Large Language Model Personalization via
  Verbal Reinforcement Learning
title_zh: 用语言强化学习把通用用户偏好适配到具体任务以提升 LLM 个性化
authors:
- Yuting Liu
- Wei Wu
- Jianzhe Zhao
- Guibing Guo
affiliations:
- Software College, Northeastern University, China
- Ant International
arxiv_id: '2608.09507'
url: https://arxiv.org/abs/2608.09507
pdf_url: https://arxiv.org/pdf/2608.09507
published: '2026-08-10'
collected: '2026-08-11'
category: LLM
direction: LLM 个性化 · 偏好适配 · 语言强化学习
tags:
- LLM Personalization
- Verbal Reinforcement Learning
- Preference Adaptation
- Meta-Learning
- Textual Optimization
- Task-Specific Compression
one_liner: 从少量样例中归纳文本重写策略，将冗长通用偏好压缩为紧凑任务相关表示，模型冻结全适配
practical_value: '- **用户画像的任务级精炼**：在搜索、推荐、广告等系统中，用户长期画像往往噪音大且与当前场景无关。可参考 AlignXada
  的做法，用一个冻结的 LLM 作为重写器，按照少量历史问答样例归纳出一条文本策略，自动把原始画像压缩为仅保留当前任务关键证据的紧凑文本，再输入下游排序/生成模型，既能节省
  token 又能避免无关信号干扰。

  - **语言强化学习调优提示或检索策略**：Verbal RL 不更新任何模型参数，只迭代修改策略文本，非常适合黑盒 LLM API 场景。在推荐解释、对话式推荐等应用里，可以仿照此法用自然语言反馈优化系统提示、检索改写规则等，低成本迭代出更有效的模板。

  - **Agent 记忆的动态重组优于简单检索**：实验表明 RAG（BM25 检索相关块）虽然也能压缩，但会破坏偏好的整体连贯性，导致性能下降。在构建智能体长期记忆时，应当考虑用重组而非仅检索的方式为不同下游任务生成任务特定的记忆视图，例如在购物助手、客服
  agent 中根据意图从完整记忆生成精简版上下文。

  - **自适应采样改善反馈质量**：策略优化时从支持集合中按“改善/退化/持续成功/持续失败”四类状态均匀采样，可提供更平衡的诊断信号，该方法可直接用于推荐系统里用少量样例调优提示词时的样例选择过程，提升策略的泛化性和稳定性。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
长期用户偏好摘要通常包含多场景信息，当下游任务（如邮件写作、商品推荐）到来时，无关内容不仅浪费 LLM 上下文窗口，还可能成为强干扰导致模型输出偏离用户真实意图。直接按任务手动拆分画像不现实，因此需要一种自动机制，能从少量任务样例中学会如何把通用偏好压缩成既紧凑又充分保留任务关键证据的适配版本。

**方法关键点**  
- **AlignXada 框架**：将偏好适配建模为学习一条可复用的文本精炼策略。策略由元学习器（冻结 LLM）生成，重写器（另—冻结 LLM）按策略把原始偏好改写成任务适配的偏好，全程不更新权重。  
- **语言强化学习优化**：从一个包含（用户画像、任务输入、期望输出）的小支持集出发，每轮先执行当前策略获得下游模型输出和评价分，再汇总成结构化自然语言反馈（平均分、失败模式等），元学习器据此生成新版策略文本，重复多轮后选择验证集最优的策略。  
- **自适应采样**：为充分利用支持集，每轮采样时按“改进/退步/稳定成功/持续失败”四个状态均匀分配名额，让反馈更均衡。  

**关键结果**  
基于 PersonaMem‑v2 和 MemoryCD 构造的复合 benchmark 覆盖 13 个任务（对话、排序、评分、生成等）和 3 个下游模型：
- 全 39 任务‑模型 cell 中 33 个得到提升，平均增益 +3.82 分；
- 精炼后画像平均仅保留原始 token 的 22.8%，且增益与保留率几乎无关（r=0.06）；
- 在 36 个 cell 中优于 RAG 基线，RAG 平均反而拉低 3.46 分；
- 忠实度审计显示 97.5% 的精炼声称在原偏好中有支撑，83.3% 的可用偏好证据被保留，说明主要进行了受控压缩和重组。

**核心洞察**  
任务导向的偏好重组远比基于查询的局部检索更有效，且用语言反馈迭代优化策略是一种训练无关、适应黑盒模型的实用范式，可直接融入个性化 Agent 的记忆管理。
