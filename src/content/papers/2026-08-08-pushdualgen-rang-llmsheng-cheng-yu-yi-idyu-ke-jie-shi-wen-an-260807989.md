---
title: 'PushDualGen: Enabling LLMs to Generate Semantic IDs with Interpretable Copy
  for Industrial Push Recommendation'
title_zh: PushDualGen：让LLM生成语义ID与可解释文案的工业推送推荐框架
authors:
- Manjia Lin
- Da Li
- Yan Wang
- Yong Jin
- Zheming Ding
- Wei Yuan
- Lei Yan
- Yanan Xia
- Lu Zhang
- Fan Yang
affiliations:
- Kuaishou Technology, Beijing, China
arxiv_id: '2608.07989'
url: https://arxiv.org/abs/2608.07989
pdf_url: https://arxiv.org/pdf/2608.07989
published: '2026-08-08'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Push Recommendation
- Semantic ID
- LLM
- Generative Recommendation
- Interpretability
- Industrial Deployment
one_liner: 先生成SID再生成可跳过解释的轻量框架，在快手十亿用户推送中有效播放率+8.5%，不满意度-37.7%
practical_value: '- **并行 SID 构建**：采用多个独立码本并行量化，避免残差 SID 的误差累积与层级依赖，可直接用于商品/内容的多粒度高压缩表示

  - **SID 与 LLM 对齐**：通过 Text2SID 和 SID2Text 双向任务微调，并冻结原词表只训练新增 SID token embedding，轻量且稳定，适合将推荐系统离散索引注入
  LLM

  - **多 token 绑定策略**：合并高频 n-gram 与语义原子实体为单 token，降低推理序列长度，在生成推荐文案或搜索词时可显著压缩成本

  - **生成信号与召回融合**：将 LLM 生成的 Top‑N SID 编码成向量与用户特征融合后做 ANN 检索，可提升冷启动物料曝光与长尾覆盖率，对电商冷启动物品召回有直接参考'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
推送推荐须主动触达，一旦推荐偏差会直接引发用户不满，因此对准确性与可解释性要求极高。先前 OneRec‑Thinking 在生成 SID 前引入 CoT 以提供推荐理由，但额外解码开销使其难以满足十万 QPS 级低延迟需求。本文提出 **PushDualGen**，目标是兼顾推理效率与可解释性。

## 方法关键点
1. **并行 Semantic ID (SID) 构建**：使用 8 个 learnable compression token 从多模态编码器获得并行嵌入，各自用 K‑means（K=512）独立量化，避免残差 SID 的层级误差累积，每个视频压缩为 8 个 token。
2. **场景感知 SID 适配**：注册特殊 token 扩展 LLM 词表，通过 Text→SID 与 SID→Text 双向任务在 Qwen3‑0.6B 上微调，让 LLM 理解并生成 SID，仅训练新增 SID embedding，冻结原词表。
3. **个性化 SID 与文案生成**：输入用户交互历史、画像等，模型首先生成目标视频的 SID，随后可选择性生成推荐理由文案（copy），两者用 special token 分隔；训练目标为 L_SID + λ·L_Copy。采用多 token 绑定将高频 n‑gram 与实体合并为单 token 以降低推理序列长度。
4. **表征融合在线服务**：将生成的 Top‑20 SID 编码为向量 e_s，与用户特征向量 e_u 融合后做 ANN 检索，使生成式信号直接参与召回。

## 关键结果
在快手 1.5 亿用户 14 天 A/B 测试中，相比原有的级联推荐服务：
- 有效播放率相对提升 **+8.50%**，不满意度相对下降 **‑37.70%**
- 推送点击 PV +0.43%，DAU +0.05%
- 消融实验：去掉 SID 适配阶段 Pass@1 从 0.335 降至 0.319，并行 SID 替换为残差 SID 也导致性能下降
- 长尾视频曝光比例从 23.2% 提升至 24.1%，优化了内容生态

> **最值得记住**：PushDualGen 将解释生成放在 SID 之后，既可跳过又无需增加核心推理延迟，是工业生成式推荐落地时平衡性能与效率的有效范式。
