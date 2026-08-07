---
title: The Bitter Lesson of Tool Calling
title_zh: 工具调用的苦涩教训：代码执行 vs JSON 调用大规模评估
authors:
- Ishan Patel
- Sahil Sen
- Elias Lumer
- Vamse Kumar Subbiah
affiliations:
- PricewaterhouseCoopers, U.S.A
arxiv_id: '2608.06370'
url: https://arxiv.org/abs/2608.06370
pdf_url: https://arxiv.org/pdf/2608.06370
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 工具调用范式评估
tags:
- programmatic tool calling
- JSON tool calling
- LLM agents
- BFCL v4
- parallel fan-out
- context rot
one_liner: 11/14 模型程序化工具调用匹敌或超越 JSON 调用，并行与长链场景下优势显著
practical_value: '- **Agent 工具接口设计**：在电商搜索推荐 Agent 中，若需并行调用多个商品 API 或串行执行多步查询，可考虑用代码执行（如
  Python 脚本）替代原生 JSON 工具调用，避免 JSON 在高并发时遗漏调用，并减少推理轮次。

  - **多工具链式调用优化**：对于需要多步顺序调用的推荐流程（如先查用户画像、再查商品、再查促销），程序化方式可在单次推理中完成整链，降低延迟，且长链场景下准确率优势可达
  18.8%。

  - **上下文干扰下的鲁棒性**：当 Agent 需要从大量工具定义中选取正确 API 时（类似电商平台有数十个微服务），JSON 调用准确率下降，而程序化调用更稳定，实际部署时可避免因无关工具定义污染上下文导致的失败。

  - **模型选型启示**：程序化工具调用效果与模型代数相关，较新的模型（如 GPT-5.6、Claude Sonnet 5）能稳定发挥优势，旧模型可能出现编码问题（如换行符转义错误），选型时需针对性测试。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
LLM 智能体通常以 JSON 格式调用工具，但 coding 模型天然擅长写代码。已有工作理论上证明用可执行代码替代 JSON 调用能提升多工具任务的成功率并减少交互轮次，但在标准化基准上、跨多个模型代际的严格比较一直缺失。本研究系统评估了“程序化工具调用”（PTC）与原生 JSON 工具调用在 BFCL v4 上的表现，回答“能否用代码执行安全替代 JSON 调用”以及“哪种模型、哪些场景下更有优势”。

**方法**  
- **范式定义**：JSON 调用是标准做法，模型输出结构化 JSON 对象；PTC 则将工具封装为带类型的 Python stubs，模型写一个 Python 脚本（包含导入、调用、输出），通过子进程一次执行并捕获结果，无需额外推理轮次。  
- **评估基准**：从 BFCL v4 中选取 309 个条目，覆盖 8 个类别（简单/多重/并行/实时等），使用确定性评分，比较准确率（所有调用完全正确）。  
- **消融设计**：三个子实验——顺序链式调用（链长 2-20）、并行扇出（同时调用 7-48 个独立函数）、上下文泛滥（注入 128 个无关函数定义），分别测量范式的结构性优势。  
- **模型集合**：14 个模型，包括 Claude 3.5/4/5 系列和 GPT-4o/4.1/5/5.4/5.6 系列，跨度 20 个月。

**关键结果**  
- 在 BFCL v4 主评测中，11/14 模型 PTC 准确率持平或超过 JSON 调用，GPT-5.6-Sol 与 Terra 绝对提升 10.6%。  
- 链式任务中，PTC 优势随链长增加而放大，长度 ≥12 时绝对差距达 18.8%；PTC 将两轮推理合并为一轮，延迟减半。  
- 并行任务中，PTC 在所有扇出水平保持 100% 枚举准确率，而 JSON 调用在 Claude Sonnet 5 上超过 70 个并行调用时开始遗漏，暴露出 JSON 序列化的硬性限制。  
- 上下文泛滥下 PTC 平均提升 5.5%，JSON 调用平均下降 2.3%，PTC 对无关工具定义不敏感。  
- 旧模型（如 GPT-4o、GPT-4.1）因生成 `\n` 转义符而非真实换行导致脚本执行错误，使得 PTC 失效，提示范式迁移依赖模型代码生成质量的代际提升。
