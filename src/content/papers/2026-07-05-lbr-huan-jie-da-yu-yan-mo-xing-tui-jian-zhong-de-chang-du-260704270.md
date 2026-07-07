---
title: 'LBR: Towards Mitigating Length Bias in Large Language Models for Recommendation'
title_zh: LBR：缓解大语言模型推荐中的长度偏差
authors:
- Hongchen Li
- Bohao Wang
- Jingbang Chen
- Weiqin Yang
- Hang Pan
- Bingde Hu
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- The Chinese University of Hong Kong
- University of Science and Technology of China
- Bangsun Technology
arxiv_id: '2607.04270'
url: https://arxiv.org/abs/2607.04270
pdf_url: https://arxiv.org/pdf/2607.04270
published: '2026-07-05'
collected: '2026-07-07'
category: RecSys
direction: LLM 推荐偏差缓解
tags:
- Length Bias
- LLM-based Recommendation
- Attention Calibration
- Effective Information Length
- Constrained Decoding
one_liner: 首次识别并缓解 LLM 推荐中输入注意力偏差和输出解码偏差，提出轻量级长度感知注意力校准与有效信息长度归一化
practical_value: '- 在电商/搜索推荐中，若使用 LLM 基于文本描述生成候选商品，可借鉴 **有效信息长度归一化** 改善排序分数：利用商品标题
  Trie 树约束的节点分支数计算 token 信息量，归一化时使用信息长度而非 token 长度，避免偏好短或长商品，一站式解决长短标题 bias。

  - 在 LLM 输入 prompt 中，不同长度商品描述会导致长商品获得过多注意力，可借鉴 **长度感知注意力偏移** 方法：根据商品 token 长度在注意力
  logits 中加入偏移（如 δ(l) = -log(a·l+b)），仅需两个额外参数，几乎不增加训练开销。

  - 对于已采用约束解码（前缀树）生成有效商品的 LLM 推荐系统，LBR 可插件式集成，无需改动模型结构，实验显示平均 NDCG@5 提升 16.82%。

  - 在搜索词推荐或 query 改写场景，也可利用 query 模板的 Trie 结构计算信息量，改进候选排序公平性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机：** LLM 推荐将物品表示为文本描述，不同物品标题长度差异悬殊，导致两个隐蔽的长度偏差：**输入侧**，长描述物品在自注意力中积累更多注意力重量，扭曲用户偏好建模；**输出侧**，累加对数似然天然偏好短物品，而常规长度归一化又因忽略前缀树（Trie）约束下 token 信息量差异，反而偏袒长物品。现有方法未能有效应对，影响推荐准确性与公平性。

**方法关键点：**
- **长度感知注意力校准 (LAAC)**：在注意力 logits 中加入长度相关偏移项 𝛿(𝑙)=−log(𝑔(𝑙))，𝑔(𝑙) 建模为线性函数，端到端学习，抵消长物品的注意力优势，使期望累计注意力与长度无关。
- **有效信息长度归一化 (EILN)**：基于 Trie 分支因子定义 token 信息量（Hartley 熵），计算有效信息长度 𝑈(𝑦)，替换原始 token 长度进行分数归一化，并加权 token 对数概率，等价于每比特信息的平均对数似然。

**关键实验：** 在 Amazon Toys、Office、Books 数据集上，以 LLaMA3.2-3B 为骨干，对比 BIGRec、LLaRA 及多种去偏基线（D3、CFT、S-DPO 等）。LBR 在 BIGRec 和 LLaRA 上平均 NDCG@5 提升 16.82%（最高 26.79%），显著降低推荐分布与真实分布的方差，注意力权重几乎与物品长度无关，且训练/推理开销几乎可忽略。

**核心理念：** 轻量、模型无关的去偏框架 LBR 通过校准注意力和信息论归一化解码分数，有效消除 LLM 推荐中的长度偏差，提升准确性与公平性。
