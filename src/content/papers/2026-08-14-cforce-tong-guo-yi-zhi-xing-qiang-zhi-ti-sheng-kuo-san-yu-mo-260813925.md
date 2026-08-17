---
title: 'CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing'
title_zh: CForce：通过一致性强制提升扩散语言模型并行解码
authors:
- Yuji Ren
- Chenkai Xu
- Zhuocheng Gong
- Jianguo Li
- Zhijie Deng
affiliations:
- Shanghai Jiao Tong University
- Ant Group
arxiv_id: '2608.13925'
url: https://arxiv.org/abs/2608.13925
pdf_url: https://arxiv.org/pdf/2608.13925
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: dLLM 并行解码一致性蒸馏
tags:
- dLLMs
- Consistency Distillation
- Parallel Decoding
- LLaDA
- Confidence Adaptive KL
- Self-rollout
one_liner: 提出 Consistency Forcing 蒸馏方法，用后期掩码预测监督早期预测，改善 dLLMs 高并行解码的质量
practical_value: '- **低延迟生成场景可迁移**：电商创意文案、商品标题、push 文案等对延迟敏感且可接受部分生成的场景，可以尝试用 dLLM
  并行解码替代 AR 解码，并采用 CForce 蒸馏抑制早期掩码预测错误传播，在高并行预算下获得更好的速度-质量权衡。

  - **蒸馏目标设计值得借鉴**：Confidence Adaptive KL 动态结合前向 KL（模式覆盖）和反向 KL（模式坍缩），可在推荐模型蒸馏、策略蒸馏或
  LLM 蒸馏中用于平衡学生模型输出的多样性与准确性，尤其适合标签软化的场景。

  - **自回滚轨迹训练提升训练-推理一致性**：业务中若使用迭代式生成（如多轮 Agent 交互、多次改写），可以收集模型自身推理轨迹，用后期步的高置信预测作为早期步的监督信号，缓解训练与推理分布不一致。

  - **edit-capable 解码的监督思路**：后期 token-to-token 修正可反哺早期 masked-state 预测，对带修正/编辑能力的生成流程（如搜索词改写、推荐理由生成）有参考价值。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：扩散大语言模型（dLLMs）通过单次前向预测多个掩码实现高速并行生成，但激进并行策略下早期去噪阶段预测不可靠，错误会传播到后期，导致质量下降。

**方法关键点**：
- 提出 Consistency Forcing（CForce），一种蒸馏方法，强制早期阶段的掩码预测与后期阶段对齐。
- 在预收集的自我推演轨迹上训练，改善训练-推理一致性。
- 引入 Confidence Adaptive KL Divergence 作为蒸馏目标，结合前向 KL 和反向 KL 的优点。
- 理论分析表明一致性目标可近似最小化早期阶段的预测误差。
- 方法同时适用于 mask-to-token 解码和 edit-capable 解码；在 edit-capable 场景中，后期的 token-to-token 修正为早期 masked-state 预测提供额外监督。

**结果**：在非编辑和可编辑的 LLaDA 模型上实验，CForce 改善了速度-质量权衡，尤其在高并行解码预算下优势明显；论文未给出具体数值，但图 1 展示了不同温度参数下速度-质量曲线的提升。代码开源。
