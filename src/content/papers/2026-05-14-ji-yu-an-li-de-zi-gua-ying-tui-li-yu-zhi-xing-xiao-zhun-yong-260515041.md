---
title: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use
title_zh: 基于案例的自适应推理与执行校准用于LLM工具调用
authors:
- Renning Pang
- Tian Lan
- Leyuan Liu
- Piao Tong
- Sheng Cao
- Xiaosong Zhang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2605.15041'
url: https://arxiv.org/abs/2605.15041
pdf_url: https://arxiv.org/pdf/2605.15041
published: '2026-05-14'
collected: '2026-05-16'
category: LLM
tags:
- CBR
- Tool Use
- Adaptive Reasoning
- RL
- Schema-Faithful Execution
- LLM
one_liner: 利用历史执行轨迹构建案例，提取复杂度与失败轮廓，联合校准推理预算与工具执行结构
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
工具使用拓展了大模型的能力边界，但可靠的工具调用要求在推理深度与结构有效性之间取得平衡。不同查询需要的中间推理量不同，统一策略要么冗长低效，要么造成关键约束验证不足。同时，工具执行受严格的结构约束，传统强化学习仅提供粗粒度任务反馈，难以定位函数名、参数类型、约束违反等细粒度错误。现有工作将推理控制和执行优化视为独立问题，缺少根据历史执行经验联合校准两者的机制。

## 方法关键点
- **执行案例构建**：将历史工具调用轨迹组织为结构化案例，包含查询、推理链、工具调用、执行结果及案例轮廓。
- **案例轮廓提取**：从基模型的执行行为中自动推导复杂度轮廓（hardness score）和失败轮廓（记录函数名、参数键、类型、约束、值等维度错误）。
- **推理预算校准**：利用复杂度轮廓控制长度惩罚强度，简单案例强惩罚避免过度推理，困难案例保留充足推理空间，使模型自主学会简洁或充分的思考链。
- **模式忠实工具优化**：基于失败轮廓定义六维结构奖励（名称、键、类型、约束、值、精确匹配），提供密集可解释的归因信号，将自由推理转化为结构合规的工具动作。
- **训练流程**：在SFT预热后，采用GRPO算法，将上述轮廓信号注入复合奖励（推理侧、格式侧、工具侧），并结合Easy-to-Hard课程策略稳定训练。

## 关键实验
在BFCLv2和ToolBench上评估，以Qwen2.5-7B-Instruct、Qwen2.5-Coder-7B-Instruct、Llama-3.2-8B-Instruct为骨干，对比SFT、GRPO及多个工具使用方法。CAST在Qwen2.5-7B-Instruct上BFCLv2总体执行准确率达88.43%（+5.85 vs SFT），平均推理长度减少26%（175.4 tokens vs 236.9）。在Qwen2.5-Coder-7B-Instruct上，Live执行提升至82.43%（+7.51）。ToolBench任务成功率同样显著提升（Pass 80.67%，Win 79.43%）。消融表明，联合校准两个轮廓才能获得最佳效果；复杂度轮廓使GRPO训练方差显著下降。

## 核心启示
历史执行案例不仅是监督样本，更是结构化的校准知识源——通过复杂度与失败轮廓，可以驱动LLM在工具使用中自适应地分配推理预算并严守调用规范。
