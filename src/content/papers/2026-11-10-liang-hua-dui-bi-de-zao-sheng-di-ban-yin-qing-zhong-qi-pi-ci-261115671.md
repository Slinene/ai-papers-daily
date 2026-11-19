---
title: 'The Noise Floor of a Quantization Comparison: Engine, restart, batch and kernel
  drift, measured against 8-bit and 4-bit effects in two decision models'
title_zh: 量化对比的噪声地板：引擎、重启、批次与核漂移及 8/4 位效应
authors:
- Aleks Blagojevich
- Trevor Sunderland
affiliations:
- Level5
arxiv_id: '2611.15671'
url: https://arxiv.org/abs/2611.15671
pdf_url: https://arxiv.org/pdf/2611.15671
published: '2026-11-10'
collected: '2026-11-19'
category: Eval
direction: 量化评估 · serving drift
tags:
- quantization
- LLM serving
- decision models
- reproducibility
- evaluation
- kernel drift
one_liner: 系统测量非量化因素造成的决策翻转，发现 4-bit 量化效应普遍超过噪声地板
practical_value: '- 部署 LLM 决策模型（意图分类、工具调用、标签判定）前先建立“噪声地板”：同一模型受引擎切换、重启、批大小、kernel
  选择影响，决策翻转可达 0–0.92%，不能把这些差异误判为量化收益或损失。

  - 4-bit 量化（Q4_K_M / NVFP4）的决策级翻转显著超过所有非量化因素；业务上低成本上线 4-bit 时，应评估每条记录决策翻转率而非总体 accuracy，否则
  accuracy 只净变 6 题但隐藏 436 题变差。

  - vLLM 重启/实例差异在 FP8/NVFP4 下可翻转 0–22 条决定，而 llama.cpp 重启完全 bit-identical；追求可复现时优先选择确定性更高的引擎或固定实例/随机种子。

  - 预注册 5 个假设中 2 个失败并在 27B 上复现失败，说明直觉会错；做模型升级/压缩实验时可借鉴预注册和公开 per-record outputs 的做法。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：量化模型通常与 BF16 原版对比，但对比过程会改变服务引擎、服务器实例、请求批处理方式，甚至 kernel 选择，这些非量化因素会污染量化效应评估。

方法：在 NVIDIA GB10 上，对 Cloudflare 两个决策模型 Clef-flash (9B) 和 Clef (27B) 的 2,400 条公开决策，分别测量引擎、重启、批大小、kernel 漂移，然后把量化效应定义为超出这些噪声地板的部分；并预注册 5 个假设。

结果：非量化源造成 0–0.92% 决策翻转。llama.cpp 重启完全 bit-identical；vLLM 重启翻转 Clef-flash 0/5/20（BF16/FP8/NVFP4），Clef 4/0/22；第三个实例使 NVFP4 达到 4–22。换引擎翻转 6–16，改批大小 8–15，Gated DeltaNet kernel 变换 10–14。单引擎内量化效应更大：Q8_0 为 0.88%/1.04%，FP8 为 2.12%/1.62%，Q4_K_M 为 5.79%/3.50%，NVFP4 为 5.79%/5.67%。所有 4-bit 区间均排除全部非量化源。两个预注册假设失败并在 27B 上重现失败。总体 accuracy 掩盖大部分影响：Q4_K_M 只净变 6 题（-0.02 点），但 436 条决策变差；NVFP4 使 Clef-flash 损失 0.95 点、Clef 损失 0.65 点。代码、量化配方、逐条输出和预注册均已发布。
