---
title: 'LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying
  LLM Routers'
title_zh: LLMRouter：LLM 路由器开发、评估与部署的统一基础设施
authors:
- Tao Feng
- Fangxu Yu
- Haozhen Zhang
- Zhongjie Dai
- Liangqi Yuan
- Zijie Lei
- Weizhi Zhang
- Kunlun Zhu
- Haodong Yue
- Keyang Xuan
affiliations:
- University of Illinois Urbana-Champaign
- University of Maryland, College Park
- Nanyang Technological University
- Purdue University
- University of Illinois Chicago
arxiv_id: '2608.06867'
url: https://arxiv.org/abs/2608.06867
pdf_url: https://arxiv.org/pdf/2608.06867
published: '2026-08-06'
collected: '2026-08-15'
category: Other
direction: LLM 路由统一框架与评测基准
tags:
- LLM Router
- Model Routing
- Benchmark
- Infrastructure
- Cost-Quality Tradeoff
- Personalization
one_liner: 提出统一 LLM 路由五组件公式、开源模块化基础设施与 xRouteBench 基准，系统比较 16+ 路由器并给出成本与个性化关键发现
practical_value: '- 做 LLM 路由时可将策略抽象为「编码器→打分→决策规则→学习信号」，按组件模块化开发，便于快速替换编码器（如用户/上下文
  embedding）和损失函数；LLMRouter 的开源实现可当内部 Router 服务的脚手架。

  - 电商/搜索推荐中不同 query/任务对模型能力和成本敏感度差异大，统一评估质量+推理成本的方式值得照搬，建议建立类似 xRouteBench 的内部基准，用候选模型池自动产出路由标签。

  - 实验结论提示在严格成本预算下轻量路由器反而更优；部署 LLM Agent 或生成式推荐服务时，应把单模型强大与路由开销一起评估，不要盲目追求复杂路由器。

  - 个性化路由（user-conditioned routing）增益稳定，可把用户画像/历史行为嵌入作为条件输入，让路由决策感知用户，提升推荐、广告文案生成等场景的个性化效果。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
单一 LLM 无法在所有查询和预算约束下都最优，模型路由是成本效益部署的关键；但现有路由器形式化各异、实现不兼容，且缺乏标准化评估流水线，难以公平比较和扩展。  

**方法关键点**  
将 LLM 路由统一为顺序决策过程，用五个组件刻画路由器：context encoders、model encoders、scoring functions、decision rules、learning signals，覆盖单轮、多轮与个性化路由三类。基于该公式构建自动 pipeline，通过在候选模型池上系统运行基准构造路由监督，并联合评估响应质量与推理成本。由此产出基准 xRouteBench，覆盖通用 LLM 任务、记忆增强、视觉（图像/视频）、时间序列及个性化路由场景。开源模块化基础设施 LLMRouter 提供 16+ 代表性路由器实现，新增路由器只需实现路由方法与损失函数。  

**关键结果数字**  
learned routers 相对最强固定模型基线相对提升 14.6%；在严格成本约束下，轻量级路由器排名反超，更具竞争力；user-conditioned routing 带来一致的个性化增益。
