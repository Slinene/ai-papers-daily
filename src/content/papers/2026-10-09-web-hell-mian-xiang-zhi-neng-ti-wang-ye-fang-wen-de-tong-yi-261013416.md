---
title: 'Web$hell: A Unified Interface for Agentic Web Access'
title_zh: WEB$HELL：面向智能体网页访问的统一接口
authors:
- Sunghwan Kim
- Deogyong Kim
- Sangam Lee
- Donguk Kwon
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.13416'
url: https://arxiv.org/abs/2610.13416
pdf_url: https://arxiv.org/pdf/2610.13416
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 网页访问统一接口设计
tags:
- Agent
- Web Interface
- Web Navigation
- Web Search
- Deep Research
- LLM
one_liner: 提出统一网页访问接口 WEB$HELL，将网页信息与动作编译为可寻址对象并持久缓存，以更低成本在搜索/导航/深度研究任务上全面领先。
practical_value: '- 电商购物 Agent 可将商品列表、筛选器、分页、详情页编译为统一对象；grep 定位到“价格”“尺码”等文本时，通过 association
  直接关联可执行的 action address，避免反复解析 DOM 和多工具切换。

  - 复用 WEBCACHE 思路：保存页面快照并按 page address 引用，状态变化后生成新版本、旧版只读，适合比价、购物车修改前回看等长程多步任务；工程实现可仿照
  addressable cache。

  - 优先用确定性 HTML 语义规则而非模型推理做页面编译，针对 select/option/label、a、table 等电商高频元素设计 constructor，成本可控且响应稳定。

  - 评估 Agentic web 任务时不要只看 success，应同时跟踪 turns / input tokens / cost；搜索+浏览器+文件系统的简单混合不一定提升效果，统一接口往往更划算。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM agent 越来越多直接访问开放网页，但现有 search-augmented、browser-based、filesystem-based 三类 access model 各自偏向信息收集或交互，长程任务需要同时完成宽域信息收集、浏览器操作和证据复用，混合方案成本高或掉点。作者预实验发现 HybridSB 在 WideSearch 输入 tokens 增加 290%、成本增加 272%；HybridSBF 虽降低搜索成本但 WebArena-Verified 导航性能下滑。

**方法关键点**：
- WEBCONTRACT 定义统一 object schema：每个网页元素编译为带 address / value / association 的对象；页面按 text、tables、links、actions 等类型组织，提供目录与统一操作 schema。
- WEBCOMPILER 用基于 HTML 语义的确定性规则把 DOM 编译为信息对象和动作对象，不依赖额外模型推理；保留 label、选项、关联元素等上下文。
- WEBCACHE 持久缓存编译页面，支持 retrieve / grep / read / execute；状态变化后生成新 page address，旧状态只读保留，支持回看。
- agent 通过 request-response 循环与接口交互，用对象地址指定检查或执行操作，避免重复解析页面。

**关键结果**：在 WideSearch、SealQA、WebArena-Verified、WebWalkerQA、DeepResearchBench、DeepWeb-Bench 六个基准上全面超过 Fetch-then-Explore、HybridSBF、CLI-Anything Browser。WideSearch Item F1 0.782 vs 0.745，SealQA 0.720 vs 0.665，WebArena-Verified 成功率 0.679 vs 0.578，WebWalkerQA 0.671 vs 0.636，DeepWeb-Bench 31.11 vs 28.37。Deep Research 场景 turns 仅 17.6，成本 1.87M tokens，远低于 HybridSBF（30.9 turns / 2.75M）和 CLI-Anything Browser（52.4 turns / 4.03M）。

**最值得记住的一句话**：把网页元素编译成“带地址、带值、带关联”的对象，并用统一缓存与操作接口暴露给 agent，比简单叠加 search+browser+filesystem 更有效且成本更低。
