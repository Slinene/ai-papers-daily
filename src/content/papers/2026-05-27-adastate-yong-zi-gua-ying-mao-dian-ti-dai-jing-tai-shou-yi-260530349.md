---
title: 'AdaState: Self-Evolving Anchors for Streaming Video Generation'
title_zh: 'AdaState: 用自适应锚点替代静态首帧以提升流式视频生成动态性'
authors:
- Yusuf Dalva
- Pinar Yanardag
affiliations:
- Virginia Tech
arxiv_id: '2605.30349'
url: https://arxiv.org/abs/2605.30349
pdf_url: https://arxiv.org/pdf/2605.30349
published: '2026-05-27'
collected: '2026-05-31'
category: Other
direction: 流式视频生成 · 自适应 KV 缓存锚点
tags:
- streaming video generation
- adaptive anchors
- KV cache
- autoregressive diffusion
- relative time encoding
- hidden state recurrence
one_liner: 将自回归视频扩散模型中的静态首帧锚点替换为与内容同步演化的自适应隐状态，打破场景僵化并显著增强运动与镜头变化
practical_value: '- **生成式序列的自适应锚点设计**：在生成式推荐（如 Semantic ID 逐 token 生成）或 query 改写链中，借鉴用可演化的隐状态取代固定首
  token 锚点，避免早期 token 过度主导后续生成，可提升长期推荐的多样性与动态适应性。

  - **KV cache 作为状态载体**：将 KV 缓存视作循环的隐状态，通过注意力机制实现状态转移，无需额外模块；可在 Agent 的对话记忆或工具调用链缓存中利用该思路，在保持效率的同时实现自适应上下文演化。

  - **相对时间与绝对位置的解耦**：将时间编码与绝对步数解耦，使生成过程在任意长度上保持一致的位置结构，可应用于无限长序列的推荐生成或滚动式创意文案生成，避免
  positional encoding 漂移导致的性能退化。

  - **隐状态去噪但不渲染的机制**：在电商场景中，可为推荐解释/创意文本生成引入一个“幕后状态”来追踪长期目标，与可见输出同步去噪但不出现在最终文本中，帮助保持主题连贯性而不压制内容变化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：自回归视频扩散模型按块生成流式视频时，始终将首帧的 KV 表示作为注意力缓存中的特权锚点。由于首帧是最干净、无误差的位置，它吸引了不成比例的注意力，抑制了视频动态，即使场景本应自然演化，构图也被锁定在初始视点。结果导致运动、镜头移动和场景推进被压制，视频变得时间浅层、静态僵化。

**方法**：提出用**自适应状态**替代静态锚点。该状态是一个隐藏潜变量，模型在每个块中与内容一起去噪，但从不渲染。生成时，模型不再引用冻结的首帧，而是通过同时关注前一状态和当前内容，在每一步生成自己的场景锚点，从而产生随生成内容演化的参考。同时，将绝对时间编码改为相对时间编码：无论生成进行了多远，每一步的位置结构都相同，状态转移在所有块上保持一致。这使得生成过程引入了一种循环：去噪充当转移函数，KV 缓存作为状态载体，无需任何外部模块。

**关键结果**：实验表明，自适应状态大幅提升视频动态性，生成视频中的运动和场景递进更丰富、更自然，有效缓解了静态锚点导致的运动衰减和幻觉重复。
