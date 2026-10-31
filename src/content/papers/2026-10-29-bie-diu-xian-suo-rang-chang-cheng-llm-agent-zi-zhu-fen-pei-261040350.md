---
title: 'Don''t Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive
  Resource Self-Allocation'
title_zh: 别丢线索：让长程 LLM Agent 自主分配认知资源
authors:
- Zheng Zhu
- Xiaozhuan Liang
- Xi Chen
- Bei Yu
- Jiaya Jia
affiliations:
- The Chinese University of Hong Kong
- Tencent
- The Hong Kong University of Science and Technology
arxiv_id: '2610.40350'
url: https://arxiv.org/abs/2610.40350
pdf_url: https://arxiv.org/pdf/2610.40350
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: Agent 长程上下文管理 · 多 episode RL
tags:
- LLM Agents
- Context Management
- Long-Horizon Reasoning
- Multi-episode RL
- Working Memory
- GAIA
one_liner: CORAL 用可调用的记忆管理与上下文重置工具，让 Agent 自主 checkpoint 并跨 episode 做 RL，GAIA 上 8B
  达 42.8% 且 token 成本少 6-7 倍
practical_value: '- 在电商/搜索的 long-horizon Agent（如导购调研、售后多跳查询、广告素材调研）中，可引入显式 Working
  Memory 工具：用 MM 维护“任务进度 + 已验证事实”，在上下文过大时触发 CO 清空历史只保留 memory。能显著降低线上 token 成本（本工作输入
  token 减少 87.4%），并缓解长会话中模型注意力被旧上下文稀释。

  - 训练数据可把 multi-episode 轨迹按上下文重置边界拆成独立对话，后续 episode 的输入 = system prompt + user task
  + 上一 episode 产出的 memory state；这比平铺拼接更符合推理现场，且天然教会模型“从检查点续跑”。推荐在 SFT 时对 observation
  tokens 做 loss mask，只学 agent 自己的 thought/action。

  - 对于弱/中等开源模型，光靠 prompt 加工具可能无效甚至掉点（Qwen3-8B prompting 仅 20.4% vs ReAct 19.4%）；建议走“SFT
  + 简单 RL”。RL 不需要复杂信用分配：把 trajectory 最终 reward 广播到所有 episode 并池化做 group advantage（Multi-episode
  ARPO），即可提升 checkpointing 策略并稳定输出方差。

  - 工程上注意 Memory 污染：CO 重置会永久丢弃历史中可交叉验证的证据，错误事实一旦写入且被 reset 后不可恢复。推荐 MM 写得保守、CO 只在上下文真正难管理时调用；必要时给
  memory 条目保留 provenance/引用，以便后续校验。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：LLM Agent 在长程任务中，每个 Thought-Action-Observation 循环都会在上下文里堆积冗长环境反馈和失败历史，造成“认知过载”，稀释注意力、破坏规划。现有压缩/蒸馏多为规则触发或外部模型，且没有把 checkpoint 作为可学习策略。

**方法关键点**：
- CORAL 提供两个 agent 自主调用的工具：MM（Memory Management）维护 Task Progress（计划与子目标状态）和 Verified Facts（已确认事实）；CO（Context Optimization）执行硬重置：清空对话历史，只把当前 memory 作为 observation 注入下一 episode。
- 一条轨迹被 CO 切分为多个 episode，后续 episode 初始上下文 = system prompt + user task + memory state。
- SFT：从 WebShaper 合成问题，Claude Sonnet 4 生成 2,932 条 web trajectories + 241 数学轨迹；按 CO 边界拆成 3,682 个对话；loss 仅计算 agent 生成的 thought/action tokens，observation 被 mask。
- Multi-episode ARPO：把 trajectory 最终奖励广播给所有 episodes，全部 episode 池化后按 question 归一化做 group advantage，跨 episode 做信用分配，使 checkpointing 策略可学。

**关键结果**：GAIA 上 Qwen3-8B 从 ReAct 19.4% 提高到 SFT 41.6%、RL 42.8%；Level 2/3 提升显著（45.7%/19.8% vs CK-Pro 42.3%/8.3%）。Claude Sonnet 4 仅 prompt 版达 65.0%，接近 OpenAI Deep Research 67.4%。BrowseComp 上 CORAL 比 ReAct 高 8.0 点（30.7% vs 22.7%）。推理成本：每轨迹输入 token 136K vs 1,078K（少 87.4%），LLM calls 15.2 vs 45.3，峰值上下文 12.7K vs 30.6K；训练后 CO 调用仅 0.21 次，说明 Checkpoint 质量而非重置频率是关键。

**最值得记住**：管理好注意力不是精度税而是精度来源——更少 token 换来更高准确率，关键在于把“何时压缩/重置”变成 agent 可学习的策略。
