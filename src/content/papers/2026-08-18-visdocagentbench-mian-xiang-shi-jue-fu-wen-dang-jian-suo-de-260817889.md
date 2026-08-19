---
title: 'VisDocAgentBench: Benchmarking Agents for Visually Rich Document Retrieval'
title_zh: VisDocAgentBench：面向视觉富文档检索的智能体基准评测
authors:
- Lexiang Hu
- Yanzhao Zhang
- Mingxin Li
- Dingkun Long
- Yikang Li
- Fuwei Zhang
- Yisen Wang
- Zhouchen Lin
affiliations:
- Peking University
- Alibaba Group
arxiv_id: '2608.17889'
url: https://arxiv.org/abs/2608.17889
pdf_url: https://arxiv.org/pdf/2608.17889
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: 多模态文档检索智能体评测
tags:
- Visually Rich Document Retrieval
- Agentic Search
- Benchmark
- Multimodal Retrieval
- Late Interaction
- Evidence Path
one_liner: 提出视觉富文档检索基准，暴露强静态检索在桥接证据上近乎失效，而工具智能体可恢复但依赖规划器与视觉表示
practical_value: '- 电商/广告搜索中，商品详情页、广告落地页、海报等视觉富文档不能只用 OCR 文本召回；强视觉 late-interaction
  检索（如 Nemotron ColEmbed）对直接匹配收益巨大，但面对需要上下文消歧的查询会失效。建议将强视觉检索作为 discovery，叠加 Agent
  的迭代检查与证据重排序。

  - 同一 index/tool 接口下不同 planner 的 R@1 从 19.17% 到 67.50%，说明单纯接入工具不等于有效检索；应重点优化 planner
  的搜索改写、检查策略和最终排序，并利用 trace 诊断失败在 discovery、examination 还是 ranking。

  - 页面/图片 inspection 是最大增益点（去掉后 R@1 掉 15.8/21.7 点），因此多模态 Agent 必须保留原始视觉图，不能只用 OCR
  文本或 caption；on-demand OCR/crop 可做局部验证，但要平衡全局探索，否则长链路性能会反弹。

  - 对需要多跳证据的查询，给 Agent 提供完整 support context 能显著提升 R@10；业务可实现为初期附加候选 support pages
  或引入 evidence-role aware 状态，避免模型被表面相似项锚定。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：视觉富文档（学术论文页、商品详情页、广告落地页）中，相关性由文本、版式、图表等联合编码；现有检索评测多为一次性 query-page 匹配，而 Agentic search 基准多只看下游 QA/报告分数，缺少对最终文档排序的直接评测。因此需要一个 closed-corpus 基准来比较 static 与 agentic retrieval，并暴露多跳证据下的瓶颈。

**方法关键点**：
- 构建 VisDocAgentBench：100 篇论文、2375 页图像，120 个查询，均衡覆盖 direct / one-bridge / two-bridge 证据结构。
- 构造管线：角色化描述符（query anchor、semantic bridge、visual target descriptor）+ 有向关系，经语义对齐、路径组合、全文档人工+AI 双盲打分、硬负样本校验，保证目标唯一且证据链有效。
- 评测契约：所有系统输出 top-10 页面排序；static 检索与 tool-using agents 同台比较。工具包括视觉/OCR 搜索、页检查、区域裁剪、排序提交，最多 12 步交互。

**关键实验与结果**：
- 强 late-interaction 视觉检索器 Nemotron-ColEmbed-VL-8B-V2 overall R@1 40%，direct 97.5%，但 two-bridge 仅 2.5%，说明 query-target 匹配无法解决分布式证据。
- 同一工具接口下 planner 差异巨大：视觉路线 R@1 从 19.17% 到 67.50%，OCR-text 路线最高 37.50%；所有 planner 视觉路线均优于 OCR 路线。
- Ablation：移除 page inspection 掉点最大（视觉 -15.84，OCR-text -21.67）；移除 iterative search 掉 8.34/9.17；提供完整 support context 后 L2/L3 R@1 和 R@10 均提升。
- 轨迹分析：视觉检索的 target discovery 83.3% vs OCR-text 58.3%，失败集中在发现、检查与证据角色整合。

**最值得记住的一句话**：强视觉匹配解决直接命中，但多跳文档检索必须由 planner 驱动、且保留视觉原始信息和证据导向的验证。
