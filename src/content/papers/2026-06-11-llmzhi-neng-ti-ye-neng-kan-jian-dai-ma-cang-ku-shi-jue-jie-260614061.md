---
title: LLM Agents Can See Code Repositories
title_zh: LLM智能体也能“看见”代码仓库：视觉结构提升效率的秘密
authors:
- Dongjian Ma
- Silin Chen
- Yufei Yang
- Yulin Shi
- Yanfu yan
- Xiaodong Gu
affiliations:
- Shanghai Jiao Tong University
- Xi’an Jiaotong University
- Zhejiang University
arxiv_id: '2606.14061'
url: https://arxiv.org/abs/2606.14061
pdf_url: https://arxiv.org/pdf/2606.14061
published: '2026-06-11'
collected: '2026-06-15'
category: Agent
direction: 多模态Agent · 代码仓库可视化
tags:
- LLM Agents
- Multimodal
- Code Repository
- Vision
- Software Engineering
- Efficiency
one_liner: 首次系统评估多模态仓库可视化对LLM Agent任务解决的影响，发现视觉辅助可降26% token开销且不损精度。
practical_value: '- **混合模态Agent架构**：在电商/推荐Agent中，可将系统拓扑图、服务依赖图、商品知识图谱等可视化信息作为补充输入，与文本上下文结合，使Agent更高效地理解复杂环境结构，减少纯文本描述带来的冗长token消耗。

  - **故障定位阶段的视觉加速**：在推荐系统排障、多Agent协作调试等场景，提供可视化调用链路或状态快照，能帮助Agent更快定位问题来源，类似论文中视觉在fault
  localization阶段的突出效果。

  - **自主探索深度控制**：让Agent根据视觉结构的复杂程度自行决定探索深度，避免不必要的文本查询，可以迁移到Agent规划（如动态选择RAG查询层级、多级推荐链的探索）中，实现按需获取信息。

  - **工程实现借鉴**：论文的混合模态设计验证了“视觉结构图 + 文本浏览”的比纯视觉或纯文本更具性价比，可直接套用在需要Agent理解大型项目结构（如推荐pipeline、微服务架构）时，用图表快速建立全局认知，再用文本精读关键部分。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM Coding Agent几乎完全以文本方式消费代码仓库，而人类开发者会利用文件夹层次、依赖关系等视觉结构来快速定位。随着多模态大模型（MLLM）的进步，一个自然的问题是：Agent能否从仓库的可视化表示中受益？本文首次系统性地研究了这一问题。

**方法**：作者在仓库级别 issue 解决任务上，对比了纯文本、纯视觉（如仓库结构截图）以及文本+视觉混合三种表示方式。实验涉及4个最新的多模态模型，并详细分析了在不同阶段（如故障定位）和不同探索策略下的表现。

**关键结果**：1）纯视觉设置导致准确率下降且token消耗上升，因为Agent缺乏符号细节，会反复进行视觉查询来补偿；2）将可视化结构图（如文件依赖图、目录树）作为文本界面的补充，可使输入token消耗减少高达26%，同时issue解决准确率维持甚至提升；3）可视化在故障定位阶段以及Agent自主控制探索深度时最为有效。

这些发现指明了下一代Coding Agent混合模态设计的实用路径：用视觉快速把握全局结构，用文本精准获取细节，实现效率与效果的平衡。
