---
title: 'Procedural Graphs: Self-Evolving Execution Structures for LLM Agents'
title_zh: 面向 LLM Agent 的过程图：自演化的执行结构
authors:
- Yuxing Lu
- Yicheng Chen
- Shanchan Wu
- Sercan Ö. Arık
affiliations:
- Google
- Georgia Institute of Technology
- Peking University
arxiv_id: '2609.09153'
url: https://arxiv.org/abs/2609.09153
pdf_url: https://arxiv.org/pdf/2609.09153
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: Agent 过程性记忆与自演化图结构
tags:
- Procedural Graph
- LLM Agent
- Self-Evolution
- Tool Use
- Memory
- Validation Gating
one_liner: 用可编辑的 (procedure, relation, procedure) 图组织过程性知识，在线按当前节点生成局部引导，离线通过验证门控自演化图结构
practical_value: '- 在搜索/推荐 Agent 工作流中，把工具或技能（query 改写、召回、精排、解释、政策校验）抽象为过程图节点，边属性写
  condition/guidance/pitfalls；推理时用最近一次 tool call 做 exact match 定位，取 2-hop 邻域生成 guidance，比注入全图省
  token 且效果更好。

  - 离线自演化：用成功/失败轨迹对比让 LLM refiner 提出增删节点/边、改属性，必须通过 held-out validation 不降分才提交；保留
  rejection memory，避免重复无效修改。可迁移到自动优化广告投放、选品、客服 Agent 的流程。

  - 图结构在权重外，便于审计、回滚和人工修正，适合电商合规/风控；不需要 fine-tune 模型。

  - 注意效率：localized generative guidance 在长轨迹上能减少 solver steps，但总 token 仍可能上升，需缓存或选择性生成。'
score: 9
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM Agent 沿长轨迹行动时，往往依赖不断增长的扁平行历史，过程性知识隐式分布在生成中，容易目标漂移、工具乱序、重复无效动作。现有 memory/reflection 方法保存经验但不显式连接步骤；workflow/state machine 显式但依赖人工设计。需要一种结构化、可编辑、能随执行反馈改进的程序性记忆。

## 方法关键点
- **过程图 PG**：有向属性图，节点抽象工具动作、推理步骤或状态；边为 (procedure, relation, procedure) 三元组，属性包含 condition、guidance、pitfalls，描述何时可迁移、如何执行、避免什么。
- **在线推理**：用最近一次 tool call 精确匹配定位当前节点，抽取 2-hop 出边邻域；guidance LLM 读取子图拓扑和最近 w=3 步轨迹，生成逐步情境 guidance，追加到 solver prompt；软引导，不强制约束动作。
- **离线自演化**：每轮在训练 batch 上执行，refiner 对比失败/成功轨迹，提出 Add/Delete/Update 图编辑；候选图在 held-out validation 上评估，只有验证分数不降才提交；被拒候选进入 rejection memory，作为后续迭代的负例。
- **初始化**：可从零开始构建，也可从专家先验出发；自演化能修复有缺陷的专家图。

## 关键实验
- 在 HotpotQA、MultiChallenge、GDPval、ALFWorld、tau-bench、BFCL v3 及 EnterpriseArena 上，4 个 LLM 共 24 个设置中 PG 在 21 个上第一或并列第一；对比最强 baseline 赢 19 次、平 2 次、输 3 次，符号检验 p=4.3e-4。
- 长周期 EnterpriseArena：PG 显著提升生存率，Claude 44%→58%，Gemini Pro 6%→34%，Grok 26%→40%；测试生存率 85% vs baseline 0%。
- 构建模式：scratch + online evolution 在 HotpotQA 上 Ans F1 从 71.21 提升到 78.79；MultiChallenge 中 flawed expert prior 使分数从 87.50 降到 58.93，自演化恢复到 92.86。
- 效率：localized generative guidance 相比 full graph generative 在 ALFWorld 省 70.9% token，GDPval 省 18.1%，MultiChallenge 省 14.8%，并在长轨迹上减少 solver steps。

## 最值得记住的一句话
把“what to do next”组织成可编辑的 (procedure, relation, procedure) 图，比全文记忆和人工 workflow 更稳定，且自演化可以修复有缺陷的专家先验。
