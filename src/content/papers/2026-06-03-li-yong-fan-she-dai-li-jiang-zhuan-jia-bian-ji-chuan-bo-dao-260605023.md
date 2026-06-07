---
title: Scaling Expert Feedback with Reflective Edit Propagation in Compositional Knowledge
  Bases
title_zh: 利用反射代理将专家编辑传播到组合知识库
authors:
- Jiajing Guo
- Xueming Li
- Jorge Piazentin Ono
- Wenbin He
- Liu Ren
affiliations:
- Bosch Research North America
- Robert Bosch GmbH
arxiv_id: '2606.05023'
url: https://arxiv.org/abs/2606.05023
pdf_url: https://arxiv.org/pdf/2606.05023
published: '2026-06-03'
collected: '2026-06-07'
category: Agent
direction: 知识库构建 · 反射式传播编辑
tags:
- Knowledge Base
- Reflective Agent
- Edit Propagation
- Human-in-the-loop
- Intent Inference
one_liner: RAID 系统通过意图推理和反思式规划，将单条专家修正自动传播到全部知识条目，实现规模化知识库维护
practical_value: '- 电商后台商品知识库维护：当专家修正一条属性描述（如规格、材质）时，可自动识别隐含意图并传播修正到所有相关商品条目，减少重复审核。

  - 多模态/预标注数据清洗：在 Agent 辅助标注流程中，利用反思式规划将标注人员的单次修正规则泛化，批量修正相似错误，提升数据迭代效率。

  - 客服系统 FAQ 库更新：将人工对一条 FAQ 的修正意图（如更新政策）传播到所有相关文档，保持知识一致性，降低运维成本。

  - 人机协同的 Agent 设计范式：借鉴“意图推理 → 反思计划 → 用户确认执行”的三步结构，在推荐解释生成、风险文案修正等场景中平衡自动化与专家控制。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：垂直领域知识库依赖专家手工审核，LLM 可高效生成初稿但逐条校对不可扩展。传统“修正-保存”模式无法将单次专家反馈转化为全局性知识更新。
**方法**：提出 RAID 系统，包含三个关键组件：(1) Intent Inference：从单条专家编辑中推断语义意图；(2) Reflection-based Planning：基于意图反思，生成包含候选修订项的传播计划；(3) User Controlled Execution：由用户选择执行，确保安全可控。系统利用 LLM 作为反射代理，在结构化知识库上实现编辑的自动化传播。
**结果**：在公开数据集上验证了意图推理和传播的可行性，专家用户研究表明 RAID 能有效捕获专家修正意图并扩展到整个知识库，减少了人工审核工作量，并支持在工业知识库中规模化推广专业经验。
