---
title: '$τ$-Rec-Books: A Disclosure-Controlled Benchmark for Requirement Elicitation
  in Agentic Recommender Systems'
title_zh: τ-Rec-Books：控制需求披露的智能推荐系统需求诱导基准
authors:
- Bharath Sivaram Narasimhan
- Karthik R. Narasimhan
affiliations:
- Independent Researcher
- Princeton University
arxiv_id: '2611.04459'
url: https://arxiv.org/abs/2611.04459
pdf_url: https://arxiv.org/pdf/2611.04459
published: '2026-11-03'
collected: '2026-11-04'
category: Eval
direction: Agentic RecSys 评测 · 需求诱导
tags:
- Agentic Recommender Systems
- Requirement Elicitation
- Benchmark
- User Simulation
- Structured Search
- LLM Agents
one_liner: 提出控制需求披露时机的书籍推荐评测基准，揭示隐藏需求下智能体成功率从 0.975 跌至 0.283
practical_value: '- 在电商对话推荐 Agent 中，应内置“先问全字段再推荐”的 check：mixed 失败几乎都因不主动询问，显式要求 ask
  能让所有模型 mixed 成功率从最低 0.419 拉到 ≥0.931。可在 prompt 或状态机里把关键硬约束字段逐一询问后再进入检索。

  - 对隐藏偏好/未说需求，不要只把 reject 当失败信号；维护一个“可能隐藏约束”集合，被拒绝商品满足的候选约束都删掉，优先推荐覆盖剩余约束最多的候选。该
  eliminating 策略在 hidden 任务上是 0.956 vs 0.622，远超 popularity。

  - 给 Agent 的工具接口优先做结构化过滤（类目、品牌、价格区间、格式等），而不是只给 top-k 关键词搜索；硬约束场景下 structured search
  平均 +7.1 分，且目录变大时几乎不掉点。

  - 用规则化用户 + 目录元数据校验可低成本复现 disclosure-controlled 评测，无需 LLM judge；在 prompt 或版本迭代时，可先跑这种可验证
  benchmark 再上人类评估，特别关注 hidden NVR 的弃权与 untested recommendation 比例。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：真实对话推荐中用户很少一次性说清需求（ReDial 中仅 36% 主动说出首个类型/年代/地区需求），但现有评测不区分需求是在开场、被问时还是从不披露。τ-Rec-Books 固定请求、只改变披露时机，度量智能体主动询问与验证需求的能力。

方法关键点：
- 数据：150 个任务家族 × 3 披露条件 = 450 任务；20k Wikidata 书籍目录（CC0），含 5k/10k 子集；字段为 genre/language/country/publication year；有 15 个无有效答案（NVR）家族。
- 披露条件：volunteer 开场全部说出；mixed 开场只说一个，被问才说其余；hidden 至少保留一个需求全程不说，问到了拒绝但接受候选书籍并给出 ACCEPT/REJECT。
- 用户与评分：规则化模拟用户按模板回答，ACCEPT/REJECT 只基于目录元数据，无需 LLM judge；5 项协议检查（最多推荐一本、不推历史书、格式检查、NVR 弃权、必调用 recommend）。
- 接口：keyword 用 BM25 top-20 vs structured 用字段联合过滤分页。
- 智能体：DeepSeek/GLM/Qwen/GPT-6.1 Sol；提示变体 base、ask、ask-and-verify、protocol；脚本参照 popularity 与 eliminating。

关键数字：
- 满意度任务成功率随披露条件下降：volunteer 0.975 → mixed 0.756 → hidden 0.283（所有模型/接口一致）。
- structured search 平均 +7.1 分，主要由 Qwen 贡献；目录从 5k 到 20k，keyword 掉 4.2 分，structured 几乎不降。
- mixed 失败主因是不问；加 ask 提示后所有智能体 mixed 成功率 ≥0.931。
- hidden 失败 78% 因推荐了从未提出过的书；要求先 propose 后，成功率达 0.483–0.617，仅追平 popularity 基线，但低于 eliminating 基线 0.956；加入 protocol 提示后达 0.708–0.825，仍不及 eliminating。
- 使用 LLM 用户（GLM/Qwen）整体下降 7.4–10.2 分，但披露梯度仍保持。

最值得记住的一句话：披露时机比检索接口和目录大小重要得多；隐藏约束必须靠“先提议后提交 + 用拒绝反向剔除候选需求”来解，而 LLM agent 目前仍明显弱于可解释拒绝的脚本策略。
