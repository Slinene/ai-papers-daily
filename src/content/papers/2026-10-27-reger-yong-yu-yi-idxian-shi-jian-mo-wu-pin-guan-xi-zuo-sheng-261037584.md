---
title: 'REGER: Modeling inter-item Relations with Semantic IDs for Generative Recommendation'
title_zh: REGER：用语义ID显式建模物品关系做生成式推荐
authors:
- Yuxi Huang
- Silin Zhou
- Chenhao Wang
- Zihan Li
- Gangming Guo
- Pei Ke
- Shen Gao
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2610.37584'
url: https://arxiv.org/abs/2610.37584
pdf_url: https://arxiv.org/pdf/2610.37584
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · Semantic ID 与偏好蒸馏
tags:
- Semantic ID
- Generative Recommendation
- Knowledge Distillation
- Sequential Recommendation
- Item Relations
- RQ-VAE
one_liner: 通过语义邻居生成预训练、SID边界局部注意力与分层偏好蒸馏，显式建模生成式推荐中的物品语义与协同关系
practical_value: '- GSR 语义邻居生成预训练可借鉴：对电商/长尾 item，在 GR 训练前先让 encoder-decoder 从源 item
  SID 生成 top-K 语义近邻 SID，使 token embedding 与 backbone 继承内容相似性，适合冷启动物品和稀疏交互场景。

  - ITSA 的混合注意力值得落地：在历史编码器里保留一部分 global head，同时增加 item-local head，只允许当前 item 与前一 item
  的完整 SID 之间 attention，显式建模相邻 item 的定向转移，不增加参数，可迁移到现有 T5/Transformer 编码器。

  - HCPD 蒸馏很实用：用线上判别式模型（如双塔或 SASRec）的偏好分，在 SID 前缀树每个合法 next token 上构造条件分布，对 ground-truth
  前缀做 KL 蒸馏，能利用候选 item 相对排序信息，比 CE 单点监督更好；训练开销低，推理零额外成本。

  - 工程注意点：HCPD 需要在每个 prefix 对 legal tokens 重归一化，避免 full vocabulary 概率干扰；蒸馏权重 λ 与 local/global
  head 比例建议按数据集调参，Beauty/Sports 约 0.8，Toys 约 1.0。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐（GR）用残差量化得到 Semantic ID，再自回归生成下一个 item。但标准 GR 有三处缺陷：随机初始化的 token embedding 和从零训练的 backbone 不能直接继承物品语义相似性；历史编码时物品序列被展平成 token 序列，全局双向 self-attention 不显式尊重 SID 边界，也缺乏相邻 item 的定向转移约束；生成阶段只用 CE 监督真实 SID，忽略了候选 item 之间的协同偏好和竞争关系。

**方法关键点**  
REGER 分两阶段解决上述问题：
1. **Generative Semantic Retrieval (GSR)**：先用 item 文本 embedding 取 top-K 语义近邻，构造“源 item SID → 邻居 item SID”的生成任务预训练 GR backbone，让 token embedding 和模型在推荐训练前就学到内容语义相似性。
2. **Item Transition Structure Attention (ITSA)**：在编码器层同时保留 token-global head（全历史双向 attention）和 item-local head（只允许当前 item 与前一 item 的完整 SID 互相 attention），显式注入短程 item 转移结构，不改变参数量。
3. **Hierarchical Collaborative Preference Distillation (HCPD)**：基于 SID 前缀树证明 item 偏好分布可精确分解为前缀条件分布乘积，item 级 KL 可分解为加权前缀条件 KL。据此把冻结判别式推荐模型（DuoRec）的 item 偏好分布转成每个 prefix 的 legal next-token 条件分布，在 ground-truth 前缀上做 KL 蒸馏，与 CE 联合训练。

**关键结果**  
在 Amazon Beauty / Sports / Toys 三个 2014 数据集上，REGER 超过所有生成式基线，并优于大部分判别式基线：Beauty R@5 从 TIGER 0.0435 提升到 0.0594；Sports R@5 从 0.0283 到 0.0357；Toys R@5 从 0.0422 到 0.0612。消融显示 HCPD 贡献最大，移除后 R@5 下降 10.9%–18.0%。单独给 TIGER 加 HCPD，Beauty R@5 可达 0.0535，训练内存仅微增、推理速度不变。

**最值得记住的一句**：GR 不能只靠 SID 分词或 CE 单点监督，显式把 item 级语义、转移和偏好关系注入 generator 训练，能带来稳定收益。
