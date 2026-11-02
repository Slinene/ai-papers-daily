---
title: 'RangeSWA: Training-Free Length Extrapolation for Continuous Diffusion Language
  Models'
title_zh: RangeSWA：连续扩散语言模型的免训练长度外推
authors:
- Guangfu Guo
- Xiaoqian Lu
- Linsey Pang
- Weiran Yao
- Haolin Chen
- Long Cheng
- Kunpeng Liu
affiliations:
- Clemson University
- University of Ottawa
- PayPal
- actA V A AI
arxiv_id: '2610.42084'
url: https://arxiv.org/abs/2610.42084
pdf_url: https://arxiv.org/pdf/2610.42084
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 连续扩散语言模型 · 长度外推
tags:
- Continuous Diffusion Models
- Length Extrapolation
- Sliding Window Attention
- Training-Free
- Long Text Generation
one_liner: 提出训练无关的 RangeSWA，通过滑动窗口+远程块摘要+动态检索缓解连续扩散语言模型长文本生成的重复与漂移
practical_value: '- 长序列生成（如商品详情文案、营销邮件、多轮对话 Agent 的长期记忆）可借鉴“局部窗口 + 远程块摘要 + 检索”的混合注意力策略：不重新训练，只改推理时
  attention mask 和 token 组织，减少长输出的重复和跑题。

  - 位置重映射与条件注意力校正的思路可迁移到已有 LLM/扩散推荐模型做长度外推：将训练时位置范围线性/非线性映射到更长范围，同时对 conditioning
  的注意力权重做校正，避免因训练分布偏移导致的崩溃。

  - 去噪阶段自适应窗口调度值得在扩散式生成推荐（如连续扩散生成 item embedding 或描述）中尝试：前期大窗口保持全局一致性，后期缩小窗口强化局部细节，可平衡多样性与准确性。

  - 但连续扩散语言模型本身在电商/广告场景尚未成为主流，落地需先评估该范式与自回归模型相比在成本、延迟上的优势；该方法主要为学术贡献，工程迁移门槛较高。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：连续扩散语言模型在生成长度超过训练长度时出现文本重复、语义漂移和质量下降，且现有方法常需要重新训练。
**方法**：提出 RangeSWA，免训练。组合局部滑动窗口注意力（只允许 query 看到邻近 token，保留局部细节）、远程块摘要（将远距离块压缩为摘要向量）和动态内容检索（在需要时从远程块中检索相关 token）来支持长距离上下文访问；同时采用位置重映射（将训练位置范围映射到更长范围）、条件注意力校正（修正扩散模型中对 conditioning 的注意力分布）和去噪阶段自适应窗口调度（在不同去噪步调整窗口大小）来缓解长度外推带来的退化。
**结果**：在多个连续扩散语言模型上实验，RangeSWA 显著降低生成困惑度和文本重复率，改善长文本生成质量。
