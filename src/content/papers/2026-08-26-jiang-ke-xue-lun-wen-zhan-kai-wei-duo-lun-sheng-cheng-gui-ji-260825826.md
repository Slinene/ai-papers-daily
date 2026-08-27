---
title: Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued
  Pre-Training
title_zh: 将科学论文展开为多轮生成轨迹用于继续预训练
authors:
- Qiankai Xu
- Qiguang Chen
- Zixin Su
- Wenhao Huang
- Yue Gao
- Jiaheng Liu
- Ge Zhang
affiliations:
- ByteDance Seed
- Nanjing University
- Evolvent AI
arxiv_id: '2608.25826'
url: https://arxiv.org/abs/2608.25826
pdf_url: https://arxiv.org/pdf/2608.25826
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: 合成写作轨迹 · 继续预训练
tags:
- Synthetic Data
- CPT
- Writing Trajectory
- Scientific Papers
- Long Context
- SFT
one_liner: 把 arXiv 论文展开为“写作请求→全局计划→逐节思考→正文”多轮轨迹，构建 60B token CPT 语料，提升写作与长文阅读
practical_value: '- **真实业务长文本可反向构造“写作过程”数据，不改写内容**：电商商品详情页、广告落地页、搜索导购长文、Push 文案等结构清晰的长文本，保留原文为答案/正文，反向生成用户
  request + 全局规划 + 每段写作前 deliberation，适合 CPT 或 SFT，能提升文案生成、摘要、长文阅读，同时把事实锚定在原文减少幻觉。

  - **结构化文档拆成多轮轨迹，让模型学会规划与分段生成**：按 section/block 拆分，在每段正文前插入 pre-writing deliberation，比“整篇+一段思考”更细粒度；对推荐理由生成、商品对比、报告生成等任务，可把商品参数、卖点、用户评论作为不同
  section 来构造数据。

  - **数据构造不依赖大模型，用 4B/9B 开源模型即可**：论文显示 4B 生成器下游效果最好，且更难拟合的 synthetic data 更有训练价值；业务上可以低成本大批量生产
  trajectory 数据，不必上最强 API。

  - **评估也锚定 held-out 真实文本，并生成 rubric/checklist**：可借鉴到业务评测：从近期未用于训练的真实商品/query/文章抽取，让
  LLM 反向生成题目 + 评分规则，用代码可检查的 checklist 做格式/事实约束，配合 LLM judge 打分。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：高质量人类文本接近耗尽，合成数据需求剧增。已有工作多在短网页文本上重构局部思考，缺乏文档级结构；科学论文结构统一、密度高、真实写作过程存在，适合把“反向重构生成过程”的范式提升到文档级。

**方法关键点**：
- 共享预处理：清洗 arXiv LaTeX 正文，去掉附录/引用/图表，结构过滤，去重，并按时间窗口划分训练与评测集。
- CPT 轨迹：固定论文正文/摘要原文，反向合成写作请求、全局计划、逐节 pre-writing deliberation；将论文展开为多轮轨迹，30B token 原文扩展为 57-60B token，median 长度从 11K → 28-29K。
- 生成器使用 Qwen3.5-4B/9B/27B，温度 1.0，8K token budget；不同生成器风格不同。
- SFT：反向固定 passage 为答案，生成任务 prompt 和思维；29 种任务类型，得到 200K 样本。
- PAW-Bench：从 held-out 论文生成 task + rubric/checklist；2,940 个任务，15 种类型，时间窗晚于训练数据，避免泄漏。

**关键实验**：基于 Qwen2.5-7B，CPT 50B tokens（30B trajectory + 20B FineWeb-Edu）对比 FineWeb-Edu-only 和 Plain-Paper 两个控制组；SFT 用 DeepWriting 或混合 Our-Mixed。结果：Our-Data-4B + DeepWriting 写作 Avg 54.34 vs 基线 51.90；PAW-Bench rubric 59.47 vs 55.42；Plain-Paper 无提升。推理不降：OpenThoughts SFT 后 Avg 46.82 vs direct SFT 46.32；长文阅读 Qasper、LongBench v2 均有提升。生成器大小影响很小，4B 反而最佳；更难拟合的 4B corpus 下游收益最高。

**最值得记住的一句话**：保持真实文本不变，反向重构其生成过程，将扁平文档展开为多轮轨迹，是提升写作与长文能力的有效数据策略——且小生成器足够，训练损失更高的合成语料反而更有价值。
