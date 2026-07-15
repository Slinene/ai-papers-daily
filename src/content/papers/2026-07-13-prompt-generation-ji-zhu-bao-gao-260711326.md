---
title: Prompt Generation Technical Report
title_zh: Prompt Generation 技术报告
authors:
- Dan Ou
- Gui Ling
- Hao Wan
- Hongbin Zhou
- Jialiang Cheng
- Jiangnan Pang
- Silu Zhou
- Wei Shi
- Weichen Ye
- Wenming Zhang
affiliations:
- Taobao Search Team
arxiv_id: '2607.11326'
url: https://arxiv.org/abs/2607.11326
pdf_url: https://arxiv.org/pdf/2607.11326
published: '2026-07-13'
collected: '2026-07-15'
category: GenRec
direction: 生成式检索 · 配置驱动框架
tags:
- Generative Retrieval
- Prompt Engineering
- Feature Engineering
- Configuration-Driven
- LLM
- Industrial Deployment
one_liner: 通过配置驱动框架解耦生成式检索中的特征处理与模型架构，实现快速实验、统一部署和低延迟推理
practical_value: '- **配置即实验**：你的业务中每次加特征都要改模型代码吗？PG 把特征类型（文本、嵌入、组合、序列）和处理组件（映射、分桶、投影、合并等）都声明在
  JSON 里，换特征只需改配置，几天变几分钟，适合快速迭代。

  - **统一线上/线下特征一致性**：训练—服务偏移（Training-Serving Skew）是推荐/搜索的顽疾。PG 的事件追踪机制记录线上原始特征，训练时回放，保证一致性
  >99%，直接可复用。

  - **Token 压缩实用**：长行为序列（如 45K tokens）被 PG 压缩至约 11K tokens 仍有离线收益，用 mean/combo 合并等算子控制
  token 预算，平衡效果与成本，对 LLM4Rec 场景有直接借鉴。

  - **插件化扩展**：自定义合并算子（如 attention merger）通过注册即可集成，不改框架，便于在电商搜索/推荐中试验特征融合策略。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式检索将推荐/搜索转化为序列生成问题，但工业部署中特征工程与模型架构紧密耦合：每增改一个特征都要改动训练和推理代码，多场景复用困难，迭代慢且易造成线上/线下特征不一致。根本在于特征处理逻辑与模型结构的绑定。

**方法关键点**
- 提出 Prompt Generation (PG) 框架，用两个声明式 JSON 文件（prompt_feature.json 和 prompt_template.json）作为唯一真源，驱动离线和在线流程，彻底解耦。
- 定义四类特征：Text (原始字符串)、Embedding (预训练向量)、Combo (子特征组合)、Sequence (时序序列)，并统一通过可组合的三大组件处理：Preprocessor (文本标准化/分桶)、Projector (维度对齐)、Merger (均值/求和/Concat-MLP 等令牌聚合)。
- 在线推理架构分为 Prompt Service（特征检索与组装）和 Prompt Generator（令牌化与 LLM 推理），支持动态束搜索和优化，延迟开销几乎可忽略。
- 事件追踪机制记录线上原始特征，离线训练回放，消除训练—服务偏差。

**关键结果**
在淘宝搜索任务上，PG 配置下组合特征方案（SID + combo_mean）相对 SID-only 基线在 HR@50 和 HR@5000 分别提升 +0.61% 和 +0.31%，同时维持 token 长度与基线相当。推荐任务中，通过合并策略灵活平衡效果和 token 预算。线上 A/B 测试中，PG 部署后淘宝搜索成交单量提升 +0.47%，GMV 提升 +0.51%。
