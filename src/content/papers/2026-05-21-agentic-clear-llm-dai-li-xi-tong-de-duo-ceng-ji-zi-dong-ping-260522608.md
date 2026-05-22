---
title: 'Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents'
title_zh: Agentic CLEAR：LLM 代理系统的多层级自动评估框架
authors:
- Asaf Yehudai
- Lilach Eden
- Michal Shmueli-Scheuer
affiliations:
- IBM Research
arxiv_id: '2605.22608'
url: https://arxiv.org/abs/2605.22608
pdf_url: https://arxiv.org/pdf/2605.22608
published: '2026-05-21'
collected: '2026-05-22'
category: Eval
direction: 代理行为多层级自动评估
tags:
- Agent Evaluation
- Multi-Level Feedback
- LLM Judge
- Error Analysis
- Dynamic Taxonomies
- Observability
one_liner: 一种无需预定义错误分类的动态多粒度代理评估方法，自动生成系统、节点与步骤级的文本诊断洞察
practical_value: '- **多粒度自动诊断**：可将步骤级、trace级、系统级评估嵌入电商 Agent 开发流水线，自动发现重复工具调用、策略错误、输出格式违规等问题，替代人工逐条检查
  trace。

  - **无需预定义错误分类**：动态生成评估维度（rubric）和错误模式，适合频繁变化的推荐流程或购物 Agent，大幅降低适配成本。

  - **可集成到已有观测平台**：支持 LangFuse 格式，提供 PyPI 包，可以快速接入现有 Agent 观测系统，利用 LLM Judge 输出补充自动评分以外的文本解释。

  - **对齐人类标注的可靠参考**：与 TRAIL 错误分类的 macro-F1 达 0.459，能够替代部分人工审核，尤其适用于线上 Agent 质量监控与回归检测。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
代理系统在多步骤交互中变得愈发自主，但其行为评估仍依赖观测平台静态日志或手工错误分类，无法动态适应新任务。现有方法要么只提供基础指标，要么依赖固定分类体系，缺少可自动生成细粒度、可操作诊断的框架。  

**方法关键点**  
- **两级流水线**：先由 LLM Judge 对每条 trace 进行步骤级（Js）、trace 级（Jt）和基于任务生成 rubrics 的合规性评估（Jr+Jv）；随后用 CLEAR 算法聚类实例反馈，聚合为系统级和节点级洞察。  
- **三层输出**：系统级表面跨任务失败模式；节点级定位具体子代理（如规划节点、执行节点）的缺陷；trace 级保留每步的评分与原因。  
- **零预定义分类**：Judge 动态生成任务相关的评估标准和错误描述，不依赖固定错误类型。  
- **工程落地**：PyPI 包 + 命令行接口 + 交互式 UI，接收 LangFuse 格式 trace，直接嵌入开发流程。  

**关键实验**  
- 在 AppWorld、GAIA、SWE‑bench Verified Mini、τ²‑bench 四项基准及七种代理‑模型组合上验证（共计数万次 LLM 调用）。  
- 与人类标注的 TRAIL 错误分类对齐：GPT‑5 法官在 full+partial 匹配下 macro-F1 达 0.459，涵盖 12 个相关类别中的 10‑12 个。  
- 任务成功预测：AppWorld 上 AUC 最高 0.89（GPT‑5 trace 级评估），τ²‑bench 则因政策隐式性而偏低（≤0.62），说明方法信号因领域而异。  
- 法官模型对比：GPT‑5 输出比 OSS‑120B 更长、更领域具体，表明法官选择显著影响诊断深度。  

**核心结论**  
Agentic CLEAR 以无固定分类的方式实现了与专家分类高度一致的可操作诊断，为代理系统评估从“观察”迈向“理解与改进”提供了实用方案。
