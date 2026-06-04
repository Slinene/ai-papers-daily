---
title: 'SAILRec: Steering LLM Attention to Dual-Side Semantically Aligned Collaborative
  Embeddings for Recommendation'
title_zh: SAILRec：双端语义对齐与分层注意力引导的LLM推荐
authors:
- Xi Wu
- Jiale Wang
- Zihan Wang
- Yichen Gao
- Xiaocui Yang
- Shi Feng
- Daling Wang
- Yifei Zhang
affiliations:
- Northeastern University, China
arxiv_id: '2606.04514'
url: https://arxiv.org/abs/2606.04514
pdf_url: https://arxiv.org/pdf/2606.04514
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: LLM推荐中的协作知识注入与注意力控制
tags:
- LLM Recommendation
- Collaborative Filtering
- Attention Steering
- Semantic Alignment
- Contrastive Learning
one_liner: 通过双端语义对齐和分层注意力引导，改善LLM推荐中协作嵌入的语义可达性与层级利用。
practical_value: '- **用户侧语义画像码本对齐**：用风格/情感/意识形态码本通过历史交互加权投票生成用户语义 target，然后将协作嵌入对齐到这些离散标签的
  LLM 表示上。电商场景可直接替换码本为商品属性（品牌、价格段、类目、风格等），解决匿名 user embedding 在 LLM 中难以理解的问题，同时提供可解释的推荐理由。

  - **分层的注意力引导策略**：浅层抑制、中层无干预、深层增强协作 token 的注意力。这可以推广到任何向 LLM 注入外部嵌入（如知识图谱、多模态特征）的场景——避免过早干扰语言编码，在决策层强化外部知识，通过简单的偏置控制即可实现，无需改动模型结构。

  - **分阶段训练策略**：先冻结 MF 得到协作嵌入，再单独训练映射模块做语义对齐，最后联合微调 LoRA 和映射模块。这种“预训练-对齐-下游适配”的流程可以复用：将任意推荐特征（如协同信号）先对齐到
  LLM 语义空间再参与微调，比一步联合训练更稳定。

  - **基于注意力诊断的模型设计**：在深度上观察协作 token 的注意力分布，并根据其深度依赖特性设计干预策略。实际工作中可以通过类似诊断分析（layer-wise
  attention to special tokens）来检验额外注入的特征是否被 LLM 合理利用，并指导何时增强/抑制。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
现有 LLM 推荐方法将协作过滤模型的 embedding 注入 LLM，但未分析 LLM 内部如何利用这些协作知识。论文通过诊断实验发现：协作 embedding 的注意力具有深度依赖（浅层弱、中层逐渐增强、深层活跃），且语义对齐能显著改变利用模式并提升性能。这表明既要让协作 embedding 与 LLM 语义空间对齐，又要控制其在哪一层发挥作用。

**方法关键点**  
- **双端语义对齐**：用户侧构建风格/情感/意识形态码本，根据交互历史加权投票选出用户语义 profile，将其 LLM 表示作为 target；用 Q-Former 变体将 MF 的 user embedding 映射为三个协作 token，并通过 InfoNCE 损失与对应语义 target 对齐；item 侧直接对齐到 item 标题的 LLM 表示。  
- **分层注意力引导**：将 Transformer 层划分为浅(30%)、中(50%)、深(20%)三组，浅层对协作 token 的 key 位置加负偏置（抑制），中层不加偏置（自然交互），深层加正偏置（增强），且深层偏置随层深度递增。  
- **训练流程**：1) 先训练 MF 并冻结；2) 用对比学习分别 warm-up user/item 映射模块；3) 基于 LoRA 进行 SFT，同时联合优化映射模块。

**关键结果**  
在 MovieLens-1M 和 Amazon-Book 数据集上，SAILRec 在 AUC、UAUC、NDCG、MAP 上全面超过 CoLLM、SeLLa-Rec、HatLLM 等基线。例如在 MovieLens-1M 上 AUC 达到 0.7571（+1.43%），Amazon-Book 上 AUC 0.8393（+2.02%）。消融实验证实去掉注意力引导或对齐均导致性能下降，浅抑制/中无干预/深增强的 S-N-E 策略最优，验证了协作知识不应过早干扰文本编码、应在决策阶段强化的假设。

**核心洞见**  
协作 embedding 在 LLM 中的利用必须满足两个条件：语义上可理解（通过双端对齐），时间上在正确的层出现（通过分层注意力引导）。
