---
title: 'TVIR: Building Deep Research Agents Towards Text--Visual Interleaved Report
  Generation'
title_zh: TVIR：面向文本-视觉交错报告生成的深度研究智能体
authors:
- Xinkai Ma
- Zhiqi Bai
- Dingling Zhang
- Pei Liu
- Yishuo Yuan
- He Zhu
- Jiakai Wang
- Qianqian Xie
- Yifan Zhao
- Xinlong Yang
affiliations:
- Nanjing University
- Alibaba Group
arxiv_id: '2606.02320'
url: https://arxiv.org/abs/2606.02320
pdf_url: https://arxiv.org/pdf/2606.02320
published: '2026-05-31'
collected: '2026-06-03'
category: Agent
direction: 深度研究智能体的多模态报告生成与评估
tags:
- Deep Research Agents
- Text-Visual Interleaved Report
- Multi-Agent Framework
- Multimodal Evaluation
- Visual Evidence Grounding
one_liner: 首个同时评估文本与视觉证据的多模态深度研究基准与多智能体框架，揭示现有系统重文字轻视觉的短板
practical_value: '- **多模态报告生成可复用范式**：TVIR-Agent 的“规划-视觉素材实例化-顺序写作-全局整理”四阶段流水线可直接用于电商市场分析报告、竞品追踪等长文生成，其中将视觉需求（检索图片、代码生成图表）显式纳入大纲规划的思路能显著提升图文一致性。

  - **视觉证据的可靠性检查**：通过 Chart Generator 自动爬取数据、交叉验证并生成代码图表，保留数据源 URL，同时用 VQA 工具过滤低质量检索图片，这类机制可迁移到商品分析、库存预警等需要数据可视化且要求来源可追溯的业务场景。

  - **双路评估框架的启发**：将评估分解为文本评估（引用支持、指令对齐、写作质量等）和视觉评估（图表质量、图文整合、源一致性）的范式，可复用来构建电商领域生成内容（如商品详情页、营销文章）的质量审查系统，重点检测装饰性
  vs 证据性配图的差异。

  - **多智能体角色分工**：Planner+Image Searcher+Chart Generator+Writer+Polisher 的松耦合设计，允许按需替换或升级单个组件，适合团队并行开发；针对电商
  Agent，可将 Writer 替换为适配商品描述的风格模块，或将 Image Searcher 接入内部图库。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有深度研究智能体（Deep Research Agents）大多只生成纯文本报告，忽略真实分析报告中图表、截图等视觉元素作为核心证据的角色。即使生成了图像，也常是装饰性补充，缺乏对视觉内容的事实一致性、来源可靠性和图文对齐的评估。这导致生成报告在金融、政策、科研等高风险决策中可信度不足。为此，本文提出 TVIR，重新将深度研究定义为文本与视觉交错生成的多模态综合任务。

**方法关键点**：
- **TVIR-Bench**：100 个专家精心设计的多模态深度研究任务，覆盖 10 个领域，要求必须包含检索图片和代码生成图表，并附有评估清单。任务按复杂度分三级，强调视觉元素须为分析子目标服务。
- **TVIR-Agent**：分层多智能体框架，包括 Planner（搜索并生成带视觉需求的结构化大纲）、Image Searcher（Google 搜图+质量过滤+VQA 相关度验证）、Chart Generator（爬取数据、交叉验证、代码绘图并保留源链接）、Writer（基于大纲和已写章节动态上下文顺序写作，自动插入视觉资产）和 Polisher（全局参考文献去重重编号、图表重编号）。
- **双路评估**：文本评估含引用支持、指令对齐、写作质量、分析深度、事实逻辑一致性；视觉评估含多模态组成、图表质量、图题质量、图文整合、图表与源一致性。提取事实-引用对和图表元数据后，由 GPT-5.2 作为裁判自动打分。

**关键实验**：
- 在 TVIR-Bench 上评测了 9 个系统（包括 Gemini、Grok、Claude、Perplexity、Manus 等商用产品及 3 个 TVIR-Agent 变体）。
- TVIR-Agent（Claude-4.5-Sonnet）取得最高综合分（74.44），显著优于最强商用系统 Manus-1.6（69.73）。
- 在引用支持上，TVIR-Agent（GLM-4.7）得分 68.64，超越商用最佳 21.11 分；在图题质量上领先 8.35 分。
- 消融实验：移除 Chart Generator 导致视觉评估从 78.62 暴跌至 60.91，证实图表生成是视觉可信的关键。
- 结构错误分析：商业系统常出现来源不可追溯、编号缺失等错误，TVIR-Agent 总错误数最低，但可追溯性仍是所有系统的共同挑战。

**值得记住的一句话**：*当前深度研究系统“重文字、轻视觉”，严格的双路评估表明，显式地将视觉证据融入规划与生成是提升报告可信度的必由之路。*
