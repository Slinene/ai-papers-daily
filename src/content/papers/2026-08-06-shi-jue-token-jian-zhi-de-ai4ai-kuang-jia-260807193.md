---
title: An AI4AI Framework for Visual Token Pruning
title_zh: 视觉 Token 剪枝的 AI4AI 框架
authors:
- Zhen Liu
- Wenli Huang
- Wei Song
- Yuhan Liu
- Zhiqin Yang
- Jingwen Fu
affiliations:
- Xi'an Jiaotong University
- Ningbo University of Technology
- North China University of Technology
- MiLM Plus, Xiaomi Inc.
- Hong Kong University of Science and Technology
arxiv_id: '2608.07193'
url: https://arxiv.org/abs/2608.07193
pdf_url: https://arxiv.org/pdf/2608.07193
published: '2026-08-06'
collected: '2026-08-15'
category: Multimodal
direction: LLM 驱动的视觉 Token 剪枝策略自动设计
tags:
- Visual Token Pruning
- MLLM
- LLM-driven search
- TPDSL
- Training-free
- Inference optimization
one_liner: 提出 AutoPrune，用 LLM 驱动 TPDSL 自动设计视觉 token 剪枝策略，免训练，删 94.4% token 仍保持 99%
  以上性能
practical_value: '- 多模态推理降本：电商商品图/视频理解、广告创意理解等多模态服务中，可借鉴 AutoPrune 的训练-free 剪枝思路，用领域特定语言描述预算控制、token
  打分、选择约束，快速替代手工规则，降低 prefill 延迟。

  - 残差式策略搜索：不从头搜索，而是在强基础策略上做残差修改，缩小搜索空间并让 LLM 聚焦关键组件；该思想可迁移到推荐系统策略搜索、特征选择、排序规则自动调优。

  - 可复用原子库：将剪枝/召回/过滤等策略拆成可组合原子操作，跨模型和场景迁移；业务中可构建相似 DSL 与原子库，降低策略迭代成本。

  - 推理加速指标参考：删 94.4% 视觉 token 仍保持 99% 性能，FLOPs 降 9.9×，prefill 延迟降 6.4×；对低延迟电商搜索/推荐中的多模态
  LLM 服务有直接工程参考价值。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视觉 token 剪枝方法依赖固定手工启发式，需要昂贵专家试错；剪枝目标、预算和模型架构多样化使人工设计空间变得难以驾驭。论文探索能否让 LLM 自动设计有效的视觉 token 降量算法。

**方法关键点**：提出 AutoPrune，一个训练-free 的 LLM 驱动视觉 token 剪枝策略设计框架。核心是 Token Pruning Domain-Specific Language（TPDSL），包含 131 个可复用原子，覆盖预算控制、token 打分、选择约束和 token 重组。关键设计是每个搜索状态表示为对强基础策略的残差修改，而非从零生成；这缩小了搜索空间，并引导 LLM 关注对性能影响最大的策略组件。

**关键结果**：在 14 个多模态基准和 3 个 MLLM backbone 上验证了有效性、效率与可迁移性。即使移除 94.4% 的视觉 token，AutoPrune 仍保持全量 token 性能的 99% 以上，同时 FLOPs 降低 9.9×，prefill 延迟降低 6.4×。
