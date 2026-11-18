---
title: 'TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and
  Frameworks'
title_zh: TeleChat 到 Xing 4：在国产芯片与框架上推进前沿 Agent 大模型
authors:
- Xingchen AGI Lab
- Baotian Hu
- Bingkai Yang
- Boyang Wang
- Changzai Pan
- Chao Lyu
- Chao Wang
- Chen Li
- Chenshuo Pan
- Chenyu Lin
affiliations:
- Xingchen AGI Lab, China Telecom
arxiv_id: '2611.22115'
url: https://arxiv.org/abs/2611.22115
pdf_url: https://arxiv.org/pdf/2611.22115
published: '2026-11-16'
collected: '2026-11-18'
category: Training
direction: 国产芯片大模型训练与推理优化
tags:
- MoE
- Ascend
- MindSpore
- Speculative Decoding
- Agent Training
- Long Context
one_liner: 在昇腾 NPU 上实现 285B 参数 LLM 训练，并推出 29B MoE 开源模型与 TeleGym Agent 训练平台
practical_value: '- **推理降本增效**：电商搜索/推荐场景部署 LLM 时，可采用 wider-and-shallower MoE + 稀疏激活，如
  29B 总参数仅激活 4B，大幅降低每 token 计算成本，适合高并发线上推理。

  - **长序列行为建模**：原生 256K 上下文能力可借鉴到用户行为序列建模或长对话购物助手；在算力受限时用 MLA + DSA + 跨层 IndexShare
  压缩 KV cache，减少长序列内存占用。

  - **投机解码加速在线服务**：块级 draft 模型 + 轻量 correction head 方案可嵌入推荐/搜索的 LLM 服务，报告中解码吞吐提升 2.67×–3.77×，直接降低在线延迟。

  - **Agent 训练 pipeline 设计**：TeleGym 的 disaggregated asynchronous execution + partial
  rollout 可借鉴到电商 Agent（选品、客服、导购）的强化学习训练，应对任务时长差异大、策略频繁更新场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**

大多数开源 LLM 在 GPU 上训练，而国产芯片与框架上的大规模训练面临独特系统挑战。Xing 4 系列旨在验证并优化基于昇腾 NPU 和 MindSpore 的前沿模型训练与推理能力。

**方法关键点**

架构上探索了稀疏激活、注意力设计、深度/宽度权衡与投机解码的平衡，最终采用 MLA 注意力 + DSA 与跨层 IndexShare 支持长上下文服务，优化 MHC 算子，选用 wider-and-shallower MoE 拓扑，并设计了块级 draft 模型 + 轻量校正头的投机解码方案。预训练基础设施基于 MindSpore HyperParallel，结合拓扑感知混合分片、高效分布式优化器、长序列与激活内存协同管理，并通过 CPU affinity 与核心隔离降低宿主调度干扰。后训练引入 TeleGym 统一 Agent 执行平台，通过 disaggregated asynchronous execution、bounded oversampling 和 partial rollout 连接轨迹构建与策略优化，适应异构任务时长并保持轨迹连续性。

**关键结果**

开源 29B MoE 模型，每 token 激活 4B 参数，支持原生 256K 上下文，全部在 Ascend NPU 上训练。在 8192 张 Ascend 910C 卡上完成 285B 模型预训练。相比 MLA-only 基线，prefill 吞吐提升 4.68×；投机解码带来 2.67×–3.77× 解码吞吐提升；消除流水并行后吞吐提升 16.1%。
