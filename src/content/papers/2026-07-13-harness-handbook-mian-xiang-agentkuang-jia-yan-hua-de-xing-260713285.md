---
title: 'Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and
  Editable'
title_zh: Harness Handbook：面向Agent框架演化的行为中心可读表示与渐进式代码定位
authors:
- Ruhan Wang
- Yucheng Shi
- Zongxia Li
- Zhongzhi Li
- Yue Yu
- Junyao Yang
- Kishan Panaganti
- Haitao Mi
- Dongruo Zhou
- Leoweiliang
affiliations:
- Tencent
- Indiana University
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
arxiv_id: '2607.13285'
url: https://arxiv.org/abs/2607.13285
pdf_url: https://arxiv.org/pdf/2607.13285
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: Agent harness 行为定位与编辑辅助
tags:
- Agent Harness
- Behavior Localization
- Code Understanding
- LLM-Assisted
- Static Analysis
- Progressive Disclosure
one_liner: 通过静态分析+LLM自动构建行为手册并引导渐进披露，解决Agent harness修改中的行为定位瓶颈
practical_value: '- **维护行为手册辅助搜推系统Agent harness迭代**：在电商搜索推荐的多阶段pipeline（召回、粗排、精排、重排）中，Agent
  harness常跨模块分布，修改一个业务逻辑需定位多处代码。借鉴Harness Handbook思路，可对搜推系统Agent框架做静态分析+LLM结构化，自动生成行为-代码映射表，让开发者快速找到所有相关实现点。

  - **用渐进披露降低LLM Agent的规划成本**：BGPD从高级行为描述逐步引导到具体代码细节，可迁移到内部代码修改Agent（如用LLM规划代码变更）——先定位行为，再展开实现细节，节省推理token并提高编辑计划准确性。

  - **强化行为定位验证机制**：在实际的Agent harness变更中，引入对候选代码位置的静态验证，可避免LLM规划阶段产生幻觉导致的错误修改，这对高频迭代的电商大促策略调整很有价值。

  - **拥抱行为为中心的文档化自动化**：搜推Agent的prompt、工具调用、状态管理常分散在多个文件，可仿照此方法生成可读的“行为手册”，降低新人上手和跨团队协作的成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：生产环境中的Agent harness（管理prompt、状态、工具调用、执行协调的代码框架）随模型、API、环境演变频繁修改，但修改请求描述系统应该做什么，代码库按文件/模块组织，开发者需手动从行为描述映射到散落在各处的实现代码，行为定位成为瓶颈。

**方法**：提出Harness Handbook——通过静态程序分析和LLM辅助的行为结构化，从harness代码库自动合成以行为为中心的表示，将每个行为与其对应的源代码位置链接起来。同时设计Behavior-Guided Progressive Disclosure (BGPD)策略，引导编码Agent从高层行为描述逐步深入到相关实现细节，并验证候选代码位置是否正确。

**结果**：在两个开源Agent harness的多类修改请求上评估，Handbook-Assisted规划显著改善了行为定位准确率和编辑计划质量，同时减少了规划阶段的token消耗。提升最大的场景涉及分散的实现点、冷门执行路径和跨模块交互。这表明演化复杂Agent系统的瓶颈不仅在于生成编辑，更在于确定编辑应该在哪里发生。
