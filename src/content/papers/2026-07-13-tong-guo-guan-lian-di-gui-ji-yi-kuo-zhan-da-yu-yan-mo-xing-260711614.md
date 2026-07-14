---
title: Extending LLM Context via Associative Recurrent Memory
title_zh: 通过关联递归记忆扩展大语言模型上下文
authors:
- Gleb Kuzmin
- Ivan Rodkin
- Aydar Bulatov
- Yuri Kuratov
- Lyudmila Rvanova
- Mikhail Katkov
- Ilia Sochenkov
- Misha Tsodyks
- Timothy Baldwin
- Mikhail Burtsev
affiliations:
- MBZUAI
- Lomonosov Moscow State University
- Weizmann Institute of Science
- Institute for Advanced Study, Princeton
- London Institute for Mathematical Sciences
arxiv_id: '2607.11614'
url: https://arxiv.org/abs/2607.11614
pdf_url: https://arxiv.org/pdf/2607.11614
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: 递归记忆增强的 LLM 长上下文扩展
tags:
- Associative Memory
- Recurrent Memory
- Long Context
- Transformer
- Efficiency
- Curriculum Learning
one_liner: 提出 ARMT 训练方案，在长文本任务中用 30% 更少计算量保持性能并泛化到更长序列
practical_value: '- **长序列用户行为建模**：在电商推荐中，可利用 ARMT 以恒定内存处理超长用户交互序列（如跨月行为），突破原生 Transformer
  的上下文限制，且 FLOPs 降低 30%，适合线上 RT 服务。

  - **合成数据与课程学习策略**：面向特定领域的 LLM 微调（如商品长描述生成、多文档促销文案），可借鉴其合成长文本 + 逐步延长的课程学习方案，稳定提升长上下文泛化。

  - **选择性记忆集成**：在推荐精排或生成式推荐模型中，仅部分中间层插入关联记忆模块，平衡额外计算开销与长程依赖捕捉，可作为模型架构渐进增强的思路。

  - **分布外长度泛化**：训练时使用有限长度数据，推理时自动泛化到更长序列，对广告竞价中实时拼接的多源长特征流处理有参考意义。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：标准 Transformer 处理长上下文的计算和内存成本随序列长度平方增长，限制 LLM 在需要整合数十万 token 信息的长文档 QA、多轮对话等应用中的实用性。ARMT（Associative Recurrent Memory Transformer）通过恒定内存消耗的递归记忆机制，有望突破这一瓶颈。

**方法关键点**：
- 构建两个领域特定的长上下文数据集（如技术报告、长对话），用于模拟实际微调场景。
- 设计全套 ARMT 训练方案：在原有模型基础上继续预训练，利用合成数据生成工具扩充长文本样本，引入课程学习由短到长逐步增加序列长度，并在模型中间某几层选择性集成关联记忆模块，避免全层改动带来的资源开销。
- 采用类似“压缩-回忆”的注意力和记忆更新机制，使记忆状态随时间步递归传递，保持内存占用量恒定。

**关键结果**：
- ARMT 增强的模型能处理远超原始上下文窗口的输入（如从 8K 扩展到 32K token），且性能不低于窗口内基线。
- 对从未见过的更长序列（分布外长度）泛化能力显著优于无记忆的变体。
- 在原始上下文窗口内，ARMT 模型减少约 30% FLOPs，保持同等效果，效率优势明显。
