---
title: Online Skill Learning for Web Agents via State-Grounded Dynamic Retrieval
title_zh: 基于状态引导动态检索的Web Agent在线技能学习
authors:
- Jiaxi Li
- Ke Deng
- Yun Wang
- Jingyuan Huang
- Yucheng Shi
- Qiaoyu Tan
- Jin Lu
- Ninghao Liu
affiliations:
- University of Georgia
- Tencent America
- New York University
- The Hong Kong Polytechnic University
arxiv_id: '2606.04391'
url: https://arxiv.org/abs/2606.04391
pdf_url: https://arxiv.org/pdf/2606.04391
published: '2026-06-02'
collected: '2026-06-10'
category: Agent
direction: Web Agent在线技能学习 · 动态检索
tags:
- web agents
- online skill learning
- state-grounded retrieval
- sliding-window extraction
- MMR reranking
one_liner: 提出状态引导动态检索，将技能复用从任务级改为步级，滑动窗口提取子过程与MMR重排提升Web Agent成功率。
practical_value: '- 动态技能检索：电商Agent执行多步任务（如比价、下单）时，可借鉴状态引导的动态检索，在每个决策步根据当前页面状态和任务目标检索最相关技能，避免固定技能集带来的状态不匹配。

  - 滑动窗口提取子过程：将成功的任务轨迹切割为可复用的小段程序（如“填写搜索关键词并点击按钮”），生成文本描述与可执行代码配对的技能库，平衡了技能的通用性与执行粒度，可用于构建可复用的业务操作库。

  - 文本-代码双表示：技能的自然语言描述用于检索，代码片段用于实际执行，两者解耦但仍保持关联，便于后续维护和更新。推荐系统内的多步操作（如配置营销活动）可用类似方案沉淀操作Know‑how。

  - MMR重排去重：为避免检索到的技能高度重叠，采用最大边际相关性重排，在相关性和多样性间取得平衡。这个trick可以直接用于任何基于embedding的检索增强场景，防止返回结果冗余。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有在线技能学习方法在Web Agent中通常采用任务级的一次性技能复用：开局根据任务指令检索一组技能，全程固定不变。这忽略了Web执行过程中页面状态不断变化的事实，导致后期技能与状态错配。需要一种能在每个中间步动态检索合适技能的方法。

**方法关键点**：
- **滑动窗口提取**：从评估为成功的轨迹中，用长度为2~5的滑动窗口切割出局部子过程，经LLM判断可复用性后，转化为文本描述+可执行Python代码的技能对，形成中间粒度的技能库。
- **文本-代码双表示**：每个技能由自然语言描述（用于检索匹配）和代码片段（用于实际执行）组成，兼顾检索与执行。
- **状态引导的动态检索**：在任务执行的每一步，将当前页面状态摘要与任务目标文本拼接，计算与技能描述的余弦相似度，并利用最大边际相关性（MMR）重排前M个候选，选出5个既相关又多样的技能注入当前决策。
- **在线学习范式**：技能库随任务流逐步更新，每次仅使用已学技能，无地面真理信号，依赖评估器判断轨迹成功与否。

**关键结果**：在WebArena五个域（Shopping、Admin、Reddit、Gitlab、Map）上，使用GPT‑4.1时SGDR平均成功率37.5%，较最强基线CER提升10.6%；使用Qwen3‑4B时平均成功率24.3%，提升10.0%。同时，平均交互步数显著减少（GPT‑4.1下从6.0步降至4.8步），证明技能复用提高了效率。消融实验验证了任务+状态联合检索、MMR重排、滑动窗口粒度的收益。

**值得记住的一句话**：将技能检索从任务级一次性注入变为步级状态感知的动态检索，是提升Web Agent在长程任务中成功率和效率的关键设计。
