---
title: Prefix Sliding for efficient test-time scaling
title_zh: 前缀滑动：高效测试时扩展
authors:
- Niklas Muennighoff
- Zhengyang Wang
- Zeyi Chen
- Weijia Shi
- Binyuan Hui
- John Yang
- Dapeng Jiang
- Mika Senghaas
- Fares Obeid
- Johannes Hagemann
affiliations:
- Stanford University
- University of California, Santa Barbara
- Prime Intellect
- University of Washington
arxiv_id: '2608.26070'
url: https://arxiv.org/abs/2608.26070
pdf_url: https://arxiv.org/pdf/2608.26070
published: '2026-08-26'
collected: '2026-08-27'
category: Reasoning
direction: 长程推理 · 前缀滑动窗口
tags:
- test-time scaling
- sliding window attention
- KV cache
- long-horizon reasoning
- RL training
- inference efficiency
one_liner: 保留前缀与最近滑动窗口、丢弃中间推理 token，实现恒定成本的长程推理，无训练 3 倍加速
practical_value: '- 长程 Agent/工具调用（多跳搜索、自动比价、复杂排障）：把 system prompt、工具定义、任务描述固定为 prefix，中间推理只保留最近
  2048-4096 的 sliding window；能显著降低 KV cache 与时延，且基本不掉点。

  - 用 GRPO/在线 RL 训长 reasoning/Agent 模型时，直接复用 truncated backpropagation：只把最后 4×window
  tokens 传给 trainer，loss 只算最后 window；可避开 OOM，KL 偏差小，适合异步 RL 长 rollout。

  - 工程上避免用 last k / summary 做长上下文压缩：会重复处理 token 或引入额外摘要 step，导致显存锯齿与延迟尖峰；Prefix Sliding
  的 custom kernel 用 tile skipping 能保持吞吐稳定，接近 vanilla sliding window。

  - 注意适用边界：若 Agent 要读长文档、长 API 返回或长代码补全（类似 LiveCodeBench），窗口建议至少 16K，或把关键证据动态追加到 prefix；短文本任务（query
  改写、短推荐理由）加速有限。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：test-time scaling 让模型推理更长，但 full attention 的成本随已生成 token 数持续增长，长程推理在显存与时延上不可承受。实验观察到中间推理 token 重要性快速衰减，而系统前缀与最近 token 持续获得高注意力。

**方法关键点**：
- 保留固定 prefix（系统指令、工具 schema、任务描述）+ 最近 sliding window，只在这两部分内计算注意力，每 token 成本恒定。
- 无训练直接用于现有 Transformer；位置嵌入采用 Continue PE 复用缓存，Reset PE 效果相似。
- RL 训练中使用 truncated backpropagation：只把最后 4×窗口的 token 传到 trainer，loss 只算最后窗口，近似完整梯度。
- 自定义 FlashAttention kernel：intra-tile masking + inter-tile skipping，达到接近 vanilla sliding window 的吞吐。
- 与 last k、summary、纯 sliding window 对比：前两者有重复处理/额外摘要开销，后者丢失 prefix 信息。

**关键实验**：
- 在 Qwen3-1.7B 上，Prefix Sliding 无训练约 3x 加速，同时保持 AIME25/MATH500/GPQA 准确率。
- 生成速度稳定在约 5000 tok/s，而 full attention 随长度持续下降。
- RL 训练中，在相近显存预算下，Prefix Sliding 可支持 100K+ token 的 rollout，获得更高 reward。
- 消融：LiveCodeBench 需至少 16K 窗口匹配 full attention；短任务 HealthBench 加速有限。

**最值得记住的一句话**：中间推理 token 可丢弃，prefix 和最近窗口必须保留，这使任意长推理拥有有界成本。
