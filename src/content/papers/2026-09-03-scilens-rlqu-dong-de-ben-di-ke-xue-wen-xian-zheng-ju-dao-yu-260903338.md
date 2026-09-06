---
title: 'SciLENS: RL-Driven Autonomous Agents for Scientific Localized Evidence Navigation
  and Synthesis'
title_zh: SciLENS：RL驱动的本地科学文献证据导航与综述智能体
authors:
- Leqi Zheng
- Jinbo Su
- Yuying Li
- Chaokun Wang
- Weiping Wang
- Haitao Li
- Jiajun Zhang
- Shannan Yan
- Zhaolu Kang
- Rong Fu
affiliations:
- Tsinghua University
- Renmin University of China
- Institute of Information Engineering, CAS
- USTC
- Peking University
arxiv_id: '2609.03338'
url: https://arxiv.org/abs/2609.03338
pdf_url: https://arxiv.org/pdf/2609.03338
published: '2026-09-03'
collected: '2026-09-06'
category: Agent
direction: Agent 科学文献证据导航
tags:
- Autonomous Agents
- Process Reward
- Citation Graph
- Evidence Grounding
- Local LLM
- RL
one_liner: 全本地科学文献Agent，以结构可视化与逆向分解过程奖励训练，性能对标GPT-5.2
practical_value: '- 把“结构可视化”作为 agent 可调用工具放进推理循环：在电商知识图谱（商品、类目、品牌、共购关系）上先抽取多跳子图，压缩成图表/拓扑摘要喂给
  LLM，避免原始实体列表塞满 context；适合类目规划、趋势综述、归因分析等宏观任务。

  - 自动化标注管道：用已有行为图/商品知识图谱构建多跳子图问题，采用多模型共识（如 3-5 个强模型投票）过滤，零人工标注生成用于推荐/搜索 agent 的监督与
  RL 训练样本。

  - 逆向分解式过程奖励：奖励不只给最终答案，将最终证据链反推成“规划→检索→引用”的 rubrics，分别给过程 reward；可迁移到购物助手、搜索 agent
  训练，约束中间过程必须引用真实商品/证据，提升可追溯性。

  - 全本地双 tier 索引+LLM：若业务对隐私/合规有要求，可参考本地向量库+图索引服务约千万级商品/内容，既保证离线可部署，又降低 API 成本，适合电商搜索/推荐中的合规助手。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：科学文献规模暴涨，综述 agent 依赖闭源在线服务，限制可复现、隐私与离线部署。

**方法关键点**：SciLENS 构建全本地双层索引，覆盖约 1200 万学术记录；将结构可视化作为可调用工具引入推理循环，把复杂引文拓扑压缩成图表以缓解 context 耗尽，支撑宏观综述。训练数据无需人工标注：从引文知识图谱抽取多跳子图，采用 20 个前沿模型交叉共识验证。训练时通过逆向分解 rubric 策略提供细粒度过程奖励，强化早期规划与严格证据 grounding。

**关键结果**：在 6 个科学基准（标准 QA、引用准确率、事实推理、结构综述）上显著超越开源基线，性能与 GPT-5.2、Gemini-3.0-pro 可比。
