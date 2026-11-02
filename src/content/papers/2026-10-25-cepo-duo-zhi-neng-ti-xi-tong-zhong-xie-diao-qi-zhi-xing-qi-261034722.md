---
title: 'CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent
  Systems'
title_zh: CEPO：多智能体系统中协调器-执行器提示优化通用框架
authors:
- Jongha Kim
- Seohyun Lee
- Jonathan Minho Chung
- Jinsung Yoon
- Hyunwoo J. Kim
affiliations:
- Korea University
- KAIST
- Google Cloud AI Research
arxiv_id: '2610.34722'
url: https://arxiv.org/abs/2610.34722
pdf_url: https://arxiv.org/pdf/2610.34722
published: '2026-10-25'
collected: '2026-11-02'
category: MultiAgent
direction: 多智能体提示优化框架
tags:
- Multi-Agent Systems
- Prompt Optimization
- Coordinator-Executor
- LLM Agents
- Shared Prompt
one_liner: 将多智能体提示拆分为共享协调器提示与专属执行器提示，并分别按角色更新，可稳定提升现有提示优化器效果
practical_value: '- 在电商多 Agent 系统（如 query 改写、召回、排序、文案生成）中，可把系统级协调规则放共享 coordinator
  prompt，把各 Agent 执行细节放 executor prompt；统一更新 coordinator 能防止多 Agent 局部优化偏离整体目标。

  - 不必替换已有 prompt 优化器：CEPO 是结构化外壳，可直接叠加在 DSPy/OPRO 等现有搜索器上，改造流程成本低，论文在 11 个 benchmark
  上显示稳定提升。

  - 对预算敏感的业务 prompt 优化：CEPO 在 document-understanding MAS 的受控实验中显示优化预算效率更好、随 Agent
  数扩展性能提升；可用少量预算先优化 coordinator，再分配预算给 executor。

  - 架构上保持 executor 可独立调参/热更新，例如商品推荐解释、广告文案生成等下游执行器可单独迭代，不影响全局协调逻辑。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多智能体系统需要有效的系统级协调与专门的 Agent 级执行，但现有 prompt 优化通常把这些功能耦合在各自 Agent 的 prompt 里，导致协调规则分散、难以一致更新。

**方法关键点**：CEPO 将 prompt 结构拆成共享 coordinator prompt 和 Agent 专属 executor prompt。coordinator 负责系统级协调规则，executor 负责单 Agent 执行指令；优化时按各自角色给出更新方向。CEPO 只提供 prompt 结构和优化指导，底层搜索仍由现有 prompt 优化器完成，因此可泛化叠加到多种优化器上。

**关键结果**：在 4 个领域、11 个 benchmark 上，将 CEPO 应用到 4 种现有 prompt 优化器均能一致提升性能；消融和定性分析支持该设计；文档理解 MAS 的受控实验还显示优化预算效率提升，且性能随 Agent 数量扩展更好。
