---
title: Hierarchical Quantization with Domain-Adaptive Sparse Routing for Generative
  Cross-Domain Recommendation
title_zh: 面向生成式跨域推荐的分层量化与域自适应稀疏路由方法
authors:
- Haiying He
- Xiaopeng Li
- Yuchen Gu
- Kuo Cai
- Bo Chen
- Jingtong Gao
- Yejing Wang
- Derong Xu
- Ruiming Tang
- Guorui Zhou
affiliations:
- City University of Hong Kong
- Kuaishou Technology
arxiv_id: '2608.06997'
url: https://arxiv.org/abs/2608.06997
pdf_url: https://arxiv.org/pdf/2608.06997
published: '2026-08-07'
collected: '2026-08-10'
category: GenRec
direction: 生成式跨域推荐 · 分层语义ID与自适应路由
tags:
- Generative Recommendation
- Cross-Domain
- Semantic ID
- Mixture of Experts
- Hierarchical Quantization
- Routing Consistency
one_liner: 提出分层共享-路由量化与稀疏专家混合的生成式跨域推荐框架，结合路由一致性正则化，显著提升稀疏域性能。
practical_value: '- **分层量化码本设计**：多域业务中，可构建共享粗粒度码本捕获通用语义（如“运动鞋”），并用可路由的细粒度码本捕捉品类特有细节（如“篮球鞋低帮”），替代全共享或全独立码本，适用于跨品类生成式推荐。

  - **稀疏 MoE 的 shared+specialized 结构**：在跨域 Transformer 中，始终激活一个共享专家处理通用模式，同时通过 Gumbel-Softmax
  路由选择激活一个特化专家，实现条件化参数分配，既保持推理高效性又提升域特异性，适合大促场景下统一多域模型。

  - **跨粒度路由一致性正则化**：生成 Semantic ID 时，每个 item 对应多个 token，强制其路由分布与 item 级池化分布对齐（KL 散度），可有效降低
  token 级路由变异，提高 item 表示连贯性，实现简单，仅需在 loss 中加入该项。

  - **负载均衡防止路由坍塌**：对码本或专家路由概率施加均匀分布偏差正则，简单有效避免少数容量被过分使用，确保所有专家得到利用，工程上易于落地。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：跨域推荐中，不同领域的物品既共享高层语义，又存在细粒度的领域特有模式。现有生成式方法多采用全局共享码本或轻量适配，难以同时提供共享容量与自适应容量，导致稀疏域性能受限。

**方法关键点**：
1. **分层域感知量化器 (HDQ)**：前 L-1 层使用全局共享码本逐层残差量化，捕获粗粒度语义；最后一层通过 Gumbel-Softmax 路由从 K 个专用码本中选择一个进行残差建模，实现细粒度域自适应。
2. **域自适应稀疏 MoE (DAS MoE)**：每个 token 通过一个始终激活的共享 FFN 专家，并由轻量门控网络从 K 个特化专家中动态选择激活一个，形成共享+特化的条件计算。
3. **跨粒度路由一致性学习 (CRCL)**：对同一 item 的多个语义 token，将其路由分布向 item 级平均表示的分布对齐（KL 散度），并辅以 MoE 负载均衡损失，防止路由坍塌。

**关键结果**：在 Amazon (Clothing-Sports, Electronics-Phones) 和 Douban (Books-Movies) 三个跨域对上进行评估，HD-REC 对比最强基线 GenCDR 在 H@10 上取得显著提升：Sports +17.6%、Electronics +16.3%、Phones +9.9%，Clothing 和 Douban 也有稳定增长。消融实验验证了各组件贡献；推理开销仅增加约 2.5%；item 级路由方差降低约 6 倍，证明了路由一致性的有效性。

*核心启示：共享码本适用于粗粒度语义，自适应路由提供细粒度域适应；跨域统一模型需在 token 级保持专家路由一致性以提升稀疏域性能。*
