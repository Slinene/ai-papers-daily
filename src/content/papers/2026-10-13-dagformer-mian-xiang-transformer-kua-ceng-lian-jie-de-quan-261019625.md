---
title: 'DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections'
title_zh: DAGFormer：面向 Transformer 跨层连接的全局拓扑预测
authors:
- Xiaocong Yang
- Yuren Hao
- ChengXiang Zhai
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.19625'
url: https://arxiv.org/abs/2610.19625
pdf_url: https://arxiv.org/pdf/2610.19625
published: '2026-10-13'
collected: '2026-10-19'
category: Training
direction: Transformer 跨层拓扑预测训练
tags:
- DAGFormer
- cross-layer connections
- topology predictor
- Transformer
- dynamic routing
one_liner: 引入联合训练的拓扑预测器一次性规划全局跨层连接，以输入自适应强度路由信息，显著提升 Transformer 效率与效果
practical_value: '- 动态连接强度与一次性全局拓扑规划的思路，可用于超大推荐模型中多专家/多塔间的信息路由：不再固定每层连接，而是由轻量预测器根据用户/场景/输入特征决定后续模块间的连接权重，提升模型容量利用率。

  - 在训练预算受限时，DAGFormer 用 5B tokens 达到 vanilla 10B 的效果，说明拓扑可学习能降低预训练数据需求；对于电商/广告领域需要频繁微调预训练
  LLM 或构建垂直模型，可尝试用类似连接搜索减少算力与数据成本。

  - 指令微调后 AlpacaEval win rate 63-70%，并且剪枝下退化最小，表明该架构对下游任务和压缩友好；可用于将大模型蒸馏或裁剪到线上推理服务时，保留路由结构以获得更好的性能-成本平衡。

  - 对于 Agent 多步决策，可将“哪些模块/工具互相通信”看作全局拓扑预测问题，由控制器一次性规划整条推理路径的依赖关系，可能取代逐步的局部路由，提升长程任务的一致性。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：标准 Transformer 的残差连接使所有层共享同一信息带宽，后期层只能从前层累加和中读取信息，层间通信方式固定；现有跨层路由方法逐层独立设置连接，缺乏全局视图，可能陷入次优拓扑。

方法关键点：DAGFormer 引入一个与主干网络联合训练的拓扑预测器，对整模型所有跨层连接进行一次性规划，预测每条连接的强度。在标准残差之外，增加从早期层到后期层的直接连接，连接强度由输入 token 动态决定，从而使路由具备输入自适应性。训练时预测器与模型参数同步更新，共同优化最终损失。

关键结果：在 75M、300M、1B 的 OLMo-2 对比中，WikiText-2 perplexity 比 vanilla Transformer 降低 17%-25%；1B DAGFormer 训练 5B tokens 的效果超过 vanilla 训练 10B；相同数据和预算下，超过四种路由基线。在 13 个常识、科学、阅读和数学任务上，300M 和 1B 模型平均准确率提高 2.0-2.5 个点；指令微调后 AlpacaEval win rate 达 63%-70%，领先所有路由基线；结构化剪枝实验中，六项设置里五项退化最少，表现出更好的压缩鲁棒性。
