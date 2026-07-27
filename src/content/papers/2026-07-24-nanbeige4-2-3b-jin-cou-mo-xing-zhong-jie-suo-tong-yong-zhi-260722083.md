---
title: 'Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Mode'
title_zh: Nanbeige4.2-3B：紧凑模型中解锁通用智能体能力
authors:
- Nanbeige Lab
- ':'
- Chen Yang
- Chengrui Huang
- Fufeng Lan
- Hanhui Chen
- Hao Zhou
- Huatong Song
- Jiaqi Cao
- Jiaying Zhu
affiliations:
- Nanbeige Lab
- Boss Zhipin
arxiv_id: '2607.22083'
url: https://arxiv.org/abs/2607.22083
pdf_url: https://arxiv.org/pdf/2607.22083
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 紧凑通用智能体模型
tags:
- Looped Transformer
- Agentic RL
- tool use
- code agent
- office agent
- compact model
one_liner: 3B参数的紧凑模型在代码、办公、工具使用等智能体任务上全面超越9B/12B模型，同时保持强推理能力
practical_value: '- **多阶段 RLHF 通用化**：先对 Think/Non-Think 响应混合 RLHF，能跨任务、跨模式减少循环生成与格式错误，提升推理与智能体任务的稳定性。可用于电商对话/操作型
  Agent 的异常输出抑制。

  - **长度控制推理 RL**：离线建立长度预算+难度感知惩罚，鼓励简洁推理，可适配推荐解释或搜索推理链的延迟约束，平衡效率与效果。

  - **行动级过程奖励**：在 Agentic RL 中为工具调用准确性、信息增益设计逐步骤 rubrics 作为过程奖励，提供密集反馈，可迁移至交互式推荐 Agent
  的长程训练，稳定多步规划。

  - **混合环境数据合成**：组合真实 MCP 服务、Python 可执行接口和 LLM 模拟工具，扩大轨迹多样性。电商搜索推荐系统可借鉴构建高覆盖率的仿真环境，低成本生产高质量多轮交互数据。

  - **Turn-level loss masking**：仅对正确回合计算损失但保留错误上下文，适合训练多轮对话推荐，避免学习错误行为的同时利用完整语境恢复。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
小模型在单领域智能体任务（如代码、办公）已有突破，但缺乏通用性，常以牺牲推理能力为代价。本文探讨在一个 3B 参数预算下，能否同时支持代码、办公、复杂工具使用等多种智能体能力且保持强大推理性能。

**方法关键点**  
- **Looped Transformer**：重用同一 Transformer 层堆叠进行第二轮处理，在不增加参数的前提下提升有效深度与容量，从零预训练 28T tokens。  
- **SFT 数据合成**：构建覆盖仓库级代码、工具使用、办公任务的大规模轨迹。设计闭源仓库→任务→轨迹的闭环管线，利用执行信号和 rubric 进行轨迹级、回合级过滤；混合环境融合真实 MCP 服务、Python 可执行 API、LLM 模拟工具。  
- **多阶段 RL 流程**：① **两阶段 RLHF** 先对 Think/Non-Think 响应混合训练，抑制重复、格式错误等异常，跨任务、跨模式提升稳定性；② **长度控制推理 RL** 引入离线预算+难度感知长度惩罚，在正确率高的问题上鼓励简洁推理；③ **行动中心 Agentic RL** 使用结果奖励与工具调用准确性、信息增益等过程奖励，密集分配信用，稳定长程训练。

**关键结果**  
在 SWE-bench Verified（46.9% vs Qwen3.5-9B 33.8%）、PinchBench-V2（74.7% vs 68.2%）、MCP-atlas（57.8% vs 47.4%）、GDPval rubrics（74.3% vs Gemma4-12B 68.5%）等全面领先；推理任务 GPQA-Diamond 达 87.4%，HMMT-Feb-2026 达 82.8%，LiveCodeBench-V6 达 72.5%。在 OpenClaw 本地助理场景中，办公、深度研究任务显著超越同尺寸及 9B 模型。

**一句话**  
小模型通过架构巧思和数据/RL 工程的系统组合，可以在多维度智能体能力上反超数倍参数的大模型。
