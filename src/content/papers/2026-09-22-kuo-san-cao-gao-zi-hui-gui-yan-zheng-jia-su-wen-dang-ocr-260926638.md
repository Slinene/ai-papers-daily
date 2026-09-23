---
title: 'Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative
  Decoding'
title_zh: 扩散草稿 + 自回归验证加速文档 OCR
authors:
- Dohyun Kim
- Sungjun Han
- Hyungguk Kim
- Yusik Kim
- Jamin Shin
- Paul Hongsuck Seo
- Hongjoon Ahn
affiliations:
- Trillion Labs
- Korea University
- Seoul National University
arxiv_id: '2609.26638'
url: https://arxiv.org/abs/2609.26638
pdf_url: https://arxiv.org/pdf/2609.26638
published: '2026-09-22'
collected: '2026-09-23'
category: Other
direction: 扩散草稿 + 自回归验证加速生成
tags:
- self-speculative decoding
- diffusion
- OCR
- GRPO
- inference acceleration
- AR verification
one_liner: 参数共享 AR-block-diffusion 模型并行草稿 + AR 验证，实现 OCR 解码 3.94 倍加速
practical_value: '- 生成式推荐/广告文案等 input-grounded 长文本任务可借鉴：用 diffusion 并行生成多个 draft token，再用共享参数的
  AR 路径做因果验证，接受多 token 提交，无需额外 drafter 网络。

  - GRPO 直接优化共享 drafter 参数，用序列级或结构级奖励（如文本格式、关键词覆盖）避免 diffusion trajectory likelihood
  估计，训练更稳定且可优化业务目标。

  - 自推测解码可嵌入现有 serving 框架（如 SGLang），平均每 forward 提交 9.7 tokens，适合高吞吐低延迟的在线文案生成、query
  推荐场景。

  - OCR/文档理解中的结构化输出（HTML/LaTeX）奖励信号可类比于电商场景的结构化商品描述、广告落地页生成，可直接复用奖励设计思路。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：AR OCR 模型需逐 token 解码，推理速度受限；diffusion 可并行生成但直接提交多 token 易出错，因为 token 间依赖未知。

方法：提出 GravityOCR，一个参数共享的 AR-block-diffusion 模型，联合训练并行 drafting 和因果 AR verification。draft 阶段用 diffusion 并行生成多个候选 token；verification 阶段用同一参数的 AR 路径按因果顺序校验，接受可提交的连续 token 段，每轮可提交多个 token，无需独立 drafter 网络。AR 路径还使 GRPO 可直接用序列级和结构级 OCR 奖励（如文本准确率、标记格式）优化共享参数，避免 diffusion trajectory 的似然估计。

结果：在 OmniDocBench v1.6 上，AR-path GRPO 将 Overall score 从 94.92 提升至 95.16，接近原 GLM-OCR 的 95.48，且不降低 diffusion drafting 效率。SGLang 部署中平均每 forward pass 提交 9.7 个输出 token，decode-only 加速 3.94×（region crops），端到端页面处理加速 1.32×。
