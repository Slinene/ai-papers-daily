---
title: 'Bridging Exploration and Persona: Information-Directed Dueling for Test-Time
  Agent Personalization'
title_zh: 桥接探索与人格：测试时 Agent 个性化的信息导向对决
authors:
- Jie Mao
- Pingchen Lu
- Xiangyi Wang
- Hengquan Huang
- Shuang Qiu
- Min Zhang
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- University of Copenhagen
- City University of Hong Kong
- East China Normal University
arxiv_id: '2610.24385'
url: https://arxiv.org/abs/2610.24385
pdf_url: https://arxiv.org/pdf/2610.24385
published: '2026-10-16'
collected: '2026-10-24'
category: Agent
direction: Agent 个性化 · 信息导向 dueling bandit
tags:
- Agent Personalization
- Dueling Bandit
- Information-Directed Sampling
- Test-Time Adaptation
- LLM Agents
one_liner: 提出 ID-TAP，将信息导向采样与神经 dueling bandit 结合，在十轮二元比较内高效适配 agent persona
practical_value: '- 在电商客服、推荐理由生成或文案创作等场景，若需要在线选择 persona、话术风格或 prompt 模板，可用成对比较（A/B
  偏好）作为轻量反馈信号；相比点击或评分，二元偏好收集成本低且噪声小。

  - 借鉴 BT explorer + 信息导向采样选择 challenger：不要随机探索或纯贪心 exploitation，在固定比较预算（如 10 次）下能显著提升样本效率；该策略可直接嵌入在线文案/推荐理由的风格优选。

  - 对新 query 或新用户冷启动，利用相似度加权 warm start 将历史 query 的比较证据迁移过来，比从零学习更快；电商多 query 场景中
  query embedding 相似度即可作为工程上的加权依据。

  - 模型结构上采用 query-conditioned 共享网络：跨 query 共享统计强度，同时保留 query-specific score，能处理 query
  条件化偏好，避免全局单模型丢失个性化差异；可作为 prompt/persona 精排器的轻量在线更新模块。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 的行为高度依赖 persona（system prompt 中的行为/风格描述），但适合的 persona 随 query 变化，且用户偏好隐式、有噪声。在线测试阶段只能依赖轻量交互，常见交互形式是候选回答的成对比较；在大规模离散 persona 空间下，如何用少量比较高效适配是核心挑战。

**方法关键点**：ID-TAP 将 persona 选择建模为神经 dueling bandit，采用信息导向采样（IDS）选择 challenger。整体由两部分组成：query-conditioned 神经网络效用模型和轻量 Bradley-Terry explorer。神经模型跨 query 共享统计强度，同时保留 query-specific 分数；相似度加权 warm start 把相关 query 的历史比较证据迁移到新 query；BT 更新可高效评估候选挑战者。

**结果**：在 7 个用户条件生成基准上，分别用 reference-based 和 model-based 偏好模拟器评估，固定 10 轮比较预算下，ID-TAP 取得最强的聚合性能，优于对比基线。
