---
title: 'AGR: Agentic Generative Retrieval with Tool-Augmented Search'
title_zh: AGR：工具增强搜索的智能体生成式检索
authors:
- Ming Yang
- Yaqi Yin
- Zhibo Wang
- Xiaoze Jiang
- Jingwei Zhuo
- Chao Zhang
- Quanzhi Zhu
- Weiguo Zheng
- Liang Zeng
- Yunfeng Zhao
affiliations:
- Fudan University
- Kuaishou Technology
arxiv_id: '2610.26831'
url: https://arxiv.org/abs/2610.26831
pdf_url: https://arxiv.org/pdf/2610.26831
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式检索 · Semantic ID 工具增强
tags:
- Generative Retrieval
- Semantic ID
- Tool-Augmented
- Feature Injection
- Agentic Retrieval
- Online A-B
one_liner: 把异构特征封装为可调用工具，按需在 SID 解码中注入观察 token，实现请求与层级自适应的生成式检索
practical_value: '- 将用户长期行为、意图、位置、新鲜度等特征封装为 tool token + observation token，在 beam
  search 每个候选前缀上按需触发；不确定分支（如电影 vs 游戏）才调用对应工具，避免把全量特征塞进 prompt，既可降噪声也可省 serving 成本。电商搜索/推荐生成式召回中，可对用户历史点击序列、实时意图、价格敏感度、库存/时效做同样工具化。

  - 训练数据构造的 when/where 规则可直接复用：只用 target 侧与请求侧一致且未显式出现的特征做正样本；计算 ρ_i = log P(同属性 item
  | prefix) 的增量，选信息增益最大的 SID 深度插入工具；sequential 工具用 Vote（前缀匹配投票）近似最大化预测增益，工程实现简单。

  - 长行为序列压缩为单个 observation token 的 Vote/Attn 方案值得抄：对比直拼 400 个 GSU token，Recall@50
  基本持平（0.3237 vs 0.3241），训练时间降 81.8%，serving GPU 降 42.9%，适合有长用户行为序列但不能承受长 prompt 成本的场景。

  - 两阶段训练 + 对新增 tool token 的 loss 动态缩放 α_k（用 SID vs tool 难度比 clip 到 [0,1]）能稳定扩工具，避免破坏已学好的
  SID 表示；这为线上迭代新增特征/工具提供低风险路径。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业生成式检索依赖大量异构特征，但现有静态特征注入要么全量编码（成本高、噪声大），要么按固定方案注入，无法回答“何时注入”和“注入到 SID 哪个层级”。特征效用随请求和 decoding 深度变化，静态方案容易在 feature-conflicting 样本上提升 PPL，且信号无法集中在最该起作用的层级。

**方法关键点**
- AGR 把特征封装为工具，词汇表扩展为 SID ∪ tool token ∪ observation token；模型在解码时可发 tool token 触发外部函数，返回 observation token 注入下一步，不增加 autoregressive context 长度，每个 beam path 有最多 M 次工具调用。
- 工具分两类：structured feature tools（意图、位置、新鲜度等离散属性，映射为 learnable token）与 sequential feature tools（用户行为序列 GSU，用 Vote/Attn 压成单个 token）。
- 训练数据构造遵循“when/where”原则：仅保留 target 侧与请求侧一致且特征未显式出现的 (t,i) 样本；用 ρ_i = log P(同属性 item | prefix) 的增量选择信息增益最大的深度，sequential 工具用 arg min ρ_i。
- 两阶段训练：先 SID pretraining，再做 tool-augmented fine-tuning；对新增 tool token 的 loss 用 α_k 动态缩放，防止不稳定。

**关键实验**
在快手工业搜索、Qilin、JDSearch、KuaiSAR 上，对比 TIGER、TIGER Distill Teacher、UniSearch、GLASS、GEMs。AGR Recall@50 相对 TIGER 提升 6.4%～14.0%，MRR@50 提升 5.2%～19.7%；工业集 Recall@50 +14.01%。在线 A/B：Relevance +0.205%，Query Reformulation Rate -0.690%，Search Penetration +0.060%。GSU 工具对比直拼 400 tokens：训练时间 -81.8%，serving GPU -42.9%。

**一句话记忆**：把特征注入变成模型可自主调用的工具，使生成式检索从“被动生成 SID”升级为“对 item 和 feature 的联合决策”。
