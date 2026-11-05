---
title: 'SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding'
title_zh: SpecOPD：分支并行在线蒸馏加速推测解码
authors:
- Tianyu Liu
- Jun Zhang
- Wenjie Huang
- Yuhao Shen
- Tianqi Xu
- Xinyue Hao
- Hongyaoxing Gu
- Xuyang Liu
- Baolin Zhang
- Yating Zhu
affiliations:
- Qwen Business Unit of Alibaba
- University of Science and Technology of China
- Zhejiang University
- Carnegie Mellon University
- University of Edinburgh
arxiv_id: '2611.02846'
url: https://arxiv.org/abs/2611.02846
pdf_url: https://arxiv.org/pdf/2611.02846
published: '2026-11-01'
collected: '2026-11-05'
category: Training
direction: LLM 推测解码 · 在线蒸馏
tags:
- Speculative Decoding
- On-policy Distillation
- LLM Inference
- Parallel Drafting
- Acceptance Length
one_liner: 提出分支并行在线蒸馏框架 SpecOPD，将草稿采样与目标监督解耦并行，大幅提升接受长度与训练吞吐
practical_value: '- 在 LLM 在线服务（如对话式推荐、智能客服、广告文案生成）中使用推测解码时，可借鉴 SpecOPD 的分支并行思路：将 drafter
  的采样与监督解耦，在 reference anchors 处并行采样多个分支并打包成 proposal tree 共享 target-prefix 计算，显著提高训练吞吐与接受长度。

  - E2E-TV 代理目标直接优化 acceptance length，替代传统 KL/MSE 蒸馏损失，能让 drafter 在推理时获得更贴近实际加速的改进；业务中训练轻量生成模型时可尝试类似的端到端目标。

  - 针对 full/sparse/linear attention 的三种工程实现（tree masks、branch-consistent indexer groups、indexed
  state replay）可直接复用到多分支或树状注意力结构的训练与推理框架，尤其适合需要并行采样多候选生成的 Agent 场景。

  - 若业务链路中存在生成式推荐或 Agent 的延迟瓶颈，可评估引入轻量级 drafter 作为提案器，结合本文的并行 OPD 思想降低在线推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推测解码通过 draft-then-verify 加速 LLM 推理，但整体加速取决于 acceptance length。并行 drafter 能在一次前向中生成多个 token，但现有 on-policy distillation 依赖顺序 rollout 收集监督，效率低且限制接受长度提升。关键洞察：on-policy 监督不必继承顺序依赖，draft block 只需 reference prefix 和 draft-sampled history 即可监督。

**方法**：SpecOPD 在 reference anchor 处从不断演变的 drafter policy 采样独立分支，并行化草稿采样与目标监督；将分支打包成 proposal tree 共享 target-prefix 计算。对 full attention 使用 tree masks，sparse attention 使用 branch-consistent indexer groups，linear attention 使用 indexed state replay 保留分支历史。训练采用 E2E-TV 代理目标直接优化 acceptance length。

**结果**：在 8B full-attention、27B full-linear、125B sparse-linear 目标上，覆盖三种并行 draft 架构和四个任务领域，最高将 mean acceptance length 提升 41.45%，监督 token 吞吐较 sequential-rollout OPD 高 16.09 倍，生成加速最高达 3.56 倍。
