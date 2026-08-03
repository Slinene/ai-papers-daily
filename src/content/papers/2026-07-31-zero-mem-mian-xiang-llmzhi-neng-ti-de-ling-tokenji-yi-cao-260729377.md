---
title: 'Zero-Mem: Zero-Token Memory Operations for LLM Agents'
title_zh: Zero-Mem：面向LLM智能体的零Token记忆操作
authors:
- Yilin Xiao
- Zhehan Zhu
- Yujing Zhang
- Jin Chen
- Zijin Hong
- Luyao Zhuang
- Qinggang Zhang
- Shengyuan Chen
- Xiaocao Ouyang
- Lingfei Ren
affiliations:
- The Hong Kong Polytechnic University
- Southwestern University of Finance and Economics
- Jilin University
arxiv_id: '2607.29377'
url: https://arxiv.org/abs/2607.29377
pdf_url: https://arxiv.org/pdf/2607.29377
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 零Token记忆操作
tags:
- zero-token memory
- agent memory
- graph-based retrieval
- provenance-preserving
- evidence calibration
- LLM agent
one_liner: 提出零Token记忆框架，用实体图和时序层次替代生成式抽象，全部记忆操作不占用LLM调用或Token。
practical_value: '- **零LLM记忆管道**：记忆构建、检索、路由、校准等全部环节都用确定性算法和编码器完成，避免生成式抽象，可直接用于电商Agent的“用户长期偏好/行为记忆”，将记忆部分与最终生成解耦，极大降低Token开销和延迟。

  - **双视图结构化检索**：实体-上下文图捕获跨会话关联，时间层次保留对话局部性和状态，通过查询路由动态加权融合。推荐系统Agent可以仿造这种“关系+时序”双重索引，处理用户多轮意图变迁与跨会话关联。

  - **证据校准与封闭**：检索后自动补充关系桥接和局部上下文，再用边界与类型滤波提炼证据，最后对答案进行确定性校验。这套方法可复用到电商QA或对话推荐的后处理阶段，提高生成事实性与一致性，无需额外LLM调用。

  - **保留原始痕迹**：Zero-Mem不生成中间摘要或笔记，所有证据都可追溯到原始交互，适合需要审计、合规且长周期交互的电商客服或导购场景，在低成本下提供可解释的原文支持。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：现有LLM Agent的记忆系统大多依赖额外的LLM调用生成摘要、记忆卡片或图索引，这不仅带来持续的Token和时间成本，还可能在抽象过程中丢失原始证据的细节。Zero-Mem提出一种“零Token记忆操作”范式：在所有记忆相关环节（构建、组织、检索、路由、校准）完全不调用LLM、不消耗输入输出Token，仅最终问答环节使用LLM，从而在保持竞争力的同时大幅降低开销。

**方法关键点**：
1. **源头保留**：直接以原始交互痕迹作为记忆源，不做生成式压缩或改写。
2. **双视图构建**：$
- $实体-上下文图：用NER抽取实体，实体与所在上下文单元构成共现边，相邻上下文单元构成邻接边，权重由共现频率决定，形成关系索引。
   - 时间层次：将对话组织为 turn → window → episode → local span 的多粒度结构，保留对话顺序、局部上下文和会话边界。
3. **查询路由**：从查询中提取轻量画像（subject、keywords、answer-type、temporal cues），根据问题结构判断偏关系型还是偏局部时序型，决定双视图的融合权重ρ。
4. **双视图检索与融合**：图视图用实体对齐+个性化PageRank传播激活，层次视图用粗到细的episode-window-turn召回，两者经归一化后按ρ加权融合。
5. **证据封闭与校准**：对融合后的主证据补充图桥接邻居和时间局部上下文，再经确定性过滤（违反边界、实体要求等）和排序，输出紧凑证据集合；最终答案按答案类型、证据支持度进行确定性后校准。

**关键结果**：
- 在长期对话记忆基准LoCoMo上，GPT-4o-mini下平均F1达到59.15，BLEU-1 52.96，比此前最强基线GAM分别提升5.40和5.45分；Qwen2.5-14B下所有子任务全面第一。
- 在长上下文多跳推理HotpotQA上，不同上下文长度（56K/224K/448K）均取得最高F1，平均领先第二名的稳健基线5.52分。
- 效率对比：记忆操作0 LLM Token消耗，总时间334.77秒（0.22秒/查询），比最快速基线LightMem延迟降低57.6%，同时F1和BLEU-1分别高出约10%和11.5%。
- 消融实验证实实体图与时序层次互补，证据封闭与校准分别带来约4.2/3.2和2.0/2.8 F1/BLEU-1增益。

**核心 insight**：结构化记忆并不必须生成中间表示；通过保留原始痕迹并构建互补的非生成式视图，可以实现高性能且零LLM开销的证据选择。
