---
title: Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite
title_zh: 面向LLM智能体的分层图记忆：路径级定位与协调重写
authors:
- Xiawei Yue
- Boran Wang
- Xiaoqing Zhang
- Shuxin Zheng
- Ziwei Zhang
affiliations:
- Nankai University
- Zhongguancun Academy
- Beihang University
arxiv_id: '2608.05095'
url: https://arxiv.org/abs/2608.05095
pdf_url: https://arxiv.org/pdf/2608.05095
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent记忆演化与证据定位
tags:
- Hierarchical Graph Memory
- Path-level Localization
- Coordinated Rewriting
- Agent Memory
- Long-term Reasoning
- Conflict Resolution
one_liner: 提出分层图记忆框架HiGram，通过MicroGraph路径级定位与协调重写，提升长程对话问答质量并大幅降低Token消耗
practical_value: '- 借鉴分层图记忆架构：将用户记忆分为粗粒度节点（如商品类别、场景）和细粒度记忆单元（具体行为、事实），降低检索时遍历全量历史的开销。

  - 路径级证据定位：在电商对话推荐中，根据当前查询和用户反馈，定位支持推荐理由的证据子图（如购买序列、偏好演变路径），减少上下文噪声。

  - 协调重写机制：当用户信息更新时（如地址变更、偏好改变），不仅更新单个事实，还要更新依赖该事实的推断记忆（如推荐策略），保持一致性，避免过时信息。

  - Token效率优化：通过在推理时只加载定位到的子图和路径，显著降低LLM调用Token数，在实时场景中更可行。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
长程推理 Agent 的记忆系统需要随新事实与反馈持续高效更新。现有图记忆方法将所有记忆存为平铺图，随时间累积会引入大量无关上下文，增加证据选择成本；更新时仅独立修改记忆单元，忽略证据路径的传播，导致重复重写且可能残留过时依赖。本文指出记忆组织与更新的粒度应当匹配查询所依赖的证据结构。

## 方法关键点
- **分层图记忆架构**：上层节点（主题、对象类别、上下文）连接具体记忆单元（MemoryUnit），形成粗到细组织，避免检索时遍历全图。
- **MicroGraph 路径级定位**：
  - 根据查询与更新构造临时记忆单元，提取锚点定位相关 MicroGraph，构建支撑子图。
  - 在子图中枚举候选证据路径，通过匹配临时记忆的属性、依赖一致性等选出受影响证据路径，确定重写区域。
- **协调重写**：在选定的路径内，先进行**单元内重写**更新记忆状态，再根据依赖关系进行**单元间重写**，撤销无效依赖，维持证据一致性。

## 关键实验结果
- **数据集**：LoCoMo（长程对话问答）与 MemConflict（冲突感知记忆评估）。
- **基线**：LoCoMo 比 LoCoMo（全历史）、MemoryBank、A-MEM、ReadAgent、MemGPT、Mem0；MemConflict 比 MemOS、LangMem、Letta、Mem0、A-MEM。
- **主要结果**：
  - LoCoMo 上 HiGram 平均 F1 与 LLM-J 最高，且 Token 消耗仅为全历史的 7.2%（GPT-5.4）或 ReadAgent 的 15.8%（GPT-4o）。
  - MemConflict 上整体最优，动态冲突 UOCS 49.14、静态冲突 AA 68.75/CRS 68.06、条件冲突 AA 90.00，证据选择 SEH@3 81.06、SRS 77.31 均领先。
  - 消融显示移除 MicroGraph 组织导致 Token 增加 68.6% 且 LLM-J 下降；移除支撑子图各指标均下降。
  - 协调重写策略优于仅追加或关系级更新，尤其在静态冲突上优势显著。

## 核心启示
记忆系统的关键不在于存储更多历史，而在于能精准定位查询与更新共同影响的证据路径，并协调更新记忆状态与依赖关系。
