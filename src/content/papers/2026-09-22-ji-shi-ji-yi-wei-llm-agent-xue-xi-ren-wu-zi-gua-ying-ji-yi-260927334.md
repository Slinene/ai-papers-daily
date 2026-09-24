---
title: 'Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents'
title_zh: 即时记忆：为 LLM Agent 学习任务自适应记忆策展
authors:
- Yefan Zhou
- Yang Li
- Zeyu Leo Liu
- Semih Yavuz
- Shafiq Joty
affiliations:
- Salesforce AI Research
arxiv_id: '2609.27334'
url: https://arxiv.org/abs/2609.27334
pdf_url: https://arxiv.org/pdf/2609.27334
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: Agent 记忆 · 读时策展 / GRPO
tags:
- Agent Memory
- GRPO
- Read-time Curation
- Task-Adaptive
- LLM Agents
one_liner: 把记忆策展从写时推迟到读时，保留原始轨迹并按当前任务合成紧凑 payload，用 GRPO 以即时成功奖励训练策展器，显著提升 Agent 成功率与效率
practical_value: '- 把用户行为序列 / 任务执行日志以原始轨迹存入记忆库，不在写入时总结；推理时用当前 query 或 task 条件化地检索并动态生成
  brief，可适配不同下游任务，避免信息过早丢失。

  - 训练一个独立于执行器的轻量策展器（curator），用 GRPO 以即时任务奖励（成功与否）更新；奖励无延迟，无需人工分组相关任务，训练稳定且可跨 executor
  迁移。

  - 工程上：检索用 BM25 仅在任务描述上做，轻量解耦；存储时用 LLM-as-judge 只滤出成功轨迹，比保留全部并标注是否正确更有效；生成的紧凑 payload
  能降低 executor 输入 token 50% 左右和步数 28% 以上。

  - 冷启动直接空记忆库上线即可，warm-start 收益不大；若需进一步提升，可做一次 staged bank refresh（用训练好的 curator 重建训练库）但收益有限。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 agentic memory 系统普遍在任务完成后立即蒸馏 trajectory 成 reflection、skill、workflow 等固定产物，再由相似度检索。这导致两个根本问题：信息在写时被不可逆丢弃；单一 query-independent 摘要必须服务多种未来任务。同时写时策展面临长时程 credit assignment，难以训练。

**方法关键点**
- 记忆库只存原始 trajectory，不做任何摘要；用 executor-as-judge 过滤成功轨迹，只保留正例。
- 检索用 BM25 在任务描述上选 top-k raw trajectories。
- 策展器 πφ 输入当前任务 xt 与检索轨迹，输出紧凑 task-adaptive payload，包含相关经验、可迁移策略和针对当前任务的具体指导。
- 执行器 πL 冻结，只训练策展器，实现跨 executor 迁移。
- 训练：GRPO，每个训练任务检索轨迹 → 生成 G 个候选 payload → 冻结 executor 分别执行获得即时任务奖励 → 组内 advantage 更新策展器，无 value network；奖励无延迟，无需任务分组。
- 部署时记忆库在线增长，初始为空。

**关键实验**
在 ALFWorld、WebShop、τ2-bench 上，JITMEM 比最强 baseline 分别高 16.2、16.3、3.9 个绝对成功率点。未训练策展器已接近或超越写时记忆方法，例如 WebShop 上 JITMEM-gemini 达 61.0 SR，而 SkillOS 为 41.0。与 RL 训练的写时方法 SkillOS 相比，ALFWorld 77.4 vs 61.2，WebShop 32.8 vs 16.5。效率方面，相对写时方法，输入 token 降低 50.3%–56.3%，executor steps 降低 28.4%–31.4%。消融显示，task-conditioned curation、quality-filtered storage 和保留 raw trajectories 各自独立贡献。

**最值得记住的一句话**
有效的 agent 记忆不仅取决于存什么，更取决于何时、针对哪个任务进行策展。
