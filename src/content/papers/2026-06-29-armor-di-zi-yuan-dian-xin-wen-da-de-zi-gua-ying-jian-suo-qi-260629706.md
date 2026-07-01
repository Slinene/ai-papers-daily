---
title: 'ARMOR: Adaptive Retriever Optimization for Low-Resource Telecom Question Answering'
title_zh: ARMOR：低资源电信问答的自适应检索器优化
authors:
- Heshan Fernando
- Quan Xiao
- Yan Xin
- Tianyi Chen
affiliations:
- Rensselaer Polytechnic Institute
- Cornell University
- Samsung Research America
arxiv_id: '2606.29706'
url: https://arxiv.org/abs/2606.29706
pdf_url: https://arxiv.org/pdf/2606.29706
published: '2026-06-29'
collected: '2026-07-01'
category: RAG
direction: 检索增强生成 · 自适应检索器优化
tags:
- RAG
- retriever optimization
- low-resource QA
- temperature learning
- contrastive learning
- query adaptation
one_liner: 冻结生成器，仅微调查询编码器，联合 RAG 似然与 InfoNCE 并学习各自温度，提升低资源 RAG 效果
practical_value: '- **低资源检索适配策略**：当类目冷启或新业务标注稀疏时，可冻结下游生成/推荐模型，仅微调查询编码器，避免生成模型过拟合并保持通用能力，适合电商搜索中的长尾
  query 优化。

  - **多目标联合训练与可学温度**：将 RAG 生成质量信号（如点击/转化）与 InfoNCE 对比损失结合，为两个 softmax 分布分别学习温度参数，自动调节分布尖锐度，可迁移到推荐系统中平衡语义相关性与业务指标。

  - **正则化防遗忘**：微调查询编码器时加入与冻结基编码器的距离正则化，类似持续学习，适合在电商搜索中持续引入新知识而不破坏已有检索能力。

  - **温度分离控制**：在检索和对比学习中采用独立的可学温度，可解决电商搜索不同场景（导航 query vs 宽泛 query）对检索精细度的不同需求。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：电信问答证据分散，低资源子域中生成器微调易过拟合且损害通用能力。理论分析表明，在有限参数和软检索假设下，查询编码器调优的估计误差更小，因此转向冻结生成器、适应检索器的路线。

**方法**：提出 ARMOR，联合优化两个目标：
1. **RAG 文档似然**：最大化生成答案的正确性，梯度通过检索分布反向传播至查询编码器。
2. **InfoNCE 对比损失**：提升查询与相关文档的语义匹配几何。

为平衡两个目标，为 RAG 检索分布和 InfoNCE 的 softmax 各自学习一个温度参数，自适应控制平滑度；同时对查询编码器施加正则化，约束其不偏离冻结的基编码器，防止灾难性遗忘。

**结果**：在电信检索和生成 QA 基准上，ARMOR 比仅使用一个目标或固定温度的方法在证据召回和答案质量（ROUGE 等）上均有显著提升，验证了自适应温度与正则化的有效性。
