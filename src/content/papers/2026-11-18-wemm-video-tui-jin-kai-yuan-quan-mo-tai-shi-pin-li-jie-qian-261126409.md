---
title: 'WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding'
title_zh: WeMM-Video：推进开源全模态视频理解前沿
authors:
- Changli Tang
- Jie Yang
- Tianyi Wang
- Lei Li
- Daoze Zhang
- Zijie Xin
- Zhan Liu
- Li Li
- Jinchang Xu
- Fengyun Rao
affiliations:
- WeChat Vision, Tencent Inc.
- Tsinghua University
arxiv_id: '2611.26409'
url: https://arxiv.org/abs/2611.26409
pdf_url: https://arxiv.org/pdf/2611.26409
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 全模态视频理解与推理
tags:
- Omni-Modal
- Video Understanding
- Audio-Visual
- Hybrid-Thinking
- Open-Source
- RL
one_liner: 开源中英双语全模态视频理解模型家族，混合思维训练刷新开源SOTA并超越部分闭源模型
practical_value: '- 混合思维模式（非思维快速响应 vs 显式逐步推理）可迁移到推荐Agent：简单商品查询或实时推荐走低延迟非思维模式，复杂会话式推荐或跨模态商品对比走思考模式，兼顾速度与推理深度。

  - 音视频联合理解能力可用于电商短视频/直播内容理解，自动提取商品卖点、场景、音频信息，辅助生成推荐理由、广告文案或搜索词，提升内容推荐相关性。

  - 后训练中的抗重复MrDPO和专家RL可借鉴到推荐多样性优化：设计重复惩罚损失减少相似商品集中曝光，用专家奖励信号（如点击、转化、停留时长）做细粒度RL微调。

  - 开源评估与复现pipeline可迁移到内部多模态评测：统一构建视频、音频、文本多维度评估，快速对比不同Agent/LLM在业务数据上的表现。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：视频理解，尤其是伴随音频的动态场景理解，是多模态智能的核心挑战。现有模型在音视频联合感知与推理上仍存在局限，且开源社区缺乏能与闭源模型抗衡的全模态视频理解模型。

**方法关键点**：推出中英双语全模态基础模型家族WeMM-Video，覆盖2B、4B、9B、35B-A3B四种规模。模型统一处理文本、图像、音频、视频，采用混合思维范式：非思维指令模式提供快速直接响应，思维模式支持显式逐步推理。训练分两阶段：约1.2万亿token多模态语料上的渐进式预训练，以及包含多教师OPD、抗重复MrDPO和专家RL的多阶段后训练。其中OPD利用多教师蒸馏优化输出分布，MrDPO通过抗重复约束缓解生成重复问题，RL针对特定任务进行专家级奖励优化。

**关键结果**：在120+基准上评估，全模态视频理解与推理取得开源SOTA。旗舰35B-A3B显著超越Qwen3.5-Omni-Flash、Seed2.0-Mini-0428等闭源模型，并缩小与Gemini-3.0-Flash的差距；9B版本超越更大的开源模型Qwen3-Omni-30B-A3B-Instruct。模型、评测与复现pipeline均已公开。
