---
title: 'CoWindow Attention: Full Causal Coverage Is a Collective Property'
title_zh: CoWindow 注意力：全因果覆盖是头集合的集体属性
authors:
- Jingze Shi
- Zhangyang Peng
- Xianduo Li
- Yanlin Qi
- Xiaotian Lin
- Haoxian Chen
- Liangdong Wang
- Guang Liu
- Yuyu Luo
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Beijing Academy of Artificial Intelligence
- Université Paris Cité
arxiv_id: '2609.32704'
url: https://arxiv.org/abs/2609.32704
pdf_url: https://arxiv.org/pdf/2609.32704
published: '2026-09-25'
collected: '2026-09-29'
category: LLM
direction: LLM 稀疏注意力 · 集体因果覆盖
tags:
- Sparse Attention
- Long Context
- Tensor Parallelism
- Collective Coverage
- Training Efficiency
one_liner: 用 KV 头互补长程窗口实现全因果覆盖，训练/解码延迟降 7.4x/3x 且质量接近 FullAttn
practical_value: '- 长上下文 LLM 用于用户行为轨迹、会话日志或 Agent 工具调用历史时，可考虑把 FullAttn 换成 CoWA 式结构：近邻窗口保留最近行为/当前会话，prefix-sink
  固定放 user profile 或 system prompt，远处历史按 KV head 切分互补窗口，训练和推理都能省显存省 FLOPs，同时不牺牲关键关联召回。

  - 静态位置窗口比动态 router/indexer 更适合线上：不需要额外检索选择，避免了线上 TopK 漂移和 router 延迟；如果业务里做长序列检索式注意力，可以借鉴
  position-defined sparsity + collective coverage，把长程访问做成确定性分片，工程实现更稳。

  - 多 GPU 部署时按全局 KV head 索引分配窗口，与 tensor parallelism 对齐，每个 rank 只持有互补窗口的 KV cache，可降低长上下文推理显存和
  KV cache 访问；适合商品描述生成、Agent 多步轨迹分析等长上下文服务降本。

  - 用 synthetic associative recall 快速评估长序列建模是否保留 item 关联，比直接跑长上下文 benchmark 更便宜，适合在推荐系统用户行为序列建模上线前做快速
  ablation。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：FullAttn 在每个 attention head 中重复暴露完整因果历史，即使 FlashAttention 提升 IO 效率，冗余计算和显存流量仍然存在。已有观察表明不同 attention head 会分化出局部/长程功能，因此值得用跨 KV head 的互补窗口替代每个 head 的全局访问，在不牺牲覆盖的前提下降低注意力成本。

**方法关键点**：
- CoWA 为每个 KV head 分配三个窗口：共享 near-diagonal 窗口保留最近上下文；prefix-sink 窗口保留序列开头；互补 long-range 窗口按 breakpoints 将剩余历史等宽分给不同 heads。每个 head 局部稠密、远距离稀疏，但所有 heads 的 union 覆盖完整因果前缀。
- 采用 bottom-right-aligned causal distance 统一定义训练、prefill 和 decoding，无需 router/indexer；window 用四元组 (sink width, near width, gap, long-range width) 描述。
- 执行上通过全局 KV-head 索引与 tensor parallelism 对齐，互补窗口跨 rank 保持；block traversal 直接跳过不可见 KV blocks，避免额外 selection overhead。

**关键结果**：
- 8K window-matched ablation：CoWA 100% coverage 达到 89.73%，FullAttn 为 89.97%；重复窗口在 12.5%-50% coverage 下显著下降。
- 8K/d_model=512 合成 associative recall：CoWA 89.73% vs FullAttn 89.97%，DSA/MoBA 约 50%-54%，NSA 25%。
- 128K tokens、8 H100 TP=8：训练 forward/backward latency 降 7.4x/8.6x，decoding latency 降 3.0x，decoding peak operator memory 降 7.6x。
- Scaling law 0.6B-14B：CoWA 在 perplexity 上贴近 FullAttn，14B 32K 训练 total FLOPs 降 28.5%；14B/32B 模型在知识、推理、RULER 32K/128K 上保持相近分数。

**最值得记住的一句话**：全因果覆盖可以是 head 集合的集体属性，不需要每个 head 复制完整历史也能保持召回与质量。
