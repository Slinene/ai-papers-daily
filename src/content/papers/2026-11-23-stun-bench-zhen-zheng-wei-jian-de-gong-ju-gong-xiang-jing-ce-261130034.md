---
title: 'STUN-Bench: Truly Unseen Tools for Evaluating Shared Tool Experience'
title_zh: STUN-Bench：真正未见的工具共享经验评测基准
authors:
- Abhijit Chakraborty
- Ni Trieu
- Vivek Gupta
affiliations:
- Arizona State University
arxiv_id: '2611.30034'
url: https://arxiv.org/abs/2611.30034
pdf_url: https://arxiv.org/pdf/2611.30034
published: '2026-11-23'
collected: '2026-11-24'
category: Eval
direction: 工具路由 · 共享经验评测
tags:
- Tool Retrieval
- Shared Experience
- Benchmark
- Data Leakage
- LLM Agents
- Evaluation
one_liner: 发布 STUN-Bench 分割，暴露共享工具经验造成的候选拥挤与数据泄漏，路由准确率从 0.534 跌至 0.278
practical_value: '- 在 Agent 工具检索/RAG 场景，别把工具描述和历史调用经验放进同一个向量索引；经验条目会挤掉从未被使用的新工具/冷启动工具。建议分成两个索引：catalog
  索引先召回工具描述，再单独用经验索引做重排或附加特征。

  - 离线评估要防泄漏：测试工具必须同时从共享经验池和 retriever 训练数据中剔除，不能只按方法侧 ''unseen''；否则共享经验会被高估，甚至结论反转。

  - 如果业务里要给新商品/新广告做候选召回，历史交互日志直接混入商品描述索引会导致新物料曝光不足；可参考 separate index 方案，给冷启动 item
  预留候选配额或独立通道。

  - 通用 embedding（如 Jina-v2）对经验拥挤更敏感，任务专用 retriever 更稳；有工具/物料检索数据时，值得训练自己的双塔 retriever。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：StableToolBench 声称测试“unseen”工具，但其 ToolBench instruction pool 含全部测试 query 并标注了 gold tool，导致共享经验方法受益于泄漏。

**方法**：STUN-Bench 构造 172 个 held-out tools，确保不出现在共享经验池和 retriever 训练数据中；模拟五个 client 贡献历史请求，对比同一索引混合经验 vs 仅描述、以及独立经验索引。

**关键结果**：在 Jina-v2 下，held-out tools 路由准确率从 0.534 降到 0.278，出现经验条目“crowding”挤掉未见工具描述；任务专用 retriever 损失小得多，分离索引能恢复大部分损失；共享经验相对描述的结论在防泄漏后被反转。
