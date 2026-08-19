---
title: 'StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents'
title_zh: StagedWorkspace：面向知识工作 Agent 的版本化工作空间
authors:
- Yining Hua
- Hongbin Na
- Yifan Zhou
- Akshay Kalose
- Cyrus Ayubcha
- Levi Lian
affiliations:
- Harvard University
- Raycaster AI
- University of Technology Sydney
- University of Washington
- Stanford University
arxiv_id: '2608.18050'
url: https://arxiv.org/abs/2608.18050
pdf_url: https://arxiv.org/pdf/2608.18050
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 工作空间版本管理与状态一致性
tags:
- Agent
- Knowledge Work
- Version Control
- Workspace Management
- Benchmark
- Document Editing
one_liner: 提出带版本控制的工作空间，将解析视图与 diff 绑定到文件内容哈希，显著提升知识工作 Agent 的文件编辑与问答性能
practical_value: '- 对于电商/广告场景中需要 Agent 自动生成或修改文档（如商品详情、营销报告）的流水线，可采用内容哈希将解析视图与原生文件绑定，防止
  Agent 在异步处理中引用过时版本，确保最终提交一致性。

  - 引入 staged edits 与 review diff 机制，让模型在每次修改后看到 diff 再继续下一步；在多轮编辑任务（如广告文案迭代）中能显著减少累积错误，提升最终质量，类似代码
  Agent 的版本控制实践。

  - 若构建基于 RAG 的知识工作 Agent（如自动撰写商品卖点、审核规则文档），采用 dual parsed/native access：结构化解析用于快速检索，原生文件用于精确校验，可平衡效率与准确性。

  - 在评测或监控此类 Agent 时，将 evidence、staged edits 和提交产物作为显式状态转换进行打分，而不是只看最终输出，更能反映真实工作流中的质量。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：知识工作 Agent（编辑代码库、文档、表格、幻灯片等）在执行任务时，搜索使用的解析视图、编辑的原生文件、审查的 diff 与最终提交产物可能指向不同版本，导致状态不一致。编码 Agent 已有 repository contracts，但 PDF/电子表格/幻灯片/笔记本等格式缺乏明确契约。

方法关键点：提出 workspace-state contract，要求每个视图显式绑定到工作空间状态的某个版本。实现 StagedWorkspace，将 parsed records 和 review diffs 绑定到原生文件的 content hashes，通过 dual parsed/native access 让 Agent 同时访问结构化解析结果和原始文件，并能查看 diff。此外引入 staged edits 和 evidence 审查，将修改过程作为显式状态转换。

关键结果：在 OfficeQA Pro 与 APEX-Agents 固定 harness 上，dual access 对所有测试模型均得到最高点估计；相比单视图，OfficeQA Pass@1 提升 8.3–12.1 分，APEX 平均 rubric 分提升 4.7–9.2 分。SW-AGENT 在 OfficeQA 上达 63.9%（Gemini 3.1 Pro），APEX 上 42.1（GPT-5.4 Nano），远高于已发表同模型分数 29.3% 和 25.5。57 个文件编辑任务的配对消融显示，diff 可见时分数更高。
