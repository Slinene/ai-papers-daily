---
title: Instruction Duplication as an Inference-Time Control Primitive
title_zh: 指令复制作为推理时控制原语
authors:
- Victor Lavrenko
affiliations:
- PeaceTech VC, Israel
arxiv_id: '2609.04024'
url: https://arxiv.org/abs/2609.04024
pdf_url: https://arxiv.org/pdf/2609.04024
published: '2026-09-03'
collected: '2026-09-06'
category: LLM
direction: LLM 推理时控制与轨迹利用
tags:
- instruction duplication
- inference-time control
- procedural following
- trajectory state
- answer engineering
one_liner: 重复程序性指令可在不改训练/解码下提升过程遵循，下游轨迹消费时价值显著
practical_value: '- 在需要显式推理轨迹的推荐/搜索场景（如商品推荐理由生成、多步 Agent 决策、查询改写），对关键过程指令做重复（尤其 trailing
  duplicate）可低成本提升过程遵守，且不改变最终答案分布，便于下游解析和修复。

  - 评估 LLM 应用时不能只看最终准确率，需增加过程遵循指标（如关键步骤覆盖率、premature commitment）；否则可能低估指令重复等推理时控制的效果。

  - 若下游系统消费轨迹（如规则校验、多级推荐流水线、审核模块），指令复制可放大价值；否则可能只有微小提升。建议在关键流程指令或末尾约束处重复，并监控轨迹状态指标快速
  A/B 测试。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：可控语言模型系统需要过程遵循，特别是下游检查或修复生成轨迹时，但传统方法依赖重训练或解码改变。

**方法关键点**：提出指令重复——仅重复程序性指令，不改变模型权重或解码策略，作为黑盒推理时控制。在 7 个指令微调模型、300 个医学多选题、8 个放置条件下生成 16800 次，测量 All-8 诊断、TF-IDF recall、最终准确率、premature commitment；并在 Answer Engineering (AE) 场景中验证下游轨迹修复价值。

**关键结果**：从一份指令到两份，All-8 通过率从 90.22% 升至 93.17%（+2.95 pp，消除剩余失败 30.2%）；Pre-provisional TF-IDF recall 从 73.44% 升至 74.81%（+1.38，Holm 校正 p<0.001）；最终答案准确率保持 60.21%；premature commitment 从 1.52% 增至 2.30%（p=0.00536）。盲审未达预注册 28/30 确认标准（10/30 确认，20/30 平局）。但在下游 AE 中，trailing duplicate 将 SSNHL 端点从 84.2% 提升至 97.1%；传导诊断分支从 78.6% 降至 73.8%（仍高于无编辑基线 58.9%）。结论：指令复制是放置敏感的低复杂度控制，实际价值通过下游系统消费显式轨迹体现。
