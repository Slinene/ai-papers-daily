---
title: 'MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents'
title_zh: MEMOIR：长程 LLM Agent 的训练免记忆生命周期
authors:
- Mayank Anand
- Subham Raj
- Aman Vaibhav Jha
- Sriparna Saha
affiliations:
- Indian Institute of Information Technology Allahabad
- Indian Institute of Technology Patna
arxiv_id: '2611.07631'
url: https://arxiv.org/abs/2611.07631
pdf_url: https://arxiv.org/pdf/2611.07631
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 长程记忆生命周期优化
tags:
- LLM Agents
- Memory Lifecycle
- Retrieval
- Consolidation
- UCB
- Training-Free
one_liner: 训练免记忆生命周期：使用后归因更新检索优先级，压缩前用 judge 门控筛查证据保留
practical_value: '- 记忆写入不要用静态重要性打分：对电商 Agent 中的用户偏好、历史行为、搜索词等记忆，采用“使用后归因”在线修正检索优先级，避免陈旧记忆挤占新证据。

  - 合并/摘要压缩前引入 judge-gated screening 验证证据保留，适合对话摘要、长期偏好摘要等场景；把昂贵的 judge 校验放离线周期性执行，保证线上写路径无额外
  LLM 调用。

  - 检索阶段加入 UCB 式探索奖励，给曝光不足的记忆更多召回机会，可迁移到推荐系统多路召回或记忆检索，提升长尾 query/用户偏好覆盖。

  - 工程实现可复用：在线只做轻量检索与写入，压缩和筛查异步离线完成，有助于控制 latency 和成本。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长程 LLM Agent 需要跨会话记忆，但现有系统写记忆时使用静态重要性分数，使用后不更新，导致压缩可能破坏未来查询所需证据，检索偏向陈旧记忆。

**方法**：MEMOIR 为训练免生命周期，将 judge 门控压缩与事后归因统一。压缩前 screening gates 验证答案相关证据是否被保留；每次查询后 attribution 估计哪些检索记忆支撑答案并更新检索优先级；UCB 式探索奖励提升曝光不足记忆的召回，避免高频记忆挤出有用少见证据。

**结果**：在 1,905 条 LoCoMo QA 对上，完整检索栈证据 recall@5 较裸余弦提升 11.92 个百分点；confidence-gated feedback 再加 1.50 个百分点（无需参考答案或 reranker 训练）；部署不可用 oracle 总体 +1.84、多跳 +8.05。Judge 门控合并使文本证据 recall 从 58.82% 到 59.08%，活跃存储减少 1.42%，100 次审计合并 0 损失，单侧 95% 上界损失率 2.95%。在线写路径无额外 LLM 调用，合并筛查放离线。
