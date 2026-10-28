---
title: 'On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models
  via Commit-Order Prediction'
title_zh: SPOT：通过提交顺序预测增强扩散语言模型的推测解码
authors:
- Eliezer Shlomi
- Eliron Rahimi
- Avi Mendelson
- Chaim Baskin
affiliations:
- Technion – Israel Institute of Technology
- Ben-Gurion University of the Negev
arxiv_id: '2610.22543'
url: https://arxiv.org/abs/2610.22543
pdf_url: https://arxiv.org/pdf/2610.22543
published: '2026-10-25'
collected: '2026-10-28'
category: LLM
direction: 扩散语言模型推理加速 · 推测解码
tags:
- Diffusion Language Models
- Speculative Decoding
- Commit-Order Prediction
- Inference Acceleration
- SDAR
one_liner: 提出SPOT小模型预测扩散语言模型的下一个提交位置，构建候选树实现无损推测解码，吞吐最高提升3.4倍
practical_value: '- 若业务使用扩散语言模型生成文本（如商品描述、推荐理由、query 扩展），可部署 SPOT 这类 0.62M 参数的 drafter，仅读目标模型输出分布预测更新顺序，目标模型单次
  pass 验证，实现无损加速，额外计算成本极低。

  - 非自回归生成场景（如并行生成多个推荐解释、多位置 mask 填充）可借鉴“顺序外置”思路：训练轻量模型预测哪些位置先提交，减少大模型前向次数，适合低延迟实时推荐。

  - SPOT 的 drafter 只依赖目标模型输出分布，具备跨模型迁移能力，可以在多个不同扩散语言模型间复用，降低频繁换模型的部署成本；业务上可训练一个通用
  drafter。

  - SPOT-Sets 支持动态阈值解码下一次性提交多个位置，适合同时生成多个字段（标题、标签、摘要）的任务，在 SDAR-8B 上平均提升 59% 吞吐，可借鉴到多字段并行生成的工程实现。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

扩散语言模型（DLM）支持并行生成，但精确解码每轮只填充一个 mask 位置，速度受限；多 token 解码有损。推测解码对自回归模型是无损加速标准，但无法直接迁移到 DLM，因为 DLM 必须同时决定生成什么（token）和在哪里生成（位置）。作者发现目标模型上一轮预测在超过 90% 的位置已经给出正确 token，但不知道下一个提交位置，因此顺序预测成为关键瓶颈。

**方法关键点**

提出 SPOT（Speculating Positions Order Trajectory），一个仅 0.62M 参数的小模型，只读取目标模型输出分布，预测下一次提交位置（commit-order）。SPOT 据此提出候选 continuation 树，目标模型通过状态相等性在单次 pass 中验证。通过 Coupled-noise match（共享 Gumbel 噪声）保证任意温度下验证无损。进一步提出 SPOT-Sets，用于动态阈值解码：一次 pass 提交多个位置，同时预测整个 commit set 及其 token。

**关键结果数字**

在 SDAR-8B 上，SPOT 将目标 pass 次数减少多达 6.8 倍，吞吐最高达标准解码的 3.4 倍，在 T=0 和 T=1 下均匹配或超过校准与训练无关基线。SPOT 的 drafter 可跨模型迁移，在六个不同 DLM 上成功迁移；SPOT-Sets 经轻量校准也可迁移。在动态阈值解码之上，SPOT-Sets 将 SDAR-8B 吞吐平均再提升 59%。
