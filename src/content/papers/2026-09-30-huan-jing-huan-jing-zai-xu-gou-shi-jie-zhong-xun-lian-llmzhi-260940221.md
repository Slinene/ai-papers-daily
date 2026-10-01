---
title: 'PhantomEnvironments: Training LLM Agents in Fictional Worlds'
title_zh: 幻境环境：在虚构世界中训练LLM智能体
authors:
- Anmol Kabra
- Swathi Saravana Selvam
- Albert Gong
- Chao Wan
- Christian Belardi
- Dongyoung Go
- Katie Z. Luo
- Kilian Q. Weinberger
affiliations:
- Cornell University
- Stanford University
arxiv_id: '2609.40221'
url: https://arxiv.org/abs/2609.40221
pdf_url: https://arxiv.org/pdf/2609.40221
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: 规则生成合成环境训练搜索Agent
tags:
- RL
- LLM Agent
- Synthetic Environments
- Multi-hop Search
- GRPO
one_liner: 用零成本规则生成的虚构多跳问答环境做RL训练，得到可迁移到真实多跳基准的LLM搜索agent
practical_value: '- 可构建规则生成的“虚拟商品/用户图谱”环境，以零边际成本生成多跳query-answer对，用于RL训练搜索/推荐agent，避免依赖LLM生成数据带来的幻觉和污染。

  - 用纯线性跳数（hop）作为难度主轴，优先训练问题分解与逐跳检索；comparison类题型可按需混入50%以定向补强比较推理，不要盲目加constraints防止模型学会逐字query捷径。

  - 真实业务数据有知识时效和memorization shortcut问题，可把规则环境作为跨域/新库存的鲁棒训练补充，尤其当线上query超出训练分布时；关闭knowledge
  advantage，让模型学通用搜索技能。

  - 监控agent搜索调用次数随问题难度的缩放行为，可以作为训练质量指标；Qwen2.5在虚构环境交互后涌现线性search scaling，提示可将其作为模型是否掌握自适应检索预算的信号。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

动机：训练LLM搜索agent受环境瓶颈限制，需要可验证奖励、长轨迹、低成本。真实Wikipedia数据昂贵且时效局限；LLM合成数据有幻觉、污染和成本问题。本文探索用纯规则生成的虚构世界环境，无LLM、零边际成本、可验证，训练通用搜索能力。

方法关键点：基于PhantomWiki的规则生成社交图谱和模板文章，生成最大7跳的多跳问题，编译为Prolog查询保证答案可验证；把文章放入搜索索引，让agent通过<search>检索、<answer>回答，多轮交互。沿用Search-R1的RL配方：GRPO、F1奖励，约55K问题，全职微调四个模型（Qwen2.5-3B/7B、Llama-3.2-3B、Phi-4-mini）。训练时使用e5-base-v2检索器top-3，评估时用Qwen3-Embedding-4B和32768上下文，最多20轮。

关键实验：在六个真实多跳基准上，四个模型平均F1提升：旧基准1.7×，新基准2.2×；Llama-3.2-3B在SynthWorlds-SM上从3.8提升到27.0（7.1×）。与真实NQ+HotpotQA训练对比：in-domain真实占优（56.7 vs 52.2），out-of-domain幻境占优（32.1 vs 28.4），且幻境使SynthWorlds知识优势KA从8%关闭到0%。未见过的虚构宇宙和10倍大的检索池中性能保持。复杂度消融：线性hops是主要迁移来源，比较题型可针对提升比较问题，约束题反而导致逐字query捷径损害迁移。Qwen模型涌现搜索预算随难度线性缩放。

最值得记住的一句话：规则生成的虚构环境是训练通用搜索agent的免费、可验证、不过时的数据源，值得作为真实数据的补充。
