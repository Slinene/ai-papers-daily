---
title: 'OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs'
title_zh: OmniDelta：面向全模态LLM的技能驱动令牌压缩预算分配
authors:
- Haoyang Huang
- Wenjie Huang
- Tianqi Xu
- Hongyaoxing Gu
- Kang Tan
- Yikai Fu
- Yuhao Shen
- Tianyu Liu
- Baolin Zhang
- Jun Zhang
affiliations:
- Zhejiang University
- Qwen Application, Alibaba
- Carnegie Mellon University
- University of Chinese Academy of Sciences
- University of Science and Technology of China
arxiv_id: '2607.25669'
url: https://arxiv.org/abs/2607.25669
pdf_url: https://arxiv.org/pdf/2607.25669
published: '2026-07-27'
collected: '2026-07-30'
category: Multimodal
direction: 全模态LLM推理优化 · 令牌压缩预算分配
tags:
- token compression
- budget allocation
- OmniLLM
- skill-driven
- efficiency
- audio-video
one_liner: 提出无训练的意图感知+内容感知双层动态预算分配，在不改变总压缩比下提升全模态LLM效率
practical_value: '- 意图感知模态间分配：在推荐场景中处理视频+音频的商品讲解时，可根据用户查询意图（如“查看材质”或“试听音质”）动态调整视觉与音频令牌保留比，避免平均分配浪费资源。

  - 内容感知模态内分配：利用局部复杂度和时间冗余性重分配帧/音频段预算，可在短视频推荐中仅保留关键帧，降低推理成本而不丢失信息。

  - 训练免费、即插即用：框架无需修改模型或重新训练，可直接集成到现有多模态推荐模型中，快速获得压缩效益。

  - 显存与延迟优化显著：25%保留比下降低22%显存、1.64倍加速，适合大规模在线推荐服务中多模态内容的高吞吐处理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：全模态大模型（OmniLLM）统一理解文本、音频、视频，但长序列带来高推理成本。现有压缩方法多在固定总预算下选择重要令牌，但忽略了前期的预算分配——查询与音视频的直接相似度不可靠，均匀的模态内预算可能丢失关键证据或保留冗余。

**方法**：OmniDelta，一个无训练的、技能驱动的双层分配框架。首先构建音频和视频技能池，采用意图感知的模态间分配，根据查询需求偏移固定令牌预算（例如，问题侧重声音时给音频更高保留比）。然后在模态内，基于局部复杂度和时间冗余重新分配音频段和视频帧预算，实现内容感知的精细调节。最终得到的局部预算可与现有剪枝策略（如FastV）结合，总保留令牌比例不变，但预算使用位置更优。

**结果**：在四个音视频基准和两个Qwen2.5-Omni模型上，OmniDelta建立了新的准确率-效率帕累托前沿。以7B模型25%令牌保留为例，GPU显存降低22.0%，端到端推理加速1.64倍，且准确率优于均匀预算和直接相似度预算。
