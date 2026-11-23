---
title: Speculative Decoding Is Less Speculative Than You Think
title_zh: 投机解码比你以为的更少靠猜
authors:
- Guanning Zeng
- Andrea Zanette
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.27891'
url: https://arxiv.org/abs/2611.27891
pdf_url: https://arxiv.org/pdf/2611.27891
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM 推理加速 · Speculative Decoding
tags:
- Speculative Decoding
- Gumbel-max
- Draft Tree
- Asynchronous Prefetching
- LLM Serving
- Sampling Randomness
one_liner: 预采样并同步验证随机数，以零训练方式指导投机树构建与异步预取，最高提速24.6%
practical_value: '- 若线上已在 vLLM/SGLang 中用 EAGLE/MTP 等投机解码做 LLM serving（商品文案、Agent 规划等），可把
  DICE 的种子同步逻辑直接接入：用 counter-based hash 按 request seed + absolute token position 生成验证随机数，draft
  与 verify worker 本地可复现，无需随机数通信；不改 drafter 权重、不改变输出分布，只换候选分配策略。

  - 树形候选中可用已知 Gumbel draw 修正 draft logits：score = softmax((α·draft_logits + T·g)/σ)，按累积路径分决定
  expand/verify 节点；α、σ 仅用线上前 2000 个节点校准即可，适合无法离线训练的环境。

  - 若做异步预取（如 SSD），不要平均对待所有 next-round 前缀：用 acceptance uniform 预测 stopping position（最大熵截断指数模型，无额外参数），结合已知
  Gumbel draw 对 correction/bonus token 排序，选 top-B 结果预取；实验中 cache hit rate 可从约 60%
  提到约 80%。

  - 高并发 serving 尤其值得关注：DICE 在 C=1 到 64 都保持相对 AR 的加速，而部分并行 drafter 在 C=64 时掉到 AR 以下；适合电商大促或广告高峰时的
  LLM 请求高峰。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
Speculative decoding 的加速取决于 drafter 能否预先命中 target 实际采样路径。现有工作大多靠更强的 drafter 或训练来逼近 target 分布 q≈p，但忽略了另一部分不确定性：采样随机性。论文指出，验证用的 random draws 可以在 drafting 前生成并同步给 drafter 和 verifier，从而把“未知采样结果”变成“已知条件”来指导投机计算分配，且不改变目标采样分布。

**方法关键点**  
- 提出 DICE，预采样并同步验证随机数（Gumbel draws / acceptance uniforms）。工程上用 counter-based hash 按 request seed + absolute token position 生成，draft 与 verify worker 本地可复现，无需传随机 buffer。
- 树形解码：在每个节点用 draft logits + 已知 Gumbel draw 估计 target 下一 token：brx = softmax((α dx + T g)/σ)，累积路径分 bw(xv)=bw(x)brx(v)；用于 child proposal、节点扩展和最终 top-N 验证节点选择。α,σ 由线上前 2000 个节点最大似然校准，通常 1–3 个 prompt 即可。
- 异步预取：用 acceptance uniform 和最大熵截断指数模型估计停止位置 bP(k)，再结合已知 Gumbel draw 对 correction/bonus token 打分，选 top-B 的 (k,v) 结果预取下一轮 draft。

**关键结果**  
- 在 18 个 model–backend 配置、Spec-Bench 和 SPEED-Bench 上，DICE 相对原始 tree 方法吞吐均有提升：Spec-Bench 最高 +21.5%，SPEED-Bench 最高 +24.6%；平均接受长度 τ 一致上升。
- 异步 prefetch 在 Alpaca/GSM8K/HumanEval/UltraFeedback 上，cache hit rate 从 45.6–67.6% 提升到 69.8–80.7%，吞吐提升最高 +13.7%。
- 随温度升高，优势扩大；并发 C=1 到 64，DICE 在 SGLang 和 vLLM 均快于 EAGLE-4/DFlash2/DSpark，且 C=64 时部分并行 drafter 掉到 AR 以下，DICE 仍保持 1.19–1.28× AR。
- 消融表明收益来自“同步的真实 draws”，而非噪声扰动：shuffled draws 反而降低 τ 11–14%；16 节点的 DICE 可达到 EAGLE-4 64 节点的 τ。

**一句话**  
采样随机性不应在投机推理中被当作未知噪声；预采样并同步验证随机数，是零训练成本、不破坏输出分布的通用加速手段。
