---
title: 'Orchestra-o1: Omnimodal Agent Orchestration'
title_zh: Orchestra-o1：面向全模态智能体的编排框架
authors:
- Fan Zhang
- Vireo Zhang
- Shengju Qian
- Haoxuan Li
- Hao Wu
- Jinyang Wu
- Donghao Zhou
- Zhihong Zhu
- Zheng Lian
- Xin Wang
affiliations:
- CUHK
- LIGHTSPEED
- PKU
- THU
- Tongji University
arxiv_id: '2606.13707'
url: https://arxiv.org/abs/2606.13707
pdf_url: https://arxiv.org/pdf/2606.13707
published: '2026-06-09'
collected: '2026-06-15'
category: MultiAgent
direction: 多智能体编排与训练
tags:
- Multi-Agent Orchestration
- Omnimodal
- GRPO
- LLM
- Agent Swarm
one_liner: 提出支持文本/图像/音频/视频的全模态多智能体编排框架，通过模态感知任务分解与并行执行实现高效协作。
practical_value: '- **多模态任务解耦**：将感知（图像/音频/视频分析）与行动（搜索、代码执行）拆分为专业化子Agent，由主Agent统一调度，可迁移至电商商品理解场景（如同时处理商品图、详情视频、用户评论）。

  - **依赖感知并行调度**：对无依赖的子任务（例如提取图像地点和音频事件）并行执行，显著降低延迟。在推荐系统流水线中，可并行请求多模态编码服务或外部知识库，加快响应速度。

  - **离线强化学习训练编排模型**：DA-GRPO 利用专家轨迹和四维奖励（格式、动作、工具合理性、决策质量）离线训练，无需在线执行子Agent即可获得密集监督。适合在内部数据上低成本训练任务编排模型，避免线上试错开销。

  - **能力匹配路由**：将工具/模型选择形式化为能力向量匹配问题，可根据子任务难度动态分配不同规格的模型（如轻量模型做简单提取，强模型做复杂推理）。电商搜索/推荐中可借鉴同类思路，按请求复杂度路由到不同算力资源。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有LLM智能体大多局限于文本或视觉，而真实场景中文本、图像、音频、视频共存且交互。原生全模态模型（如Gemini-3-Pro）在需要长程推理、工具使用等复杂任务上仅62.5%准确率，现有编排框架则缺乏统一的模态感知分解和并行机制。

**方法关键点**：
- **Orchestra-o1框架**：解耦高层编排与低层感知/行动，主Agent维护依赖图，将任务分解为可并行子任务，分派给配备专用工具的ReAct子Agent。
- **模态感知分解与并行**：识别子目标间的依赖，只有前置完成才执行，将就绪子任务并行调起，从理论上获得线性加速比。
- **能力匹配选择**：根据子任务需求向量与子Agent/工具的能力向量及成本-延迟属性，动态选择最优后端和工具组合。
- **DA-GRPO训练**：基于GRPO改进，使用专家轨迹和四维奖励（格式正确、动作有效、工具合理、决策质量）进行离线强化学习，训练开源主Agent（Qwen3-8B → Orchestra-o1-8B），避免在线执行昂贵的多智能体轨迹。
- **数据处理**：利用种子数据 + 五种改写策略（枢轴交换、时间偏移、数值重组等）生成1200条多样化训练样本，经LLM验证确保锚点事实覆盖和无模态捷径。

**关键实验**：
- 数据集：OmniGAIA，含文本/图像/音频/视频的9个类别的全模态基准。
- 对比：原生全模态模型（Gemini-3等）、编排框架AOrchestra。
- 主结果：GPT-5作为主Agent时达到72.8%准确率，超越Gemini-3-Pro 10.3%，比AOrchestra提升32.8%，同时成本更低（341.6 vs 565.7）；开源Orchestra-o1-8B达到30.0%，大幅领先之前最佳开源模型20.8%；困难任务上提升尤其明显。

**核心洞察**：显式编排带来的模块化、并行化和专业化能力，让多模态智能体系统在性能和效率上均优于单一大模型的“通才”方案。
