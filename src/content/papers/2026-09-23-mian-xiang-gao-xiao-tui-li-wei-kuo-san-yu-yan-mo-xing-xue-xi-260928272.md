---
title: 'Towards Efficient Reasoning: Learning Causal Shortcuts for Diffusion Language
  Models'
title_zh: 面向高效推理：为扩散语言模型学习因果捷径
authors:
- Dian Jin
- Kairong Han
- Baohong Li
- Xinpeng Dong
- Zijing Hu
- Nuanqiao Shan
- Fei Wu
- Kun Kuang
affiliations:
- Zhejiang University
- Shanghai AI Laboratory
arxiv_id: '2609.28272'
url: https://arxiv.org/abs/2609.28272
pdf_url: https://arxiv.org/pdf/2609.28272
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 扩散语言模型推理训练优化
tags:
- Diffusion Language Models
- Causal Shortcuts
- Reasoning
- SFT
- Masking Strategy
- Training Efficiency
one_liner: 提出CSL框架，通过提取因果捷径并优先掩码训练，提升扩散语言模型推理精度与收敛速度
practical_value: '- 如果业务中尝试用 Diffusion LM 做推理型任务（如 Agent 规划、推荐理由生成），不要用 random masking；先提取推理链中的关键
  token（causal shortcuts），优先 mask 这些 token 做 SFT，能明显提升收敛速度和最终精度。

  - 论文给了一套 step-by-step token extraction 流程，可以从业务数据里自动挖出“因果捷径” token 链，适合迁移到需要生成结构化推理路径的场景（如电商导购
  Agent 的决策链路）。

  - 核心结论是：在双向扩散模型的 SFT 中，控制 mask 分布比随机 mask 更高效，这个思想也可以借鉴到其他 masked/denoising 序列模型训练中，作为训练效率调优手段。

  - 对线上推理有启发：如果已部署 DLM，可以通过识别并保护 causal shortcut token 来减少探索空间，加快生成收敛，降低推理延迟。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Diffusion Language Models（DLMs）凭借双向注意力和并行生成展现强推理能力，但 random masking 下的探索空间远大于自回归模型，导致训练难以聚焦到对推理真正关键的 token。作者定义 causal shortcuts 为覆盖全文、能显式引导正确推理轨迹的 token 链，并分析其对推理精度和收敛速度的影响。

**方法关键点**：提出 Causal Shortcut Learning（CSL）框架。先用 step-by-step token extraction 从数据中提取因果捷径；训练时对这些 token 实行 parallel prioritized masking，而不是随机 mask，使模型沿因果捷径更高效、更准确地收敛到正确答案。

**关键结果数字**：在多个推理 benchmark 和两个基座模型上，CSL 稳定超过现有 SFT-variant 方法；相比 SFT-only 平均提升 1.92%，在 MATH-500 上最高提升 4.20%。
