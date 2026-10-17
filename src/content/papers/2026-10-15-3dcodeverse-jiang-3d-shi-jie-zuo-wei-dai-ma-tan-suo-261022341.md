---
title: '3DCodeVerse: Exploring 3D Worlds as Code'
title_zh: 3DCodeVerse：将 3D 世界作为代码探索
authors:
- Yipeng Gao
- Ziyao Zeng
- Jinfa Huang
- Yijiang Li
- Haolin Xiong
- Wang Qin
- Xinlei Yu
- Youheng Yao
- Jie Zhang
- Kun-Yu Lin
affiliations:
- University of Southern California
- Yale University
- University of Rochester
- University of California, San Diego
- Google DeepMind
arxiv_id: '2610.22341'
url: https://arxiv.org/abs/2610.22341
pdf_url: https://arxiv.org/pdf/2610.22341
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智能体 3D 代码生成与验证
tags:
- 3D coding
- Multi-agent
- Code Generation
- Automated Verification
- Fine-tuning
- LLM
one_liner: 构建可执行 3D 代码数据集与多智能体验证框架，微调开源模型显著提升 3D 代码生成质量
practical_value: '- 构建领域专用代码生成系统时，可借鉴“可执行验证 + 视觉反馈”闭环：让 agent 生成的代码在沙箱中执行，结合空间测量与渲染截图，自动筛选和修正，减少人工评估成本。

  - 多智能体 DAG 编排比单轮生成更稳定：将需求拆解为独立节点（生成、校验、修正），每个节点有明确输入输出和失败重试，适合电商场景中复杂的代码/工具调用任务（如数据管道、商品页面生成）。

  - 高质量可执行代码数据集是微调开源模型的关键：通过收集开源代码、格式转换与 agent 合成扩充，打包运行时环境与验证记录，可低成本复用于内部工具调用或结构化生成任务。

  - 组件级消融与胜率评估提供工程取舍依据：在真实业务中，针对自动评估管线做组件级分析，能快速定位影响生成质量的关键环节，避免盲目堆叠。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 在通用代码生成上表现提升，但 3D 场景/对象等可编辑、可验证的代码生成仍缺乏高质量数据集与评估手段，阻碍开源模型能力提升。

**方法**：3DCodeVerse 包含三部分。一是 3DCodeVerse-2M 数据集：收集开源 3D 代码、转换专用表示、用编码 agent 生成新程序，每个样本打包源码、运行环境、描述和验证记录。二是 3DCodeVerse Harness：多智能体有向无环图（DAG）框架，通过执行检查、空间测量和视觉反馈自动评估并迭代修正生成程序，生成过程中无需人工反馈。三是系统实验：微调开源模型建立基线，对 harness 各组件做消融，归纳 3D 编码实践建议。

**关键结果**：在 3DCodeVerse-2M 上微调显著提升开源模型 3D 编码能力；当 Claude Opus 5.5 使用该 harness 时，与 Claude Design (3D Object) 的成对人工评估取得 90% 胜率。
