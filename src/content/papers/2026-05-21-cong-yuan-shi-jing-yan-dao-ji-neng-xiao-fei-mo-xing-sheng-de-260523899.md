---
title: 'From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated
  Agent Skills'
title_zh: 从原始经验到技能消费：模型生成Agent技能的全生命周期系统研究
authors:
- Zisu Huang
- Jingwen Xu
- Yifan Yang
- Ziyang Gong
- Qihao Yang
- Muzhao Tian
- Xiaohua Wang
- Changze Lv
- Xuemei Gao
- Qi Dai
affiliations:
- Fudan University
- Microsoft Research
- Shanghai Jiao Tong University
arxiv_id: '2605.23899'
url: https://arxiv.org/abs/2605.23899
pdf_url: https://arxiv.org/pdf/2605.23899
published: '2026-05-21'
collected: '2026-05-25'
category: Agent
direction: Agent技能生命周期分析与效用评估
tags:
- Agent Skills
- Skill Lifecycle
- Utility Evaluation
- Skill Extraction
- Negative Transfer
- Meta-Skill
one_liner: 系统评估模型生成领域技能全生命周期，揭示技能效用模式并提出元技能引导改善提取质量。
practical_value: '- 技能评估应引入效用导向指标（提取效力EE、目标可进化性TE），替代纯文本质量判断，避免因表面流畅性选择实际有害的技能。

  - 经验池中成功与失败轨迹的混合比例显著影响技能质量，应根据任务类型定向调控——多步推理类任务可适度增加失败样例，避免纯成功池造成过拟合。

  - 避免直接让LLM以“可读性”筛选技能，而是基于验证过的维度（如失败机制编码、可操作具体性、高风险操作黑名单）设计引导提示，用元技能先验提升提取的实战收益。

  - 技能在跨模型复用时表现差异大，消费方需进行小规模适配测试，电商/推荐Agent中应评估技能对不同基座模型的适用性，避免负迁移。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：语言Agent越来越多地通过复用技能（Skill）来积累经验，尤其是领域级、模型自动生成的技能能大幅降低人工成本。然而，现有工作大多只研究技能生命周期的单一阶段（如只评测消费效果），缺乏从经验生成、技能提取到技能消费的端到端系统性理解。这篇工作通过构建全生命周期评估框架，回答三个核心问题：模型生成的领域技能是否真正有效？何时有效？成功或失败的关键因素是什么？

**方法关键点**：
1. 定义三阶段流水线：目标模型在训练分割上执行任务生成包含成功与失败轨迹的经验池；提取器模型通过“逐轨迹分析+分层合并”的两阶段最小化框架将其蒸馏为结构化技能；同一目标模型在测试分割上使用该技能，以无技能基线为参照计算性能增益（∆）。
2. 引入两个解耦指标：**提取效力（EE）**测量固定提取器在不同目标上的平均增益；**目标可进化性（TE）**测量固定目标在不同提取器生成技能下的平均增益。
3. 覆盖五个差异化领域（ALFWorld、SpreadsheetBench、SWE-bench-Verified、SEAL-0、BFCL-v4），六个目标模型（GPT、Gemini、Qwen系列），五个提取器模型，形成完整的交叉矩阵。
4. 探究阶段驱动因素：操控经验池成功/失败比，对比技能格式与文本流畅度，分析跨模型迁移时的行为变化，并最终从高增益技能对中蒸馏出“元技能”准则。

**关键结果**：
- 模型生成技能在75%的配对上带来正向提升，但25%出现负迁移，且强大的任务执行者未必是优秀的技能提取者。
- 经验池的最佳成功/失败比因域而异：电子表格任务偏好高成功率池，软件工程任务倾向混合池，实体交互任务则失败轨迹信息量更大；纯失败池效果最差。
- 技能格式（有序/无序/清单/散文）和文本流畅度均无法预测实际效用，LLM评委在无指导下选择高增益技能的准确率仅46%，对差异>5pp的技能对更是逆转到15.8%。
- 经验合的验证准则（失败机制编码、可操作具体性、高风险操作黑名单）作为元技能注入提取prompt后，在所有测试单元中一致提升技能质量，平均额外增益+1.55pp，并将LLM判断准确率提升至73.8%。

**一句话总结**：技能效用只能通过效用指标检验，而非文本观感；基于领域特性和经验池组成的元技能引导能稳健改善提取质量。
