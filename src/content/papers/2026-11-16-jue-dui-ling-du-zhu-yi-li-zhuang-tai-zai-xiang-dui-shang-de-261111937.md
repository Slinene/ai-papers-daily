---
title: Attention at Absolute Zero
title_zh: 绝对零度注意力：状态在项对上的零温读取高阶注意力层
authors:
- Mostafa &#39;Neo&#39; Mohsenvand
affiliations:
- MIT Media Lab
arxiv_id: '2611.11937'
url: https://arxiv.org/abs/2611.11937
pdf_url: https://arxiv.org/pdf/2611.11937
published: '2026-11-16'
collected: '2026-11-19'
category: Reasoning
direction: 零温高阶注意力 · 长度外推与关系推理
tags:
- zero-temperature attention
- higher-order attention
- length extrapolation
- relational reasoning
- CLRS-30
one_liner: 构建状态位于 item 对上的高阶注意力层，以零温度读取 witness 并只传递计数比较比特，在长度外推与关系推理上远超软注意力
practical_value: '- 在用户长期行为序列建模中，可尝试用零温 hard selection（max + tie count）替代 soft attention
  聚合，避免长序列下权重分散，提升长度外推稳定性；tie count 可保留不确定性。

  - 高阶成对状态适合建模关系型特征，如商品共现、替代/互补、用户-商品图中的路径推理，可将 pair state 作为额外特征或辅助任务。

  - 只传递比较计数的离散 bits，利于工程上做量化、缓存和可解释性；在线推理时减少浮点状态，便于规则抽取与验证。

  - 弱监督/仅从答案训练的思路可用于冷启动或标注稀缺场景，如只利用用户点击/转化答案学习关系判断，不依赖逐条标注。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：软注意力随输入规模增大出现三个失效模式：权重分散到更多候选、学到的分数无法分辨逐渐缩小的差距、soft state 在循环中漂移。

方法：该高阶注意力层把状态放在 item 对 (a,b) 上；对每第三个 item k 作为 witness，通过两条腿 (a,k) 与 (k,b) 评判。以零温度读取，保留最佳 witness 及并列数量，只传比较这些计数的比特；每轮从输入和比特重建 pair state；仅从答案训练。三个设计分别对应消除三种失效。

结果：最大检索中，比训练集大 1000 倍的集合上 10 个种子至少 99.95% 正确，soft count 版本在 4096 items 掉到 42%。CLRS-30 无 hints，一般形式（一半通道零温、嵌入数字、携带实值状态）超过最佳已发表模型（部分任务用 hints）；全冷层在 9/12 个仅依赖比较的任务上全部测试输入正确。从 yes/no 答案学习 2-SAT 和二染色在 500 变量精确，奇偶方程不能表达。旁置冻结 7B LM，1000 条语句的家庭关系链精确，训练仅 16 条，模型单独 44%；有限权重检查证明每个块的正确性在所有尺寸上。CLUTRR 给定图，5-10 关系全部故事正确，学得 62 条规则；从文本，冻结模型、无手写规则、只训练小 read-in，将开放 7B 模型从 33% 提升到 65%，超过除前沿推理模型外无手写规则系统。
