---
title: 'Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language
  Models without Instruction Tuning'
title_zh: 解锁语音-文本组合能力：无需指令微调的遵循指令语音语言模型
authors:
- Congrui Du
- Yang Zhang
- Kaizhi Qian
- Shiyu Chang
affiliations:
- University of California, Santa Barbara
- MIT-IBM Computing Research Lab, IBM Research
arxiv_id: '2607.02214'
url: https://arxiv.org/abs/2607.02214
pdf_url: https://arxiv.org/pdf/2607.02214
published: '2026-07-02'
collected: '2026-07-03'
category: Multimodal
direction: 语音语言模型 · 权重组合跨模态迁移
tags:
- speech language model
- weight interpolation
- instruction following
- model merging
- cross-modal transfer
one_liner: 仅通过一次语音预训练后与文本指令微调向量权重相加，零语音指令数据实现指令遵循语音模型
practical_value: '- **多模态助手低成本构建**：可将已有强大指令遵循能力的文本LLM快速扩展为语音助手，仅需一轮语音适配预训练，无需昂贵的大规模语音指令数据，适合电商语音搜索、客服等场景快速原型。

  - **权重算术即插即用**：方法本质是模型融合（基座+任务向量），工程实现极其简单，可直接复用现有文本LLM的训练成果，减少重复训练成本，为Agent系统增加语音交互通道提供新范式。

  - **模态能力解耦升级**：当文本LLM基座或指令微调版本迭代时，只需重新计算任务向量并与原有语音适配权重组合，实现语音能力的快速升级，适合迭代快速的业务场景。

  - **可推广到其他模态**：该组合策略不限于语音，可借鉴用于图像、视频等模态的指令遵循迁移，为统一多模态推荐交互（如语音搜索、图像评论理解）提供统一框架。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：语音语言模型（SLM）的指令微调成本极高，不仅需要处理长语音序列，还需覆盖文本LLM已有的大量指令与新兴语音特定指令。现有方案依赖大规模语音指令数据合成，难以规模化。本文旨在找到一种无需语音指令微调即可让SLM获得强指令遵循能力的路径。

**方法**：提出SpeechCombine，分两步：首先取一个文本LLM基座模型，在其上对30k小时语音数据进行连续预训练，得到能够理解语音的适配模型；然后计算该文本LLM的指令微调版与基座版的权重差（即“指令遵循任务向量”），直接将此向量加到语音适配模型的权重上。整个过程无任何语音指令数据参与，也无需对齐训练。

**结果**：仅凭一次语音预训练和简单权重相加，所得模型在多种语音指令遵循任务（包括文本导向、语音导向及跨模态指令）上表现强劲，不仅完好保留了原始文本LLM的知识与能力，还将其成功迁移至语音域。该方案突破了语音指令数据依赖瓶颈，为SLM训练开辟了新方向。
