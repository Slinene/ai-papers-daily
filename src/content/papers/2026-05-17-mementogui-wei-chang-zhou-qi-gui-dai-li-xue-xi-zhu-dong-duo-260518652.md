---
title: 'MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI
  Agents'
title_zh: MementoGUI：为长周期 GUI 代理学习主动多模态记忆控制
authors:
- Ziyun Zeng
- Hang Hua
- Bocheng Zou
- Mu Cai
- Rogerio Feris
- Jiebo Luo
affiliations:
- University of Rochester
- MIT-IBM Watson AI Lab
- University of Wisconsin-Madison
arxiv_id: '2605.18652'
url: https://arxiv.org/abs/2605.18652
pdf_url: https://arxiv.org/pdf/2605.18652
published: '2026-05-17'
collected: '2026-05-20'
category: Agent
direction: GUI 代理 · 主动多模态记忆管理
tags:
- GUI Agent
- Multimodal Memory
- Long-Horizon
- Episodic Memory
- Working Memory
- Memory Control
one_liner: 提出即插即用的主动多模态记忆框架，不微调 GUI 骨干，通过学习写入、压缩、检索视觉工作记忆与情景记忆提升长周期任务表现
practical_value: '- **双时间尺度记忆架构**：将记忆解耦为工作记忆（在线保存任务状态）和情景记忆（跨任务经验复用），可参考设计电商 Agent
  的长会话状态管理与跨会话知识积累，避免上下文无限膨胀。

  - **自动数据管线生成监督信号**：从交互轨迹自动构造步骤重要性、摘要、ROI 框和检索需求等训练标签，可迁移到对话或操作型 Agent 的记忆选择标注，降低人工成本。

  - **即插即用的记忆注入方式**：仅用文本摘要和 ROI 裁剪图像，不引入特殊 token 或架构改动，直接作为冻结 GUI 骨干的输入，便捷增强已有 Agent
  的长程决策能力。

  - **长周期评估指标**：提出基于 VLM 的语义动作匹配、任务进展、记忆一致性评分，可参考用于评估电商场景下多步任务的决策质量和记忆使用合理性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 GUI 代理在单步视觉定位与动作预测上进步明显，但长周期任务中跨界面状态保持仍然脆弱。常见方法依赖原始历史回放或纯文本记忆，要么引入冗余截图，要么丢弃局部视觉证据。因此，长周期 GUI 控制不应只视为上下文长度问题，而应抽象为主动记忆控制：何时更新记忆、保存什么、如何压缩、何时检索。  

**方法关键点**  
- **MementoGUI 框架**：冻结 GUI 动作骨干，外挂记忆控制器 MementoCore，将交互历史转化为决策导向的多模态上下文。  
- **记忆结构**：分为工作记忆（追踪任务内状态）和情景记忆（存储可跨任务复用的经验）。工作记忆按事件重要性阈值写入，含文本摘要和 ROI 裁剪图像；情景记忆通过向量粗排 + 学习型相关性选择精排。  
- **MementoCore 实现**：共享冻结 Qwen3-VL 骨干，附加四个 LoRA 适配器分别负责步骤处理（重要性评分、事件摘要、ROI 框、检索触发）、工作记忆压缩、情景记忆写入和情景记忆选择。记忆以文本和图像形式直接注入 GUI 骨干的输入，无需特殊 token 或架构改动。  
- **数据管线**：从计算机使用轨迹自动构造四个记忆操作的 SFT 数据，并对步骤处理和压缩模块构造 DPO 偏好对。  

**关键结果**  
在 GUI-Odyssey、MM-Mind2Web 和自建 MementoGUI-Bench 上，MementoGUI 在多个开源 GUI 骨干（UI-Venus-1.5-8B、MAI-UI-8B、GUI-Owl-1.5-8B/32B）及 API 代理（GPT-5.5、Gemini-3.1-Pro）上，一致超过无历史、历史重放和纯文本记忆基线。例如，GUI-Odyssey 上 UI-Venus-1.5-8B 的动作匹配从 54.58 提升至 68.32，轨迹成功率从 1.29 升至 3.57。消融实验证实 ROI 视觉证据和两阶段检索的增益，扩大控制器容量可进一步提升。
