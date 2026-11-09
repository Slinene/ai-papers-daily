---
title: 'BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design'
title_zh: 原生 FP4 KV Cache 解码的算法-系统协同设计
authors:
- Dayou Du
- Woon Yee Ng
- Guangming Sheng
- Nick Lau
- Jianyi Cheng
- Luo Mai
affiliations:
- University of Edinburgh
- Tencent Hunyuan
arxiv_id: '2611.09825'
url: https://arxiv.org/abs/2611.09825
pdf_url: https://arxiv.org/pdf/2611.09825
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 推理加速 · FP4 KV Cache
tags:
- KV cache
- FP4
- LLM serving
- quantization
- attention optimization
- throughput
one_liner: 算法-系统协同实现原生 FP4 KV cache 解码，精度接近 BF16 且吞吐提升 2.4-3.0×
practical_value: '- 长上下文 LLM 推理（电商客服 Agent、多轮对话、推荐理由生成、RAG 长文档）中 KV cache 是内存和带宽瓶颈，可考虑
  NVFP4/MXFP4 原生 FP4 量化，避免精度优先算法的向量码本查找开销。

  - 实现 FP4 KV 量化时需关注三类误差：query 量化的双残差拆分、softmax 概率下溢的 scale 保护、key outlier 的平滑+Hadamard+scale
  search，这些 trick 可直接复用于自研推理优化。

  - 在支持 FP4 Tensor Core 的硬件（如 B300）部署，可预期峰值吞吐提升 2.4-3.0×，精度损失小于 1 分；适合 LLM 特征生成或线上
  Agent 场景降本提并发。

  - 推理系统优化应算法与 attention kernel 协同，transposed softmax + fused probability quantization
  + stacked query MMA 可消除 decode 的 softmax 瓶颈，值得在自建 serving 框架中借鉴。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

长上下文 LLM serving 中 KV cache 占用主导内存和带宽，4-bit microscaling 格式（NVFP4/MXFP4）可压缩 cache 并利用 FP4 Tensor Core，但现有 FP4 KV 系统直接量化精度差，精度优先的 4-bit 算法又因向量码本查找拖慢解码。为此，BitDecoding-FP4 通过算法-系统协同解决精度与效率矛盾。

算法侧针对三类误差：Dual-Residual Query Quantization 将 query 拆成两个 FP4 张量，把 query logit 误差从 60% 降到 1%；Underflow-Aware Probability Scaling 防止 E4M3 scale 把长上下文概率舍入为 0；Outlier-Aware Key Quantization 结合静态平滑、Hadamard rotation 和 scale search 抑制 key outlier。系统侧通过 transposed softmax、fused probability quantization 和 stacked query MMA 消除 softmax 瓶颈，适配 paged KV cache。

在 dense/MoE 模型、GQA/MLA 架构上，NVFP4 精度在 BF16 KV 0.5 分内，MXFP4 1 分内；RL 训练 rollout 中跟踪 BF16。B300 上 Qwen3-4B 与 Qwen3-30B-A3B 端到端峰值吞吐比 BF16 KV 高 2.4-3.0×。
