---
title: 'Highlight-Then-Summarize: Learning to Compress Evidence for Long-Context Understanding'
title_zh: 先高亮后摘要：学习为长上下文理解压缩证据
authors:
- Zhaoyuan Xia
- Qinghongbing Xie
- Yung Xiang Hue
- Jianguang Jiang
- Gaofeng Lu
- Zhenyu Jiao
- Xing Yuan
- Dai Dai
- Tong Mo
- Long Zeng
affiliations:
- Peking University
- Baidu Inc.
- Tsinghua University
arxiv_id: '2609.31382'
url: https://arxiv.org/abs/2609.31382
pdf_url: https://arxiv.org/pdf/2609.31382
published: '2026-09-25'
collected: '2026-09-28'
category: Reasoning
direction: 长上下文推理 · 证据压缩与强化学习
tags:
- Long-Context
- Evidence Summarization
- Process Reward
- GRPO
- Evidence Grounding
one_liner: 提出 Highlight-Then-Summarize：先定位证据再生成问题条件摘要，压缩长上下文并提升推理
practical_value: '- 在电商/Agent 场景中，对长商品说明、多跳用户评论、客服对话或政策条款，可让模型先输出「证据块 ID + 关键 span」再生成「问题条件摘要」，最后作答；这样既保留溯源能力，又减少无关内容对推理的干扰。

  - 借鉴 H2S-RL 的过程奖励设计：不要只奖励最终答案，把 evidence grounding、span F1、summary ROUGE-L 和结构完整性分开给确定性的
  programmatic reward；不依赖在线 LLM judge，适合离线训练和工程化。

  - 给上下文分块并分配稳定 ID 的做法很实用：在搜索/推荐系统里对长文档、商品详情、用户历史做地址化，可支持后续引用、归因和审计，成本低。

  - H2S 在 4K 输出预算下接近 16K 的表现，说明把压缩外化为显式 intermediate 比放任长 CoT 更省 token；在线上低延迟/低成本约束下，可优先考虑先压缩证据再推理的架构。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM 在长文档、多轮对话、仓库级代码等场景中，相关证据往往稀疏、分散，并淹没在大量无关内容里。只靠最后答案监督会让模型同时完成证据定位、关系整合和任务求解，容易生成冗长推理且不稳定。因此需要把「证据选择」和「证据整合」从最终答案中解耦出来。

**方法关键点**
- H2S 三段式单条自回归轨迹：Highlight 定位证据块和 span → Summarize 生成问题条件摘要 → Answer 基于摘要作答。原文档始终保留，不是剪枝而是重组上下文。
- 数据构造 H2S-Dataset：共 6,647 个样本，来自 11 个 benchmark 家族，平均上下文 43.9K tokens；通过语义分块、BM25+语义检索、原子信息需求分解和 claim 抽取构造 Evidence–Summary–Answer 监督，并用 faithfulness / coverage / answerability 三重质检。
- H2S-RL 采用 GRPO，奖励由最终答案、证据 grounding、span F1、summary ROUGE-L 和结构 gate 联合组成，对中间过程直接监督，不依赖在线 LLM judge。

**关键结果**
- H2S-14B 在七任务 H2S-Bench 上平均 32.60，超过 Qwen3.8-27B 10.17 分、QwenLong-L1-32B 5.01 分；7B 模型平均 28.56，参数不到 QwenLong-L1-32B 的 1/4。
- RL 较 SFT 再提升 4.88 分（7B）和 3.44 分（14B）。
- 消融：去掉 summary 平均掉 8.47 分（14B），去掉 evidence 掉 4.25 分；输出预算从 4K 扩到 16K 只增加 0.96 分，说明证据压缩有效而非靠更长推理。
- 动机实验：15.19K 文档加 0.46K question-conditioned summary，Qwen3.5-Flash 准确率从 72.6 升到 96.7。

**最值得记住的一句话**：压缩不是删掉原文，而是把分散证据改写成问题条件摘要，使推理在低 token 预算下更高质。
