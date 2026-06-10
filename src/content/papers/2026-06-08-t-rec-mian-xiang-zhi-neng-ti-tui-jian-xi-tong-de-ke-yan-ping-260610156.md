---
title: '$τ$-Rec: A Verifiable Benchmark for Agentic Recommender Systems'
title_zh: τ-Rec：面向智能体推荐系统的可验证评测基准
authors:
- Bharath Sivaram Narasimhan
- Karthik R Narasimhan
affiliations:
- Independent Researcher
- Princeton University
arxiv_id: '2606.10156'
url: https://arxiv.org/abs/2606.10156
pdf_url: https://arxiv.org/pdf/2606.10156
published: '2026-06-08'
collected: '2026-06-10'
category: Agent
direction: 智能体推荐系统评估基准
tags:
- Agentic Recommender Systems
- Benchmark
- Verifiable Rewards
- Policy Compliance
- pass^k
- Preference Elicitation
one_liner: 用可验证奖励与 pass^k 一致性指标替代主观 LLM 评判，揭示当前模型在智能体推荐中的可靠性悬崖
practical_value: '- **引入 pass^k 可靠性指标**：在电商 Agent 上线前，用 pass^1/pass^2/pass^4 衡量多次执行的一致性，避免仅看单次成功率而低估长期可靠性；可结合回放测试评估模型稳定性。

  - **可验证奖励 + 揭示标记引出 (RTE)**：将约束打上 volunteer/on_ask/hidden 标签，模拟真实用户不完全表达需求的情景，迫使
  Agent 通过多轮对话主动引出偏好，可作为电商导购、客服 Agent 的对话能力测试方案。

  - **策略合规性作为第一类目标**：将领域政策（如年龄限制、已购过滤、平台可用性、赞助披露）转化为可编程检查，直接审计轨迹，可照搬到电商推荐场景中检查 Agent
  是否遵守负面清单、定价限制、合规话术等。

  - **后训练截止目录防记忆**：使用模型训练后发布的新商品（如 TMDB 2025–2026 电影）构建目录，确保评估不受训练数据泄露污染；电商可定期抓取新上架商品构建动态测试集，隔离泛化与记忆。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有会话推荐系统评估严重依赖静态对话语料的表面指标（BLEU、Recall@k）或 LLM-as-a-judge 主观评分，前者易被记忆利用，后者成本高、不一致。随着推荐系统向智能体化、多轮对话过渡，缺乏衡量偏好引出、约束推理和策略合规的可靠基准。

**方法关键点**
- 将推荐交互建模为基于工具-智能体-用户 (TAU) 循环的部分可观察 MDP，智能体通过对话和工具调用（搜索、过滤、元数据查询）逐步收集约束。
- **可验证奖励**：成功标准为结构化目录谓词（如 runtime≤120, content_rating∈{PG-13,G}），零 LLM 调用，完全确定、可复现。
- **揭示标记引出 (RTE)**：每个约束被标记为 volunteer（开场主动说出）、on_ask（仅当被问及才说）或 hidden（永远不说，但违反时拒绝），强制智能体通过对话主动挖掘用户需求。
- **pass^k 可靠性指标**：衡量在 𝑘 次独立试验中全部成功的概率，揭示单次能力指标掩盖的一致性悬崖。
- **策略合规性目标**：包括推荐工具使用、已观看过滤、可用性检查、年龄限制、赞助披露、透明度（无解任务主动放弃）等七条可编程策略检查。

**关键结果**
- 在 60 个电影任务（含 13 volunteer/32 mixed/15 hidden，含 5 个无解任务）上评估 6 个模型族的 9 种配置，最强模型 pass^1 仅 ~57%，pass^4 跌至 ~35%。
- 揭示难度呈现巨大梯度：DeepSeek V4 Flash 从 volunteer 的 0.846 降至 hidden 的 0.200，4 倍差距，说明高阶模型也有严重的信息引出短板。
- 策略合规率差异大，Qwen3-32B 可用性违规率高达 0.21；能力-延迟前沿显示 GPT-5.4 无思考模式最快（~7s/步），但 pass^1 仅 0.47，DeepSeek V4 Flash 长思考模式 pass^1 达 0.57 但延迟 ~30s。

**值得记住的一句话**：Agent 推荐系统的真正瓶颈不是一次性的正确率，而是在多变对话中稳定满足隐藏约束与策略要求的可靠性。
