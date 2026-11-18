---
title: Sage S2.1 Flash Technical Report
title_zh: Sage S2.1 Flash 技术报告：320B 科学多模态与 Agent 模型
authors:
- Kun Cai
- Haodong Chen
- Guangran Cheng
- Qingxiu Cheng
- Xu Dai
- Guanting Dong
- Qiming Ge
- Lixin Gu
- Tao Gui
- Honglin Guo
affiliations:
- Shanghai AI Laboratory
- Fudan University
- Institute of Software Chinese Academy of Sciences
- Renmin University of China
- Institute of Automation Chinese Academy of Sciences
arxiv_id: '2611.21072'
url: https://arxiv.org/abs/2611.21072
pdf_url: https://arxiv.org/pdf/2611.21072
published: '2026-11-15'
collected: '2026-11-18'
category: Agent
direction: 多模态 Agent 与工具调用
tags:
- MoE
- Multimodal
- Agent
- Scientific AI
- Tool Use
- Benchmark
one_liner: 320B 参数 MoE 科学 Agent 模型，具备多模态科学感知能力并在可验证 Agent 基准上取得领先
practical_value: '- 多模态专用 encoder + projector 映射到共享 backbone 的架构，可迁移到电商商品理解：用独立 encoder
  处理商品图、分子式、谱图、文本，再统一投射进 LLM，避免 backbone 直接处理异构原始输入。

  - 构建可验证 Agent 环境（依据执行结果、环境状态变化或提交 artifact 判定任务完成），可用于电商运营类 Agent（改价、选品、生成报表、广告优化）的离线评估和
  RL 训练，降低人工标注成本。

  - 表格/文档工具链（SpreadsheetBench 2、OfficeQA Pro）和 CLI 任务（ALE-CLI）提示：电商报表自动化、出价/预算调整脚本可通过“提交产物校验”做可复现的离线评估，提高
  Agent 可靠性。

  - 模型在 ML 实验工作流上的强项说明：搜索推荐团队可将离线实验（训练/评估/调参）封装为可验证 Agent 环境，让 LLM 自动跑实验并依据指标决策，加速迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：通用模型在科学证据推理与交互环境中的能力不足，需要统一处理文本、图像、分子图、生物序列、光谱等多模态信息，并完成工具使用、搜索、编码等 Agent 任务。

**方法关键点**：
- 320B 参数 MoE backbone；
- Sage Sci-Perception 用专用 encoder 编码分子图、生物序列，将光谱表示为有序测量 patch；
- 通过 modality-specific projectors 映射到共享输入空间，与文本和图像一起处理；
- 构建可验证环境，任务完成依据执行结果、环境状态变化或提交 artifact 核查；
- 在 33 个 benchmark、7 个领域上评估。

**关键结果**：
- 与五个 baseline 对比，OfficeQA Pro 72.2、MLE-bench Lite 90.3 HumanRank、Harvey LAB、SpreadsheetBench 2 排名第一；
- OSWorld-Verified 85.2、WebArena-Verified 67.6、DeepResearch Bench II 54.2 排名第二；
- 强项在文档证据使用、可验证电子表格和 ML 实验任务，视觉反馈的桌面和浏览器工作流也有竞争力。
