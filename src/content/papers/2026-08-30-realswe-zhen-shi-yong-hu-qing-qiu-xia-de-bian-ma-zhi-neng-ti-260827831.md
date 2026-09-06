---
title: 'RealSWE: A Compositional Evaluation of Coding Agents under Realistic User
  Requests'
title_zh: RealSWE：真实用户请求下的编码智能体组合评估
authors:
- Gyuhyeong Kim
- Hyojung Gwon
- Jeonghyeon Kim
- Kyuhong Shim
- Sunjae Lee
affiliations:
- Sungkyunkwan University
arxiv_id: '2608.27831'
url: https://arxiv.org/abs/2608.27831
pdf_url: https://arxiv.org/pdf/2608.27831
published: '2026-08-30'
collected: '2026-09-06'
category: Eval
direction: Agent 评估与提示信息组合优化
tags:
- LLM
- Coding Agent
- Benchmark
- Prompt Engineering
- Evaluation
- Realistic Inputs
one_liner: 构建多变量基准RealSWE，发现真实请求使LLM编码性能平均下降6.4pp，且明确期望行为与动机可显著提升表现
practical_value: '- 在电商/搜索/推荐的对话式 Agent 或购物助手中，用户输入通常短且非正式，应通过追问或模板引导用户明确“期望行为”和“动机”，而不是补充环境信息或复现步骤；这些高信息密度字段能显著提升任务解决率。

  - 设计 Agent 评估集时，可借鉴 RealSWE 的多变量任务家族思路：同一任务只改变信息构成和语言风格，能更稳健地测量模型对真实用户输入的适应性，避免仅用结构化基准数据高估能力。

  - 对 prompt 工程中的上下文模块做消融测试：若某些模块（如环境信息、复现步骤）只增加 token 和延迟而无实际收益，应将其裁剪或折叠为可折叠摘要，降低推理成本。

  - 训练或微调面向真实用户的 Agent 时，可加入非正式、缺失关键信息的样本，增强模型从简短输入推断意图和补全需求的能力。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 编码 Agent 主要用 SWE-bench 系列基准评估，其任务来自结构化的 GitHub issue，信息丰富且正式；但真实用户请求通常短、非正式、信息缺失，两者存在显著差异。

**方法**：作者定义六类信息分类法和四个语言风格维度，分析 SWE-chat 真实用户 prompt 与 SWE-bench Verified/Pro 的 problem statement。基于分布差异，提出 RealSWE：381 个多变量任务家族，源自 SWE-bench Verified 和 Pro，同一任务共享底层代码和 gold patch，仅改变信息构成和语言风格。用七款主流 LLM 评估。

**关键结果**：真实用户 prompt 中 88% 只含问题陈述或仅少量上下文，而基准中仅 7%；87% 真实 prompt 为非正式风格，94% 基准为正式风格。在 RealSWE 上，真实输入使模型解决率平均下降 6.4 个百分点，并可能改变模型排名。控制实验发现：包含 Desired Behavior 和 Motivation 会显著影响性能，而 Environment Information 和 Reproduction Steps 仅增加 token 无实际收益；语言风格影响较小且依赖于具体模型。结论：用户明确表达期望行为和动机，能大幅提升 LLM 的软件工程表现，尽管真实 prompt 中常被省略。
