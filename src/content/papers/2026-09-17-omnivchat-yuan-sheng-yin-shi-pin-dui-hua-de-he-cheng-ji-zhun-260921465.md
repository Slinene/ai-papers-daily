---
title: 'OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual
  Dialogue'
title_zh: OmniVChat：原生音视频对话的合成、基准与训练
authors:
- Haolin He
- Yunfei Chu
- Qi Chen
- Wen Huang
- Yuan Feng
- Muzhi Zhu
- Zheqi Dai
- Haoning Xu
- Dongchao Yang
- Chunyat Wu
affiliations:
- The Chinese University of Hong Kong
- Alibaba Token Hub, Alibaba Group
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Zhejiang University
arxiv_id: '2609.21465'
url: https://arxiv.org/abs/2609.21465
pdf_url: https://arxiv.org/pdf/2609.21465
published: '2026-09-17'
collected: '2026-09-22'
category: Multimodal
direction: 多模态LLM原生音视频对话训练与评估
tags:
- audio-visual dialogue
- multi-agent data synthesis
- RLHF
- benchmark
- omni-modal
- Qwen3-Omni
one_liner: 提出多智能体数据引擎合成音视频对话，构建基准并用多目标RL奖励训练Qwen3-Omni
practical_value: '- 多智能体合成音视频对话数据：电商直播客服、数字人导购可批量生成带场景、表情、物体的对话样本，降低人工采集成本，覆盖长尾场景。

  - 原生音频视频输入省去ASR/字幕：实时交互Agent（直播问答、语音购物助手）直接输入多模态流，降低工程链路延迟和计算开销，保留情感/环境上下文。

  - RL奖励联合优化正确性、效率与风格：对话式推荐/客服可借鉴多目标reward设计，避免只优化准确率导致回复冗长或延迟高；效率与风格项可按业务KPI调整。

  - 合成数据训练+人类录制集验证迁移：离线用合成基准快速迭代，再抽检真实用户数据验证，可作为推荐/对话系统上线前的评估流程。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：原生音视频对话（OmniVChat）允许模型直接接收音视频并返回文本，无需ASR或字幕，降低外部延迟和计算并保留感知线索。但训练数据稀缺，且回复质量难以用关键词匹配评估。

方法关键点：提出 OmniVChat-Studio 多智能体数据引擎，合成单轮/多轮音视频对话；基于合成对话构建 OmniVChat-Bench，覆盖5个能力类别、17个子类、22个场景域；设计 OmniVChat-RL 奖励，联合优化回复正确性、效率与风格；用合成对话训练 Qwen3-Omni-Instruct。

关键结果：训练后模型在 OmniVChat-Bench 及人类录制集 OmniVChat-Bench-Human 上均有提升，验证奖励设计并显示合成训练与评估可迁移至真实对话。
