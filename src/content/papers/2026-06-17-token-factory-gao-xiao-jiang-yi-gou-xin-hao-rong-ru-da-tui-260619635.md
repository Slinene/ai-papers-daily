---
title: 'Token Factory: Efficiently Integrating Diverse Signals into Large Recommendation
  Models'
title_zh: Token Factory：高效将异构信号融入大推荐模型
authors:
- Xilun Chen
- Shao-Chuan Wang
- Baykal Cakici
- Lukasz Heldt
- Lichan Hong
- Raghu Keshavan
- Aniruddh Nath
- Li Wei
- Xinyang Xi
affiliations:
- Google
arxiv_id: '2606.19635'
url: https://arxiv.org/abs/2606.19635
pdf_url: https://arxiv.org/pdf/2606.19635
published: '2026-06-17'
collected: '2026-06-19'
category: RecSys
direction: 多模态特征压缩与 soft token 融合
tags:
- Soft Token
- Feature Compression
- Large Recommendation Models
- PLUM
- YouTube
- Generative Retrieval
one_liner: 把传统稠密/稀疏特征压缩为 soft token，大幅缩短 prompt 并提升训练与推理效率，保持质量
practical_value: '- **特征压缩到 soft token 以控制 prompt 长度**：对于电商推荐中的用户行为序列（点击、加购、下单），每步行为可携带大量稠密特征（停留时长、转化率、价格等），用
  MLP 或轻量 Transformer 将每个行为压缩为 1 个 soft token，整段历史压缩为固定数量 token（如 200 条历史 → 200 个
  token），避免文本化导致的序列爆炸。

  - **固定预算的 prompt 设计**：为不同类别的特征（用户侧、候选商品侧、上下文）分别设计 Token Maker，各自输出固定数量的 soft token，保证
  prompt 总长度确定，有利于显存规划和 prefix caching。用户侧 token 在一次请求内可复用，显著降低推理延迟。

  - **序列压缩的两种工程方案**：当历史行为极长（如数千条），可先用 MLP 直接沿序列维度降维（如 500 → 50），或使用基于注意力池化的 K 项合并策略（每
  K 个行为合并为 1 个 token），在召回或粗排中节省计算，并已验证 AUC 仍有正向收益。

  - **特征融合优于丢弃**：实验表明，即使序列已被压缩，在 soft token 中融合更多的稠密/稀疏特征（如商品类目、价格档位）仍能提升 CTR 预估；在召回侧，融合充分特征的
  soft token 使新视频的 Unique Impressions 提升 67%，说明压缩不意味着牺牲信息，而是用更好的嵌入空间保留信号。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业界大推荐模型（LRM）通常依赖语义 ID 和文本化传统特征，但直接文本化会导致 prompt 极长，显存和计算开销过大。例如在 YouTube 视频推荐中，一条观看历史若用文本 SID 加稠密信号表示可占 10+ tokens，长历史直接压垮 Transformer。必须找到一种既保留信息又控制长度的方法。

**方法**
论文提出 **Token Factory** 框架，核心是 **Token Maker**：将任意异构特征（稠密值、稀疏 ID、嵌入向量）通过可学习的映射（MLP 或更复杂网络）转换为固定数量的 **soft token**（直接作为 Transformer 的输入嵌入）。
- **WH Token Maker**：把一条观看历史的多种特征（SID、频道、时长等）压缩为 1 个 soft token，整段历史变成 token 序列。
- **Query Token Maker** 与 **Candidate Token Maker**：分别处理用户级与候选商品级特征，输出固定数量软 token，并在推理时利用 query 侧 token 的缓存复用。
- **序列进一步压缩**：可通过 MLP 沿序列维度降维（如 500 条 → 50 个 token），或注意力池化每 K 个行为合并为 1 个 token，适应极长历史。

**实验**
在 YouTube PLUM 框架上的排序和生成式检索任务验证。
- 排序（CTR 预估）：Baseline 用文本 SID，每条历史 12 tokens，总 prompt 1536 tokens；Token Factory 将历史压缩为每条 1 token，总 prompt 降至 480 tokens。同样 batch size 下，初期 AUC 略低，但 1.5M steps 后追平，训练速度提升 200%；增大 batch size 后，AUC 反超 baseline。
- 生成式检索（下一视频 SID 预测）：Token Factory 将 prompt 从 768 压缩至 256 tokens，召回率 +2.0%；线上实验 Unique Impressions +16.8%，其中一天新鲜视频的曝光 +67.1%，同时 Satisfied Watch Time +0.05%。
- 消融实验：固定 480 tokens 时，soft token 相比文本 SID 能容纳更多历史，且融合更多特征的 soft token 优于仅用 SID 的版本；将历史从 200 扩至 500 并压缩为 30 tokens，AUC 再提升 0.08%。

**核心观点**
异构传统信号通过 Token Factory 映射为 soft token，不仅能解耦 prompt 长度与特征数量，还能通过端到端训练让 Transformer 更均匀地关注各类信号，消除文本化导致的注意力冗余，实现高效且高质量的推荐。
