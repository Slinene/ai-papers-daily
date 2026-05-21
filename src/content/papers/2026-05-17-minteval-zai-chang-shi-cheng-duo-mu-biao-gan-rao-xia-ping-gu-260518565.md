---
title: 'LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon
  Agent Systems'
title_zh: MINTEVAL：在长时程多目标干扰下评估 Agent 记忆系统
authors:
- Hyunji Lee
- Justin Chih-Yao Chen
- Joykirat Singh
- Zaid Khan
- Elias Stengel-Eskin
- Mohit Bansal
affiliations:
- UNC Chapel Hill
- The University of Texas at Austin
arxiv_id: '2605.18565'
url: https://arxiv.org/abs/2605.18565
pdf_url: https://arxiv.org/pdf/2605.18565
published: '2026-05-17'
collected: '2026-05-21'
category: Agent
direction: Agent 记忆评估与干扰鲁棒性
tags:
- memory-augmented agents
- long-horizon
- interference
- benchmark
- multi-target aggregation
- lookback
one_liner: 一个面向干扰密集、多领域、长时程记忆的基准，揭示现有记忆系统在回溯与聚合推理上的严重不足
practical_value: '- 在电商/推荐场景中，用户偏好频繁更新且常需回溯历史状态（如曾经喜欢某品牌），现有记忆系统由于过度依赖追加新记忆、缺乏细粒度修改/删除，导致早期信息被覆盖。建议：引入显式时间戳或版本标记，并设计支持
  CRUD 的原子记忆操作，以减少干扰。

  - 多目标聚合任务（如“用户在过去三个月内切换过几次偏好类目”）对应推荐系统中跨会话行为序列的计数或排序需求。当前 Agent 在此类问题上平均准确率仅 26.5%，大幅落后于简单召回，需要在记忆模块中增加结构化聚合算子或专门训练多跳推理能力。

  - 实验表明减少记忆更新频率（增大 chunk size，如从 7 增至 30）能显著提升回溯与计数问题的性能，而不会损害简单最近状态查询。这提示在构建长期用户画像记忆时，应优先采用粗粒度、低频更新策略，避免频繁覆盖。

  - 干扰鲁棒性分析：添加领域外噪声（如通用文本）对 RAG 类系统影响最大，而记忆增强代理相对稳健。在推荐系统中引入检索增强时，应注意检索池的噪声控制，并结合时间衰减或重要性加权来过滤无关信息。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现实中的记忆增强 Agent 需要在长时间交互中持续累积信息，且新信息常以修改、冲突的方式出现，形成破坏性记忆干扰。现有基准大多使用静态、独立的记忆片段，缺乏动态更新、跨版本回溯和跨目标聚合推理的评估。MINTEVAL 填补了这一空白，构建了干扰密集、多领域、要求回溯和多目标聚合的挑战性测试。

## 方法关键点
- **数据集**：涵盖状态追踪（bAbI）、多轮对话（HorizonBench）、维基修订、Git 提交四个领域，每个实例平均 138.8k tokens，最长 1.8M tokens，平均含 86 次更新；共 15.6k 条问答对。
- **问题类型**：单目标召回（简单查询、历史回溯）和多目标聚合（排序、计数、多跳推理），专门考察在密集干扰下的记忆鲁棒性。
- **基线系统**：完整上下文、标准 RAG、HippoRAG、MemAgent、AtomMem、Mem-α、SimpleMem，覆盖检索增强与记忆增强的主流范式。
- **评估指标**：精确匹配（EM），并分解错误源为检索/记忆构建失败和答案生成失败。

## 关键实验与结果
- 所有系统平均准确率仅 **27.9%**，最强方法 MemAgent 也仅 **33.4%**；简单问题平均 47.5%，但历史回溯降至 21.0%，多目标聚合仅 26.5%。
- 错误分解显示：**41.7%** 的性能损失源于检索或记忆构建阶段未能提供必要证据，答案生成阶段另导致 25.2% 的损失。
- 回溯距离越大，性能越差；但记忆增强系统相对更稳健，时间标记的引入可显著缓解 RAG 与全上下文方法在长距离下的退化（如 RAG 从 31.43 降至 10.45）。
- 现有记忆系统严重偏向插入操作 (平均 76.8%)，缺乏修改和删除，导致信息冗余与版本混淆；减少记忆更新频率（增大 chunk size）能有效提升回溯与聚合类的准确率。

## 核心结论
MINTEVAL 表明，真实的长期记忆远不止长上下文检索，更关键的是在干扰中忠实维护演化状态、支持细粒度修改与回溯、以及跨多目标的聚合推理，当前系统在这些维度上普遍失败。
