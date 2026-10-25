---
title: Multi-Token Prediction and Alternative Tokenization Improve Learning Latent
  Multi-Hop Graph Search at Scale
title_zh: 多Token预测与替代分词改进大规模隐式多跳图搜索学习
authors:
- Arvid Frydenlund
- FuTe Wong
- Katherine Lambert
- Frank Rudzicz
affiliations:
- University of Toronto
- Vector Institute
- Manulife Applied AI Research
- Dalhousie University
arxiv_id: '2610.31439'
url: https://arxiv.org/abs/2610.31439
pdf_url: https://arxiv.org/pdf/2610.31439
published: '2026-10-22'
collected: '2026-10-25'
category: Reasoning
direction: 多Token预测与分词改进多跳推理学习
tags:
- Multi-Token Prediction
- Tokenization
- Graph Search
- Multi-Hop Reasoning
- LLM Training
one_liner: 用多token预测和替代分词突破LLM学习隐式多跳图搜索的规模墙，实现稳定训练
practical_value: '- MTP 可作为辅助训练目标加入生成式推荐/Query 改写模型：若任务需要隐式多步推理（如从用户意图推导 query、从 query
  推导商品路径），同时预测未来多个 token 或路径节点，能强化模型对中间步骤的规划能力。

  - 分词策略对结构化生成任务影响显著：将图路径、商品序列或意图链按更合适的语义单元编码（如子路径、节点对、结构化 token）替代逐节点编码，可降低序列长度、改善学习稳定性，在电商路径生成中值得单独调优。

  - 训练信号与分词是两个正交因素，可以独立迭代；工程实现上可先在现有生成式推荐模型上分别尝试 MTP 和调整 item/path tokenization，无需整体重构。

  - 论文使用合成图任务，主要是学术贡献，业务直接迁移有限，但其“扩展墙源于监督信号与分词”的归因可迁移到其他需要长程依赖的生成场景（如会话内多跳推荐、广告序列生成）。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：语言模型能否对未见过的图，仅凭符号描述从起点生成到终点的最短路径？该任务衡量模型执行多跳计算的能力，而非记忆。此前工作发现模型在图规模增大时学习失败，但未揭示具体原因。

**方法关键点**：本文定位两个独立原因——监督信号与分词。第一，理论上证明并实验验证多token预测（MTP）的有效性：在训练时不仅预测下一个token，还预测后续多个token，提供更密集的监督，使模型更好地学习中间推理步骤；且该收益与图拓扑结构无关。第二，引入替代分词方案，将路径按更合理的语义单元切分而非逐节点编码，减少序列长度与不必要的稀疏性，降低学习难度。两者作用正交，可叠加使用。

**关键结果**：结合 MTP 与替代分词，模型在远超此前工作的图规模上稳定、一致地学会了隐式多跳图搜索任务，突破了先前观察到的扩展墙。论文未报告具体数值，但表明该方法在合成图环境具备显著规模提升。
