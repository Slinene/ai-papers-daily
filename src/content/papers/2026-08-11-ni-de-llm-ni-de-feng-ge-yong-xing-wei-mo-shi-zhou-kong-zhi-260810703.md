---
title: 'Your LLM, Your Style: Behavioral Mode Axes for LLM Behavioral Control'
title_zh: 你的 LLM，你的风格：用行为模式轴控制 LLM 行为
authors:
- Haoze Liu
- Run Liu
- Haiying Xu
- Jiahui Han
- Siyuan Fang
- Siyu Yan
- Huiqi Deng
- Guanchu Wang
- Na Zou
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- The Hong Kong University of Science and Technology
- Xi'an Jiaotong University
arxiv_id: '2608.10703'
url: https://arxiv.org/abs/2608.10703
pdf_url: https://arxiv.org/pdf/2608.10703
published: '2026-08-11'
collected: '2026-08-13'
category: LLM
direction: LLM 行为风格控制 · 激活方向
tags:
- LLM
- Behavioral Control
- Activation Directions
- Psychometrics
- Prompt Registers
- B-data
one_liner: 用情境化对比行为轨迹提取激活方向 BMA，发现 thought-derived 控制比 response-derived 更稳定干净
practical_value: '- 推荐/客服 Agent 的行为风格（推荐激进程度、解释话术、风险偏好）可用 contrastive behavioral scenarios
  快速搭建评测集；用正反行为对生成 hidden-state 方向，比自报式 prompt 更贴近线上行为。

  - BMA 控制向量可作为轻量风格开关：在多轮推荐对话中，通过加法注入 thought-derived direction 固定客服语气或决策风格，减少长 prompt
  带来的风格漂移。

  - 注意 prompt register 差异：模型在‘给建议’和‘第一人称决策’下行为会漂移；电商导购 Agent 的 prompt 应按角色/任务类型分别设计并评估，不能复用同一模板。

  - 若做生成式推荐/文案风格控制，可借鉴 contrastive traces 提取风格方向，避免频繁更新 LoRA，只做激活空间干预。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：现有 LLM 人格研究多依赖第一视角自报问卷，结果容易受题面措辞影响，且与真实交互行为脱节，难以稳定刻画和控制模型行为风格。

方法：构建情境化行为数据（B-data）框架，基于 BFI-2、DOSPERT、HEXACO 等心理测量维度，生成 3,200 个对比行为场景，覆盖 20 种行为模式与 4 种 prompt register（第一人称决策、给建议、任务执行等）。从对比场景中收集模型行为轨迹，形成行为画像；进一步从对比轨迹中提取激活空间方向，称为行为模式轴（BMA），用于控制行为风格。分别从 response 与 thought 轨迹提取 BMA 并比较。

关键结果：LLM 表现出稳定且模型特异的行为画像，同时存在 register 依赖的漂移；response-derived BMA 更易发生 trait drift，而 thought-derived BMA 更忠实于预期行为机制，能提供更干净的情境化风格控制。代码与数据已开源。
