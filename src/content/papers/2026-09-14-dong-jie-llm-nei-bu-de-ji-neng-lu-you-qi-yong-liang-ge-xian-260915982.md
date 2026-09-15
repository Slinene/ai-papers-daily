---
title: 'The Router Within: Eliciting Native Skill Routing from a Frozen LLM'
title_zh: 冻结 LLM 内部的技能路由器：用两个线性投影读出原生路由信号
authors:
- Ruishuo Chen
- Xun Wang
- Yu Chen
- Zhuoran Li
- Longbo Huang
affiliations:
- Institute for Interdisciplinary Information Sciences, Tsinghua University
arxiv_id: '2609.15982'
url: https://arxiv.org/abs/2609.15982
pdf_url: https://arxiv.org/pdf/2609.15982
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: Agent 技能路由 · LLM 原生信号读取
tags:
- Skill Routing
- Frozen LLM
- Linear Projection
- Product of Experts
- Late Interaction
- Agent
one_liner: 冻结 LLM 自身前向传播中已含技能路由信号，两个线性投影即可读出，无需外部模型或技能文本入上下文
practical_value: '- 用 frozen LLM 自身中间层做相关性/召回评分，可避开独立 embedder/reranker 的 OOD 偏移；在电商
  query 改写、商品/内容召回中，可训练两个轻量线性层从骨干 LLM 读 query 与 item 的匹配信号，尤其适合长上下文里埋没的需求。

  - token-level late-interaction + top-k voting + recency decay 可迁移到个性化检索：不做全局池化，让关键
  token 投票，对长会话轨迹用指数衰减增强最近消息权重。

  - ε-cover 压缩 token bank 对海量 item/skill 索引有实用价值：farthest-first 覆盖去冗余，分数误差有界，可显著减小索引规模，新对象只需一次前向编码。

  - 多信号 product of experts 融合（对比学习分数 + 生成似然 + yes/no 判别）可借鉴到排序融合，任一专家可一票否决，提升排序鲁棒性；再训练轻量门控决定何时触发路由，降低误触发。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

动机：技能已成为扩展 LLM agent 能力的主流方式，但现有路由方案要么把所有技能元数据塞进上下文（progressive disclosure）导致注意力分散、库规模受限；要么用独立 embedding/reranker 检索，虽上下文干净但选择能力脱离 agent LLM，不随骨干增强而提升。论文发现冻结的 agent LLM 自身前向传播中已带路由信号，只需两个线性投影即可读出。

方法关键点：
- Glance：在中间层 ℓ*（按矩阵熵的压缩谷底选择，约 70% 深度）加训练好的 query/key 线性映射；对任务每个 token 通过 max-similarity 与每个技能安装时编码的 token bank 做 late-interaction，token 投票 top-k，全库打分。
- 技能 bank 安装时用 farthest-first 构建 ε-cover 压缩，去除冗余方向，保证分数最多下降 ε，且新技能只需一次前向。
- Verdict：对 glance 短名单，恢复前向，读取生成任务似然 L 与 yes/no 判别 log-odds V。
- Ruling：product of experts 融合 g+αL+γV，任一专家可一票否决。
- 仅训练两个 768×5120 矩阵共 7.9M 参数，骨干冻结。

关键实验：Qwen3-32B 上训练一次，零样本迁移到 SkillRet test、SRA-Bench、Eval-Core 和自建 SkillTraj（372 条多轮轨迹，四个 mid-rollout 场景）。对比 progressive disclosure 和 retrieve-and-rerank 管道（外部参数 1.2B–16B），Gavel 在 written tasks 上最高领先 13.4 点（SRA-Bench）、SkillRet 3.8、Eval-Core 1.3–2.7；在 SkillTraj 四个场景领先 8.6–21.9 点。端到端 bash-agent 中，Qwen3-32B 在 Skill-Use 上正确触发技能率 0.909，超过 Codex 中更大 frontier 模型的最高 0.864，progressive disclosure 仅 0.011。0.6B 骨干上的 Gavel 已超过 32B 的 progressive disclosure。

最值得记住的一句话：冻结骨干已经携带技能选择所需的能力，学习一个轻量读出器即可将其投入使用。
