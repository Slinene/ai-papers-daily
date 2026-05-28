---
title: 'Share More, Search Less: Collaborative Parallel Thinking for Efficient Test-Time
  Scaling'
title_zh: 协作并行思维：通过信息共享减少测试时搜索冗余
authors:
- Xinglin Wang
- Hao Lin
- Shaoxiong Feng
- Peiwen Yuan
- Yiwei Li
- Jiayi Shi
- Yueqi Zhang
- Chuyi Tan
- Ji Zhang
- Boyuan Pan
affiliations:
- School of Computer Science, Beijing Institute of Technology
- Xiaohongshu Inc
arxiv_id: '2605.27030'
url: https://arxiv.org/abs/2605.27030
pdf_url: https://arxiv.org/pdf/2605.27030
published: '2026-05-25'
collected: '2026-05-28'
category: Reasoning
direction: 协作式并行推理 · Test-Time Scaling
tags:
- Test-Time Scaling
- Parallel Thinking
- Information Sharing
- Search Efficiency
- Collaborative Reasoning
one_liner: 提出训练无关的协作并行推理框架 CPT，在并行分支间实时共享压缩信息，显著提升测试时扩展的搜索效率
practical_value: '- 在多策略推荐系统的在线探索中，可借鉴共享信息池机制：不同探索分支发现的用户偏好或有效特征及时广播，避免重复探索，加速收敛。

  - Agent 多智体协作场景下，各 Agent 的中间推理结果压缩存入共享内存，其他 Agent 可直接复用，减少重复搜索，提升任务完成效率。

  - 生成式推荐中的树搜索或束搜索，可让不同束路径共享已验证的有用 token 序列信息，降低计算冗余，提升解码吞吐。

  - 工程上，CPT 的实现是轻量的、训练无关的，可直接嵌入现有并行推理管线，信息提取与去重广播开销小，易于部署。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有并行测试时扩展（TTS）方法中，搜索分支相互隔离，分支间的中间发现无法共享，导致大量重复探索，需更多步骤才能收集到正确决策所需信息。

**方法**：提出协作并行思维（CPT），一种训练无关的推理框架。在每个搜索步骤中，CPT 从活跃分支提取紧凑的中间信息，维护一个去重的查询级信息池，并通过输入上下文广播池中条目，使后续步骤中的每一分支可以重用其他分支的发现，而非重新探索相同信息。

**关键结果**：在数学推理基准 HMMT 和 AIME 上，CPT 在不同 rollout 预算和模型规模下均建立起更优的准确率-延迟帕累托前沿，优于所有强基线，验证了搜索时协作是高效并行 TTS 的有效方向。
