---
title: 'First Things First: Teaching LLM-Based Agents to Prioritize Must-Haves before
  Nice-to-Haves'
title_zh: 先必备后可选：教 LLM Agent 区分需求优先级
authors:
- Tianjie Ju
- Xinyue Xu
- Wanxuan Sun
- Lingxiao Diao
- Gongshen Liu
- Zhuosheng Zhang
- Cheng Yang
affiliations:
- Shanghai Jiao Tong University
- ByteDance
arxiv_id: '2609.05224'
url: https://arxiv.org/abs/2609.05224
pdf_url: https://arxiv.org/pdf/2609.05224
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 需求优先级推理与强化学习
tags:
- requirement-aware reasoning
- MLLM agents
- reinforcement learning
- benchmark
- e-commerce
- must-have-nice-to-have
one_liner: 构建 FTF-Bench 并推出 FTF-RL，显著提升多模态 Agent 在电商/预订/出行中区分必备与可选需求的能力
practical_value: '- 在电商/预订/导购 Agent 中，让模型先输出结构化 `<requirements>` JSON（mandatory/optional
  分列）再做推理，能显著减少把 nice-to-have 当 must-have 或漏掉硬性需求的问题；可直接改造现有 prompt 或 SFT 模板。

  - RL 训练时，除了 answer accuracy，增加 requirement classification 的 Macro-F1 作为 reward，用
  GRPO + rule-based verifiable reward 即可轻量微调多模态 Agent，不需要复杂 reward model，适合业务侧快速自建。

  - 参考 FTF-BENCH 的 unanswerable 设置，在商品筛选/酒店预订/打车等场景中增加“无候选满足全部硬性条件”的拒答评估，强制模型输出 no-match，可降低实际交易中的错误推荐率。

  - 论文发现：仅在需求优先级数据上训练，就能在 LogicVista/MathVision/InfoQA 等通用推理任务上获得提升，说明显式的 must-have/nice-to-have
  拆解训练可以作为一种通用的 reasoning 能力增强手段。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

**动机**

真实用户请求往往同时包含 must-have 和 nice-to-have 需求。例如“预订无烟双人房，最好含早餐”，现有 MLLM agent 经常因为无法区分优先级而违反硬性需求，或把软性偏好当成硬性条件过度约束，甚至在无解时仍然硬推荐。该问题在电商、酒店预订、地图/打车等真实服务场景中尤其严重，但现有 instruction-following benchmark 通常把所有指令视为同等重要，掩盖了这一缺陷。

**方法关键点**

- 构建 **FTF-BENCH**：3,649 个图像-需求对，覆盖电商、预订、地图/出行三类场景；任务分为 single-answer（唯一满足 must-have）、multiple-answer（多个候选满足 must-have，需按 nice-to-have 优先级排序）、unanswerable（无候选满足全部 must-have，应拒答）三种。所有样本经人工校验。
- 提出 **FTF-RL**：多目标 rule-based reward 包括：format reward（XML 化输出 `<requirements>/<think>/<answer>`）、answer correctness（MLLM judge 判语义等价）、requirement classification reward（Macro-F1 区分 must_have/nice_to_have）。
- 使用 GRPO 优化，KL 约束到参考策略；在 Qwen2.5-VL 和 LLaVA 上训练。

**关键实验与结果**

- 当前 MLLM 在 Direct 设置下普遍失败：Qwen2.5-VL-72B 平均准确率仅 34.48%，7B 仅 21.05%；但提供 gold requirement labels 后，32B 可到 67.72%，说明瓶颈主要在需求解析而非视觉理解。
- FTF-RL 带来显著提升：Qwen2.5-VL-7B 平均准确率从 39.78 升到 55.80（+16.02），其中 multiple-answer 场景提升 26.38 个百分点；3B 和 LLaVA 也稳定提升。
- 泛化性：只在 FTF-BENCH 上训练，Qwen2.5-VL-7B 在 LogicVista 上从 43.40 升到 47.43，MathVision 和 InfoQA 也有提升。
- 消融显示所有 reward 组件都有贡献，移除 requirement reward 后 FTF-BENCH 掉 3.4 分，移除 answer reward 掉 7.5 分。

最值得记住的一句话：许多失败不是视觉理解差，而是没有显式区分 must-have 和 nice-to-have；增加一个简单的需求分类 reward，就能显著提升多模态 Agent 的可靠性和跨任务泛化能力。
