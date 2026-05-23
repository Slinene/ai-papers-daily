---
title: Efficient Table QA via TableGrid Navigation and Progressive Inference Prompting
title_zh: 基于表格网格导航与渐进式推理提示的高效表格问答
authors:
- Amritansh Maurya
- Navjot Singh
- Mohammed Javed
- Omar Moured
affiliations:
- IIIT Allahabad
- Karlsruhe Institute of Technology
arxiv_id: '2605.20254'
url: https://arxiv.org/abs/2605.20254
pdf_url: https://arxiv.org/pdf/2605.20254
published: '2026-05-18'
collected: '2026-05-23'
category: Reasoning
direction: 表格问答提示工程
tags:
- Table QA
- Prompt Engineering
- LLM Reasoning
- Structured Data
- Fine-tuning
one_liner: 提出两种无需训练的提示框架 TGN 和 PIP，结构化解耦表格导航与推理，并可蒸馏为小模型监督信号
practical_value: '- **TGN 的三模块循环** 将表格推理分解为行导航、列导航、答案精炼，可复用于电商商品表格问答、客服对比查询等场景，提高定位准确率和可解释性。

  - **PIP 的显式列约束** 先强制识别相关列再过滤行，适用于结构化查询生成（如 Text2SQL），在推荐理由生成或属性抽取中可减少幻觉、提高检索精度。

  - **低资源监督蒸馏** 将 TGN/PIP 推理过程作为 fine-tuning 模板，在资源有限时让小模型逼近大模型效果，适合电商中大规模表格处理的成本控制。

  - **免训练快速迭代** 无需微调即可通过提示工程提升现有 LLM 的表格推理能力，适合业务快速验证和上线。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：表格问答要求 LLM 具备精确的单元格定位和多步推理能力，现有方法缺乏对导航过程的显式控制，容易产生幻觉或跳过步骤。

**方法**：提出两种结构化提示框架。`TableGrid Navigation (TGN)` 用三模块循环（行导航、列导航、答案精炼）迭代定位证据并优化答案；`Progressive Inference Prompting (PIP)` 则强制模型先识别相关列，再根据查询逐步约束行选择，形成显式的推理链。两者均无需训练，仅靠提示实现。

**结果**：在 TableBench 上，TGN 比最强基线提升 3.8 个点；在 FeTaQa 上，PIP 超越 ReAct 和 CoT 取得 SOTA。此外，这两种提示可作为监督模板微调小模型，显著缩小与大模型的效果差距，兼顾性能与成本。
