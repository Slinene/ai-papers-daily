---
title: 'Towards Verifiable Multimodal Deep Research: A Multi-Agent Harness for Interleaved
  Report Generation'
title_zh: 迈向可验证多模态深度研究：交错报告生成的多智能体框架
authors:
- Chenghao Zhang
- Guanting Dong
- Yufan Liu
- Tong Zhao
- Zhicheng Dou
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2605.29861'
url: https://arxiv.org/abs/2605.29861
pdf_url: https://arxiv.org/pdf/2605.29861
published: '2026-05-27'
collected: '2026-05-30'
category: MultiAgent
direction: 多Agent协同生成可验证多模态报告
tags:
- Multimodal
- Multi-Agent
- Factual Grounding
- Vision-Language Models
- Report Generation
one_liner: Ptah通过多智能体编排、视觉工作记忆和验证器确保图文交错报告的可靠性与跨模态一致性。
practical_value: '- 多智能体任务编排：将深度研究拆解为规划、研究、写作阶段，各阶段由专职Agent负责，电商Agent系统可借鉴此分工模式（如商品详情生成时，信息采集、文案撰写、事实核查分离）

  - 验证器作为质量守门人：通过独立Verifier Agent在执行过程中持续检查事实基础、引用一致性和跨模态对齐，可引入到生成式推荐或自动文案管线中，降低幻觉风险

  - 视觉工作记忆机制：用结构化记忆维护多模态证据的来源对应关系，避免图文错配，电商多模态Agent在生成商品描述或对比评测时可直接复用类似设计

  - 评估协议PtahEval的启示：在传统文本评估外增加图像级和呈现级指标，业务中评价多模态推荐或交互式报告时可设计类似的分层评测体系'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM驱动的自主Agent已从简单事实检索走向深度研究报告生成，但可验证的多模态深度研究仍面临挑战——开放式合成缺乏确定性真值，且需将文本论证与视觉证据交错呈现。现有方法难以保证事实可靠性与跨模态一致性。

**方法**：提出Ptah，一个多智能体框架，覆盖从用户查询到Web渲染报告的完整生命周期。规划阶段，视觉感知Agent构建包含图文元素的计划；研究阶段，Agent基于声明确收集证据，并用“视觉工作记忆”维护与源对齐的图像；写作阶段，通过声明式多模态工具调用生成交错报告。关键创新是加入Verifier Agent作为接受函数，在流程中持续检查事实基础、引用保真度和跨模态一致性，确保输出可靠。此外，设计PtahEval评估协议，在图像层和呈现层增强现有基准。

**结果**：在深度研究基准上，Ptah生成的报告在可靠性、视觉信息量和人类可用性上均显著优于强基线，验证了多智能体协作与内置验证的有效性。
