---
title: Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented
  Large Language Models
title_zh: 检索增强 LLM 的搜索状态自评估强化学习
authors:
- Taewhoo Lee
- Minju Song
- Jungwoo Park
- Chanwoong Yoon
- Junha Jung
- Hyeon Hwang
- Sanghoon Lee
- Minbyul Jeong
- Jaewoo Kang
affiliations:
- Korea University
- Amazon
- AIGEN Sciences
- University of Massachusetts Amherst
- Meridian Intelligence Global Inc
arxiv_id: '2610.30435'
url: https://arxiv.org/abs/2610.30435
pdf_url: https://arxiv.org/pdf/2610.30435
published: '2026-10-20'
collected: '2026-10-29'
category: Agent
direction: Search Agent 自评估 RL 训练
tags:
- Search Agent
- Reinforcement Learning
- Self-Assessment
- RAG
- GRPO
- Search-State Awareness
one_liner: 提出 SARL：训练时自评估搜索轨迹并据此修订，配合双重奖励，无推理开销地内化搜索状态意识
practical_value: '- **训练期自评估、推理期零开销**：在训练时给搜索/对话 Agent 增加一个隔离的 `self-assessment` 阶段，让它反思“已获得哪些证据、还缺什么”，推理时不调用评估器，不增加额外
  token 和延迟。适合线上 RAG、商品搜索 query 改写、客服多轮 Agent 直接落地。

  - **双重奖励设计可直接迁移到多轮检索/推荐场景**：用 answer correctness 的 transition（错→对、对→对、错→错、对→错）给评估动作打分，并用
  `α^(n-1)` 指数惩罚频繁评估。电商搜索中可对“多轮 query 改写是否带来召回/成交提升”设置类似不对称奖励，同时限制重复调用搜索接口，控制成本和时延。

  - **把评估与主轨迹解耦，避免长 horizon 训练崩溃**：AutoRefine/ReSeek 将反思 inline 写进每一轮，导致上下文膨胀和训练后期分数归零。SARL
  将评估放在隔离上下文，只在 INCOMPLETE 时作为 user feedback 注入。做多轮对话/深度研究型推荐 Agent 时，建议将状态评估与生成轨迹分离，可稳定扩展到
  32+ turn。

  - **无需 SFT warmup、多智能体编排或外部裁判模型**：SARL 是 standalone RL 框架，用 GRPO + 自定义奖励即可，工程复杂度低，适合资源有限的业务团队快速实验。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 search agent 虽然能迭代检索外部信息，但普遍缺乏 **search-state awareness**：无法识别已获取哪些信息、还缺哪些约束，导致两类失败——基于不完整证据的幻觉推理（如把宾大当成天主教大学）和过早终止搜索。SFT 依赖昂贵轨迹标注且泛化差；RL 用稀疏 outcome 奖励又容易在长 horizon 下训练崩溃，已有 inline 反思方法（AutoRefine/ReSeek）在扩展到 32 轮时验证分数会掉到接近零。需要一种机制让 LLM 在训练中学会内部化搜索状态意识，同时推理时不引入额外开销。

**方法关键点**  
- **自评估阶段**：在标准 think-search-answer 轨迹结束后，用同一策略模型在隔离上下文对轨迹重新评估，生成结构化判断：识别问题关键约束、分析检索证据已解决哪些约束、输出 COMPLETE / INCOMPLETE。  
- **轨迹修订**：若 INCOMPLETE，将完整评估作为一条 user feedback 注入原上下文，驱动继续搜索和修订答案；COMPLETE 则终止。评估与主轨迹解耦，避免上下文膨胀。  
- **双重奖励**：总奖励 `R_total = r_final * α^(n-1) + λ * r_assess`。`α^(n-1)` 指数惩罚评估次数，抑制依赖评估重试，鼓励前期充分搜索。评估奖励按答案正确性转移设计：错→对 `+1.0`，对→对 `+1.0`，错→错 `-0.1`，对→错 `-2.0`，强奖励修正行为、严惩退化。  
- **训练设置**：45K 混合数据（NQ 15K / HotpotQA 15K / ASearcher 15K），GRPO 优化，max 32 turns，α=0.8，λ=0.5，Qwen2.5-7B 为基座。  

**关键结果**  
在 10 个 benchmark（单跳 QA、多跳 QA、深度研究）上，SARL 平均得分 0.429，相对最强 baseline ASearcher 的 0.345 提升 **24.3%**；多跳 QA 平均相对最强 baseline 提升 **35.9%**，深度研究提升 **27.9%**。在 Musique 和 FRAMES 上相对最佳 baseline 分别提升 58.1% 和 48.3%。SARL 还超过 SFT+RL 的 RAG-R1 和训练免多智能体 MA-RAG（包括 70B 版本），跨 Llama-3.1-8B 与 Qwen2.5-14B 均稳定提升，而 GRPO 基线在换 backbone 后训练崩溃。分析显示 SARL 训练后期 unique search query 增加 2 倍以上，document recall 持续上升。

**最值得记住的一句话**  
把自评估从推理时提示变成训练期信号，并用“正确性转移 + 指数评估惩罚”双重奖励塑形，就能让 LLM 在不增加任何推理开销的情况下内化搜索状态意识，稳定扩展到长 horizon 搜索任务。
