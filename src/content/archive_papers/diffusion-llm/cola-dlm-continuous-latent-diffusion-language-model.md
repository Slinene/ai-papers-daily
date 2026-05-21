---
title: "Cola DLM: Continuous Latent Diffusion Language Model"
authors: "Hongcan Guo, Qinyu Zhao, Yian Zhao, Shen Nie, Rui Zhu, …, Yan Zeng (11 人)"
affiliation: ByteDance Seed × HKU × ANU × PKU × RUC
date: 2026-05
venue: arXiv (Seedance Team Research)
topic: diffusion-llm
topic_name: Diffusion LLM
topic_icon: 🌀
idea: 把扩散建模从「对 token 做 observation recovery」升级为「对连续隐变量做 prior transport」：先用 Text VAE 学文本↔latent 的稳定映射，再用 block-causal DiT + Flow Matching 在 latent 空间学 global semantic prior，最后由 conditional decoder 实现局部 token。用 unified Markov-path view 把自身与 AR / LLaDA / Plaid 在理论上完全区分。
paperUrl: https://arxiv.org/abs/2605.06548
codeUrl: https://hongcanguo.github.io/Cola-DLM/
tags:
  - Latent Diffusion
  - Block-causal DiT
  - Flow Matching
  - Hierarchical Latent
  - Unified Multimodal
unverified: false
detail:
  contribution: |
    提出 Cola DLM，第一次系统地把 Latent Diffusion（LDM 在图像域的范式）移植到 LLM 并给出严谨理论框架：把 LLM 的扩散建模从「token 空间观测恢复」升级为「latent 空间先验传输」(prior transport)，从而把全局语义组织与局部 token 实现解耦。配套提出 unified Markov-path 视角，可证明 Cola DLM 与 AR / LLaDA / Plaid 的本质差异；并给出 "何时该用 Cola DLM" 的三条曲线判据 (D(R) at low R + E(M) 下降 + G_infer 可控)。
  background: |
    LLM 主流仍是 AR (left-to-right + 串行推理)。非 AR 路线已分裂：(i) 离散 diffusion (LLaDA) 在 mask/absorb 状态做多步恢复，但中间离散状态难承载全局语义；(ii) 连续 token-aligned diffusion (Plaid) 改在 embedding 上去噪，但本质仍是 observation recovery，没有显式 latent；(iii) 早期 latent-space diffusion (DiffuSeq) 把 latent 当固定表示，没在 hierarchical framework 下处理。作者关键洞察：图像生成 LDM (Stable Diffusion) 早已证明 latent diffusion 优于 pixel diffusion，但 LLM 还在 token space 做扩散；**扩散的正确角色应该是「学先验」而不是「恢复观测」**。
  method: |
    **两阶段训练 + 一阶段推理**。**Stage 1 Pretrain Text VAE (500M)**：strict-causal encoder/decoder + reconstruction loss + β·KL + λ·BERT-mask loss (防 latent 塌缩)。**Stage 2 Joint VAE + Block-causal DiT (1.8B)**：DiT 块内双向注意力 + 块间因果，Flow Matching 学 latent prior `L_FM = Σ_b ‖vψ(z_t^(b), t; z_0^(<b)) − u_t^(b)‖²`；同时保持 VAE 可训，加 reference encoder KL 防 drift。总损失 `λ_VAE·recon + β·KL + λ_mask·BERT + λ_fm·FM + λ_ref·KL`。**关键设计选择（经消融）**：latent dim 16-128（d=16 时 timeshift loc=1 最优）/ VAE logSNR 可学习 / DiT block size = 16 / Joint 训练 lr 比 = 1。**Inference**：prefix 编码为 clean condition → 按 block 用 ODE solve 从噪声生成 latent → conditional decoder 出 token + KV cache。8-10 步去噪基本饱和。
  experiments: |
    **8 benchmark × 4 RQ × ~2B 参数 strictly matched 对比**。Backbone：500M VAE + 1.8B DiT (Cola DLM) vs 400M embed + 1.8B 主干 (AR/LLaDA)，OLMo 2 tokenizer，AdamW，max_len 512，scaling 跑到 **~2000 EFLOPs**，统一 few-shot generative 评估协议。**核心结果**：(1) Task Average 上 Cola DLM 在高 compute 区段达到最优，MMLU / RACE / Story Cloze / OBQA 优势显著；(2) 推理 8-10 步饱和 → block size 16 下 **1.6-2.0× 减少 sequential 生成深度**；(3) RQ1 发现 latent dim 16/64/128 → 最优 timeshift loc **1.0/1.7/2.3** 系统 drift，验证 latent 中存在 cross-dimensional shared semantic structure；(4) Section 5.1 发现 PPL 与生成质量结构性不对齐 (token-level Table 4：PPL 改善但生成 token 退化)；(5) Section 5.5 用 MMDiT + Image VAE prototype 实现 text+image unified generation (256/640 分辨率)。
  pros: |
    理论扎实：unified Markov-path view 把 AR/LLaDA/Plaid/Cola 在一个公式下区分，是新视角；strictly matched baseline (官方 LLaMA arch + LLaDA 实现 + 同 tokenizer / 同 seed) 对比 honest；4 RQ 体系化推进 (存在性 → latent 设计 → diffusion 过程 → scaling)；三条曲线判据可证明 Cola DLM 何时有效，不只是 "我们方法更好" 的经验声明；自然扩展到多模态 (共享 latent prior + modality-specific decoder)。
  cons: |
    规模偏小：2B 参数对 2026 年 LLM standard 不足以撑起 "AR 替代品" 声明；缺 instruction tuning / chat 评估；multiple-choice 任务绝对分偏低 (generative 协议导致)；PPL ≠ 生成质量虽被定义为 "特性"，但实际给 reward design / 早停带来困难；多模态部分仍是 qualitative prototype；block-causal 限制了真正的 "非 AR" 优势 (块间仍因果)；1.6-2.0× sequential 减少在工程上有意义但不算激进。
  inspiration: |
    把图像 LDM 的 latent-as-data 思路真正搬进文本生成；"prior transport vs observation recovery" 的范式区分可迁移到 Agent RL (reward design 时可以问是 recover 还是 transport)；hierarchical latent + modality-specific decoder 是 unified multimodal 的最干净路线之一；后续可追的方向：scale up to 7B/70B、和 R1 风格 reasoning RL 结合 (在 latent space 做 GRPO?)、解决 PPL 不对齐的新 objective 设计。
  takeaway: 字节 Seedance Team 出品，2026 上半年 Diffusion LLM 路线理论最扎实、对比最 honest 的框架级工作。
---
