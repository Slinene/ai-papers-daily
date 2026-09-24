---
title: 'Agent-Editing World Model: Rethinking World Modeling for LLM Agents'
title_zh: 智能体编辑世界模型：为LLM智能体重新思考世界建模
authors:
- Shuang Sun
- Guoxin Chen
- Fanzhe Meng
- Jia Deng
- Huatong Song
- Jinhao Jiang
- Wayne Xin Zhao
- Hongteng Xu
- Ji-Rong Wen
affiliations:
- 中国人民大学高瓴人工智能学院
arxiv_id: '2609.28416'
url: https://arxiv.org/abs/2609.28416
pdf_url: https://arxiv.org/pdf/2609.28416
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent 世界模型 · 决策状态编辑
tags:
- World Model
- LLM Agents
- Action Judge
- State Revision
- EditAct
- RFT
one_liner: 提出AEWM，将世界模型从预测环境观测转为编辑智能体状态，缓解任务状态污染并提升长程智能体表现
practical_value: '- 在电商/搜索 Agent 场景，不要花大力气预测高熵搜索结果或工具返回，而是训练一个动作效应判别器（critical / exploratory
  / noisy），在真实执行前截断 noisy 决策，直接编辑 reasoning+action 再执行，能减少无效检索和错误假设累积。

  - 三分类（critical / exploratory / noisy）比二元好坏更实用：保留信息收集类探索动作，避免过度剪枝；可用于 query 选择、页面抓取、工具调用门控等环节。

  - 用修正后的轨迹做 rejection sampling fine-tuning（AEWM-RFT），可将在线干预能力蒸馏回小 agent，线上无需额外世界模型，适合部署受限场景；类似把
  verifier / controller 蒸馏进策略模型。

  - 数据合成可复用：用强模型标注成功轨迹中每步贡献类型，将被判为 noisy 的步作为 revision 训练样本，并依据后续真实执行是否取得实质进展过滤，能获得高质量的状态纠正数据。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现有语言世界模型通常预测环境观测（工具响应、搜索结果、终端输出），但这些观测高熵且依赖执行细节，预测困难且价值有限。更关键的是，长程 LLM Agent 在部分观测下容易把未经验证假设当事实、保留过时计划、把局部进展误当完成，这些错误会进入历史并持续污染后续决策，即任务状态污染。AEWM 转而建模推理与动作如何塑造未来任务进展，不重建环境观测。

**方法关键点**  
- **Action Judge**：给定执行前状态（任务+历史+候选 reasoning-action），预测其属于 critical（关键进展）、exploratory（有效降低不确定性）或 noisy（无进展/重复/方向错误）。  
- **State Revision**：对 noisy 的候选，从同一可见历史生成修正的 reasoning-action，替换当前 continuation，而不是只给 critique。  
- **EditAct**：将判断与编辑嵌入真实执行循环，仅替换 noisy 决策，保留 productive 动作，真实环境仍提供观测。  
- **训练**：跨 Search / Terminal / SWE 三域，先 mid-training 52B tokens 获得交互知识，再 SFT 120K 样本（Action Judge 60K + State Revision 60K）校准两能力。  
- **AEWM-RFT**：用 EditAct 产生的高质量轨迹做 rejection sampling fine-tuning，把状态纠正能力内化回 agent，推理时不再需要 AEWM。

**关键实验**  
在 3,000 决策的 Action Judge benchmark 上，AEWM 达到 70.5% macro-F1，比最强 frontier baseline DeepSeek-V4-Pro 高 10.6 个百分点。EditAct 在六个 benchmark、三个 backbone 上平均分提升 6.7/5.2/3.2 点（对应 Qwen3.5-4B/9B/35B-A3B），且超过 step-level/trajectory-level Best@3。AEWM-RFT 在 BrowseComp、Terminal-Bench 2.0、Doc2Repo 上比 Self-RFT 高 2.2–2.6 点，无需在线 AEWM。消融显示直接编辑优于 agent resampling 和 reasoning hint，联合编辑 reasoning+action 优于只编辑单一组件。

**最值得记住的一句话**  
不要预测世界，编辑状态：在真实执行前把有问题的 reasoning–action continuation 替换掉，比预测高熵工具响应或只给 critique 更有效。
