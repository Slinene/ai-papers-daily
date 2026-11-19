---
title: Clover-35B-A3B-Preview Technical Report
title_zh: Clover-35B-A3B-Preview 技术报告
authors:
- DiffuSpace Technical Team
affiliations:
- DiffuSpace
arxiv_id: '2611.24636'
url: https://arxiv.org/abs/2611.24636
pdf_url: https://arxiv.org/pdf/2611.24636
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: 扩散语言模型 · 块扩散解码
tags:
- Diffusion LM
- Block Diffusion
- MoE
- Gated DeltaNet
- Self-Speculative Decoding
- Agentic LLM
one_liner: 35B 总参 3B 活跃的块扩散 MoE 模型，通过 BD-GDN 与自投机解码在多个 Agent 基准上领先并实现高效部署
practical_value: '- 电商/客服 Agent 可复用自投机解码：用同一模型做 draft 和 verify，避免单独训练轻量 drafter，在长上下文工具调用场景下比
  DFlash 2 有更高的 committed tokens/round 和吞吐；可尝试把块扩散 draft 和熵阈值 acceptance 引入线上 Agent
  推理。

  - 多判断联合预测：将同一上下文的多个分类/属性抽取/合规判断放在一个 diffusion block 中单次去噪生成，实测 complete-set accuracy
  从 65.4% 提升至 77.0%，8 问题延迟仅 164ms，适合电商批量结构化提取、商品审核、多标签分类。

  - MoE 部署优化：按 workload 路由统计做 GPU/CPU 专家放置，高频专家放 GPU，可在 16GB 消费卡上将 decode 从 66.6 tok/s
  提高到 97.5 tok/s；同时 INT4 group size 32 比 g128 更精细，保留更多质量。

  - 长上下文多轮交互：用 Gated DeltaNet 循环状态压缩已完成 prefix，而非维护全量 KV cache，可降低显存并与当前 block 双向注意力结合；对需要长会话的导购/客服
  Agent 有借鉴意义。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
扩散语言模型通过并行去噪提供不同于自回归的生成路径，但现有开放 DLM 在 agent 任务上仍明显落后于同规模 Qwen 基线，例如 LLaDA2.2 flash 和 DiffusionGemma 在 SWE-bench Verified / Terminal-Bench 2.1 上差距明显。Clover 将 Qwen3.6-35B-A3B 的文本骨干改造成块扩散模型，目标是同时提升 agentic coding/tool use 能力与高吞吐推理。

**方法关键点**
- 架构：35B total，3B active MoE；40 层中 3 层 BD-GDN + 1 层 full attention 重复 10 次，每层后接 dMoE（256 routed experts + 1 shared expert）。
- BD-GDN：已完成前缀写入 Gated DeltaNet 循环记忆，当前块内做双向 softmax 注意力；历史 readout 与块内 tokens 共享 softmax，加入 learnable block-size calibration 和 zero-initialized right-context convolution。
- 训练：two-stream clean/noisy 序列，块大小从 {4,8,16,32} 均匀采样；联合 masked diffusion loss 与 auxiliary AR next-token loss。
- 解码：块级 expert coreset + entropy-based self-speculative decoding，配合 presence/repetition/length 惩罚。
- 部署：INT4 expert weights + GPU/CPU 混合执行，routing-informed expert placement。

**关键结果数字**
- Agent：SWE-bench Verified 73.6、Terminal-Bench 2.1 51.7，均居首；Terminal-Hard 38.1、SWE-Pro 46.5 也领先。
- 通用：GPQA Diamond 83.8、MMLU-Pro 84.8、MATH-500 96.2、LiveCodeBench 72.6。
- 吞吐：H200 agent replay 556.6 tok/s、daily chat 356.7；GB300 上 680 tok/s；RTX 5070 Ti 16GB 量化部署下 top-8 97.5 tok/s、top-6 106.3 tok/s。
- Decision model：单次去噪联合预测相关答案，Multiple500 complete-set accuracy 65.4%→77.0%，Sudoku 22.0%→76.0%；8 问题组延迟 164ms，比并行独立调用快 1.52×。

**一句话**：Clover 证明块扩散语言模型可以在 agentic 任务上超越同规模自回归模型，并通过自投机解码与混合量化部署同时获得高吞吐。
