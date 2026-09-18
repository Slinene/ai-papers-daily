---
title: 'To Copy or Not to Copy: Controlling Speculative Decoding via Intrinsic Model
  Signals'
title_zh: 何时复制：用模型内在信号控制投机解码
authors:
- Roy Eisenstadt
- Ido Cohen
- Edo Cohen-Karlik
- Lior Wolf
- Itamar Zimerman
arxiv_id: '2609.20186'
url: https://arxiv.org/abs/2609.20186
pdf_url: https://arxiv.org/pdf/2609.20186
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM 推理加速 · 投机解码
tags:
- Speculative Decoding
- EAGLE
- Copy Detection
- Probing
- LLM Inference
- Throughput
one_liner: SwitchSD 用轻量探针识别 LLM 的复制意图，动态切换神经草稿与上下文复制，吞吐最高提升 15%
practical_value: '- 在部署 LLM 推理服务（如推荐文案生成、Agent 工具输出）时，可借鉴 SwitchSD 的 copy-intent 探针：对目标模型中间层训练轻量分类器，判断当前
  token 是否应从上下文复制，避免 Prompt Lookup Decoding 的误触发。

  - 对于大量 copy 场景（商品描述扩写、基于历史行为生成推荐理由、模板填充），混合策略明显优于单一神经草稿；用 hidden-state probe 代替
  n-gram 重叠启发式，可减少意外重复。

  - 工程上可将 EAGLE/PLD 作为两个 draft 后端，通过探针分数做低成本路由，无需重新训练主模型；如果业务里 copy 密度高，预期可获得 10%+
  吞吐提升。

  - 可复用的结论：copy 不是一个表面 n-gram 模式，而是 LLM 内部可检测的控制信号；把复制判断从规则升级为模型感知，能直接提升投机解码效率。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：Speculative Decoding 存在神经草案与上下文复制两种策略，各有优劣。现有复制方法依赖 n-gram 重叠触发，容易把表面重复误判为复制意图，导致 false-positive，反而降低吞吐。

**方法关键点**：SwitchSD 把“复制”视为 LLM 的潜在控制信号，在目标模型内部表示上训练轻量探针，以高精度识别真实 copy-intent（AUC > 0.99）。系统根据探针信号动态在神经草案（如 EAGLE）与上下文复制之间切换，避免误触发。

**关键结果**：在 Llama 和 Qwen 系列模型上，SwitchSD 相比 EAGLE3 等 SOTA 基线最高提升吞吐 15%，将复制从噪声启发式转变为模型感知的解码策略。
