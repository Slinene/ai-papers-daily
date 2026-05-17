---
title: 'EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration'
title_zh: 基于潜在流恢复的分秒级人类动画生成
authors:
- Wuyang Li
- Yang Gao
- Mariam Hassan
- Lan Feng
- Wentao Pan
- Po-Chien Luan
- Alexandre Alahi
arxiv_id: '2605.15042'
url: https://arxiv.org/abs/2605.15042
pdf_url: https://arxiv.org/pdf/2605.15042
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 视频生成·长时一致性维护
tags:
- Video Generation
- Long-Horizon Animation
- Latent Flow
- Post-Training
- Drift Mitigation
- LoRA
one_liner: 通过持久潜在上下文记忆与恢复流匹配解决长时动画生成中的累积漂移
practical_value: '- 持久上下文记忆机制可借鉴到多轮对话 Agent 中，维护长期用户状态或商品上下文连贯性，防止遗忘。

  - 恢复流匹配的隐式恢复目标类似于生成式推荐解码中加入一致性约束，可尝试在序列生成中保持全局一致性。

  - 轻量 LoRA 微调策略成本低，对于需要持续优化长序列输出的业务（如商品描述生成、对话流）有借鉴意义。

  - 分块处理+跨块记忆传播的思路可应用于长文本/序列生成，例如分块生成推荐理由时跨块传递上下文向量，避免语义漂移。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：长时人类动画生成面临累积漂移，包括静态背景退化（低质量漂移）和角色身份不一致（语义漂移），现有分块生成方法难以保持长时一致性。

**方法**：提出 EverAnimate，一种高效的后训练方法。核心是通过两个机制将生成锚定到持久潜在上下文记忆：(i) 持久潜在传播，在分块间维持潜在记忆，传递身份与运动信息，缓解时间遗忘；(ii) 恢复流匹配，在采样中通过速度调整引入隐式恢复目标，提升块内保真度。仅需轻量 LoRA 微调。

**结果**：在 10 秒视频生成上，PSNR 提升 8%，SSIM 提升 7%，LPIPS 降低 22%，FID 降低 11%；在 90 秒长时生成上，进一步提升至 PSNR 15%、SSIM 15%、LPIPS 32%、FID 27%，显著超越现有方法。
