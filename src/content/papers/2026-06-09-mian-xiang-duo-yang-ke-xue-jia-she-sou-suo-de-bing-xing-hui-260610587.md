---
title: Towards Diverse Scientific Hypothesis Search with Large Language Models
title_zh: 面向多样科学假设搜索的并行回火进化框架
authors:
- Haorui Wang
- Parshin Shojaee
- Kazem Meidani
- Kunyang Sun
- José Miguel Hernández-Lobato
- Teresa Head-Gordon
- Jiajun He
- Chandan K. Reddy
- Chao Zhang
- Yuanqi Du
affiliations:
- Georgia Institute of Technology
- Virginia Tech
- Carnegie Mellon University
- University of California, Berkeley
- University of Cambridge
arxiv_id: '2606.10587'
url: https://arxiv.org/abs/2606.10587
pdf_url: https://arxiv.org/pdf/2606.10587
published: '2026-06-09'
collected: '2026-06-12'
category: Other
direction: 多样性假设搜索 · 并行回火进化
tags:
- LLM
- Hypothesis Generation
- Evolutionary Search
- Parallel Tempering
- Diversity
one_liner: 用多温度层并行进化与信息交换，在固定验证预算下提升假设质量与多样性
practical_value: '- **多样性保持机制可迁移至生成式推荐**：在 Semantic ID 生成或候选集采样时，借鉴多温度并行搜索与信息交换，缓解模式坍塌，产出多样且高质量推荐结果。

  - **探索-利用权衡的新思路**：多 Agent 协作中，每个 Agent 可对应不同温度，高温度者负责探索，低温度者负责精细利用，定期交换优质种子，既能保持群体多样性又不失收敛效率。

  - **固定预算下的采样策略**：推荐系统召回阶段常需有限算力生成多个候选池，论文中“采样问题”视角与温度调度方法可直接启发多样性召回的设计，在预算内平衡覆盖率和精度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：科学发现中，LLM 被用于生成假设，但传统进化搜索易陷入优化陷阱，导致多样性坍塌，而科学家需要一组高质量备选假设以应对验证噪声和高昂成本。现有方法在探索与优化间失衡。

**方法**：将假设搜索重新定义为固定验证预算下的采样问题，提出 EvoDiverse —— 一个受并行回火（parallel tempering）启发的进化框架。框架在多条温度链上并行进化候选假设群：高温链鼓励探索，低温链专注收敛；链间通过 Metropolis-Hastings 准则进行假设交换，在保证各链细致平衡的前提下传递多样性信息，同时引入验证预算的动态感知调度，提升整体效率。

**结果**：在分子发现、方程发现和算法发现三类任务上，与基线（单温度进化、随机搜索等）相比，EvoDiverse 在相同验证预算下，假设质量指标（如准确率、Top-1 性能）平均提升 12%–35%，多样性指标（如平均不相似度、覆盖范围）提升 20%–50%；并且产出的候选在下游更昂贵的验证中表现出更强的鲁棒性。
