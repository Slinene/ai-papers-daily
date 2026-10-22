---
title: 'DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents'
title_zh: DeLoop：用重复动作自监督训练长程 Agent 避免循环
authors:
- Tianle Chen
- Pushkar Singh
- Ketan Todi
- Biswajit Paria
- Qijia He
- Wenqi Wang
- Yuwen Tan
- Jike Zhong
- Sugato Basu
- Deepti Ghadiyaram
affiliations:
- Google
- Boston University
- University of Washington
- University of Southern California
- Google DeepMind
arxiv_id: '2610.19376'
url: https://arxiv.org/abs/2610.19376
pdf_url: https://arxiv.org/pdf/2610.19376
published: '2026-10-13'
collected: '2026-10-22'
category: Agent
direction: 长程 Agent 的自我监督去循环训练
tags:
- LLM agents
- self-supervision
- DPO
- context compression
- loop detection
- tool calling
one_liner: 把 agent 重复动作当负样本、同 rollout 后续恢复动作当正样本做 DPO，大幅降低上下文压缩下的循环率
practical_value: '- 在电商/广告的 multi-step agent 流程（购物助手、广告投放优化、搜索 query 改写 agent）里，可以先加一个结构化的重复检测器：把
  tool/API call 做 canonicalize（忽略空格、参数顺序），再对比返回 observation；相同的 (call, observation)
  就是 loop。这些信号可以直接用于在线拦截，也能变成训练数据。

  - 用 agent 自己的 rollout 挖掘偏好对：rejected = 重复动作，chosen = 同一条 rollout 里第一个后续非重复动作。无需
  reward、gold answer、LLM judge，适合业务里大量失败/无效日志的自监督学习；LoRA DPO 成本低。

  - 上下文压缩/总结会明显放大 loop。如果系统里做了会话压缩、摘要、截断，建议监控压缩后的 loop rate，并且不仅优化 compressor/memory，还要训练
  policy 学会使用已有历史记录。

  - DeLoop-Mix 证明跨域自挖 pair 可以提升泛化：电商场景可以把搜索、推荐、客服等不同 agent 任务的 loop pair 混合训练，既压低重复动作，又提升任务成功率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
长程 LLM agent 在执行工具调用时经常重复已经做过的动作：同一个 tool call、同样参数、返回相同 observation，这类动作不增加任何新信息，被定义为 loop。上下文压缩会加剧该问题：CodeGym 上 Qwen3-8B 全历史 loop rate 为 29.0%，在 4,096 token 摘要压缩后升到 57.3%。并且 looping runs 的失败率明显更高、交互 step 与 token 成本更大。更好的 context management 只能决定保留什么历史，不能保证 policy 会利用历史避免重复。

## 方法关键点
- 结构化 loop 检测：对每个 tool call 做 canonicalize（忽略空白、参数顺序），如果 (canonical_call, observation) 之前出现过，则当前 step 是 looping action。
- 偏好对挖掘：在 agent 自己的 rollout 中，将 looping action 作为 rejected y−；若同一 rollout 后续出现第一个 non-loop 且 canonical call 不同的动作，则作为 chosen y+。两者共享 loop 发生前的历史 x。
- 训练：用 DPO 训练 policy 偏好 y+ 而非 y−。Qwen3-8B 用 LoRA、β=0.05、约 8,000 个自挖 CodeGym pairs。无 task reward、gold answer、LLM judge。
- DeLoop-Mix：额外加入 Terminal-Bench 等跨域 rollout 挖出的 pairs，提升泛化。

## 关键实验
在 CodeGym 300 个 held-out 任务、摘要上限 4,096 tokens 下：
- Qwen3-8B loop rate 从 57.3% 降到 6.1%（9.4×）；steps/task 从 15.00 降到 4.67；tokens/task 从 23.9k 降到 12.7k；task success 保持 25.9%（DeLoop-Mix 提升到 30.3%）。
- 模型规模扩展：Qwen3-14B success 从 45.1% 提升到 52.3%；Qwen3-32B 从 37.7% 提升到 44.8%，loop rate 均大幅下降。
- 消融：仅用 chosen 动作做 SFT，loop rate 仍为 37.7%；DPO 对比负样本至关重要。用 loop flag 作为 GRPO 惩罚只能降到 15.0%。
- 跨环境：ALFWorld、Open-AgentRL、AppWorld、ScienceWorld 中 loop rate 均下降；BrowseComp-Plus 上 loop rate 从 22.4% 降到 1.2%。

> 最值得记住的一句话：把 agent 自己的 loop 当作负样本、同一 rollout 后续打破 loop 的动作当作正样本，就能在无 reward/gold/judge 的情况下显著减少重复动作。
