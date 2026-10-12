---
title: 'ReplaySSM: Cache SSM Inputs, Not State'
title_zh: ReplaySSM：缓存 SSM 输入而非状态
authors:
- Ze-Wei Liou
- Harris Nover
- Amey Naik
- Andrii Skliar
- Igor Shovkun
- Ido Shahaf
- Tri Dao
affiliations:
- Princeton University
- NVIDIA
arxiv_id: '2610.13778'
url: https://arxiv.org/abs/2610.13778
pdf_url: https://arxiv.org/pdf/2610.13778
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM 推理加速 · SSM 状态缓存优化
tags:
- SSM
- inference optimization
- speculative decoding
- quantization
- vLLM
- state cache
one_liner: 通过 checkpoint 加近期输入缓冲替代逐步状态读写，显著降低 SSM 状态 I/O 并支持高效投机解码与混合精度
practical_value: '- 在线推理中若使用 Mamba-2、Gated DeltaNet 等 SSM 或混合模型，可参考 ReplaySSM 的 checkpoint
  + input buffer 设计，将状态更新从逐步改为周期性批量更新，减少约一半状态内存流量；直接降低首 token 延迟和长序列 decoding 成本，对搜索推荐场景中的
  Agent 长链推理和工具调用尤其有用。

  - 投机解码的 rollback 可以从复制/恢复完整状态改为只移动输入 buffer 的指针，极大降低回滚开销；在推荐系统里做批量候选生成或 LLM 推理时，可为投机验证阶段节省内存和计算，提高吞吐。

  - 混合精度技巧：输出计算使用低精度 checkpoint，循环更新使用高精度 checkpoint，两个副本分离，避免量化误差进入后续 recurrent state。如果在线模型需要对状态做量化压缩，可采用此方法降低
  KL 散度和下游效果损失。

  - 工程实现上可以直接集成到 vLLM 等现有推理框架，不要求替换模型结构；业务中若已使用 vLLM 部署 SSM 或混合架构，可评估开启 ReplaySSM
  获取 1.2-1.47x 标准解码加速或 1.8x 于投机解码的吞吐提升。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：SSM（如 Mamba-2、Gated DeltaNet）在每一步解码时都要读写固定大小的循环状态，造成较高状态 I/O 和较低算术强度；同时状态逐步更新难以低成本回滚，状态量化误差还会持续累积到后续更新中，限制推理吞吐和量化效果。

方法关键点：ReplaySSM 不再逐 step 维护完整状态，而是将循环展开，把状态表示为「周期性 checkpoint + 最近 SSM 输入 buffer」。输出计算与 checkpoint 更新分离：大部分 step 只从输入 buffer 重算输出，不写状态；每隔 K 步才做一次 checkpoint 更新，从而约减半主导状态内存流量。最近输入 buffer 让投机解码的 rollback 变为简单的 buffer 指针回退，验证时无需物化中间状态；同时低精度 checkpoint 只用于输出计算，高精度 checkpoint 用于循环更新，避免低精度舍入误差进入后续状态。

结果：在 vLLM 中实现，针对 Mamba-2 和 Gated DeltaNet。batch size 256 下，四个混合模型的标准解码相比 tuned vLLM baseline 加速 1.20–1.47x；两个 120B 级模型上约 1.8x 于 vLLM 投机解码吞吐；混合精度设置相对共享低精度 checkpoint 显著降低输出 KL 散度和下游准确率损失。
