---
title: 'DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression'
title_zh: DeepSeek-V4.1-Flash：极限压缩KV缓存的长上下文多模态MoE
authors:
- DeepSeek-AI
- Anyi Xu
- B. Li
- Bangcai Lin
- Bing Xue
- BingCheng Xian
- Bingzheng Xu
- Bochao Wu
- Bowei Zhang
- Boyi Deng
affiliations:
- DeepSeek-AI
arxiv_id: '2609.19969'
url: https://arxiv.org/abs/2609.19969
pdf_url: https://arxiv.org/pdf/2609.19969
published: '2026-09-16'
collected: '2026-09-18'
category: Agent
direction: Agent推理优化 · KV缓存压缩
tags:
- KV Cache Compression
- Long Context
- MoE
- Agent
- Sparse Attention
- FP4 Quantization
one_liner: 通过跨层KV复用、FP4量化与SWA有界重放，将每token全局KV缓存降至890字节，实现近恒定decode成本
practical_value: '- **KV缓存压缩方案可直接迁移**：跨层复用全局KV与Top-K索引（CSA2的Full/Reindex/Reuse三模式）可大幅降低长上下文Agent的内存占用，尤其适合电商多轮对话、工具调用频繁的场景，可将持久化KV缓存缩小至1/8。

  - **CED架构适合输入重的工作负载**：prefill阶段仅激活前一半层（8B参数），对输入token极多的场景（如商品详情+用户行为序列拼接）能显著降低首token延迟，可借鉴其非对称激活设计。

  - **SWA Bounded Replay的工程取舍**：用近似的窗口重放替代精确重建SWA KV，仅需重放最近n_win个token，就能免去持久化SWA缓存，节省SSD和主机内存，适合在线推荐系统中高频短会话的上下文管理。

  - **FP4量化用于KV缓存而非matmul**：对KV cache做训练时量化（QAT）可安全使用FP4精度，仅存储减半而不依赖硬件原生FP4矩阵乘支持，可复用到现有推理引擎，降低HBM压力。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
长horizon Agent的普及使模型工作负载变得输入密集，prefill计算成本高，大KV缓存占用HBM与SSD容量及带宽，成为部署成本的主要瓶颈。降低KV缓存占用和长上下文计算开销是扩大Agent应用规模的关键。

**方法关键点**
- **CED架构**：40层网络分为20层因果编码器和20层解码器，解码器全局KV从编码器末层隐状态投影得到，prefill仅激活8B参数、decode激活16B，将prefill复杂度从O(NL)降至O(NL/2)。
- **CSA2稀疏注意力**：跨层共享全局KV与索引器K，支持Full/Reindex/Reuse三种模式；分层稀疏索引器让后续索引层只在候选池内评分，将decode期每次查询的索引成本从线性降为常数。
- **FP4主KV缓存**：采用MXFP4格式（E2M1）量化KV缓存，训练时QAT，存储减半且无需FP4原生矩阵乘支持；SWA KV保持FP8。
- **SWA Bounded Replay**：不再持久化SWA KV，仅重放最近n_win个token近似重建，使持久KV缓存缩小至V4-Flash的1/8。
- **其他优化**：Single-Pass mHC将激活内存访存减半；Engram条件记忆模块（196B参数）增强记忆；DSpark投机解码提升吞吐。

**关键实验**
在45T多模态token上预训练，支持1M上下文。全局KV缓存每token 890字节，为V4-Flash的1/4、V1的1/437；持久KV缓存为V4-Flash的1/8；单token decode FLOPs从4K到1M上下文仅增加1/4。在Terminal-Bench、DeepSWE、AutomationBench等Agent基准上匹配闭源前沿模型，可完成95%以上真实任务；Base模型在知识/推理/编程上以1/3总参数达到V4-Pro-Base水平。

**最值得记住的一句话**：通过架构级跨层复用、FP4量化与有界重放三个维度的联合压缩，DeepSeek-V4.1-Flash将每token全局KV缓存降至890字节，实现近恒定的decode计算成本，大幅降低长上下文Agent的部署门槛。
