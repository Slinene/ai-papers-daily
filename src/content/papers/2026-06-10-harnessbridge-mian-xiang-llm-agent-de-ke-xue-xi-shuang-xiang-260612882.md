---
title: 'HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness'
title_zh: HarnessBridge：面向 LLM Agent 的可学习双向控制器
authors:
- Xiaoxuan Wang
- Haixin Wang
- Alexander Taylor
- Jason Cong
- Yizhou Sun
- Wei Wang
affiliations:
- University of California, Los Angeles
arxiv_id: '2606.12882'
url: https://arxiv.org/abs/2606.12882
pdf_url: https://arxiv.org/pdf/2606.12882
published: '2026-06-10'
collected: '2026-06-12'
category: Agent
direction: Agent 交互接口 · 可学习 harness 优化
tags:
- HarnessBridge
- LLM Agent
- Observation Projection
- Action Projection
- Instruction Tuning
one_liner: 将 Agent 与环境的交互接口参数化为可学习的双向投影，通过指令微调轻量模型，在提升任务成功率的同时大幅降低 token 消耗和轨迹长度。
practical_value: '- **可学习的交互策略**：Harness 不再靠人工规则，可用轻量模型学习观察压缩和动作拒绝策略，适用于电商客服 Agent、多步推荐交互等长周期对话场景，减少无效交互和上下文膨胀。

  - **双向投影设计**：Observation Projection 保留关键信息、压缩冗余、丢弃无关内容，并维护 active-state index，可直接复用到复杂
  Agent 的上下文管理中；Action Projection 通过轨迹证据拒绝无效动作并给出改进建议，可提升如工具调用、搜索 API 交互的效率。

  - **轻量模型的控制器模式**：用 0.8B 模型控制 35B+ 生成器，推理开销仅约生成器的 7%，该模式在成本敏感的电商 Agent 部署中极具参考价值，可用小模型做交互仲裁。

  - **统一指令微调范式**：将观察压缩与动作校验统一为条件生成任务，采集带约束的轨迹数据，可泛化到不同生成器，适合需要快速适配不同 LLM 后端的推荐或对话系统。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：LLM Agent 在长周期任务（如软件工程、终端操作）中重度依赖手工设计的 harness 来管理观察和动作，但随交互增长，手工规则难以扩展，常导致上下文膨胀、无效动作循环和过高 token 消耗。这个问题在需要多步工具调用和长时间交互的 agent 系统中尤为突出。

**方法关键点**：
- **双向投影策略**：将 harness 形式化为环境→Agent 的 observation projection 和 Agent→环境的 action projection。Observation projection 对原始轨迹单元做 pass/compress/drop 决策并产出 active-state index，仅暴露决策关键信息给生成器；Action projection 判断生成器提议动作是否应该执行，若拒绝则提供轨迹证据驱动的反馈（concern/evidence/suggestion）。
- **统一指令微调**：把两种投影都转换为条件生成任务，用同一个轻量模型（Qwen3.5-0.8B）进行指令微调，数据来自已解决任务的高质量轨迹，并强制要求压缩内容可溯源至原始历史。
- **数据筛选**：仅保留成功轨迹中的高质量投影决策，平衡 pass/reject 比例，避免过激压缩或永久性信息丢失。

**关键实验**：
- 在 Terminal-Bench 2.0 和 SWE-bench Verified 上测试 Qwen3.5-35B-A3B 和 GLM-4.7-Flash 等生成器。HarnessBridge 在 SWE-bench Verified 上成功率与最佳基线持平甚至更好，同时 token 消耗降低超 23%；在 Terminal-Bench 2.0 上对 Qwen3.5 成功率从 30.3% 提升到 33.7%，token 减少 46.8%。
- 泛化实验显示，用 Qwen 轨迹训练的 harness 可直接用于 GPT-5.4、Claude 等商业模型，成功率不降且 token 大幅减少（GPT-5.4-Nano 成功 +25%，token −90.7%）。
- 消融实验证实双向投影缺一不可，同时剔除任一模块都会降低成功率。

**核心洞察**：通过可学习的双向投影来优化 Agent 与环境的接口，不仅能压缩上下文、阻断无效动作，还能用极低的控制成本获得跨生成器的泛化能力，这为复杂 agent 系统的工业化部署提供了新的轻量范式。
