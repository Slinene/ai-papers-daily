---
title: Register Tokens for Bounded-State Reasoning in Diffusion Language Models
title_zh: 扩散语言模型有界状态推理的寄存器令牌
authors:
- Albert Ge
- Chandan Singh
- Yufan Zhuang
- Xiaodong Liu
- Jianfeng Gao
- Frederic Sala
affiliations:
- University of Wisconsin–Madison
- Microsoft Research
- UC San Diego
arxiv_id: '2609.16372'
url: https://arxiv.org/abs/2609.16372
pdf_url: https://arxiv.org/pdf/2609.16372
published: '2026-09-13'
collected: '2026-09-17'
category: Reasoning
direction: 扩散语言模型 · 有界状态推理
tags:
- Diffusion Language Models
- Register Tokens
- Bounded-State Reasoning
- Chunked SFT
- GRPO
- Memory Tokens
one_liner: 用固定位置的寄存器 token 在分块生成间携带连续状态，优于离散文本携带，代码生成提升显著
practical_value: '- 在长期会话、导购或任务型 Agent 中，若上下文预算受限，可借鉴 register token：在固定位置放少量可学习连续
  slot，每轮结束后用一次额外 forward 把状态写入 slot，下一轮复用，避免无限拼接历史；训练时随机 mask prompt 并加入全掩码轮次，防止模型直接看原文绕过状态编码。

  - 对分块生成长代码、营销文案或批量商品描述的场景，register carry 可替代 full-context，每 chunk 只多一次 forward，论文实验得到
  3.4–5.6× wall-clock 加速，代码 pass@1 高于无 carry 的 full-seq SFT。

  - RL 微调时，register 可作为可微状态通道：chunked GRPO 的 advantage 能跨 chunk 回传到 register 写入，适合长
  horizon 奖励稀疏任务；同时低维 register 可用线性 probe 做状态审计，判断模型是否记住用户目标、任务进度等。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
扩散语言模型（dLLM）通过并行去噪生成，但在长链推理与代码生成场景中，跨生成块通常需要保留前文，attention 成本随长度二次增长。论文探索在固定窗口内生成、只用一个固定大小的携带状态继续推理，即 bounded-state multi-chunk reasoning。

**方法关键点**
- 引入固定位置 register tokens：每个 chunk 去噪后额外前向一次，读取 register 位置的 last-layer hidden states；下一 chunk 将这些 embedding 注入相同位置，清除上一 chunk 文本。
- 使用 chunked SFT 训练，防止模型绕过寄存器：对 continuation chunk 随机 prompt-mask，阻断 completion/register 直接或间接注意 prompt；每个 chunk 首个 pass 全掩码 completion，迫使预测依赖寄存器。
- 对比 baseline：full-sequence SFT（无 carry）、discrete text carry（携带最后 4 个 token id）、memory tokens（重建前 chunk 的连续压缩）。
- 数据：60K OpenMathInstruct-2 + OpenCodeInstruct，模型为 LLaDA-8B 与 Dream-7B；math 使用 C=128、最多 8 chunks，code 使用 C=64、最多 16 chunks。

**关键结果**
Registers 在所有 12 行对比中超过 discrete text，math 最大 +8.5，code 最大 +19.5；尤其在代码生成上，registers 大幅优于 full-seq SFT，多数成功程序跨 chunk 完成。全上下文在 1024 token 下更准，但 bounded carry 有 3.4–5.6× wall-clock 加速。chunked diffu-GRPO 在 LongArithmetic 上带来 +8.1 reward；线性探针能以 R=0.84 从寄存器解码 running total、以 80% 准确率预测下一操作，表明寄存器存有可解释的任务状态。

最值得记住的一句话：在固定上下文的生成式推理中，少量可读写的连续寄存器状态可以替代保留完整文本，同时具备紧凑性与可解释性。
