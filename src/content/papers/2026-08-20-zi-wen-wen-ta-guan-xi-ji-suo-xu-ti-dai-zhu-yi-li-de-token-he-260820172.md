---
title: 'Ask Self, Ask Others: Relation Is All You Need'
title_zh: 自问问他：关系即所需——替代注意力的 token 混合新范式
authors:
- Yuting Ge
- Pengju Yang
- Mingkai Nie
affiliations:
- City University of Hong Kong
- Jilin University
- National University of Singapore
arxiv_id: '2608.20172'
url: https://arxiv.org/abs/2608.20172
pdf_url: https://arxiv.org/pdf/2608.20172
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 替代 Attention 的 token-mixing 基础架构
tags:
- Relation
- Token Mixing
- Self-Exchange
- FlashRelation
- Linear Relation
- Decoder-only LLM
one_liner: 提出 Self-Exchange Relation 算子，将 token 混合拆成先建关系再分配信息流，在 10M/30M/100M 语言模型上
  NLL 全面优于 MHA
practical_value: '- 可借鉴显式 Self/Exchange 分解：在用户行为序列建模（如点击序列、曝光序列）中，可把 token 混合拆成 Self（自身历史/当前意图）和
  Exchange（与其他 item 的关系）两阶段，先构造关系再归一化，可能更利于可解释和稀疏控制。

  - FlashRelation 的 tile 化扫描 + 只缓存 P2 和 I 两个投影状态，相比标准 KV cache 省去 query 缓存；线上低延迟场景可尝试类似“只存必要投影”的缓存设计。

  - Linear Relation 将历史压缩成 d_h×d_h 矩阵状态，75% 线性层 + 25% 全 Relation 层混合在 30M 尺度 NLL 仅
  1.278，说明线上长序列低延迟场景可用大部分线性层加少量 full 层，平衡效率与效果。

  - 注意这些结果均在 100M 参数以下语言模型，业务迁移需先在自有推荐序列模型中小规模验证；但将“关系构建”与“信息流分配”解耦的思路可迁移到 attention
  变体或 GNN 消息传递中。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：现有 Attention 将 pair-wise 兼容性分数直接归一化为信息流，一个标量同时承载关系构建与流量分配，缺乏显式关系阶段。论文主张“关系先于流量”，将 token 交互拆成 Self（自关系）和 Exchange（与他者关系）两种角色，先构造关系矩阵再 Softmax，提升序列建模的表达能力与可解释性。

方法关键点：
- SER（Self-Exchange Relation）：投影 P1, P2, I；Self 用 sigmoid，Exchange 用 SiLU，加入长度校正 -λ log i；下三角矩阵 R 后 Softmax 得到 F。
- MHR：多头并行，头间用 Givens 旋转混合信息分支 I，保持正交性，交替配对相邻头。
- 精确分解：归一化流量可分解为 Self mass 与 aggregate Exchange mass，Exchange 内部分配由原始 Exchange 分数决定，与长度校正无关。
- FlashRelation：利用该分解做 tile 化在线 softmax 扫描，不物化全矩阵；Linear Relation 将历史 Others 压缩为 d_h×d_h 循环状态，复杂度 O(T d^2/H)；Hybrid 为 75% Linear + 25% Full；Relation Cache 只缓存 P2 与 I 两个投影，等效 KV 但省去 query。

关键实验：
- 10M/30M/100M 参数量、TinyStories/SmolLM 语料、150M/450M/1.071B tokens 训练，Full Relation 最终验证 NLL 较 MHA 分别降低 0.0412/0.0151/0.0310。
- 消融：去掉 count calibration 或单头显著变差；Exchange-only transport、Raw-X 通信也变差；No Givens 影响小。
- 系统：FlashRelation 比物化 Full Relation 快 3.60–4.41×；达到 FlashAttention 吞吐的 76.4–84.9%；Hybrid Relation（9 层 Linear + 3 层 Full）30M 级 NLL 1.2780。

值得记住：Token mixing 不必围绕信息流直接组织，可以先显式构造 Self/Exchange 关系，再让 Flow 跟随 Relation。
