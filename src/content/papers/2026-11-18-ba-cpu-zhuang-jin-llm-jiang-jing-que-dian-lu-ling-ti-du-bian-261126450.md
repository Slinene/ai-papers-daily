---
title: 'A CPU Inside an LLM: Zero-Gradient Compilation of Exact Circuits into Pretrained
  Weights'
title_zh: 把 CPU 装进 LLM：将精确电路零梯度编译进预训练权重
authors:
- Tanmay Sah
affiliations:
- Independent Researcher
arxiv_id: '2611.26450'
url: https://arxiv.org/abs/2611.26450
pdf_url: https://arxiv.org/pdf/2611.26450
published: '2026-11-18'
collected: '2026-11-21'
category: LLM
direction: LLM 权重内电路编译 · 零梯度算术
tags:
- LLM
- zero-gradient
- circuit compilation
- model editing
- arithmetic
- sidecar
one_liner: 零梯度将精确算术电路写入预训练 LLM 权重，保持 NL 能力并支持流式续写
practical_value: '- 在电商/广告 Agent 中，价格折扣、预算、ROI 分成等精确计算常依赖外部工具调用，打断生成并增加延迟。可借鉴：对 4–6
  位高频算术子任务离线编译为权重内电路或旁路模块，实现无工具调用、流式 inline continuation，适合低延迟、需中句恢复的交互。

  - 其 width extension \(d\to d+K\) + \(\sqrt{d/(d+K)}\) 归一化补偿 + differential tied
  unembeddings 提供一种不训练主模型即可注入确定性 token/结构化输出的机制；可在生成式推荐/Semantic ID 解码中试验注入数值 ID 或
  Base-1000 数字编码，降低 NL 能力损失。

  - 工程部署上，factorized block-sparse sidecar + INT8/INT4 仅用 4.6–8.1 GiB 显存，可理解为模型“能力插件”：按需加载精确计算模块，避免为小概率算术需求全域微调。

  - 但当前覆盖运算仍以算术/布尔为主，业务上可迁移价值取决于是否有大量确定性小计算；纯推荐排序优化场景直接借鉴有限。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：预训练 LM 在多位算术上仍不可靠，现有路线要么梯度微调，要么外部工具解释器，后者会中断解码并带来延迟。

**方法关键点**：用闭式、零梯度电路移植原语把确定性计算直接写入预训练权重，零训练样本、零运行时 hook。核心机制包括：两层 Mellin-GLU 正交采样，处理 SwiGLU/GeGLU 中的 RMSNorm 缩放，使 log-spaced gate grid 动态范围 >250× 并带 IEEE 754 误差界；跨 token 缩放抵消用 signed Chebyshev Indefinite-RoPE self-sink attention 与 SiLU-antisymmetric GatedDeltaNet；轴对齐宽度扩展 \(d\to d+K\) 配合 norm 补偿、Base-1000 BPE 输出与差分 tied unembeddings。编译器生成 4–8 位有符号加减乘电路及布尔/Majority/Parity 电路。

**关键结果**：6 位算术 N=1,200 BF16，Granite 3B 99.17%、Qwen 3.5 4B 100.00% ALU-prefix 精度，FP32 sidecar 可达 100%；中句续写 98%–100%，远超 LoRA 42.2%/61.7% 且 LoRA 无 inline continuation。显存 7.89/10.65 GiB，INT8/INT4+FP32 下 4.60/8.14 GiB；14/14 Tango splits 全过，OOD 触发 0/11,134。
