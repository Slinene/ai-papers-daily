---
title: 'Agentic Abstention: Do Agents Know When to Stop Instead of Act?'
title_zh: 智能体弃权：何时停止行动而非继续交互
authors:
- Han Luo
- Bingbing Wen
- Lucy Lu Wang
affiliations:
- University of Leeds
- Southwest Jiaotong University
- University of Washington
- Allen Institute for AI
arxiv_id: '2606.28733'
url: https://arxiv.org/abs/2606.28733
pdf_url: https://arxiv.org/pdf/2606.28733
published: '2026-06-26'
collected: '2026-07-01'
category: Agent
direction: Agent 弃权决策与上下文工程
tags:
- Agentic Abstention
- LLM Agents
- Benchmark
- Context Engineering
- WebShop
- Terminal-Bench
one_liner: 研究LLM智能体在任务不可行时的弃权决策，揭示及时弃权是主要瓶颈，并提出用少量交互轨迹蒸馏停止规则以显著提升弃权效率和成功率。
practical_value: '- **电商对话Agent应具备环境感知的及时弃权机制**：当用户需求无法在商品库中满足时（如“买粉色客厅枕头”但无粉色枕头），Agent不应持续无效搜索，而应在首次搜索失败后即停止并提供替代建议，避免浪费推理资源和用户等待时间。

  - **利用少量失败轨迹提炼弃权规则**：借鉴CONVOLVE方法，用极少（20条）不可行任务的交互日志生成动态“弃权手册”，注入系统提示，可显著提升Agent对不可行需求的及时识别，无需模型重训，适用于快速迭代的在线购物助手。

  - **评估指标需侧重及时性**：放弃率（AbsRec@K）和路径加权成功率（SPL）比单纯的任务完成率更能反映Agent的决策效率。在电商Agent评测中加入“最早可弃权步”的标注，可精准定位Agent是否过度搜索或过早放弃。

  - **Agent脚手架设计影响弃权行为**：在终端/工具调用场景中，不同的Agent框架（如Codex CLI vs Terminus 2）会显著影响弃权的时机和频率，说明即便基座模型相同，交互循环设计和观测结构也会左右Agent的“止损”能力，推荐场景应选择弃权保守性更适中的框架。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM智能体（Agent）主要关注任务完成能力，但真实应用（如电商购物、终端操作）中大量指令本身不可行或交互后才发现无解。若Agent一味继续搜索、点击，不仅浪费计算资源，还损害用户体验。文中定义“智能体弃权”（Agentic Abstention）为多步交互中判断何时应停止行动的序列决策问题，区别于传统QA场景的单步弃权。

**方法关键点**：
- 将弃权建模为部分可观察马尔可夫过程，动作空间包含执行、回答、弃权，弃权仅在任务不可行或信息不足以解决时发生。
- 在WebShop（网页购物）、Terminal-Bench 2.0（终端任务）和交互式问答三个场景构建超过28,000条指令的弃权基准，包括请求层面的不可行（如主观偏好、欠指定、假前提）和环境层面的不可行（如隐藏目标商品、移除前置文件）。
- 评估13种LLM及2种Agent脚手架，并设计及时弃权召回（AbsRec@K）和路径加权成功率（SPL）等指标。
- 提出CONVOLVE：一种上下文工程方法，从少量（20条）交互轨迹中通过反思模型提炼出分块的弃权规则手册（playbook），注入新任务的系统提示，无需微调模型参数。

**关键结果**：
- 所有模型及时弃权率均低，网页场景最佳及时弃权召回仅26.7%，终端场景仅21.6%；QA中假前提和欠指定意图类最为困难。
- 扩大模型规模仅提升最终弃权率，不改善及时性；推理增强反可能降低总体弃权率；Agent脚手架对弃权影响显著。
- CONVOLVE使Llama-3.3-70B的及时弃权率从26.7%升至57.4%，总体弃权率达到100%，小模型生成的规则同样可有效迁移到大模型。

**核心启示**：智能体弃权的关键不是“最终能否放弃”，而是“能否在最早可能时刻停止”；用极低成本的离线下文蒸馏即可逼近最优弃权行为，为生产级Agent的容错与成本控制提供实用路径。
