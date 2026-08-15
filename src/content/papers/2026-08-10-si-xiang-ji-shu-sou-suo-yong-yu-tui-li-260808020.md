---
title: Thought-Level Beam Search for Reasoning
title_zh: 思想级束搜索用于推理
authors:
- Lijie Yang
- Hongyin Luo
- Jiawei Zhao
- Tri Dao
- Ravi Netravali
affiliations:
- Princeton University
- MIT CSAIL
- Meta AI
arxiv_id: '2608.08020'
url: https://arxiv.org/abs/2608.08020
pdf_url: https://arxiv.org/pdf/2608.08020
published: '2026-08-10'
collected: '2026-08-15'
category: Reasoning
direction: test-time 推理算力分配 · 思想级束搜索
tags:
- thought-level beam search
- test-time compute scaling
- hidden-state scorer
- KV cache
- vLLM
- reasoning
one_liner: 将 test-time 推理建模为硬件约束下的算力分配问题，用固定容量池的 thought-level beam search 动态剪枝并分支高质量前缀
practical_value: '- 对 Agent 多步规划/多候选生成：把并行采样改为固定容量池的 beam search，用轻量 scorer（如 hidden-state
  probe）做中间过滤，周期性淘汰低分候选并从高分前缀继续展开，可显著降低 token 消耗并提高正确路径命中率。

  - 长上下文生成（如商品文案、多轮推荐对话）中，利用 prefix caching 共享 KV cache，对不同分支只算增量 token，节省显存和推理成本；同时解耦逻辑搜索树与物理调度，避免内存压力下的贪心退化。

  - 对 reasoning/planning 评估器：设置 warmup 阈值，延迟评分直到步骤充分展开，减少早期噪声误判；用 score-weighted majority
  vote 聚合答案，比等权投票更能利用置信度信号。

  - 工程实现：保持活跃请求数恒定（zero-sum allocation）并让调度器与搜索逻辑解耦，在 vLLM 等 serving 引擎上可达高硬件利用率，减少排队延迟。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Test-time compute scaling 是 LRM 性能的主要驱动力，但主流并行采样效率极低：大量错误轨迹浪费算力，长上下文迅速耗尽 KV cache，造成排队延迟；而剪枝方案虽省 token，却导致 GPU 饥饿，且不主动重分配算力，输出分布几乎不变。核心问题从“花多少算力”转向“算力花在哪”。

**方法关键点**
- 将 test-time reasoning 形式化为部分轨迹上的受限算力分配问题，提出 Gambit：固定容量池 C 上的 thought-level beam search。
- 每 Δ=200 tokens 触发一次 tournament：按平均分数排序，淘汰 K=16 个最低分轨迹，并从 K 个最高分前缀分支，维持活跃数恒定（zero-sum allocation）。
- 评分器用轻量 hidden-state probe（off-the-shelf 2层 MLP 或自训练 history-aware sequence scorer），并设置 warmup w=12K tokens，延迟评分避免早期噪声。
- 系统层引入 decoupled memory management：scheduler view 与 tree view 分离，被调度器淘汰的轨迹成为 ghost trace，仍占逻辑容量，防止贪心退化；分支通过 prefix caching 共享 KV cache。

**关键实验与结果**
在 AIME 2025/2026、HMMT 2024/2025、GPQA-Diamond 上，使用 Qwen3-4B-Thinking、DeepSeek-R1-8B、Phi-4-reasoning-plus-14B 评估，对比 SC@256、Slim-SC、DeepConf、STEP。相同硬件约束下，Gambit 相对 STEP 在 HMMT-24 提升 +6.7%，AIME-25 提升 +3.3%；token 消耗较 SC 最多降低 68.5%（Phi-4 HMMT-25）；trace 完成吞吐提高 >2×；系统开销 <1%。

**最值得记住的一句话**
算力分配应由被动采样转向主动的、硬件感知的 thought-level beam search：固定容量池 + 周期性 prune-and-branch 在同等硬件下同时实现更高精度与更低 token 消耗。
