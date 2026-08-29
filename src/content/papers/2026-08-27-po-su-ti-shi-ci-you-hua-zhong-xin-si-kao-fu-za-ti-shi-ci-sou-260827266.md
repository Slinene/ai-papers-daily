---
title: 'Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search'
title_zh: 朴素提示词优化：重新思考复杂提示词搜索的必要性
authors:
- Yuan Chang
- Xiaoqi Chen
affiliations:
- Purdue University
arxiv_id: '2608.27266'
url: https://arxiv.org/abs/2608.27266
pdf_url: https://arxiv.org/pdf/2608.27266
published: '2026-08-27'
collected: '2026-08-29'
category: Agent
direction: 提示词优化 · 教师-学生轻量迭代
tags:
- prompt optimization
- LLM
- agent
- reinforcement learning
- transferability
- efficiency
one_liner: 提出单谱系迭代的提示词优化方法NPO，用强教师模型结合轨迹反馈，以更少rollout达到或超越复杂搜索方法GEPA
practical_value: '- **提示词工程做减法**：NPO 证明在固定 student 模型下，用单谱系 + 滑动窗口轨迹反馈 + 强教师（如 GPT-5.5）就能达到甚至超过
  GEPA 等复杂搜索方法；在电商/广告 agent 中可直接套用此简单框架，避免维护多个候选 prompt 池和 Pareto 选择，节省工程复杂度。

  - **公平评测技巧**：使用共享伪随机种子生成环境实例，让不同方法在完全相同的问题分布上比较，降低环境噪声；在业务 AB 测试或策略对比时，若环境可 seed，可借鉴此设计提高对比的统计可靠性。

  - **约束解码隔离格式错误**：用 token-level trie 约束模型输出合法动作（如 JSON 字段、合法选项），使性能评估专注决策质量而非格式好坏；在电商推荐/搜索等结构化输出场景（如生成
  query、商品属性）可显著减少不必要的失败，同时保留 reasoning 自由。

  - **跨模型迁移 prompt**：在便宜小模型上优化出的 prompt 可直接迁移到同家族大模型且收益保持（如 Qwen3-8B 优化后迁移到 Qwen3-32B），跨家族也有正向收益；实际工作中可先在小模型上迭代
  prompt，再部署到线上大模型，避免重复优化成本。

  - **防泄漏监控**：对比优化 prompt 与训练/验证集答案的重叠度，发现主要积累训练集信息而验证集几乎不泄漏；业务中做 prompt 自动优化时也应监控此类污染，避免上线后效果虚高。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**  
自动 prompt 优化是提升 LLM/Agent 性能的重要方向，与 RL 互补，可在不改变模型权重的情况下通过 deployment-time 适应任务。但近期方法（如 OPRO、ProTeGi、MIPRO、GEPA）日趋复杂，依赖 beam search、候选池、Pareto 选择等。本文质疑这种必要性：是否简单的单谱系迭代就能达到相似效果？  

**方法关键点**  
- 提出 Naive Prompt Optimization (NPO)：维护单一 prompt lineage，每次迭代用当前 prompt 执行一个 minibatch 的 rollout，收集完整轨迹和逐条奖励；将最近 W 轮（滑动窗口）的 prompt、轨迹、奖励一并喂给教师模型，让教师直接生成下一版 prompt。  
- 对比 OPRO 只输入历史 prompt 和标量分数，NPO 提供更丰富的轨迹级反馈，但保留 LLM-as-optimizer 的简单性。  
- 实验设计强调低方差：使用共享伪随机种子（matched environment instances）保证不同方法在相同环境分布上评估；用 constrained decoding（token-level trie）强制模型输出合法动作，排除格式错误干扰，只衡量决策质量。  
- 教师模型变化：Qwen3-8B（self-revision）→ DeepSeek-V4-Flash → GPT-5.5，学生固定为 Qwen3-8B。  

**关键实验与结果**  
- 在 IFBench 和 HotpotQA 上，NPO 用更少 rollout 达到与 GEPA 相当或更好性能；教师越强，NPO 优势越突出。例如 IFBench 上 NPO+GPT-5.5 最高 val score 约 0.88，GEPA+GPT-5.5 约 0.87；HotpotQA 上 NPO+GPT-5.5 最高约 0.68，GEPA+GPT-5.5 约 0.61。  
- 跨学生迁移：在 Qwen3-8B 上优化出的 prompt 直接迁移到同家族大模型（Qwen3-14B/32B）时，性能提升基本保持；跨家族（Llama-3.1/3.3-70B、StepFun）也有正向但略低且波动更大。  
- 22 个 TextArena 游戏：NPO 与 GEPA 总体相当，GRPO（LoRA 训练）在某些 prompt 优化不擅长的游戏上提供互补增益，没有全面赢家。  
- 泄漏检测：优化后的 prompt 与训练集答案重叠自然增加，与验证集答案重叠可忽略，排除了评测答案泄漏导致的虚高。  

**最值得记住的一句话**  
强教师模型的推理能力 + 丰富的轨迹反馈可以替代优化器端的复杂搜索；简单的单谱系迭代不仅有效，而且产生可跨模型迁移的 prompt 提升。
