---
title: An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender
  Systems
title_zh: 零数据对话推荐系统引导的实证研究
authors:
- Rohan Surana
- Junda Wu
- Zhouhang Xie
- Yu Xia
- Nathan Kallus
- Julian McAuley
affiliations:
- University of California, San Diego
- Netflix Inc.
- Cornell University
arxiv_id: '2504.15476'
url: https://arxiv.org/abs/2504.15476
pdf_url: https://arxiv.org/pdf/2504.15476
published: '2026-08-27'
collected: '2026-09-05'
category: RecSys
direction: 零数据CRS引导 · 合成对话数据
tags:
- CRS
- Synthetic Data
- Active Learning
- LLM
- Fine-tuning
- Zero-data
one_liner: 系统实证零数据下用评论、元数据、协同信号合成对话训练CRS，主动选择提升数据效率
practical_value: '- 新域冷启动可直接用 review、metadata、user-item logs 构造 synthetic SFT 数据，不依赖真实对话日志；生成时用目标模型
  last hidden state 选种子，比随机/popularity 省 teacher LLM calls。

  - active selection 别只当预处理：JS diversity 与 Fisher information 提供不同信息角度，metadata/CF
  信号加入表示后可进一步提升，尤其大 budget 时更明显。

  - 低资源场景合成数据可超过约 1k 真实对话，可先合成再混入少量真实数据；真实数据已很大的 ReDial 中合成增益有限，需要更严格过滤。

  - 小模型用 Full-SFT 往往比 LoRA 更能消化合成对话数据；如果 LoRA 不涨，换 Full-SFT 或检查数据质量。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
对话推荐系统通常依赖昂贵、稀缺且受隐私约束的领域对话数据。直接部署 LLM 又面临成本、知识陈旧和隐私问题。现实可用的非对话信号如评论、元数据和用户-物品交互，能否零数据引导出可用的 CRS，此前缺少系统实证。

**方法关键点**
- 定义 zero-data CRS：无任何领域对话语料，只允许 reviews、metadata、user-item interactions。
- 三阶段 pipeline：select → generate → fine-tune。用目标模型最后一个 transformer 层的 hidden states 得到种子表示，再做主动选择。
- 两种无标签选择策略：Jensen-Shannon diversity 强调分布覆盖；Fisher information 用 last-layer 近似做贪心 log-determinant 设计，强调参数信息增益。
- 对每个选中 item，采样 3 条 review 和 5 个来自 Reddit 电影推荐讨论的风格模板，由 GPT-4o 生成 query；再让 teacher 为该 query 生成 20 个 pseudo-target recommendations，形成 (query, rec list) 训练对。
- 在 Qwen2.5-1.5B、Qwen3-4B、Llama3-3B 上对比 LoRA 与 Full-SFT，并验证 NBCRS 传统模型。

**关键结果**
- domain-grounded 合成数据一致超过 zero-shot 和 naive GPT-Generated；在 INSPIRED 上 Qwen2.5-1.5B 的 Recall@1 相对 zero-shot 提升 +207.8%，而 GPT-Generated 仅 +18.8%。
- JS/Fisher 主动选择优于随机和 popularity 选择，能更省 teacher calls；popularity 选择常不如随机。
- metadata 和 CF 信号加入选择表示后带来额外提升，尤其大 budget 下更明显。
- 在 INSPIRED 约 1k 真实对话的低资源设定中，纯合成数据超过原训练集；合成+真实进一步互补；在 ReDial 大体量真实数据下合成增益很小甚至略降。

最值得记住的一句话：非对话领域信号是否有效，关键不只是“用 LLM 多生成文本”，而是先做信息量导向的种子选择，并把 metadata/CF 作为选择信号一起编码。
