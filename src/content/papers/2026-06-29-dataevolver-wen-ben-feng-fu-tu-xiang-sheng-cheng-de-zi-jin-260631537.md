---
title: 'DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image
  Generation'
title_zh: DataEvolver：文本丰富图像生成的自进化多智能体数据构建
authors:
- Siyu Yan
- Yizhen Gao
- Yilin Wang
- Dongxing Mao
- Alex Jinpeng Wang
affiliations:
- Central South University
- The Hong Kong University of Science and Technology
arxiv_id: '2606.31537'
url: https://arxiv.org/abs/2606.31537
pdf_url: https://arxiv.org/pdf/2606.31537
published: '2026-06-29'
collected: '2026-07-02'
category: MultiAgent
direction: 自进化数据飞轮 · 多智体协作
tags:
- multi-agent
- data construction
- text-rich image generation
- self-evolving
- feedback-driven
- OCR
one_liner: 将数据构建建模为反馈驱动的策略演化，利用拒绝样本的失败信号迭代改进，显著提升文本图像生成质量
practical_value: '- 借鉴“拒绝样本有价值”的理念：在推荐/搜索的样本标注或数据清洗中，错误样本不仅该丢弃，其错误原因可被结构化记录并反馈到后续的数据采集策略中，减少同类错误反复出现。

  - 多 Agent 分工模式可迁移到数据飞轮工程：Retriever（数据采集）、Verifier（质量评估）、Critic（汇总语义洞见）、Generator（合成补缺）分别对应数据链路的采集、质检、归因分析和合成增强，可直接指导推荐系统训练数据管线的设计。

  - 利用 LLM 做 Critic 进行语义级反馈总结，可以帮助发现数据分布的覆盖盲区，例如在商品文案生成或搜索词推荐中，自动识别未充分表达的语义类型，并触发针对性合成或采集。

  - 迭代构建框架本身是轻量的：不需要改变下游模型结构，只改变数据供给方式，适合在现有推荐模型训练流程中嵌入实验。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有文本丰富图像生成的数据构建多采用“爬取-过滤-冻结”静态范式，丢弃大量包含 OCR 错误、语义不匹配等有效失败信号的被拒样本，导致后续构建轮次重复同类失败模式。

**方法**：提出自进化多智能体框架 DataEvolver，将数据构建视为反馈驱动的策略演化过程。四个智能体各司其职：
- **Retriever**：采集候选样本；
- **Verifier**：为样本打质量分并标注拒绝原因；
- **Critic**：汇总轮次级反馈，生成语义反馈，发现覆盖不足的类别；
- **Generator**：基于反馈定向合成补全缺失区域。
多轮迭代中，上一轮的反馈记忆指导下一轮的数据构建，使数据分布逐步优化。

**关键结果**：在 PixArt-α 上用 0.75M 数据训练，OCR-F1 在 TextScenesHQ 上相对最强基线提升 85.3%，LongTextBench 上提升 35.3%；在 Show-o2 上也有同等迁移提升，证明方法不依赖特定生成器。
