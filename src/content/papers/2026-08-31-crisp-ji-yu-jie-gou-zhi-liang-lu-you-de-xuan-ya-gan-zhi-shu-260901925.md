---
title: 'CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated
  Routing'
title_zh: CRISP：基于结构质量路由的悬崖感知输入自适应稀疏预填充
authors:
- Huu Huy Nguyen
- Chien Van Nguyen
- Franck Dernoncourt
- Ryan A. Rossi
- Linh Ngo Van
- Jieyang Chen
- Thien Huu Nguyen
affiliations:
- University of Oregon
- Adobe Research
- Hanoi University of Science and Technology
arxiv_id: '2609.01925'
url: https://arxiv.org/abs/2609.01925
pdf_url: https://arxiv.org/pdf/2609.01925
published: '2026-08-31'
collected: '2026-09-04'
category: Other
direction: 动态稀疏注意力·长上下文预填充优化
tags:
- sparse attention
- long context
- LLM inference
- prefill
- dynamic routing
- attention sink
one_liner: 用结构质量代理替代JSD路由，以噪声地板阈值替代累积覆盖阈值，消除长上下文预填充的O(n)噪声积累
practical_value: '## 可借鉴点

  - 如果电商/Agent 场景中需要对长商品描述、评论、用户会话或多轮记忆做长上下文 LLM 推理加速，prefill 阶段可优先考虑动态稀疏注意力；CRISP
  的 Cstruct 路由只需最后 query block 的代理注意力在首尾 anchor 区间做切片，省去 JSD 需要的 pooled matmul 与 KL
  开销，工程实现更轻。

  - 稀疏 token/block 选择不要用固定累积覆盖（如 top-p 累计 0.95）。有 attention sink 的模型容易早停在 sink 漏掉信号，或为凑阈值收
  O(n) 噪声；改为相对噪声地板阈值（如 block 质量 p_j > αμ），α=1.0 可作为免调默认，业务侧更稳。

  - 部署时建议加 context length 门限：论文在 8k 时稀疏仍比 dense 慢约 4x，64k 以上才开始反超；短 prompt 服务不必开启稀疏预填充。长上下文
  RAG/检索类任务收益最大，聚合/多跳任务需评估精度-覆盖权衡。

  - 可复用 VS/PE 双路径思想：对低熵/高集中 head 用结构模式选择，对高熵 head 用 pooled estimation；不要对所有 head 使用同一种稀疏策略。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

长上下文 LLM 的 prefill 自注意力呈二次复杂度。FlexPrefill 虽引入动态路由，但 JSD 路由需要额外 pooled matmul 与 KL 开销；其 cumulative coverage 阈值 γ 在 post-softmax mass cliff 下存在两种结构失败：sink 质量过高导致早停漏掉信号，或 sink 质量分散时为凑阈值累积 O(n) 背景噪声。

## 方法关键点

- Cstruct 路由：直接测量代理注意力在 architectural sink（前 128 tokens）和 local recency（后 128 tokens）上的质量；O(wsink+wlocal) 常数时间，与 JSD 决策在 Llama/Qwen 上分别 94.0%/88.1% 一致。
- mass cliff 与 sink-aware 阈值：块级代理注意力排除首尾 always-retained 块后，用剩余块均值 μ 作为噪声地板；块 j 被选当且仅当 p_j > αμ，α=1.0 为校准自由默认。PE 路径保留 γ-cumsum，因为 diffuse head 无 mass cliff。

## 关键实验

在 Llama-3.1-8B 与 Qwen2.5-7B 上评测 InfiniteBench、RULER、LongBench。CRISP α=1.0 在 InfiniteBench 达到或超过 dense attention（Llama 48.7 vs 48.6；Qwen 28.7 vs 24.0）；对比 FlexPrefill γ=0.95，检索任务最高恢复 +28.0pp（Qwen passkey），LongBench 平均 +0.85/+1.66pp。512k tokens 注意力延迟加速最高 5.30×，效率优势随上下文增长而扩大，印证消除 O(n) 噪声。

## 最值得记住的一句话

稀疏预填充的 routing 应从 sink/recency 结构质量直接读取，selection 应以噪声地板为界，而非累积覆盖阈值。
