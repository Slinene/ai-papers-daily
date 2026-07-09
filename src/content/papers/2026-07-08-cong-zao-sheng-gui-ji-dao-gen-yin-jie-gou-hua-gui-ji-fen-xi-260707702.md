---
title: 'From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal
  Extraction for Agent Optimization'
title_zh: 从噪声轨迹到根因：结构化轨迹分析与因果提取优化Agent
authors:
- Ying Chang
- Jiahang Xu
- Xuan Feng
- Chenyuan Yang
- Peng Cheng
- Yuqing Yang
affiliations:
- University of Chinese Academy of Sciences
- Microsoft Research
arxiv_id: '2607.07702'
url: https://arxiv.org/abs/2607.07702
pdf_url: https://arxiv.org/pdf/2607.07702
published: '2026-07-08'
collected: '2026-07-09'
category: Agent
direction: Agent 优化 · 因果轨迹提取
tags:
- Agent Optimization
- Reflection
- Causal Extraction
- Trajectory Analysis
- Failure Diagnosis
one_liner: 提出STRACE框架，通过失败模式挖掘和因果定位剔除冗余轨迹与无关步骤，实现Agent反思优化的降噪与提效
practical_value: '- 电商搜索/推荐Agent（如多轮对话、多步查询改写）的失败诊断：可构建执行步骤间的依赖图，用LLM判定因果路径，定位根因模块，避免完整轨迹噪声。

  - 批量优化时参照STRACE的两阶段设计：先聚类失败模式，去重冗余轨迹，再在代表轨迹内做因果剪枝，减少过拟合常见但低价值错误的风险。

  - 对于在线Agent的持续优化，引入“代表性失败”选择策略，替代随机采样或全量重放，提升反思效率和优化信号的纯度。

  - 将轨迹结构化为有向依赖图的做法，可复用至复杂Agent链路的调试工具，帮助开发者快速定位瓶颈步骤。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：长程Agent优化需LLM反思执行轨迹，但真实轨迹冗余且异质，直接使用会引入噪声，导致优化过拟合低价值失败；简单截断或滑动窗口则可能丢失重要因果步骤，产生误导信号。  
**方法**：STRACE分两层构造高信噪比的优化上下文。批量层，通过挖掘失败模式（如聚类相似错误），过滤重复轨迹，保留代表性失败案例。轨迹内层，将步骤依赖关系构建为文本依赖图，并利用LLM进行因果定位，只保留影响最终失败的因果步骤，移除无关步骤，从而精准识别需要优化的根因模块。  
**结果**：在多个Agent基准上，STRACE的优化效果显著优于标准上下文过滤方法。特别是在VeruSAGE-Bench形式化验证任务中，成功优化人类专家设计的Agent，将成功率从42.5%提升到58.5%（1.4倍改进）。
