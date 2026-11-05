---
title: 'WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution'
title_zh: WISE：面向整页多模态搜索体验归因的 Agent 框架
authors:
- Wenyi Xu
- Renzhe Zhou
- Songyang Li
- Feiran Zhu
- Ruoqi Zhao
- Chenglei Dai
- Xuanping Li
- Kaiqiao Zhan
- Jingwei Zhuo
affiliations:
- Kuaishou Technology
- Independent Researcher
arxiv_id: '2611.06777'
url: https://arxiv.org/abs/2611.06777
pdf_url: https://arxiv.org/pdf/2611.06777
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 化搜索质量归因与诊断
tags:
- Agent
- Search Quality Diagnosis
- LLM
- Multimodal
- GRPO
- Benchmark
one_liner: 以 Agent 框架联合问题发现与 pipeline 归因，配合 ReTrace 和 AHPO，将搜索质量诊断 E2E 准确率从 35.25%
  提升至 75.20%
practical_value: '- **证据隔离 + 分阶段诊断**：把搜索体验诊断拆成“问题发现→问题整合→pipeline 归因”，并用 harness 强制体验证据只用于发现问题、内部管线证据只用于归因。这一边界避免
  agent 过早偷看 pipeline 信息导致归因不真实，可直接借鉴到电商搜索 bad case 分析和推荐系统归因任务。

  - **ReTrace 最小轨迹修复**：专家只标注结果、没有执行轨迹时，不要全量重生成，而是定位最早可修复决策、冻结前缀、只修复后缀，且新增 tool call
  必须真实执行。相比 Full Regeneration，token 降低 36.25% 而 Case Attribution EM 持平，适合低成本构造 agent
  SFT 数据。

  - **AHPO 失败路由优化**：把诊断失败分为 harness 限制（证据不可达/动作不支持/状态无法表达）和 policy 决策错误两类，分别改执行框架或做
  GRPO。这套“先修 body 再修 brain”的路由在 200 个 case 上路由准确率达 84.2%，对多步 agent 的迭代调优非常实用。

  - **可落地的质量审计成本模型**：WISE 单日可处理 12 万搜索 case，诊断成本约 RMB 25.60/千例，是人工的 1/223，且将诊断结果反哺相关性模型训练后，离线
  F1 提升 10.2%，线上 CTR/LVR 正向、IQRR 下降。可作为搜索推荐团队搭建自动化质量监控和模型优化闭环的参考。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
算法驱动的搜索/推荐/广告系统往往运维指标健康，但结果质量仍可能很差。已有研究要么只做用户侧质量评估，要么只做系统运维故障 RCA，缺少对“结果质量问题出自 pipeline 哪个组件”的系统性诊断。论文将 System Quality Diagnosis (SQD) 定义为：不仅识别体验问题，还要跨组件归因，并聚焦工业搜索场景。

**方法关键点**
- **WISE Agent 框架**：诊断流程分为问题发现、问题整合、pipeline 归因、最终诊断四步。harness 控制证据隔离：体验证据（文本/OCR/ASR/视觉/时间/作者）先用于发现问题；内部管线证据（候选供给、召回路径、模型分数、排序位置）仅在确认问题后引入，避免信息泄露。
- **ReTrace**：专家标注只有诊断结果，缺少训练所需的执行轨迹。先由 teacher 生成轨迹，再定位最早可修复决策节点，冻结前缀、最小修复后缀；新增 tool call 必须通过实际执行获得 observation，最后验证终点与证据一致性。相比全量重生成，token 从 32.0k 降至 20.4k（-36.25%），Case Attribution EM 保持 57.87% 不变。
- **AHPO**：对失败 case 定位最早可支持的错误，路由判断：若证据不可访问、动作不受支持、或状态/模式无法表达正确结果，则更新 harness；否则收集 hard case 用 GRPO 优化 policy。奖励采用 schema-gated hierarchical reward：先保证主决策正确，再给予细粒度奖励。
- **WISE-Bench**：12,000 个真实快手搜索 case，两阶段人工标注：先用体验证据标注问题，再结合内部 trace 标注归因组件；划分 8k/2k/2k，覆盖问题发现、pipeline 归因、端到端诊断三项任务。

**关键实验**
在 Qwen3.5-35B-A3B 上，baseline E2E EM 35.25% → SFT 69.80% → SFT+AHPO 75.20%；Qwen3.5-4B 从 20.25% → 58.25% → 69.85%。固定模型权重仅优化 harness，GPT-5.6-Terra 的 E2E EM 也能从 65.85% 升至 69.75%，说明执行框架本身贡献显著。生产部署中，WISE 日处理约 12 万搜索 case，诊断成本从人工 RMB 5,714.29/千例降至 25.60/千例（降 99.55%）；用 WISE 挖掘的 220 万相关性高估样本训练相关性模型，离线 F1 从 0.573 提升至 0.631，线上 A/B 中 IQRR -0.11%、CTR +0.15%、LVR +0.20%。

**最值得记住的一句话**
把搜索质量诊断当成 Agent 任务，并用证据隔离、最小轨迹修复和失败路由优化，能让诊断从离线 benchmark 走到线上质量保障和模型优化闭环。
