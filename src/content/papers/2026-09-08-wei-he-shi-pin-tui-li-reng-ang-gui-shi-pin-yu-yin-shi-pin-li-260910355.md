---
title: Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms
  in Video and Audiovisual LLMs
title_zh: 为何视频推理仍昂贵？视频与音视频 LLM 推理效率机制综述
authors:
- Killian Steunou
- Yannis Tevissen
- Mounîm A. El Yacoubi
arxiv_id: '2609.10355'
url: https://arxiv.org/abs/2609.10355
pdf_url: https://arxiv.org/pdf/2609.10355
published: '2026-09-08'
collected: '2026-09-13'
category: Multimodal
direction: 多模态视频 LLM 推理效率综述
tags:
- VideoLLM
- Inference Efficiency
- Token Reduction
- Frame Sampling
- Survey
- Multimodal
one_liner: 系统综述视频/音视频 LLM 的推理效率优化机制，按流水线阶段梳理 token 削减与算力降低方法
practical_value: '- 若业务涉及商品短视频/视频广告理解，可借鉴其帧采样与 token 削减思路：在离线特征抽取或在线推理中先用轻量采样+连接层压缩，控制送入
  LLM 的 token 数，降低 prefill 和 KV cache 成本。

  - 对多模态 item 表示生成，可参考连接层 token reduction 架构，把视觉/音频 token 聚合成少量语义 token，用于召回或排序特征的轻量化。

  - 建立 accuracy–cost 权衡表：在引入任何视频理解模块时，强制在同 host LLM 与输入协议下对比 FLOPs/延迟/显存，避免被跨论文异构指标误导。

  - 整体是学术综述，纯文本推荐/搜索系统直接复用点有限；但若部署视频多模态能力，可作为选型与优化清单。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：视频理解从任务专用模型转向视频大语言模型（VideoLLM），支持开放推理，但计算/内存随帧数和上下文长度增长，难以实时、移动端部署。

方法关键点：本综述按推理流水线阶段系统梳理效率机制——帧采样、模态编码、连接层 token 削减、LLM prefill 与 decode。覆盖 2022 年底以来的 VideoLLM 及早期可复用组件；收集文献中同 host 模型、同输入协议下的 accuracy–cost 对比，区分跨论文异构证据；指出音视频效率与标准化评测缺口。

关键结果：无单一数字，但整理出可复用的 token 削减和计算压缩策略；提供持续更新仓库 https://github.com/momentslab/awesome-efficient-videollm。
