---
title: 'ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction'
title_zh: ReVision：通过时间视觉冗余缩减扩展计算机使用代理
authors:
- Amirhossein Abaskohi
- Yuhang He
- Peter West
- Giuseppe Carenini
- Pranit Chawla
- Vibhav Vineet
affiliations:
- University of British Columbia
- Microsoft Research
arxiv_id: '2605.11212'
url: https://arxiv.org/abs/2605.11212
pdf_url: https://arxiv.org/pdf/2605.11212
published: '2026-06-04'
collected: '2026-06-12'
category: Agent
direction: 计算机使用代理 · 视觉冗余压缩
tags:
- Computer-Use Agents
- Visual Token Pruning
- Temporal Redundancy
- GUI Agents
- Multimodal LLM
one_liner: 去除连续 GUI 截图中的冗余视觉补丁，减少 token 开销的同时提升成功率，并让更长历史成为可能。
practical_value: '- **视觉序列输入的去冗余思路**：在需要处理连续图像（如商品展示流、用户生成内容的视频帧、广告创意迭代）的多模态推荐或 Agent
  场景，可以借鉴 ReVision 的 patch‑level 冗余检测器，训练轻量 MLP 判断 patch 是否足够相似，从而减少重复 token，降低 LLM
  推理成本。

  - **冗余移除反而提升性能的发现**：论文表明移除冗余视觉 token 会迫使模型更依赖历史中的有效信号，从而提升长程决策。这提示在推荐序列建模中，适当丢弃高度重复的特征可能有助于泛化，而不是一味保留全部信息。

  - **延迟上下文饱和点**：ReVision 通过压缩视觉 token 使模型可在相同上下文预算下纳入更多历史帧，持续获益。这对需要处理长用户行为序列的 agent
  或推荐系统启示：通过特征压缩，可以延长有效历史的长度，而非简单地增加输入。

  - **训练与推理一致的 token 过滤策略**：在微调阶段就使用过滤后的视觉轨迹，使模型学会从历史帧中“补全”信息。这种训练技巧可迁移到其他多模态序列任务，确保模型适应推理时的压缩输入。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
计算机使用代理（CUA）依赖连续 GUI 截图进行决策，但相邻截图存在大量视觉重叠（平均 45% 的 patch 完全不变），导致大量冗余视觉 token 消耗珍贵的上下文窗口。随历史帧增加，token 成本线性增长，而成功率提升却很有限，限制了长程任务的表现。

**方法关键点**  
- 提出 **ReVision Token Selection（RTS）**，一个三层 MLP 的轻量分类器，输入两个连续截图中对应 patch 的嵌入，输出该 patch 是否冗余的二元标记。  
- 使用 OmniParserV2 生成区域级 IoU 监督，训练 RTS 识别语义无变化的 patch，避免像素噪声干扰。  
- 在 AgentNet 轨迹上以滑动窗口方式构建训练数据：窗口内第一帧保留全部 token，后续帧仅保留 RTS 判定的非冗余 patch，保持原始位置编码（维持 m‑RoPE 兼容）。  
- 在过滤后的轨迹上微调 Qwen2.5-VL-7B，使模型学会从历史帧中恢复被移除的视觉信息。  
- 训练与推理使用完全一致的 token 过滤流程（Algorithm 1），无需修改底层架构。

**关键结果**  
- 在 OSWorld、WebTailBench、AgentNetBench 三个 benchmark 上，使用 5 帧历史时，ReVision 平均减少 46% 的视觉 token，同时将成功率提升约 3%（Qwen2.5-VL-7B 骨架）。  
- 在 WebTailBench 上，使用 9 帧历史时成功率达到 48.9%，远超最强的基线（<30%），且平均步数更少。  
- 历史窗口扩展实验显示：基线模型在 7 帧附近饱和，而 ReVision 可延迟饱和至 11 帧，在约 23k token 的总上下文附近才出现性能平台期。  
- 消融表明，训练中去除冗余 token 并不损害单帧 grounding 能力，且泛化到不同历史窗大小和模型家族（Qwen3-VL-8B）时依旧有效。
