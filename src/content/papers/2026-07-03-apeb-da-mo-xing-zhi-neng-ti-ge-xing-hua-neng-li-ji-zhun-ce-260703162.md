---
title: 'APeB: Benchmarking Personalization Ability of Large Language Model Agents'
title_zh: APeB：大模型智能体个性化能力基准测试
authors:
- Garry Yang
- Zizhe Chen
- Xinru Chen
- Yongqiang Chen
- Jianxiang Wang
- Deyu Zou
- Linyi Ding
- Jialiang Wu
- Yunzhong He
- Yu Gong
affiliations:
- The Chinese University of Hong Kong
- ByteDance
arxiv_id: '2607.03162'
url: https://arxiv.org/abs/2607.03162
pdf_url: https://arxiv.org/pdf/2607.03162
published: '2026-07-03'
collected: '2026-07-07'
category: Eval
direction: 个性化产品搜索 · Agent评测
tags:
- Personalization
- LLM Agents
- Product Search
- Benchmark
- History Utilization
- Query Refinement
one_liner: 构建真实个性化产品搜索基准，揭示LLM智能体在模糊意图与噪声历史下历史利用不足的核心瓶颈
practical_value: '- **历史利用率短板是当前LLM Agent的致命伤**：在模糊查询（如“校园风”）、强竞争候选下，直接喂入长历史效果甚微，应设计**显式历史摘要或查询改写模块**（如论文的VQRA），先凝练偏好再匹配，而不是端到端扔给LLM。

  - **用“硬负样本”逼近真实场景**：随机候选主要测语义匹配，硬候选（用户曾浏览但未买）才暴露个性化缺陷；业务评估推荐/搜索时，应构造**同会话内的高度相似物品池**来检验真实个性化能力。

  - **ReAct等工作流在模糊查询上未必加分**：多步推理可放大意图理解错误；在query不明确时，先迭代改写query（用历史信息）再单步决策，可能比盲目增加推理步数更有效。

  - **LLM-as-a-Judge诊断中间推理路径**：可定义意图推断、偏好提取、推荐对齐等分项指标，用LLM综合打分来定位模型失败节点，该方法可复用到电商Agent的离线优化流程。'
score: 9
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有推荐/搜索基准忽略了个性化智能体面临的真实挑战：用户输入的是模糊、早期意图（如“校园OOTD”），历史交互跨域嘈杂（视频、直播、商品浏览），候选品来自同一购物轨迹且高度相似。传统基准要么澄清了query，要么简化了历史，无法测试智能体在意图推断、偏好提取与精细对比上的联合能力。APeB填补这一空白，从字节跳动内容+电商平台的真实行为日志中抽取5648个“非平凡”购物会话，强制评估在模糊查询与强竞争候选下的个性化决策。

### 方法关键点
- **数据构建**：定义搜索→下单窗口（30分钟内），要求至少2次查询、广泛浏览（|产品+媒体| ≥ τ_v），且最终购买与意图语义对齐。提取长期异构历史（产品交互+视频/直播交互）和当前会话内的意图查询、细化查询及硬候选集（用户查看但未购买的商品）。每个用户平均187条历史记录，候选集平均14.1个商品。
- **任务与评估**：给定(query, 历史, 硬候选)，模型输出排序的Top-K推荐。指标Hit@1/5，同时用LLM-as-a-Judge对中间推理（意图推断、偏好质量、推荐质量、Agent推理连贯性）打分，定位失败原因。
- **对比方案**：传统监督模型UniSAR vs. 多种LLM（GPT-4/5, Qwen3, DeepSeek-R1）的单提示模式和ReAct/Deerflow Agent工作流；并提出VQRA，先用历史改写意图查询再单步推荐。

### 关键结果
- **强/弱意图性能倒挂**：细化查询下，LLM单提示Hit@1可达37.4%（GPT-5.2），远高于UniSAR的29.2%；但在意图查询下，LLM最多25.6%甚至略低于UniSAR的25.9%，ReAct仅带来微弱提升。
- **历史利用几乎无效**：添加60条同类历史只让GPT-5.2的Hit@1从23.8%升至25.6%（提升7.6%），远低于UniSAR的84%相对提升。LLM从历史中提取偏好信号的能力严重不足。
- **硬候选暴短板**：随机候选下LLM优势明显（GPT-5.2 Hit@1 95.9% vs. UniSAR 81.3%），换成硬候选后差距消失（25.6% vs. 25.9%），说明模型仅靠浅层语义匹配，缺乏细粒度个性化鉴别力。
- **VQRA简单有效**：用共享GPT-4.1基于历史改写模糊query，再将改写后query输入原单提示流程，多个模型Hit@1提升（最高到26.9%），验证了显式历史感知查询改写是缓解瓶颈的有效方向。
