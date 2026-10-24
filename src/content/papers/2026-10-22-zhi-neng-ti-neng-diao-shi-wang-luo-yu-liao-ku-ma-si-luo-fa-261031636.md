---
title: Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2
title_zh: 智能体能调试网络语料库吗：斯洛伐克语 FineWeb2 的 Agentic 审计
authors:
- Marek Šuppa
- Ivan Vykopal
- Jaroslav Kopčan
affiliations:
- Comenius University in Bratislava
- Cisco Systems
- Kempelen Institute of Intelligent Technologies
- Brno University of Technology
arxiv_id: '2610.31636'
url: https://arxiv.org/abs/2610.31636
pdf_url: https://arxiv.org/pdf/2610.31636
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 驱动数据审计与质量评估
tags:
- Agentic Auditing
- Web Corpus
- Data Quality
- FineWeb2
- LLM Debugging
- Executable Tests
one_liner: 用工具型 LLM agent 低成本审计斯洛伐克语 FineWeb2，产出可执行测试并发现 140 万篇机器生成内容
practical_value: '- 用一次 LLM agent 探索数据管道并产出可执行的验证规则（正则/统计特征/轻量模型），比全量 LLM 分类便宜 4 个数量级，适合定期巡检搜索/推荐语料、商品描述或
  UGC 内容的系统性污染。

  - 把「模型分类」改为「agent + 工具 + 人工盲审」的审计模式：让 agent 输出 selector 和判断依据，再抽检验证，既能估算缺陷率，又给出
  pipeline 漏检原因，便于修复上游过滤规则。

  - 预算可控的只读 API 设计值得借鉴：限制工具调用轮次和文档读取量，把单次审计成本压到几美元，可高频跑在数据入库前或日常监控中。

  - 先做静态采样/规则基线，再决定是否上 agent；论文中静态采样基线成本不足一半且能验证更多 selectors，业务上应优先用简单可解释规则覆盖大部分问题。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：多语言语料 pipeline（如 FineWeb2）用同一套 recipe 处理上千种语言，个别语言的失败模式未被预见。作者以斯洛伐克语 FineWeb2 为对象，探索用 LLM agent 做语料调试而非分类。

**方法**：使用工具型 LLM agent，通过只读、有预算的 API 探索语料库，将每个发现编译为可执行测试（selector），再由母语者验证。在 26.5M 文档上运行三次，成本仅 $2.21–$2.84。

**关键结果**：三次运行共发现 7 个 findings，覆盖 4 类现象。最大问题是机器生成内容农场，共 1,408,437 篇文档（占 5.32%），其中 86.6% 通过了更严格的过滤阈值。盲标签支持 6/7 发现，缺陷率 0.53–1.00，而随机对照为 0.08。编译出的测试套件可在 0.7 秒内扫描全库，无需 GPU，对比一次 LLM 分类需 $12k–$90k。静态采样基线成本更低且能验证更多 selectors，但 agent 额外提供精确占比、精度估计、漏检原因和可复用测试。框架、测试套件、验证数据和 agent 轨迹已开源。
