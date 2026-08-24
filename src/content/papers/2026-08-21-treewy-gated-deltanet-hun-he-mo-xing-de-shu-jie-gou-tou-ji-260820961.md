---
title: 'TreeWY: Speculative Verification for Gated DeltaNet Hybrids'
title_zh: TreeWY：Gated DeltaNet 混合模型的树结构投机验证
authors:
- Sneha Murthy Ghantasala
affiliations:
- Thomson Reuters
arxiv_id: '2608.20961'
url: https://arxiv.org/abs/2608.20961
pdf_url: https://arxiv.org/pdf/2608.20961
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM 推理 · 投机解码状态压缩
tags:
- speculative decoding
- Gated DeltaNet
- WY transform
- KV cache
- vLLM
- inference serving
one_liner: 用树结构 WY 变换消除 GDN 投机验证的逐节点状态快照，单次三角求解验证整棵草案树并只重建接受态
practical_value: '- 如果在线上部署 Qwen3.5 这类 GDN+softmax hybrid 模型做推荐理由、广告文案、Agent 回复生成，开启
  speculative decoding 前先检查 vLLM/SGLang 的 GDN 状态管理策略：默认 store-all 会在每个 draft 位置存完整
  recurrent state，高并发下状态池/KV 池先爆；TreeWY / ReplaySSM 这类只存伪值或延迟物化状态的方法能把每请求状态块从 N+1
  降到 1，直接抬高 admission batch。

  - 工程选择上，chain 草案可以融合成 CUDA graph kernel，保持低 per-step overhead；树形草案目前会破坏 graph capture，导致
  piecewise 执行，虽然接受长度提升但吞吐不一定划算。业务上先用 chain+MTP 拿稳健收益，树宽等框架融合优化后再上。

  - 对 Agent 系统长会话/多请求并发，p99 TTFT 是用户感知关键指标。TreeWY 在 memory-bound 场景把 p99 TTFT 最高降约
  40×（35B, 128 concurrency, gmu 0.6），因为不排队；若高峰期 KV 池饱和度常超过 80%，这类状态压缩比 draft 算法本身更影响尾延迟。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现代开源 LLM 多为混合架构，大部分层是 Gated DeltaNet（GDN）线性注意力，只维持固定大小循环状态 S，而不是随上下文增长的 KV cache，普通解码省内存，但投机解码遭殃：验证时为了回滚被拒绝 token，必须在每个 draft 位置快照完整 GDN 状态，且树形草稿分支不能共享，宽树直接不可行。TreeWY 的目标是去掉这些快照。

**方法关键点**：
- 利用 gated delta rule 的衰减加性注意力形式：St = αt St-1 + ṽt k_t^T，其中伪值 ṽt = βt(vt − αt St-1 kt)。只要解出所有 ṽt，状态和输出就是前序 token 的衰减加权和。
- 将草稿链/树按 DFS 先序展开为 N 个节点，祖先先于后代，得到一个严格下三角线性系统 (I + diag(β)G)Ṽ = R；一次前向代入即可求出整棵树所有节点的伪值并读出输出，相当于对整个验证窗口做 WY/UT 变换。
- 验证后只根据接受节点 a 的祖先伪值重建状态 Sa；存储 O(N dv) 的伪值矩阵，而不是每层每节点一个状态块。在 dk=dv=128 时单头状态对象压缩 128×，总体从 N+1 降到 1 个状态块，链和树一致。
- vLLM 实现中 chain 路径融合为可 CUDA graph 捕获的 Triton kernel；树路径因非因果祖先 mask 不能 graph capture，降为 piecewise，故宽树尚非吞吐收益。

**关键实验**：
- 在 Qwen3.5-35B-A3B（TP1）和 Qwen3.5-397B-A17B（TP8）上，用 B200、depth-3 MTP 草案，对比 vLLM 默认 store-all。
- 175 个匹配点，接受长度与 baseline 几乎一致（mean |Δ|=0.039）。在 35B 的 31/105 个 memory-bound 点：吞吐 1.15×、p99 TTFT 降 2.94×、端到端延迟降 1.17×，峰值 KV 池占用降至 baseline 约 1/2.6；397B 同趋势（吞吐 1.06×、TTFT 1.66×）。在 memory slack 时吞吐 0.97–0.99×，代价来自 per-step cost，不是方法本身。
- 宽树：TreeWY 每请求状态块恒为 1 块，而 store-all 从 (1,1,1) 的 4 块增至 (3,3,3) 的 40 块；接受长度 1.883→2.786，但受 draft depth 限制，树宽尚未转成吞吐。

**最值得记住的一句话**：用伪值矩阵替代逐节点循环状态快照，把 GDN 投机验证从 O(N) 状态存储降到 1 个状态块，在 memory-bound 场景直接转化为吞吐和 TTFT 收益。
