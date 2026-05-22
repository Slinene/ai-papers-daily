---
title: 'Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs'
title_zh: Mix-Quant：面向Agent LLM的量化预填充与精确解码
authors:
- Haiquan Lu
- Zigeng Chen
- Gongfan Fang
- Xinyin Ma
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2605.20315'
url: https://arxiv.org/abs/2605.20315
pdf_url: https://arxiv.org/pdf/2605.20315
published: '2026-05-18'
collected: '2026-05-22'
category: Agent
direction: Agent推理优化 · 阶段感知量化
tags:
- NVFP4
- Phase-Aware Quantization
- Agentic Inference
- Prefill-Decode Disaggregation
- FP4 Quantization
- Long-Context
one_liner: 提出阶段感知量化框架，预填充用NVFP4加速，解码保持BF16精度，在Agent任务上几乎无损且预填充加速达3倍。
practical_value: '- 对于交互多轮、上下文不断增长的Agent工作流，解码阶段对数值误差更敏感，可直接对预填充进行低精度量化（如NVFP4）而保持解码高精度，避免长轨迹中的误差累积。

  - 可借助预填充-解码分离架构，将低精度预填充worker和高精度解码worker独立部署，既不引入额外的精度切换开销，又能充分利用硬件加速（如Blackwell的FP4
  Tensor Core）。

  - 在输入token远多于输出的场景（工具调用、记忆检索、代码生成等），预填充成为瓶颈，利用W4A4量化可显著降低计算量，收益明显。

  - 量化的收益并非均匀分布在所有阶段：预填充因并行处理长上下文而适合激进量化，解码因自回归特性需保持精度，按阶段定制量化策略是简单有效的手段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent通过多轮工具调用、记忆检索和交互积累大量输入上下文，预填充阶段成为计算瓶颈。若对整个推理过程应用低比特量化（如FP4），虽能加速，但解码阶段的误差会逐步累积，严重损害长轨迹下的任务完成质量。针对这一矛盾，本文提出阶段感知的量化框架Mix-Quant。

**方法关键点**：
- 观察：预填充处理固定输入，不存在递归误差传播，且长上下文中注意力高度集中于少数token（128K上下文中3%的token占据95%注意力），因此预填充对量化鲁棒；解码自回归生成，单token错误会改变后续条件分布，极易引发雪崩效应。
- 设计：仅对预填充阶段应用NVFP4（Blackwell原生支持，微尺度缩放，块大小16，E2M1格式，两级缩放）权值-激活量化，解码阶段保持BF16精度。
- 部署：采用预填充-解码分离架构，预填充worker执行量化计算并生成KV缓存，通过NIXL传输至解码worker，解码以BF16正常进行，避免混合精度核切换与缓存对齐问题。

**关键实验**：
- 基准：长上下文与Agent基准LongBench-V2、AA-LCR、BFCL v4、LongMemEval、τ²-bench，以及数学推理MATH500、AIME。
- 模型：Qwen3-8B、Qwen3.5-9B、Gemma-4-26B-A4B-it、Gemma-4-31B-it。
- 结论：相比于统一NVFP4量化，Mix-Quant在Agent任务上平均可恢复90%以上的性能损失；例如Qwen3-8B在BFCL v4上从38.77回升至40.63（BF16为40.50），LongMemEval从49.82提升至54.85。预填充延迟在RTX 5090上实现2~3倍加速，batch和长度变化下增益稳定。

**核心洞见**：预填充对量化鲁棒（注意力集中，无误差递归），解码敏感（token选择影响轨迹），按阶段解耦量化与精度是最直接的推理加速策略。
