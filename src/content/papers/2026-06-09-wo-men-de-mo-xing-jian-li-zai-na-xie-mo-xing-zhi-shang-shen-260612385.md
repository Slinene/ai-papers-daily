---
title: Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern
  LLMs
title_zh: 我们的模型建立在哪些模型之上？审计现代 LLM 中的隐性依赖
authors:
- Sanjay Adhikesaven
- Haoxiang Sun
- Sewon Min
affiliations:
- University of California, Berkeley
- Allen Institute for AI
arxiv_id: '2606.12385'
url: https://arxiv.org/abs/2606.12385
pdf_url: https://arxiv.org/pdf/2606.12385
published: '2026-06-09'
collected: '2026-06-14'
category: LLM
direction: LLM 依赖审计与供应链透明化
tags:
- LLM Dependency
- Agentic System
- Model Supply Chain
- Audit
- Documentation
one_liner: 用 Agent 系统 ModSleuth 递归还原 LLM 开发中的 1060 个来源验证依赖，并揭示许可证、耦合等隐患
practical_value: '- 多模型流水线（如 Agent 协作、生成式推荐链路）中，可借鉴 ModSleuth 的依赖建模方法，自动追踪数据、模型、工具间的引用关系，防止文档碎片化导致的风险。

  - 在电商推荐工程中，若使用 LLM 生成内容、过滤数据或评估输出，可以利用类似的依赖图审计来管理许可证义务，避免多跳协议冲突。

  - 其操作中心关系（editing、judging、filtering 等）的依赖分类，可直接复用于组织内部模型流水线的构建与追溯，提升合规性和可解释性。

  - 对于已发布的模型或数据集，建议采用类似版本解析与工件身份对齐的机制，减少训练时与发布时不一致带来的表现差异。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**： 现代 LLM 训练越来越依赖其他模型来生成数据、过滤语料、评判输出，形成多层递归依赖。这些依赖分散在技术报告、模型卡、代码库等异构公开工件中，人工难以追踪全貌，导致许可证冲突、评估耦合等风险。  
**方法**： 提出 ModSleuth，一个基于 Agent 的系统，递归地从公开工件中重建 LLM 依赖图。关键挑战不再是信息抽取，而是定义何为依赖及协调不一致的文档引用。系统引入了直接/间接依赖形式化，用操作中心关系（如 edited by、judged by）表示异构流水线角色，并通过名称、版本、仓库对齐解析工件身份。  
**结果**： 在四个公开工件丰富的 LLM 发布（如 Llama 3、Qwen 等）上应用，恢复出 1060 个来源验证的依赖，构建大规模依赖图。这些图揭示出多跳许可证义务、训练与评估集耦合、发布工件与训练时不一致、文档自相矛盾等问题。代码与依赖图已开源。
