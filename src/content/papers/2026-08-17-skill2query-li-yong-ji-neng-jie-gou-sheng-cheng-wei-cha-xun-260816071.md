---
title: 'Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent
  Skill Retrieval'
title_zh: Skill2Query：利用技能结构生成伪查询用于Agent技能检索
authors:
- Lihui Ding
- Zihan Guo
- Bingwei Lu
- Chenyu Zhou
- Yuanjian Zhou
- Weinan Zhang
- Jianghao Lin
- Dongdong Ge
affiliations:
- Fudan University
- Sun Yat-sen University
- Shanghai Innovation Institute
- Shanghai Jiao Tong University
arxiv_id: '2608.16071'
url: https://arxiv.org/abs/2608.16071
pdf_url: https://arxiv.org/pdf/2608.16071
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent 技能检索 · 结构感知伪查询生成
tags:
- Agent Skill Retrieval
- Pseudo-Query Generation
- Knowledge Graph
- Query Expansion
- Retriever Training
one_liner: 将技能文档解析为知识图谱，三阶段生成能力对齐、参数一致的伪查询，提升检索与训练效果
practical_value: '- 对电商/Agent 平台的技能、工具、商品文档检索：不要直接把整篇文档塞给 LLM 生成伪查询；先做结构解析（能力点、参数
  schema、使用示例），再分阶段生成，能明显改善参数一致性与能力覆盖。

  - 伪查询可同时服务离线索引增强和在线查询扩展：离线对名称/简短描述这类稀疏索引收益最大；在线适合补长尾表达，配合 RRF 融合简单有效。

  - 在 fine-tune retriever 前，用 Exec-Pass、Func-Coverage、Distinct-3 等指标筛选结构合法的伪查询，比只追求表面多样性更能提升下游
  R@1/nDCG@1。

  - 当底层 LLM 推理能力较弱时，高质量技能/工具检索对端到端任务成功率提升更明显；在导购 Agent 或工具推荐中可优先把检索质量做高，而不是依赖强模型硬扛。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Agent 技能检索存在非对称匹配：用户查询短、口语化、目标导向；技能文档长、技术化、面向开发。伪查询生成能缓解标注瓶颈，但 doc2query/InPars 类方法把整篇技能文档当平文本，生成的查询往往只有主题相关，缺少具体能力 grounding 与参数一致性。论文将问题显式化为 capability-grounding gap 和 parameter-consistency gap。

## 方法关键点
- 先把每个 SKILL.md 抽成 Skill Knowledge Graph (SKG)：节点类型 Skill / Capability / Parameter / Example，边类型 has_capability / has_parameter / has_example / fill_param / demonstrates。
- 三阶段生成：Style Mimicker 从示例中抽句法模式、领域词、参数表达；Query Template Generator 基于 capability 和参数 schema 生成带 {param} 占位符的模板，强制覆盖所有 capability；Param Filler 按 examples→enum→default→type fallback 填参，并用类型/范围/枚举/必填校验。
- 生成结果支持三种用法：离线索引增强、在线查询扩展（RRF 融合）、伪查询-技能对训练 retriever。

## 关键实验
在 TheoremQA / LogicBench / ToolQA / CHAMP 上，从 26,262 个技能候选生成 700K 伪查询。生成质量上，Exec-Pass 达 42.85%，比 Few-shot +16.94pp、Zero-shot +23.88pp、SkillFlow-style +20.09pp。离线索引增强在 BM25 name 配置下，ToolQA R@1 从 5.52% 提升到 32.03%；SkillRouter 在 ToolQA 上 R@1 从 35.80% 提升到 47.34%。作为训练数据时，Skill2Query 在四个数据集上 R@1/nDCG@1 均优于 Few-shot 和 SkillFlow-style，LogicBench R@10 +10.79pp。端到端任务成功率在 DeepSeek-V4-Flash 上从 73.76% 提升到 82.33%。

最值得记住：结构化中间表示 SKG 比把整篇文档塞给 LLM 更重要——把风格、能力、参数三类信息源分开建模，是伪查询质量提升的关键。
