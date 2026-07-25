---
title: Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning
title_zh: 扩散模型推理时缩放：渐进式种子剪枝
authors:
- Rogerio Guimaraes
- Pietro Perona
affiliations:
- California Institute of Technology
arxiv_id: '2607.21591'
url: https://arxiv.org/abs/2607.21591
pdf_url: https://arxiv.org/pdf/2607.21591
published: '2026-07-23'
collected: '2026-07-25'
category: Multimodal
direction: 扩散模型推理时缩放 · 渐进剪枝
tags:
- diffusion models
- inference-time scaling
- seed pruning
- reward-guided generation
- particle filtering
one_liner: 在固定计算量下，通过早期评分并逐步剪枝扩散去噪轨迹，显著提升生成质量
practical_value: '- 生成式推荐中，若采用扩散模型生成物品语义ID，可借鉴PSP思路：在去噪早期使用轻量评分器筛选候选序列，剪枝低分路径，不增加总去噪步数却提升最终ID质量。

  - 当业务需要从多个随机种子生成的候选集（如LLM生成多条搜索词）中择优选时，可实施渐进式剪枝：用部分解码结果与指令的相关性进行早期评估，提前丢弃不佳生成，节省完整推理开销。

  - 多步推理Agent的动作序列搜索可类比种子筛选，采用粒子滤波式剪枝，在动作分支早期保留高价值路径，控制整体推理成本的同时提高最终任务完成率。

  - 工程实现上，PSP的核心是设计一个与最终奖励对齐的中间评分机制；可借鉴其“前端重探索、后端重利用”的调度策略，在固定Token预算下优化生成结果。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：扩散模型生成质量高度依赖随机种子，现有方法通过best-of-N或重采样利用额外计算提升质量，但保持常驻内存，探索不充分。本文旨在固定计算预算下，通过前端探索与激进剪枝，更有效地分配去噪计算。

**方法关键点**：
- 提出**渐进式种子剪枝（PSP）**，将去噪过程视作多轮筛选：在多个中间时间步，用预训练奖励模型对部分去噪图像评分。
- 根据评分动态剪枝候选集，仅保留top-k轨迹继续去噪，最终在末端用少量步数完成高质量生成。
- 总去噪步数保持不变（例如，N个种子各T步 vs PSP中先批处理多种子再逐步剪枝），不增加模型评估次数。

**关键结果**：
- 在扩散和流匹配骨干上，PSP在GenEval自动指标和人工评估中，相比best-of-N、重要性采样、树搜索等基线，在相同计算量下取得更高指令遵循得分。
- 方法对奖励模型选择鲁棒，且与无分类器引导等采样技巧兼容。
