---
title: 'Beyond NL2Code: A Structured Survey of Multimodal Code Intelligence'
title_zh: 超越自然语言到代码：多模态代码智能的结构化综述
authors:
- Xuanle Zhao
- Qiushi Sun
- Jingyu Xiao
- Xuexin Liu
- Haoyue Yang
- Qiaosheng Chen
- Xianzhen Luo
- Jing Huang
- Yufeng Zhong
- Lei Chen
affiliations:
- Meituan
- The University of Hong Kong
- The Chinese University of Hong Kong
- Institute of Automation, Chinese Academy of Sciences
- Nanjing University
arxiv_id: '2606.15932'
url: https://arxiv.org/abs/2606.15932
pdf_url: https://arxiv.org/pdf/2606.15932
published: '2026-06-15'
collected: '2026-06-25'
category: Multimodal
direction: 多模态代码智能综述 · 视觉到代码
tags:
- Multimodal Code Intelligence
- Visual-to-Code
- GUI Generation
- Survey
- Verification
- Agentic Code
one_liner: 系统归纳多模态代码智能任务，按代码角色与领域分类，提出以验证为中心的未来方向。
practical_value: '- 电商落地页、活动页自动生成：借鉴 GUI 代码生成方法，将设计稿或截图直接转化为前端代码，降低人工开发成本。

  - 多信号验证提升界面质量：在生成后结合视觉渲染对比、交互状态检查等互补信号，减少人工审核，提高生成代码的正确性与一致性。

  - 数据报表自动化：借鉴科学可视化代码生成（如 MatPlotAgent），从数据描述或示例图生成图表代码，用于自动化 BI 报表或运营分析。

  - Agent 工具使用与验证闭环：将代码作为可执行策略，利用多状态验证与视觉反馈确保 Agent 动作的可靠性，例如在交互式推荐场景中自动生成并验证 UI 操作脚本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 驱动了文本到代码的显著进步，但大量实际编程任务通过视觉产物（截图、图表、矢量图、视频、交互状态）表达意图，模型必须将视觉感知与可执行程序相连，因为正确性不仅依赖语法，还涉及布局、数据语义、交互行为和领域约束。现有研究分散，缺乏统一视角。

**方法**：该综述从代码在任务中的角色出发，将多模态代码智能划分为五大类：代码作为渲染产物、可编辑符号结构、科学表示、中间推理轨迹以及可执行策略或工具接口。进而按应用场景组织为四大领域：图形用户界面（GUI）、科学可视化、结构化图形、前沿任务与框架。在每个领域内整理基准与方法，并比较不同任务如何评估正确性证据。

**关键结果**：综述覆盖了 2024–2026 年间 40 余篇代表性工作，揭示了当前方法主要依赖单一视觉输入进行代码模仿，缺乏对执行后布局、交互、数据语义的多信号验证。为此提出四个验证驱动的未来方向：多信号验证（结合视觉渲染、执行结果等多重正确性证据）、多状态验证（跨交互轨迹测试行为）、跨任务迁移测试（探测可复用的视觉‑代码技能）、可验证的 Agent 轨迹（确保 Agent 决策基于视觉证据）。该框架旨在推动领域从单输出模仿走向证据支撑的可执行系统。
