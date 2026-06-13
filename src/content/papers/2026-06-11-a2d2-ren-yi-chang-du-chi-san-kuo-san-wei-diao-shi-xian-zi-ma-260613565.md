---
title: 'A2D2: Fine-Tuning Any-Length Discrete Diffusion for Adaptive Decoding'
title_zh: A2D2：任意长度离散扩散微调实现自适应解码
authors:
- Sophia Tang
- Yuchen Zhu
- Molei Tao
- Pranam Chatterjee
affiliations:
- University of Pennsylvania
- Georgia Institute of Technology
arxiv_id: '2606.13565'
url: https://arxiv.org/abs/2606.13565
pdf_url: https://arxiv.org/pdf/2606.13565
published: '2026-06-11'
collected: '2026-06-13'
category: Other
direction: 离散扩散模型 · 奖励微调与自适应生成
tags:
- discrete diffusion
- reward fine-tuning
- any-length generation
- adaptive decoding
- optimal transport
one_liner: 提出联合优化插入/去掩码策略与质量推理调度的任意长度离散扩散奖励微调框架。
practical_value: '- 将推荐列表生成建模为离散扩散过程，利用A2D2的奖励微调直接优化业务指标（如点击率），无需依赖代理奖励模型，理论上保证收敛到目标分布。

  - 自适应解码中的质量调度机制可动态控制推荐列表长度与质量平衡，例如在电商场景中根据查询意图自动调整召回数量，提升效率与精度。

  - AJD损失提供了最优路径测度的训练目标，可用于训练生成式检索模型，使生成的item序列更贴合用户偏好分布，减少曝光偏差。

  - 推理时自适应调整插入/去掩码的调度策略，可迁移到Agent的响应生成中，根据对话状态动态决定生成内容的详细程度或步骤数。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：离散扩散模型在序列生成中表现优异，已扩展至任意长度，但基于奖励的微调方法在任意长度设置下仍空白。现有固定长度微调或推理时引导无法充分利用动态生成长度的灵活性。

**方法**：提出A2D2框架，将任意长度离散扩散的插入与去掩码策略联合建模为路径测度，推导Radon–Nikodym导数，实现无需目标样本的理论收敛到奖励倾斜分布。在此基础上，定义解码误差最小化的插入/去掩码质量指标，并设计自适应联合解码（AJD）损失，可证明获得最优路径测度。推理时采用质量驱动的自适应调度，动态平衡生成长度与质量。

**结果**：在多个基准上，A2D2提升奖励优化效果，生成质量与灵活性均优于固定长度微调和推理时引导方法，验证了理论保证在实际中的有效性。
