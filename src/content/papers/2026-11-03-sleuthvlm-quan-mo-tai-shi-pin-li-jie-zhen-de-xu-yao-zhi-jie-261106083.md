---
title: 'SleuthVLM: Do We Really Need Audio-in-Video for Omni Video Understanding?'
title_zh: SleuthVLM：全模态视频理解真的需要直接听音频吗？
authors:
- Peiran Wu
- Fangfei Gou
- Zhaoxi Mu
- Changhao Zhang
- Jian Liu
- Weiqiang Wang
- Yuntao Wang
- Yuanchun Shi
- Junxiao Shen
affiliations:
- University of Bristol
- Ant Group
- Tsinghua University
arxiv_id: '2611.06083'
url: https://arxiv.org/abs/2611.06083
pdf_url: https://arxiv.org/pdf/2611.06083
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 驱动的多模态视频理解
tags:
- Agent
- Video Understanding
- Multimodal
- ASR
- VLM
- Omni
one_liner: 用 ASR 转写语音 + 仅视觉 VLM 自主侦探视频，在长视频全模态基准上超过直接听音频的 omni 模型
practical_value: '- 将音频等时序模态先转写成文本，再用仅视觉 VLM 通过 agent 循环完成视频理解，可显著降低对全模态对齐数据和巨型 omni
  模型的依赖；在电商直播切片、短视频内容理解、素材审核中可用 ASR + 27B VLM 替代闭源 omni API，降低推理成本。

  - 不预设固定流程，让 agent 自主决定何时提取哪段帧/文本，处理长视频等价于 agentic retrieval；相比一次性 glance 更有效，适合商品详情长视频、直播回放、用户购物路径视频等长程内容。

  - 结论「瓶颈在 agentic 能力而非模态对齐」提示：在推荐/搜索中引入多模态信息时，优先把预算投到可组合的 agent 工具链（检索、总结、推理）上，而不是大规模多模态联合训练。

  - 可借鉴其评估方法：按长/短视频分组，在多个 omni benchmark 上关注平均准确率提升，帮助定位多模态系统的真实瓶颈。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
全模态模型通过联合处理采样帧和音频来回答视频问题，进展主要靠放大模型规模与全模态训练数据。本文质疑：视频理解是否真的需要模型直接「听」音频？

## 方法关键点
SleuthVLM 是一个建立在仅视觉 VLM 上的 agent harness，模型从不直接听音频：语音先经 ASR 转写成文本，VLM 在没有预定义工作流的情况下自主「侦探」视频，按需抽取帧、文本线索进行推理。相比一次性 glance，它更接近 agentic perception 循环。

## 关键结果数字
在 4 个全模态基准（最长 90 分钟视频）上平均准确率 75.0%，比 Gemini 3.8 Flash 高 2.6 个百分点；在 Video-MME-v2 leaderboard 上以 77.8% 登顶；使用开源 27B VLM 时超过所有开源 omni 模型。结论：hearing 不是瓶颈，agentic 能力才是；全模态理解需要更好的 agents，而不是更大的会听模型。
