---
title: 'VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models'
title_zh: VSpark：自回归视觉-语言-动作模型的投机解码加速
authors:
- Suho Yoo
- Youngjoon Jang
- Hyebin Cho
- Taeyeop Lee
- Jaewook Jeong
- Joon Son Chung
affiliations:
- KAIST
- VGG, University of Oxford
arxiv_id: '2611.22666'
url: https://arxiv.org/abs/2611.22666
pdf_url: https://arxiv.org/pdf/2611.22666
published: '2026-11-16'
collected: '2026-11-21'
category: Other
direction: 自回归 VLA 的投机解码加速
tags:
- Speculative Decoding
- Vision-Language-Action
- Inference Acceleration
- Feature Alignment
- Action Tokenization
one_liner: 通过校准动作噪声、特征对齐和连续复用，在无损解码下将 VLA 推理加速 1.28–2.10 倍
practical_value: '- **草稿模型训练数据加噪**：在生成式推荐或 Agent 中，若用 draft 模型加速 LLM 生成 item/action
  token，可用校准噪声扩充训练数据，让 draft 见过更多“语义相同但 token 不同”的近似序列，减少因 token 级不匹配被拒绝的情况。

  - **特征对齐优于 token 对齐**：蒸馏 draft 时，不要只对齐输出 token 概率，而是对齐 target 模型中间隐藏特征。这能显著提高 draft
  与 target 在语义等价但 token 分布不同场景下的一致性，尤其适合 Semantic ID 生成式推荐。

  - **continuation reuse 工程实现**：在 speculative decoding 中，对 rejected draft 上已被 target
  验证通过的 token 序列，保留其 KV cache 和概率作为下一步候选，避免重复 forward，可提升接受率和加速比。实现时需缓存已验证片段的状态。

  - **适用边界**：该方法对自回归生成连续动作或 token 的场景有效，但前提是 draft 与 target 分布偏差可控；电商推荐中若 item token
  空间大且语义模糊，可优先考虑特征对齐与数据加噪组合。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：自回归 VLA 逐 token 生成机器人动作，推理速度慢，限制控制频率。投机解码可用轻量 draft 模型无损加速，但机器人动作 token 存在“不同序列对应相似运动”的特性，draft 预测接近正确动作时仍可能因 token 不匹配被拒绝，导致加速有限。

**方法**：VSpark 针对上述问题提出三点设计：1) 用校准动作噪声收集 rollouts，扩大 draft 训练时的状态覆盖；2) 特征对齐，训练 draft 匹配 VLA 的隐藏特征而非仅输出 token；3) continuation reuse，复用被拒绝 draft 分支上 VLA 已计算的预测作为下一验证步候选。

**结果**：在四个使用不同动作 tokenizer 的 VLA 和四个 manipulation benchmark 上，VSpark 实现 1.28x 到 2.10x 的加速，同时保持解码无损。
