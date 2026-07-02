---
title: Can Agents Generalize to the Open World? Unveiling the Fragility of Static
  Training in Tool Use
title_zh: 智能体能否泛化到开放世界？揭示工具使用中静态训练的脆弱性
authors:
- Song-Lin Lv
- Weiming Wu
- Rui Zhu
- Zi-Jian Cheng
- Lan-Zhe Guo
affiliations:
- Nanjing University
arxiv_id: '2607.01084'
url: https://arxiv.org/abs/2607.01084
pdf_url: https://arxiv.org/pdf/2607.01084
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 工具使用泛化与鲁棒性
tags:
- tool-use
- generalization
- open-world
- robustness
- perturbation-augmented fine-tuning
one_liner: 发现静态训练的工具使用智能体在开放环境分布偏移下性能脆弱，并提出扰动增强微调策略增强鲁棒性
practical_value: '- **电商智能助手/广告投放 Agent 的鲁棒性设计**：在真实业务中，用户查询、工具接口、返回数据格式会频繁变化。论文的四层偏移（感知、交互、推理、内化）框架可直接用于梳理生产环境
  Agent 的脆弱点，例如商品描述变化（感知偏移）、API 参数重命名（交互偏移）、促销规则修改（推理偏移）、知识库更新（内化偏移）。

  - **训练阶段引入数据扰动**：借鉴扰动增强微调策略，在 SFT 阶段针对查询改写、工具说明扰动、观察噪声等构造对抗样本，低成本提升 Agent 对线上突发变化的容忍度，避免频繁重训。

  - **评估测试集设计**：构建类似沙盒环境，按分布偏移等级设计回归测试集，用于持续监控上线 Agent 的泛化能力，尤其在新品类、新营销工具上线时把关。

  - **多维度泛化诊断**：论文的四层层次化偏移可作为多维度 QoS 指标，指导 Agent 在搜索推荐场景下（如商品智能推荐对话、投放策略多步推理）的优化方向，明确是哪个层次出现问题。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 在静态工具使用基准上表现优异，但真实业务环境（如电商搜索助手、广告投放助手）中用户需求、工具集、交互反馈持续变化，现有 SFT 或 RL 训练的 Agent 泛化能力堪忧。

**方法关键点**：
- 将开放世界工具使用问题形式化为 OpenAgent 设定，涵盖查询、动作、观察、领域四个维度的分布偏移。
- 构建可控沙盒环境，定义四层递进式环境偏移：感知（如工具描述、用户表达方式）、交互（如工具返回值格式、顺序）、推理（如同一工具解决不同子树问题）、内化（如新工具组合、领域知识更新）。
- 对 SFT 和 RL 训练的开源 Agent 进行全面诊断实验，发现两类训练方式在面对上述偏移时性能均显著下降。
- 提出 **扰动增强微调**（Perturbation-Augmented Fine-Tuning），在 SFT 阶段对训练数据施加感知、交互、推理层面的扰动，迫使模型学习不变表征，从而改善对开放偏移的鲁棒性。

**关键结果**：实验表明未经干预的 Agent 在不同层级偏移下成功率下降 10%~30%，而扰动增强微调可有效缩小泛化差距，部分偏移下性能接近静态分布水平。
