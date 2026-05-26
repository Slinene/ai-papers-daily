---
title: "ELF: Embedded Language Flows"
authors: "Keya Hu*, Linlu Qiu*, Yiyang Lu, Hanhong Zhao, Tianhong Li, …, Kaiming He (8 人; *Equal)"
affiliation: MIT
date: 2026-05
venue: arXiv preprint
topic: diffusion-llm
topic_name: Diffusion LLM
topic_icon: 🌀
idea: 把 Diffusion Language Model 的「连续」推到极致——从 token embedding 起，整条 denoise 轨迹都待在连续 embedding 空间，只在最后一步 t=1 才离散化；而且 denoiser 和 decoder 共享同一份网络权重（用 mode token 切分支），没有独立 decoder。配合 x-prediction + Flow Matching 的 rectified-flow 路径，让 image-domain 的 CFG / SDE 采样器自然迁移过来。
paperUrl: https://arxiv.org/abs/2605.10938
codeUrl: https://github.com/lillian039/ELF
tags:
  - Continuous DLM
  - Flow Matching
  - Embedding Space
  - Classifier-free Guidance
  - Shared Denoiser-Decoder
unverified: false
detail:
  contribution: |
    提出 ELF (Embedded Language Flows)，给出第一个「极简连续 DLM」范式：denoising trajectory 整段保留在 unrestricted 连续 embedding 空间，只在 t=1 做离散化，避免传统 continuous DLM 的 per-step rounding / cross-entropy 监督。配套 4 个关键设计：(1) pretrained T5 encoder 给 contextual embedding 作 data manifold；(2) denoiser 与 decoder 共享同一网络，靠 binary mode token (denoise/decode) 分流，零额外推理模块；(3) x-prediction 而非 v-prediction，保证 MSE 与 CE 损失能在共享网络下兼容；(4) self-conditioning 拼起 training-time CFG，自然迁移图像扩散的 quality–diversity 调控。
  background: |
    当前 DLM 分两派——离散 DLM (MDLM/Duo/E2D2) 在 token 空间直接做 categorical diffusion，是 2024-2026 主流；连续 DLM (Diffusion-LM/CDCD/DiffuSeq/SSD-LM/TESS) 把 token 拉到 continuous / simplex / manifold 上去噪，但每步加 rounding 损失或 token-level CE 约束，trajectory 仍被 "discrete shadow" 拽住，经验上长期被离散派碾压。Latent diffusion for language (LD4LG 系) 借鉴 Stable Diffusion 但需独立 decoder，pipeline 偏重。作者关键判断：连续派表现差**不是「语言天生离散」的锅，而是大家给连续 trajectory 加了太多 discrete leash**——拿掉后连续 DLM 就能拿 SOTA。
  method: |
    **Rectified Flow on embedding**：token → 冻结 T5-small encoder (35M, 512-d 上下文 embedding) → bottleneck 投 128-d 主网络空间。noise/data 走线性插值 `z_t = t·x + (1−t)·ε`，velocity `v = x − ε`。**x-prediction**：网络出 `x_θ = net(z_t, t)`，损失 `L_MSE = E[(1−t)^{-2} · ‖x_θ − x‖²]`，等价 velocity 预测但能与 t=1 的 token 预测共享权重 (v-prediction 在共享设置下崩)。**Shared denoiser-decoder**：t=1 用 token-level 损坏 `z̃` 作输入，同一网络在 "decode" mode 下出 embedding，再过可学习 unembedding W 出 logits，`L_CE = CrossEnt(W·x_θ(z̃), s)`。**单 batch 双分支**：80% 走 MSE 任意 t，20% 走 CE 在 t=1，用 mask 选择 loss。**Self-conditioning + training-time CFG**：第二次前传以前一步预测作 condition，concat 进网络；CFG 直接拟合 `x_cfg` 避免 inference 双 forward。**Sampler**：默认 ODE Euler；SDE-inspired 每步注入小噪 + shift t，等效单步 noise，few-step 表现更好。三 scale：ELF-B 105M / ELF-M 342M / ELF-L 652M。
  experiments: |
    **Unconditional OWT** (9B tokens, L=1024)，1000 generated samples，GPT-2 Large 评 Gen.PPL + unigram entropy。ELF-B (105M) vs MDLM/Duo/FLM/LangFlow (~170M)：**32 步达到 Gen.PPL=24，少 5-10× sampling 步数；只用 45B training tokens，对手 500-577B (10-13× 数据效率)；无 distillation 就压过 MDLM+SDTT / Duo+DCD / FMLM 的 distilled 变体**。Scaling 105M → 342M → 652M：Gen.PPL-entropy 前沿一致下移。**Conditional generation**：WMT14 De-En BLEU **26.4** (AR 25.2, MDLM 18.4, Duo 21.3, E2D2 24.8, CDCD 24.9)；XSum ROUGE-1/2/L **36.0 / 12.2 / 27.8** 全面最优 (MDLM 33.4/11.6/25.8, Duo 31.4/10.1/25.0)。**Ablations 关键**：(a) embedding 选择：pretrained T5 contextual > scratch encoder > pretrained token > Gaussian > learnable；(b) shared denoiser-decoder ≈ separate decoder 但更能延伸到 low Gen.PPL；(c) SDE > ODE 尤其在 8-32 步；(d) v-prediction 在共享权重下崩，x-prediction 是关键。
  pros: |
    方法极简：核心 = 末步离散化 + 共享权重 + x-prediction + Flow Matching，几行伪代码可讲清；与 Cola DLM 形成对照——Cola 走「VAE latent prior transport」，ELF 走「原 embedding 直接 flow」，两条路径都拒绝 token-space diffusion，相互佐证「连续派可行」的判断。数据/计算双效率：10× 训练 token 优势 + 5-10× sampling 步数优势，工程吸引力强。CFG / SDE / x-prediction 全是从 image diffusion 借的成熟工具，迁移成本低；conditional gen 不靠 distillation 就压过 distilled baseline。三 scale 验证 scaling 平滑。
  cons: |
    主网络依赖 35M T5 encoder 提供「data manifold」，宣传里说「无额外 inference module」但训练侧 dependency 真实存在，embedding 质量是隐性天花板 (ablation 显示 scratch encoder 略差于 pretrained)；评估仍偏 unconditional OWT + WMT/XSum 传统三件套，缺 instruction tuning / reasoning / 长文本 QA / chat 评估；few-step 下限 16-32 步，单步生成仍要 distill，相对 AR per-token 单 step 还差一截；t=1 的 token-level CE 只占 20% 训练时间，长尾词 / OOV 表现未探；和 LLaDA / Cola DLM 这种「做 LLM-style chat」的工作还差一截，方法当前停留在 seq2seq。
  inspiration: |
    与 Cola DLM 互为镜像：Cola 是「先学 latent prior 再投 token」，ELF 是「直接在原 embedding 上 flow + 末步合一」——后者更轻量，对字节业务 (生成式推荐 / Agent reasoning) 启示：若 item embedding 已经稳定 (类似 T5 encoder 给出 fixed manifold)，生成式推荐可直接在 item embedding 空间 flow，末步 argmax 出 item id，**不必为 huge vocabulary 设计 categorical diffusion**；x-prediction + shared decoder 范式天然契合「label space 很大但 embedding 已稳」的电商场景。对 Agent RL：现在 reasoning RL 全在 token space 跑 GRPO，ELF 暗示「在 embedding 上 iterative refine + 末步出 token」的 reasoning chain 可能更样本高效。training-time CFG / mean flow 对 prompt 优化 / preference alignment 是新 entry point。
  takeaway: |
    MIT 何恺明组 + Yoon Kim + Jacob Andreas，2026 上半年「连续派 DLM 翻身」的代表作，方法极简实验全面碾压，强烈推荐与 Cola DLM 并读看「连续 DLM 应该怎么做」两条路径分歧。
---

## 一句话评价

MIT 何恺明组 + Yoon Kim + Jacob Andreas，2026 上半年「连续派 DLM 翻身」的代表作。把 Diffusion Language Model 的「连续」推到极致——整条 denoise 轨迹保留在 unrestricted 连续 embedding 空间，只在 t=1 通过共享权重网络做离散化——用极简设计、10× 训练数据效率、5-10× sampling 步数优势全面碾压离散 / 连续 DLM baseline，包括 distilled 变体。

与同月发布的字节 Cola DLM 形成镜像：Cola 走「VAE latent prior transport」，ELF 走「原 embedding 直接 flow」，两条路径都拒绝 token-space diffusion，相互佐证连续派可行。
