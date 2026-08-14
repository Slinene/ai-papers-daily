---
title: 'SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries'
title_zh: SkillZip：面向可扩展 Agent 技能库的契约保持图压缩
authors:
- Xingyu Tan
- Xiaoyang Wang
- Qing Liu
- Xiwei Xu
- Xin Yuan
- Liming Zhu
- Wenjie Zhang
affiliations:
- UNSW
- CSIRO
arxiv_id: '2608.05604'
url: https://arxiv.org/abs/2608.05604
pdf_url: https://arxiv.org/pdf/2608.05604
published: '2026-08-05'
collected: '2026-08-14'
category: Agent
direction: Agent 技能库压缩与检索
tags:
- LLM Agents
- Skill Library
- Graph Compression
- Procedural Memory
- Contract Preservation
- Incremental Update
one_liner: 执行感知的 section-level 图压缩：用可逆端口化宏保持契约，压缩比 3.46x，效果最高 +12.2 点
practical_value: '- 将推荐/广告 agent 的 SOP（如商品信息清洗→类目映射→创意生成→合规校验）拆成 section-level procedural
  graph，而不是整段文本 skill；检索与缓存单位对齐到子流程，能显著降低 LLM context 占用并提高跨任务复用。

  - 借鉴契约保持压缩：压缩时显式保留流程“边界签名 + 依赖闭包 + verifier 可达性”，可保证压缩后流程仍可执行、可校验、可回滚；适合做线上推荐策略
  / 审核流程的版本化与安全压缩。

  - 宏按需展开（hydrate 紧凑依赖闭包，执行到才展开 macro）可以落地为 Agent 工具编排中的 lazy loading 与按需注入上下文，减少首轮
  token 与延迟。

  - ReZip 的“执行证据修订 risky macros”可借鉴为 skill 库 / prompt 库的在线增量更新与回滚机制：用线上执行失败信号触发局部重压缩，而不是全库重训。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM Agent 的技能库不断增长，推理时 context 预算有限；现有系统以整包技能为单位检索、按文本压缩、检索后才转执行图，导致无法在子技能粒度复用、压缩破坏流程契约、压缩后不可执行/扩展、库更新困难。

方法：SkillZip 以 section-level graph 为过程抽象单元，做契约保持压缩。它把反复出现的 contract-valid motif 重写为可逆 ported macros，保留边界签名、依赖闭包、验证器可达性和源码级扩展能力。推理时先加载紧凑的依赖闭合上下文，仅在实际需要时展开 macro。ReZip 利用执行证据增量整合新技能并修订 risky macros。

结果：在技术类和 embodied agent benchmark 上比最强基线最高提升 12.2 分；压缩比 3.46x，依赖保持 99.2%，验证器可达性 98.7%；在 200–100K 技能库规模下检索鲁棒。
