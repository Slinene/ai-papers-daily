---
title: Fast Multi-dimensional Refusal Subspaces via RFM-AGOP
title_zh: 基于 RFM-AGOP 的快速多维拒绝子空间提取
authors:
- Thomas Winninger
affiliations:
- Télécom SudParis, Évry-Courcouronnes, France
- ENS Paris-Saclay, Gif-sur-Yvette, France
arxiv_id: '2607.02396'
url: https://arxiv.org/abs/2607.02396
pdf_url: https://arxiv.org/pdf/2607.02396
published: '2026-07-02'
collected: '2026-07-06'
category: LLM
direction: LLM 安全对齐 · 多维子空间提取
tags:
- mechanistic interpretability
- refusal subspace
- RFM-AGOP
- activation steering
- LLM safety
- probe
one_liner: 利用递归特征机算法高效识别大模型的多维拒绝子空间，速度提升显著且消融效果更优
practical_value: '- 电商/Agent 场景中若使用 LLM 生成推荐理由或交互回答，可借鉴该方法快速定位“拒绝回答”或内容过滤相关的激活子空间，低成本实现安全对齐。

  - RFM 算法的高效性允许多轮在线监控，适合对延迟敏感的生产环境，比如在 Agent 每次响应前实时检测有害意图。

  - 该方法只需少量探测样本即能初始化，可迁移到垂直领域的偏好控制（如避免生成竞品信息），无需从头训练分类器。

  - 消融实验结果提示 RFM 提取的子空间比传统方法更精确，能减少对正常回复的误伤，适合需要保持转化率的推荐文案生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 拒绝有害指令的行为常被假设为单一线方向，但近期工作发现其存在于多维空间（如“拒绝锥”），传统子空间提取方法计算昂贵，难以用于长推理 trace 的模型。

方法：将递归特征机（RFM）算法应用于拒绝子空间识别，并借助线性探针提供子空间初始化。RFM 利用 AGOP（平均梯度外积）迭代更新子空间基，无需大量采样或优化。实验在 Qwen 3（推理）和 Qwen 2.5（非推理）上进行，计算耗时从小时级降至数秒。

关键结果：RFM 方法在拒绝方向消融任务上比对比方法（如 CCS、RCAb）效果更好；子空间提取速度极快（秒级），可以支持对长推理过程的实时监控。未来工作将进一步比较不同方法得到的子空间关系。
