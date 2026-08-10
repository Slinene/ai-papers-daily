---
title: 'TEPA: Revoking Stale Memories for Conflict-Robust Language Agents'
title_zh: TEPA：通过撤销过时记忆构建鲁棒语言代理
authors:
- Yan Zhou
- Yue Ouyang
- Kaiyang Zheng
- Suncheng Xiang
affiliations:
- 长沙理工大学数学与统计学院
- 上海交通大学生物医学工程学院
arxiv_id: '2608.07429'
url: https://arxiv.org/abs/2608.07429
pdf_url: https://arxiv.org/pdf/2608.07429
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 记忆生命周期与冲突消解
tags:
- Memory Pollution
- Lifecycle Revocation
- Agent Memory
- Staleness
- Conflict Keys
- TEPA
one_liner: 引入冲突键撤销机制，解决长期记忆因陈旧证据污染 prompt 导致性能下降的问题
practical_value: '- 在用户偏好、商品属性等更新场景，采用基于冲突键的记忆撤销，防止旧信息混入 prompt，提升推荐/客服 Agent 的一致性。

  - 将记忆划分为 Active/Revoked 等生命周期状态，支持审计且确保当前检索仅使用有效记忆，适合长期用户画像管理。

  - 局部撤销仅针对冲突键，避免全局重置对其他任务的影响，适合多场景搜索推荐系统。

  - 工程中应设置“无记忆基线”评估记忆模块是否带来损害；撤销操作是防止记忆污染的关键控制点。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
语言代理依赖长期记忆重用用户事实、偏好和任务经验，但当世界变化时，过时记忆仍然可以被检索并注入 prompt，导致决策错误（记忆污染）。追加式记忆等常见策略在隐藏状态反转时，表现可能劣于无记忆，亟需一种能在冲突证据出现后撤销过期记忆的机制。

**方法关键点**  
- 将记忆表示为带键的先例（precedent），每个先例拥有生命周期状态：假设、活跃、吊销。  
- 新证据到来时，按冲突键查找同键但值不兼容的活跃先例，更新支持/冲突计数；当后验均值低于阈值或近期成功率过低时，将先例吊销并移入存档，保留审计能力，检索时仅返回活跃先例。  
- TEPA-Full 增加试运行验证：候选先例需通过支持、反事实和污染检查后才可提升为活跃。  
- 评估覆盖受控隐藏漂移、真实文件执行漂移、偏好更新流以及 MemoryAgentBench 基准。

**关键结果**  
- 受控漂移完全反转阶段：追加式记忆和最后写入胜成功率仅 0.210（无记忆 0.309），TEPA 达 0.950；真实文件执行中同样显现污染，追加 0.203 vs 无记忆 0.298，TEPA 保持 0.950。  
- 偏好更新流：TEPA-Full 整体成功率 0.910，与无记忆（0.908）无显著差异，而追加式仅 0.138。  
- MemoryAgentBench SH-6k 单跳冲突解决：TEPA 匹配最后写入胜（0.890），无撤销变体降至 0.630。  
- 多跳和超长上下文边界实验表明，事实级撤销解决了单跳陈旧冲突，但需要结合检索链和上下文选择才能应对复杂场景。

**核心结论**：持久记忆必须显式管理有效性；陈旧但语义相关的过期证据可能比无记忆更糟，基于键的局部撤销是消除此类污染的关键操作。
