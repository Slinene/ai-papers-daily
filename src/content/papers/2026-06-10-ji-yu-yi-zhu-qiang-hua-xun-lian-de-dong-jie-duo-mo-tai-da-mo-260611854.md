---
title: 'Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training'
title_zh: 基于艺术强化训练的冻结多模态大模型微调方法 ART
authors:
- Michal Chudoba
- Sergey Alyaev
- Petra Galuscakova
- Tomasz Wiktorski
affiliations:
- University of Stavanger
- NORCE Research
arxiv_id: '2606.11854'
url: https://arxiv.org/abs/2606.11854
pdf_url: https://arxiv.org/pdf/2606.11854
published: '2026-06-10'
collected: '2026-06-12'
category: Training
direction: 参数高效微调 · 视觉软提示 · 强化训练
tags:
- PEFT
- Visual Prompting
- Reinforcement Learning
- Multi-modal LLM
- vLLM
one_liner: 仅优化视觉像素输入实现软提示微调，无需修改计算图，兼容vLLM等高性能引擎
practical_value: '- **多租户微调部署**：若业务中部署多模态 LLM（如商品图文理解、交互式 Agent），ART 允许在不修改模型计算图的情况下注入任务知识，每个任务只需维护一个可学习图像，避免反复编译。这对
  vLLM 等高性能推理引擎极其友好，可大幅降低多下游任务切换的成本。

  - **快速实验与迭代**：改变优化目标或任务时，只需重新训练输入像素，无需动模型权重。强化学习优化（GRPO）使奖励设计更灵活，适合需要不断调整策略的应用场景，如对话式推荐中的响应优化。

  - **视觉软提示的可解释性与风格化**：优化的视觉输入可以呈现为任务相关的艺术图像，让调试更直观，也可作为一种隐式正则，提升模型对分布外输入的鲁棒性。在推荐系统中，可尝试为不同品类或人群生成专属“视觉提示”，辅助文本决策。

  - **兼容纯文本任务**：实验在数学和工具调用等纯文本基准上取得与 LoRA 相当的效果，证明即便下游任务无真实图像输入，ART 仍能有效注入信息，因此也适用于以文本为主的推荐或
  Agent 模型，前提是底层模型为多模态架构。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 PEFT 方法 LoRA 和 Soft Prompting 都需要修改预编译 LLM 的计算图，导致无法直接部署在 vLLM 等高吞吐推理引擎上。为突破这一限制，该工作提出 ART，利用冻结的多模态 LLM 的可视输入通道，仅优化原始像素作为“软提示”，无需更改模型图。

**方法**：将输入图像视为可训练参数，通过标准的反向传播将梯度传回像素数组，不对模型权重或计算图做任何改动。为此，需将文本指令与一张可学习图片拼接送入 MLLM，只对图片像素进行优化。该方法天然支持任意微调目标（如监督或强化学习），实验中采用了 GRPO 强化训练，并允许将优化后的像素渲染成任务相关的风格化图像（“计算艺术品”）。

**结果**：在 Qwen2-VL 与 Qwen2.5-VL（7B/72B）上，于 MATH、GSM8K 数学推理基准及 BFCL 工具调用基准上，ART 达到与 LoRA 媲美的准确率，且完全兼容 vLLM，在相同推理引擎下可获得显著的吞吐优势。
