---
title: Knowledge Acquisition During Pre-training? Large Language Models Learn Better
  With Auxiliary Views
title_zh: 预训练中知识获取：辅助视图让 LLM 学得更好
authors:
- Joseph Lee
- Yidi Huang
- Dokyoon Kim
- Shu Yang
- Li Shen
affiliations:
- University of Pennsylvania
arxiv_id: '2609.04180'
url: https://arxiv.org/abs/2609.04180
pdf_url: https://arxiv.org/pdf/2609.04180
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: LLM 预训练数据表示与知识获取
tags:
- LLM pre-training
- auxiliary views
- data diversity
- knowledge acquisition
- token budget
- paraphrasing
one_liner: 辅助视图（知识重构）在固定 token 预算下比重复更能提升 LLM 知识获取，且不依赖强 teacher 生成
practical_value: '- 在电商/推荐场景构建训练数据时，不要只重复原始商品描述或用户评论，可引入多种辅助视图（如改写描述、属性问答、用户评价总结、知识图谱陈述）来覆盖同一知识的不同表述，提升模型对商品知识的记忆与推理。

  - 固定 token 预算下，优先增加辅助视图而非同文档重复。例如在微调商品理解模型时，将重复样本的 budget 分配给同一商品的不同表述（不同风格、不同角度），能更高效利用
  token，尤其对事实类属性（品牌、成分、适用人群）的 recall 有提升。

  - 辅助视图的生成不依赖强 teacher 模型，所以业务中可以用低成本 LLM 或规则模板生成多样化视图，无需昂贵的 GPT-4 级别 teacher，也能获得知识学习增益。

  - 预训练或领域继续训练时，数据多样性不足（同一商品反复出现相同描述）可能导致知识获取低效；应控制重复度，增加表述多样性。这验证了数据多样性在推荐领域大模型训练中的价值，可指导数据清洗和配比策略。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：现有预训练研究多关注语料层面特征（去重、过滤、质量、多样性），但忽略了知识表示方式这一根本问题。文章提出 auxiliary views（知识的不同表述/重构）对 LLM 知识获取有因果性帮助，并通过受控实验隔离其效应。

方法关键点：设计多组受控预训练实验，固定 token 预算，比较源文档、改写文档（paraphrase）与加入辅助视图（auxiliary views）的混合训练。关键操作：把原本分配给文档重复的 tokens 转移到辅助视图；变化 batch size、teacher 模型强度；区分 factual recall 与 inference 两类知识探究；通过 layer-wise biases 和 compression 分析机制。

关键结果：重复对知识获取是必要的，但仅靠同文档重复低效；将 token 预算从重复分配到辅助视图，在固定预算下提升学习效果，即使对事实性 recall 也有效；辅助视图的有效性不依赖生成它们的 teacher 模型强度；辅助视图有助于弥补先验知识缺口，对 contextual 和 foundational 知识形式均有帮助；机制上表现出层间偏差和压缩变化。图 1 显示在 OLMo-2-32B 上，Para. 9 + Aux 混合相比 Source-only 和 Para. 9 在 factual MCQA、inference MCQA 和 probes 上全面提升。
