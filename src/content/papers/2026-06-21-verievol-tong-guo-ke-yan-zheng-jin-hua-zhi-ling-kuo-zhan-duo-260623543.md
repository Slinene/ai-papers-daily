---
title: 'VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct'
title_zh: VeriEvol：通过可验证进化指令扩展多模态数学推理
authors:
- Haoling Li
- Kai Zheng
- Jie Wu
- Can Xu
- Qingfeng Sun
- Han Hu
- Yujiu Yang
affiliations:
- Tsinghua University
- Tencent Hunyuan
arxiv_id: '2606.23543'
url: https://arxiv.org/abs/2606.23543
pdf_url: https://arxiv.org/pdf/2606.23543
published: '2026-06-21'
collected: '2026-06-25'
category: Reasoning
direction: 多模态推理数据的可控扩展与验证
tags:
- VeriEvol
- Multimodal Reasoning
- Data Scaling
- GRPO
- Hypothesis-Test Verification
- Agent
one_liner: 将多模态数学推理的数据扩展解耦为题目难度进化与答案可靠性验证，通过假设检验验证器保证标签质量
practical_value: '- 在生成式推荐训练中，可借鉴“进化指令”思想，通过特定操作（如替换属性、增加约束）从简单样本演化出难例，提升模型对复杂 query
  的泛化能力。

  - HTV-Agent 的假设检验验证机制可用于 Agent 决策的可信度评估：在推荐解释生成或用户意图理解时，利用多源证据交叉验证，拒绝不可靠输出。

  - 数据规模与标签可靠性解耦的方法可用于构建高质量训练集：先通过进化生成多样性数据，再用验证器过滤噪声标签，提升 RL 训练稳定性。

  - 对于 Agent 系统，可设计类似离线验证管道，在部署前对规划或建议进行多轮反证，增强安全性和可靠性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态数学推理的强化学习扩展面临两大挑战——题目难度不足与答案标签不可靠。现有管线盲目信任标注器，策略方法假设答案正确，导致大规模数据质量难以保证。

**方法**：提出 VeriEvol 框架，将扩展视为可验证的数据构建问题，解耦两个维度：① **难度扩展**：类型感知进化模块从低难度图像-问题种子出发，通过特定路由的进化操作（如图像修改、约束增加）生成更难的、锚定图像的提示；② **可靠性验证**：HTV-Agent 采用假设检验形式，收集多源反面证据，仅当无法驳斥答案时才接受该样本。框架迭代生成验证数据，可直接接入现有 GRPO 风格的 RL 训练。

**结果**：在五个视觉数学基准上，进化 SFT 数据从 10K 扩展到 250K 后，平均准确率从 35.42 升至 54.73。在固定模型与 RL 配置下，VeriEvol 相比未进化的 RL 基线累计提升 +3.88，其中进化提示贡献 +1.82，HTV-Agent 贡献 +2.06，验证了数据质量对推理性能的关键作用。
