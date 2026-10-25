---
title: 'OACap: Caption-Guided Active Observation for Detailed Video Captioning'
title_zh: OACap：字幕引导主动观察的详细视频字幕生成方法
authors:
- Hao Shi
- Hong Yan
- Xiaoyang Zhang
- Qing Cui
- Chao Huang
affiliations:
- Ant Group
- Zhejiang University
- Peking University
arxiv_id: '2610.29327'
url: https://arxiv.org/abs/2610.29327
pdf_url: https://arxiv.org/pdf/2610.29327
published: '2026-10-21'
collected: '2026-10-25'
category: Multimodal
direction: 多模态 Agent 主动信息获取
tags:
- Video Captioning
- Active Observation
- Agent
- Multimodal
- Factuality Evaluation
- Tool Use
one_liner: 提出字幕中心 Agent OACap，将字幕信息缺口转为定向观察请求，迭代验证提升视频字幕质量
practical_value: '- 在生成式推荐、商品文案、详情页摘要中，把生成结果当作可检验假设，自动检测信息缺口（遗漏关键属性、无支持断言），通过结构化工具（商品库、知识图谱、用户行为
  API）补证，降低幻觉。

  - 借鉴 revision gap 与 observation gap 的分级：先基于已有上下文修订，只有确实缺证据时才触发昂贵工具调用，适合高成本 LLM 场景；在电商直播切片或短视频理解中可裁剪关键帧/区域做
  OCR 或密集采样。

  - 事实性评估指标可复用：用 claim precision + importance-aware fact coverage 评估商品描述/搜索摘要是否覆盖关键卖点且不编造；通过原子事实往返匹配衡量语义保持，替代单一文本相似度。

  - 迭代验证-修订的工作流可嵌入推荐理由生成、query 推荐解释等 Agent 流程，形成证据闭环。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：详细视频字幕需保留实体、属性、状态变化和时间关系，但单次全局处理常遗漏小物体、短动作或远距离转变；开放字幕没有 query 指定感知目标，且纯文本修订无法恢复未见事实。现有工具增强方法多依赖外部 query 或推理状态触发额外观察。

**方法关键点**：OACap 将演化中的字幕视为可检验的视频描述，通过与 provenance-aware evidence 对比暴露遗漏、无支持断言、冲突和未解决时间关系。它区分 revision gap（可由现有证据修订）与 observation gap（需触发工具调用），针对性地裁剪小物体、密集采样动作、OCR 临时文本等，随后迭代验证并修订字幕。

**结果**：使用固定 text-only reader，OACap 字幕在通用视频理解基准上持续提升性能。新基准 FSCap-Bench 的 CSFS 结合 claim precision 与 importance-aware fact coverage，对四种受控扰动在 93.0–98.3% 的有效字幕对上作出预期响应；CSRS 通过视频-字幕-视频-字幕往返匹配原子事实衡量语义保持。
