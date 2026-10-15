---
title: What Makes a Social Agent's Interactions Effective? Learning from Verifiable
  Outcomes in Paired Worlds
title_zh: 社交 Agent 交互有效性：从成对世界可验证结果中学习
authors:
- Caixin Kang
- Ke Wang
- Yuchuan Wu
- Xiaoqiang Wang
- Ling Li
- Bingxue Qiu
- Yongbin Li
- Yoichi Sato
affiliations:
- Alibaba Token Hub, Alibaba Group
- The University of Tokyo
arxiv_id: '2610.20195'
url: https://arxiv.org/abs/2610.20195
pdf_url: https://arxiv.org/pdf/2610.20195
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: Agent 社交交互 · 可验证结果奖励塑形
tags:
- Social Agents
- Outcome Verification
- Credit Assignment
- RL
- Benchmark
- Dialogue
one_liner: 提出 HICO-Bench 与 PaCPO：以成对世界可验证结果评估并训练社交 Agent，Qwen3-8B Verified Success
  20.4%→28.3%
practical_value: '- 评估体系：引入「Feasibility + Integrity」双层验证。在电商客服/导购/协商 Agent 中，可用规则校验最终订单、退款、排期等结构化结果是否满足双方约束，再让
  LLM judge 检查对话是否支撑该结果，避免只看对话流畅度。

  - 成对世界构造：对同一公共上下文只改一个私有条件（如用户预算、偏好），构成 contrast set。可用来诊断 Agent 是否真正利用差异信息，而非用同一套回复应付不同用户；也可作为回归测试集。

  - 回合级信用分配：PaCPO 的 tentative plan 探测 + 跨世界 credit 可在多轮任务型对话 RL 中复用。每轮后让模型输出「如果现在结束会提交的结果」，与另一世界的结果对比，只在关键信息披露后的分化时刻给予奖励，用
  potential-based 重分配保持总奖励不变。对训练客服主动澄清需求、协商出价等场景有价值。

  - 保守预期：即使 PaCPO 提升，绝对 Verified Success 仍只有 28.3%，说明复杂多轮交互任务上 RL 收益有限；建议先做好 SFT 初始化（SFT+PaCPO
  达 31.67%）和结构化验证闭环，再逐步引入 RL。'
score: 8
source: huggingface-daily
depth: full_pdf
---

动机：现有社交 Agent 评估主要靠 LLM judge 对对话打分，不检查最终商定的计划是否满足参与者私有约束。论文在 13 个模型上发现，Goal≥8 的对话中有 35.99% 未通过结果验证。奖励信号只在对话末端，回合贡献难以分配。

方法关键点：
- HICO-Bench：180 个日常协调场景，分资源分配、授权、有界数量、联合排程、共享资源排程、集合同意六类。每个场景有两个世界，共享公共上下文、仅一个私有条件不同，正确计划互斥。两角色持有私有卡片，对话后独立填写结构化记录；Feasibility 由程序检查两记录一致且满足双方私有条件，Integrity 由 LLM judge 检查对话是否支撑记录，两者皆过为 Verified Success。
- PaCPO：每轮后用当前策略探测 tentative plan，在两个世界分别 rollout 并交叉检查计划可行性。当差异私有条件在双方对话中已披露时打开 gate，计算 paired credit d_i,t = M_ii - M_i,1-i，与 within-world feasibility 组成 potential Φ_t = αM_ii + βd_i,t，通过 potential-based 重分配终端奖励 r'_t = r_t + Φ_t - Φ_{t-1} 保持总奖励不变，再用 PPO 更新；LoRA 训练 Qwen3-8B，固定 Qwen3-8B partner。

关键结果：
13 个模型中 Verified Success 从 Qwen3-8B 20.42% 到 Gemini 3.7 Flash 82.50%，最强模型仍留 headroom。PaCPO 将 Qwen3-8B 从 20.42% 提至 28.33%，优于 PPO 25.00% 和 GRPO 26.25%（同 384 对话）；消融显示跨世界配对、credit 时机和 disclosure gate 均重要。self-play 与 SOTOPIA transfer 也有增益。

最值得记住的一句话：高对话评分不保证计划可验证成功，需要 Feasibility+Integrity 双验证和成对世界信用分配。
