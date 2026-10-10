---
title: 'SpecFold: Folding Multi-Branch Redundancy for Faster Speculative Decoding
  in Diffusion Language Models'
title_zh: SpecFold：折叠多分支冗余加速扩散语言模型推测解码
authors:
- Chung-En Ho
- Weiyu Sun
- Cheng-Jhih Shih
- He Li
- Yong Liu
- Yingyan Celine Lin
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.04875'
url: https://arxiv.org/abs/2610.04875
pdf_url: https://arxiv.org/pdf/2610.04875
published: '2026-10-05'
collected: '2026-10-10'
category: LLM
direction: 扩散语言模型 · 推测解码加速
tags:
- Speculative Decoding
- Diffusion Language Models
- Inference Acceleration
- Triton Kernel
- Multi-branch Redundancy
one_liner: 利用多分支推测验证中的隐藏状态冗余，通过残差门控与折叠注意力/FFN降低计算，最高实现1.64倍吞吐提升
practical_value: '- 若线上用 multi-branch speculative decoding 加速 LLM 生成（如 query 改写、商品文案、Agent
  回复），可借鉴 SpecFold 的 parent-child 分支隐藏状态复用：draft branches 往往只额外 unmask 少量 token，大部分
  hidden states 与父分支高度相似，可做 token-level residual gating 跳过重复 attention/FFN 计算。

  - 算法-系统协同设计值得参考：将细粒度重用逻辑用 Triton kernel 实现为稀疏多分支执行，避免框架层 overhead，否则算法上的 FLOPs 节省难以转化为端到端吞吐增益。

  - SpecFold 与 temporal caching 正交，可与 KV cache、前缀缓存等叠加；若未来在生成式推荐中使用扩散模型生成 Semantic
  ID 序列，同样存在跨步/跨分支冗余，可借鉴类似折叠思想。

  - 论文验证了在多个 DLLM 上吞吐提升且精度不降，说明这种近似重用在文本生成任务上风险可控，适合延迟敏感的搜索/推荐在线服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型（DLLMs）通过迭代块去噪生成文本，但解码成本高；多分支推测解码虽能并行验证多个草稿分支，却引入新的计算冗余——分支间 hidden states 高度相似，因为 draft 分支继承大部分 token，只额外 unmask 少量位置。

**方法关键点**：SpecFold 利用 multi-branch 冗余，算法上执行 token-level residual gating，选择性重用 parent computation，通过 folded attention 和 FFN 降低计算，同时保留残差隐藏状态；系统上用 Triton kernel 实现稀疏多分支执行，将细粒度重用转化为端到端吞吐增益。与 temporal caching 正交，兼容现有 DLLM speculation 策略。

**关键结果**：在两个 DLLM 家族、五个模型、五个标准基准上，SpecFold 相比 Spiffy 最高加速 **1.64x**，相比 vanilla decoding 最高加速 **1.99x**，任务性能保持相当。
