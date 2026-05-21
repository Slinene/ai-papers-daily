---
title: 'IndusAgent: Reinforcing Open-Vocabulary Industrial Anomaly Detection with
  Agentic Tools'
title_zh: IndusAgent：工具增强的代理框架实现开放词汇工业异常检测
authors:
- Rongbin Tan
- Fangfang Lin
- Zhenlong Yuan
- Min Qiu
- Kejin Cui
- Mengmeng Wang
- Yi Wang
- Zijian Song
- Zhiyuan Wang
- Jiyuan Wang
affiliations:
- Institute of Computing Technology, CAS
- Santa Clara University
- New York University
- Sun Yat-sen University
- Nanyang Technological University
arxiv_id: '2605.20682'
url: https://arxiv.org/abs/2605.20682
pdf_url: https://arxiv.org/pdf/2605.20682
published: '2026-05-19'
collected: '2026-05-21'
category: Agent
direction: 多模态 Agent 工具调用与 RL 优化
tags:
- Agent
- Tool-Use
- Reinforcement Learning
- Anomaly Detection
- Multimodal
- Zero-Shot
one_liner: 提出工具增强代理框架，通过门控RL优化工具调用，在工业异常检测中取得SOTA零样本性能
practical_value: '- 在电商多模态对话中，借鉴动态区域裁剪和高频特征增强工具，帮助模型准确定位商品瑕疵或色差，减少视觉幻觉。

  - 门控强化学习目标可优化 Agent 系统中的工具调用决策，在客服机器人调用知识库或视觉工具时，实现效率与任务性能的联合优化。

  - 构建类似 Indus-CoT 的结构化数据：将全局观察、局部细节与领域先验融入推理轨迹，用于微调推荐或质检模型，提升对商品属性的细粒度理解。

  - 利用先验检索增强推理：在商品合规检查时，检索标准图作为正常先验，通过对比判断异常，可迁移至电商商品验证场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多模态大模型在开放词汇工业异常检测中存在领域不对齐推理和幻觉问题，难以分辨细微异常。

**方法**：提出 IndusAgent 代理框架。首先构建 Indus-CoT 数据集，融合全局视觉、高分辨率局部块和专家正常先验，提供精细的检测轨迹监督以微调模型。代理动态调用外部工具：动态区域裁剪、高频特征增强和先验检索，主动解决视觉歧义。引入门控强化学习目标，联合优化异常分类、定位精度、类型推理及工具使用代价，确保仅在有益时调用工具。

**结果**：在 MVTec-AD、VisA、MPDD、DTD、SDD 五个基准上，零样本性能全面领先现有方法，验证了鲁棒性和泛化能力。
